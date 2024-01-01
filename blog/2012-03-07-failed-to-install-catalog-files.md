---
title: Failed to install catalog files
layout: post
permalink: /win/failed-to-install-catalog-files/
tags:
  - Windows
---
Getting the Failed to install catalog files error? This is how you fix it. The issue is related to registry key security settings.

  1. Click **Start**
  2. Click **Run**
  3. Type in: **command**
  4. Press **enter**
  5. In the command prompt **type**: **secedit /configure /cfg c:Windowsrepairsecsetup.inf /db secsetup.sdb /verbose /areas regkeys**
  6. Press **Enter **

If it reports an error about not knowing where secedit is then you can download it from &#8220;here&#8221;. You need to download it and put it in My Computer/C.
