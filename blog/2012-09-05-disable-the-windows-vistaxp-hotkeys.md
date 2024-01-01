---
title: Disable the Windows Vista/XP Hotkeys
date: 2012-09-05T18:31:58+00:00
authors: [Luke]
tags:
  - Windows
---
  1. Click **Start**
  2. In the Search box type **_regedit.exe_**
  3. Press Enter
  4. In the registry editor locate to: _**HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesExplorer**_
  5. **Create** a 32-bit DWORD **value** called **_NoWinKeys_** and set the value to **1**.
  6. You’ll need to **log** on and back **off** for the **changes** to take effect.