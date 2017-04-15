---
title:  "SharePoint Managed Paths"
date:   2011-05-24
canonical: http://blog.staticvoid.co.nz/2011/5/24/sharepoint_managed_paths
redirect_from:
  - 2011/5/24/sharepoint_managed_paths
---
Managed paths in SharePoint are a confusing beast, so here's my explanation of how and when to use them.

Managed paths are used to define the location of every site collection inside of SharePoint. Managed paths follow the same concept as a virtual directory in IIS however they are handled directly by SharePoint. A managed path defines a sub-directory in your application which you can use as a url for a site collection. By default SharePoint 2010 creates 2 managed paths when you make a new web application and sites.

The dialogue below allows you to create managed paths and can be found in the ribbon menu for web applications in central admin.

![Managed Paths]({{site.baseurl}}/images/posts/2011/managed-paths.png)

There are 2 types of managed paths you can create:

#### Explicit Paths
These are used if you want to place a site collection directly at the sub-directory you specify. For example if you want a site collection at <a href="http://site/bob">http://site/bob</a> you would use an explicit path.

However explicit paths may only contain a single site collection.

#### Wildcard Paths
A wildcard path is used if you want to have multiple site collections under a path. For example <a href="http://site/projects/project1">http://site/projects/project1</a> and <a href="http://site/projects/project2">http://site/projects/project2</a>.

Wildcard paths can only have site collections below the path (ie no site collection at <a href="http://site/projects">http://site/projects</a>)
