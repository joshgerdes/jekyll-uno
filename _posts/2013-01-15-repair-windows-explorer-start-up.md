---
title: Repair Windows Explorer start-up
date: 2013-01-16 00:13:35 +13:00
permalink: "/win/repair-windows-explorer-start-up/"
categories:
- Windows
id: 2637
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2630
dsq_thread_id:
- '1059884588'
mfn-post-love:
- '0'
post_views_count:
- '8'
---

This usually occurs if Viruses or Spyware has infected _explorer.exe_ and changed the registry entry to stop it from starting.

  1. Click Start (orb)
  2. Type in: **regedit**
  3. Press Enter
  4. Navigate to:  **HKEY\_LOCAL\_MACHINESoftwareMicrosoftWindows NTCurrentVersionwinlogon**
  5. Double click the **Shell** entry
  6. Make sure it is set to: **Explorer.exe**
  7. Press Ok
  8. **Restart** your computer

&nbsp;

If the above doesn&#8217;t work attempt a system restore by pressing F8 during Windows Vista boot to bring up the Boot Menu and select Startup Repair.

&nbsp;

_Note: Tested with Windows Vista &#8211; ok_

_Note: Also may work on Windows 7 &#8211; though I haven&#8217;t personally tested this._