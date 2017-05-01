---
title:  "SharePoint Alternate Access Mappings"
date:   2011-05-25
redirect_from:
  - 2011/5/25/sharepoint_alternate_access_mappings
  - 2011/05/sharepoint-alternate-access-mappings.html
---
As a SharePoint developer alternate access mappings (AAM) are one of the things I see done most poorly. This is largely due to server administrators (and for that matter SharePoint administrators) being more familiar with IIS than Central Admin. Having said that the damage you can do by incorrectly configuring a farms AAM's is substantial and not immediately obvious.

#### The Theory
SharePoint is a scalable load balanced web application. Its very important to note however that it is under the covers just like every other web application that you have seen (though notably more complex). This means it consists of a set of IIS sites and Virtual Directories, some databases, a local site directory and of course a host of custom code.

However even though SharePoint appears to be just the same as any other web application in reality it has a number of subtle differences from most web applications administrators see. The reasons for this are largely to do with scalability.

To improve performance and scalability SharePoint itself installs and configures the IIS roles for the servers on which it runs. It also manages the `web.config`, site directories (eg 14 hive / SharePoint Root) and Databases. This allows the SharePoint configuration and administration services to maintain consistency across multiple web front ends.

For example if a new `WebApplication` is created inside of SharePoint the required directories, IIS sites and config files will be automatically created on all web front ends. Or in another scenario if a new feature is added to SharePoint the `web.config` changes and feature files will be rolled out to all web front ends.

#### The common mistake
The mistake people inevitably make (and its one I have personally made at one stage or another) is to go about manually editing these configurations. It looks really tempting especially if you are an IIS guru to go and tweek things inside of IIS to bend SharePoint to your will, but this causes a number of problems. For many things this just breaks the load balancing features with multiple WFE's, and hey lets face it a big proportion of SharePoint installs only have a single WFE so these modifications can often go un-(noticed/punished).

The real problem comes when modifying the `web.config` or IIS configuration directly.

If you modify the `web.config` expect your changes to randomly disappear at some stage in the future. This kinda makes sense if you think about it, SharePoint manages this file and if it needs to make some changes it will just write over what you have there.

If you are an IT pro and feel like you want to modify the `web.config`, my advice is 'just don't' and if you do expect it to get destroyed.

If you are a developer (like me) I wouldn't ever write to the `web.config` outside of a Dev environment. If you need to quickly test things in development its my opinion that this is OK however do expect your modifications to be destroyed. When you are looking to deploy what you have to a production environment there's a great class which will allow you to package `web.config` changes into a SP Feature. This is the `SPWebConfigModification` class.

If you modify *IIS settings* directly SharePoint is much less forgiving. Depending on the modification you make a number of things can happen but I find its quite common for SharePoint to simply decide that your now the `web.config` master and just stop managing it internally. This may sound good to you but its not.

The most common change I've seen is modifying the host headers of the IIS site. This is an enormous no-no, please don't ever do this (use AAM's instead). If you do go ahead and modify these any of your newly added headers will only be partly functional. Inside of SharePoint there is a lot of components which rely directly on the URL and in particular on looking this URL up internally. What you find (for the developers) is that references to `SPContext.Current` (a core piece of SharePoint goodness) will not work. This causes havoc on random SharePoint pages, web parts and custom features.

#### The right way
OK so now we know the pitfalls. The right way to do things is to forget the individual components SharePoint uses and instead use Central Admin to modify your settings.

An alternate access mapping inside of SharePoint defines a custom URL which is used to access a SharePoint web application. Think of it like a host header. You can find this on the main page of central admin, under the System Settings heading.

![Alternate Access Mappings]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/aam.png)

Inside this page you can create and edit your AAM's.

![Alternate Access Mappings]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/aam-page.png)

If you (for example) wanted to add a new URL to one of your web applications (for example add the URL [http://central-admin:5555](#) to your central admin web application  you could do so by clicking Edit Public URLs and entering the URL in the Intranet box. (note if you want to change the port you will need to use another mechanism: extend web application)

![Alternate Access Mappings]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/central-admin-aam.png)

And there you have it a correctly configured site which you can browse to without issues.
