---
title: Change the Windows 7 Logon Background
permalink: /win/win7_logon_back/
tags:
  - Windows
---
Want to know how to change your Windows 7 Logon background to something a bit more modern/fancy? Follow the options below.

  1. Launch **Regedit**, and browse to &#8216;**HKEY\_LOCAL\_MACHINESoftwareMicrosoftWindowsCurrentVersionAuthenticationLogonUIBackground**&#8216;.
  2. Double click the dword key called &#8216;**OEM Background**&#8216; (c_reate it if not there_) and set its value to **1**. **Locate** the log-in background image you&#8217;d like to use. It must be a JPG file that&#8217;s less than 245kB in size.
  3. **Copy** the **image** you want to use to **C:Windowssystem32oobeinfobackgrounds** folder.
  4. **Rename** it to **backgroundDefault.jpg**
  5. Restart computer and check out your new handy work.
