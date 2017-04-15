---
title:  "Multiple Repository Data Contexts with my Repository Pattern"
date:   2011-11-21
canonical: http://blog.staticvoid.co.nz/2011/11/21/staticvoid_io_extentions-nuget
redirect_from:
  - 2011/11/21/staticvoid_io_extentions-nuget
---
<script type="text/javascript">
    (function () {
        var nb = document.createElement('script'); nb.type = 'text/javascript'; nb.async = true;
        nb.src = 'http://s.prabir.me/nuget-button/0.2.1/nuget-button.min.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(nb, s);
    })();
</script>
I was recently doing some file and folder manipulation using System.IO and wished i had some kind of fluent interface for traversing files and folders. So i wrote a basic one.<br />
<div><br />
</div><div>This means that you can do things like this:</div><div><br />
</div><div>directory.Parents("trunk").Directories(d=&gt;d.Name== "MyProject").Files(f=&gt;f.Name.EndsWith(".sln"));</div><div><br />
</div><br />
<pre class="nuget-button" style="width:100px">Install-Package StaticVoid.Core.IO</pre>
