---
id: 3479
title: How to install .NET Framework 3.5 on Windows Server 2012 and Windows Server 2012 R2
date: 2015-01-22T18:20:45+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3479
permalink: /win/install-net-framework-3-5-windows-server-2012-windows-server-2012-r2/
mfn-post-love:
  - "0"
post_views_count:
  - "83"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4833719717"
categories:
  - Windows
---
.NET Framework 3.5 needs the source files off the Windows Server 2012 DVD in order to install. You can do this online and without needing a restart using DISM.

1. Go to a command prompt and enter this:

**dism /online /enable-feature /featurename:NetFX3 /all /Source:d:sourcessxs /LimitAccess**

_Note: Source should be the Windows DVD location, ie d: **/Source:x**_ if x is your DVD mount point.