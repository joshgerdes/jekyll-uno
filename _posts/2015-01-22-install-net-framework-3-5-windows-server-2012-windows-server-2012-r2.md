---
title: How to install .NET Framework 3.5 on Windows Server 2012 and Windows Server 2012 R2
categories:
  - Windows
date: 2015-01-22 00:00:00 +1300
---
.NET Framework 3.5 needs the source files off the Windows Server 2012 DVD in order to install. You can do this online and without needing a restart using DISM.

1. Go to a command prompt and enter this:

    dism /online /enable-feature /featurename:NetFX3 /all /Source:d:sourcessxs /LimitAccess

_Note: Source should be the Windows DVD location, ie d: **/Source:x**_ if x is your DVD mount point.
