---
title:  "SharePoint Alternate Access Mappings"
date:   2011-05-25
canonical: http://blog.staticvoid.co.nz/2011/5/25/sharepoint_alternate_access_mappings
redirect_from:
  - 2011/5/25/sharepoint_alternate_access_mappings
---
As a SharePoint developer alternate access mappings (AAM) are one of the things i see done most poorly. This is largely due to server administrators (and for that matter SharePoint administrators) being more familiar with IIS than Central Admin. Having said that the damage you can do by incorrectly configuring a farms AAM's is substantial and not&nbsp;immediately&nbsp;obvious.<br />
<br />
<b>The Theory</b><br />
SharePoint is a scalable load&nbsp;balanced&nbsp;web application. Its very important to note however that it is under the covers just like every other web application that you have seen (though notably more complex). This means it consists of a set of IIS sites and Virtual Directories, some databases, a local site&nbsp;directory&nbsp;and of course a host of custom code.<br />
<br />
However even though SharePoint appears to be just the same as any other web application in reality it has a number of subtle differences from most web applications administrators see. The reasons for this are&nbsp;largely&nbsp;to do with&nbsp;scalability.<br />
<br />
To improve performance and scalability SharePoint itself installs and configures the IIS roles for the servers on which it runs. It also manages the web.config, site directories (eg 14 hive / SharePoint Root) and Databases. This allows the SharePoint configuration and administration services to maintain&nbsp;consistency&nbsp;across multiple web&nbsp;front ends.<br />
<br />
For example if a new WebApplication is created inside of SharePoint the required directories, IIS sites and config files will be automatically created on all web front ends.Or in another scenario if a new feature is added to SharePoint the web.config changes and feature files will be rolled out to all web front ends.<br />
<br />
<b>The common mistake</b><br />
The mistake people inevitably make (and its one I have personally made at one stage or another) is to go about manually editing these configurations. It looks really&nbsp;tempting&nbsp;especially if you are an IIS guru to go and tweek things inside of IIS to bend SharePoint to your will, but this causes a number of problems. For many things this just breaks the load balancing features with multiple WFE's, and hey lets face it a big proportion of SharePoint installs only have a single WFE so these modifications can often go un-(noticed/punished).<br />
<br />
The real problem comes when modifying the web.config or IIS configuration directly.<br />
<br />
If you modify the <i>web.config</i> expect your changes to randomly&nbsp;disappear&nbsp;at some stage in the future. This kinda makes sense if you think about it, SharePoint manages this file and if it needs to make some changes it will just write over what you have there.<br />
<br />
If you are an IT pro and feel like you want to modify the web.config, my advice is 'just dont' and if you do expect it to get destroyed.<br />
<br />
If you are a developer (like me) I wouldn't ever write to the web.config outside of a Dev environment. If you need to quickly test things in development its my opinion that this is OK however do expect your modifications to be destroyed. When you are looking to deploy what you have to a production environment theres a great class which will allow you to package web.config changes into a SP Feature. This is the SPWebConfigModification class.<br />
<br />
If you modify<i> IIS settings</i> directly SharePoint is much less forgiving. Depending on the modification you make a number of things can happen but i find its quite common for SharePoint to simply decide that your now the web.config master and just stop managing it internally. This may sound good to you but its not.<br />
<br />
The most common change&nbsp;Ive&nbsp;seen is modifying the host headers of the IIS site. This is an enormous no-no, please don't ever do this (use AAM's instead). If you do go ahead and modify these any of your newly added headers will only be partly functional. Inside of SharePoint there is a lot of components which rely directly on the URL and in particular on looking this URL up internally. What you find (for the developers) is that references to SPContext.Current (a core piece of SharePoint&nbsp;goodness) will not work. This causes havoc on random SharePoint pages, web parts and custom features.<br />
<br />
<b>The right way</b><br />
OK so now we know the pitfalls. The right way to do things is to forget the individual components SharePoint uses and instead use Central Admin to modify your settings.<br />
<br />
An alternate access mapping inside of SharePoint defines a custom URL which is used to access a SharePoint web application. Think of it like a host header. You can find this on the main page of central admin, under the System Settings heading.<br />
<br />
<div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/-CB8KLKLjwXQ/Tdu4kx86l2I/AAAAAAAAAHo/I-J4MgGjINw/s1600/aam.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-CB8KLKLjwXQ/Tdu4kx86l2I/AAAAAAAAAHo/I-J4MgGjINw/s1600/aam.PNG" /></a></div><br />
Inside this page you can create and edit your AAM's.<br />
<div class="separator" style="clear: both; text-align: center;"><br />
</div><div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/-qO-rA-w9gYc/Tdu4_g0SO3I/AAAAAAAAAHs/oeHrxDYG6m8/s1600/aam-page.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="225" src="http://1.bp.blogspot.com/-qO-rA-w9gYc/Tdu4_g0SO3I/AAAAAAAAAHs/oeHrxDYG6m8/s640/aam-page.PNG" width="640" /></a></div><br />
If you (for example) wanted to add a new url to one of your web applications (for example add the url http://central-admin:5555 to your central admin web application &nbsp;you could do so by clicking Edit Public URLs and entering the url in the Intranet box. (note if you want to change the port you will need to use another mechanism: extend web application)<br />
<br />
<div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-goDLM8HdfEw/Tdu7OKTAIGI/AAAAAAAAAHw/3R95b3-vqYs/s1600/central-admin-aam.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="302" src="http://2.bp.blogspot.com/-goDLM8HdfEw/Tdu7OKTAIGI/AAAAAAAAAHw/3R95b3-vqYs/s640/central-admin-aam.PNG" width="640" /></a></div><br />
And there you have it a correctly configured site which you can browse to without issues.
