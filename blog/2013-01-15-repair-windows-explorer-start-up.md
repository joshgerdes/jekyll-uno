---
title: Repair Windows Explorer start-up
authors: [Luke]
tags:
  - Windows
date: 2013-01-15 00:00:00 +1300
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