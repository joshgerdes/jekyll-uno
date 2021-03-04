---
title: c000021a Fatal System Error
date: 2012-03-05 00:00:00 +13:00
permalink: "/win/c000021a-fatal-system-error/"
categories:
- Windows
layout: post
---

&#8220;The Session Manager Initialization system process terminated unexpectedly with a status of 0xc000026c&#8221;

Caused by a recently Windows Update

First you need to access the recovery console. Following the instructions below

  1. **Boot** with your original **Windows XP CD**. You need one which will allow you to get into the Recovery Console.
  2. Once booted, choose to use the **Recovery Console**
  3. **Choose** which **Windows installation** you need to log into. if there’s only one on that machine, it will be “1?.
  4. **Type** **in** the **Administrator password**.
  5. Change to the update folder by typing** cd WINDOWS$NtUninstallKB925902$spuninst**
  6. **Run** **this** **command** in the folder: **batch spuninst.txt** _(If the command ran correctly, you should see a spuninst.tag file, using the “dir” command)_
  7. **Restart the Computer**

_**At this point the computer should boot properly and you should install SP3 and other patches to prevent this problem from happening again.**_

If the **spuninst.tag** file **doesn’t exist**, you may have received a bunch of errors instead. There are a few reasons why this could happen, one of which is if your windows isn’t really installed on the c: drive, even if the Recovery Console always names it that way. To remove the patch manually **type** in these command in the **Command Prompt** _(By going back using the Windows CD instructions above)_

_**DEL “c:windows$hf_mig$kb925902mf3216.dll”**_
  
 _ **DEL “c:windows$hf_mig$kb925902gdi32.dll”**_
  
 _ **DEL “c:windows$hf_mig$kb925902user32.dll”**_
  
 _ **DEL “c:windows$hf_mig$kb925902win32k.sys”**_
  
 _ **DEL “c:windowssystem32dllcachegdi32.dll”**_
  
 _ **DEL “c:windowssystem32dllcachemf3216.dll”**_
  
 _ **DEL “c:windowssystem32dllcacheuser32.dll”**_
  
 _ **DEL “c:windowssystem32dllcachewin32k.sys”**_
  
 _ **COPY “c:windows$NtUninstallKB925902$gdi32.dll” “c:windowssystem32gdi32.dll”**_
  
 _ **COPY “c:windows$NtUninstallKB925902$mf3216.dll” “c:windowssystem32mf3216.dll”**_
  
 _ **COPY “c:windows$NtUninstallKB925902$user32.dll” “c:windowssystem32user32.dll”**_
  
 _ **COPY “c:windows$NtUninstallKB925902$win32k.sys” “c:windowssystem32win32k.sys”**_
  
 _ **COPY “c:windows$NtUninstallKB925902$spuninstspuninst.txt” “c:windows$NtUninstallKB925902$spuninstspuninst.tag”**_

_Sources taken from <a href="http://www.techforlunch.com/bsod-session-manager-initialization-fails-with-status-0xc000026c/" target="_blank">TechForLunch</a>_

&nbsp;
