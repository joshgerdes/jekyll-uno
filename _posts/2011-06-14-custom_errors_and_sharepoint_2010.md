---
title:  "Custom Errors and SharePoint 2010"
date:   2011-06-14
redirect_from:
  - 2011/6/14/custom_errors_and_sharepoint_2010
  - 2011/06/custom-errors-and-sharepoint-2010.html
---
We recently had a client who wanted to replace all SharePoint error pages with their own custom ones. This lead me to find a whole bunch of nasty gotchas inside of SharePoint in regards to the way it generates and handles errors.

#### SharePoint Built-in Error Pages

Out of the box SharePoint comes with a set of error pages. Notably this set does not include a custom 404 Page. Below are some of the errors you have probably seen

![An unexpected error has occurred]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/custom-error-1.png)

![Access denied]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/custom-error-2.png)

One of the critical things to understand about these pages is that while they look like an error page they are actually returning an HTTP 200 (OK) result instead of the 500 or 401 codes they are hiding. This isn’t exactly best practice.

#### The Object Model and Error Pages

The SharePoint object model contains a method for implementing a 404 error message. This is done through the `SPWebApplication.FileNotFoundPage` property which allows you to specify a custom page to which 404’s are sent. This however has some limitations; it doesn’t work in all situations.

There is also no way to change the 500 or 401 pages via the object model so I was forced to use more drastic measures to replace the error pages.

<h4>SharePoint Error Handling</h4>

SharePoint does some really interesting things in the process of requesting pages which really threw some serious spanners in the works of my custom error handling code. This is because SharePoint uses error codes internally to make sure that page requests go to the correct place. For example when you request a page in the `_layouts` directory underneath a subsite (eg [http://sharepoint/subsite/_layouts/settings.aspx](#)) SharePoint returns a permissions denied error on the first request, this is then translated by SharePoint’s error handling code to a `Server.TransferRequest` to the root level layouts folder (eg [http://sharepoint/_layouts/settings.aspx](#)) which in turn checks your relevant permissions to the page and returns the appropriate status code. A similar process if followed if a site uses a team wiki template, the root is 401’d then redirected to SitePages/Home.aspx.

Basically this makes catching errors difficult as it’s not obvious if it’s supposed to error and get caught later.

#### Using an HTTP Module to Create Custom Errors

In the end I used an HTTP Module to do my custom error handling. Below is the code I used to handle errors and pass them to my custom error pages:

``` csharp
public void Init(HttpApplication context)
{
	_httpApp = context;
	_httpApp.PreSendRequestContent += new EventHandler(WebApp_PreSendRequestContent);
}

public void WebApp_PreSendRequestContent(object sender, EventArgs e)
{
	// avoid errors in a global module.
	if (_httpApp == null || _httpApp.Request == null || _httpApp.Response == null)
	{
		return;
	}
	HttpResponse res = _httpApp.Response;
	HttpRequest req = _httpApp.Request;

	if (req.Url.AbsolutePath.Contains("_layouts/AccessDenied.aspx"))
	{
	 	_httpApp.Server
			.TransferRequest(SPUtility.GetServerRelativeUrlFromPrefixedUrl("~site/" + AccessDeniedUrl));
		return;
	}
	if (res.StatusCode < 400)
	{
		// if the request is ok just ignore it
		return;
	}
	if (res.StatusCode == 404
		&& !req.Url.AbsolutePath.EndsWith(PageNotFoundUrl, StringComparison.InvariantCultureIgnoreCase))
	 {
	 	_httpApp.Server
			.TransferRequest(SPUtility.GetServerRelativeUrlFromPrefixedUrl("~site/" + PageNotFoundUrl));
		return;
	 }
	if (res.StatusCode >= 500 && res.StatusCode < 600 && !req.Url.AbsolutePath.EndsWith(ErrorUrl, StringComparison.InvariantCultureIgnoreCase))
	{
		_httpApp.Server
			.TransferRequest(SPUtility.GetServerRelativeUrlFromPrefixedUrl("~site/" + ErrorUrl + "?statuscode=" + res.StatusCode));
		return;
	}
}
```

In a nutshell what I am doing here is the following

* Catching any requests to the friendly permission denied page, as discussed earlier 401s are used extensively for redirects inside of SharePoint so catching them will cause havoc. By catching requests to the access denied page I am hacking around the need to detect a 401.

* Ignoring any OK requests

* Catching anything which is a 404 in the web application (except the 404 page itself) and redirecting to my 404 page.

* Catching anything with an error code in the web application (except the error page itself) and redirecting to my Error page. I also included the actual status code so I can emulate it in the response.

This however wasn’t enough. Remember earlier how I said that the actual error pages in SharePoint return a 200 result? What this basically means is that you can’t simply catch the errors here as SharePoint is hiding them. So one more hack is required.

SharePoint error messages are enabled and disabled with a `web.config` node called `SafeMode.CallStack`. This is a pretty deceptive name but basically what it does is turn on or off the SharePoint custom error messages. You need to set `CallStack` true and everything will start working.


``` xml
<SharePoint>
	<SafeMode MaxControls="200" CallStack="true" DirectFileDependencies="10" TotalFileDependencies="50" AllowPageLevelTrace="false">
		<PageParserPaths>
		</PageParserPaths>
	</SafeMode>
<SharePoint>
```

Don’t forget to make your `web.config` changes with `SPWebConfigModification`.
