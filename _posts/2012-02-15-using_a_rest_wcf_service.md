---
title:  "Using a REST WCF Service"
date:   2012-02-15
excerpt: "WCF WebAPI allows REST support within WCF. This post discusses some of the gotchas of building REST services with WCF and provides a simple tutorial for creating a basic WCF REST service."
redirect_from:
  - 2012/2/15/using_a_rest_wcf_service
  - 2012/02/using-rest-wcf-service.html
---
I've been having a bit of a play with REST and WCF lately, in the past I've done this with WebAPI, however given this is still BETA software I wasn't able to use it in my current project. When I went back to basic WCF with REST I had a few issues creating a working sample, it’s quite fiddly so I thought I would post the example.

The first thing you need is a contract, here's mine:

``` csharp
[ServiceContract]
public interface IHelloService
{
	[OperationContract]
	[WebInvoke(UriTemplate = "Hello/{name}", Method = "GET")]
	string Hello(string name);
}
```

As with all WCF stuff you need your service and operation contracts, in addition for rest you need to use WebInvoke to tell it about the URL and Method you are using, fairly straight forward.

Then a concrete implementation of the contract like this:

```csharp
[AspNetCompatibilityRequirements(
RequirementsMode=AspNetCompatibilityRequirementsMode.Required)]
public class HelloService : IHelloService
{
	public string Hello(string name)
	{
	return String.Format("Hello {0} how are you?", name);
	}
}
```


Note the AspNetCompatibilityRequirementsMode header. Unfortunately you seem to
need this in both the Service definition and the web.config, which is a bit
silly IMO.

``` xml
<system.serviceModel>
	<serviceHostingEnvironment aspNetCompatibilityEnabled="true" />
</system.serviceModel>
```

Then the route binding for the service in your Global.ascx

```csharp
private void RegisterRoutes()
{
	RouteTable.Routes.Add(new ServiceRoute("/hello-service",
		new WebServiceHostFactory(), typeof(HelloService)));
}
```

This looks pretty simple but what’s important is that you use a derivative of WebServiceHostFactory, if you use a derivative of the older ServiceHostFactory, you won’t get a nice error you will just get a **blank page** via the browser.

This is all you really need for the host component of the service

To consume the service you can use the following ChannelFactory style.

``` csharp
using (ChannelFactory<IHelloService> factory = new ChannelFactory<IHelloService>(
	new WebHttpBinding(), "http://localhost:64373/hello-service"))
{
	factory.Endpoint.Behaviors.Add(new WebHttpBehavior());

	var helloService = factory.CreateChannel();
	helloService.Hello("Luke");
}
```


This is similar to how you would
normally consume a WCF service but with a few important differences

 - You must use a WebHttpBinding derivative or you will get a SOAP exception similar to the following:

 *There was no endpoint listening at
http://localhost:64373/ that could accept the message. This is often caused by
an incorrect address or SOAP action. See InnerException, if present, for more
details.*

 - You must add the WebHttpBehavior to the endpoint, I found this quite counter intuitive. If you don't you will get an error similar to the following:

 *Manual addressing is enabled on this factory, so all messages sent must be pre-addressed.*


Avoiding these gotchas will let you create REST services with WCF
