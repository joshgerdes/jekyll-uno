---
title:  "StaticVoid IO Extentions - Nuget"
date:   2011-11-21
canonical: http://blog.staticvoid.co.nz/2011/11/21/staticvoid_io_extentions-nuget
redirect_from:
  - 2011/11/21/staticvoid_io_extentions-nuget
---


I was recently doing some file and folder manipulation using System.IO and wished I had some kind of fluent interface for traversing files and folders. So I wrote a basic one.

This means that you can do things like this:

```csharp
directory.Parents("trunk").Directories(d => d.Name == "MyProject").Files(f => f.Name.EndsWith(".sln"));
```

{% include nuget.html packageId="StaticVoid.Core.IO" %}
