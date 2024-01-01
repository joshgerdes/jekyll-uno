---
title: 'c0000135 {Unable to Locate Component}'
tags:
  - Windows
date: 2012-03-05 00:00:00 +1300
---

The application has failed to start because CSRSRV.DLL was not found. Reinstalling the application may fix this problem.

First you need to access the recovery console. Following the instructions below

  1. **Boot** with your original **Windows XP CD**. You need one which will allow you to get into the Recovery Console.
  2. Once booted, choose to use the **Recovery Console**
  3. **Choose** which **Windows installation** you need to log into. if there’s only one on that machine, it will be “1?.
  4. **Type** **in** the **Administrator password**.
  5. You need to then copy a version of the file that isn&#8217;t corrupted, over the one that is. Type:** Copy d:i386csrsrv.dll c:windowssystem32csrsrv.dll**
  6. **Restart the Computer**

_This command also may indicated Harddrive failure. Scan with a Hard Drive tool such as Spinrite or HDD Regenerator to make sure the drive is in good condition._
