---
title: Logon Process has failed to create the security options dialog
date: 2012-03-25 00:00:00 +13:00
permalink: "/win/logon-process-failed/"
categories:
- Windows
---

  1. Click Start
  2. Click Run
  3. Type: msconfig
  4. Click Ok
  5. This will open  the System Configuration Utility, click Startup tab up the top
  6. Go through the startup list and uncheck everything other then your Antivirus and any other software you want starting
  7. Press Ok
  8. Restart PC

If the fix above, doesn&#8217;t work then follow this tomorrow:

  1. Click Start
  2. Type: cmd and press Enter
  3. Type: sfc /scannow _(You might need the Windows CD as it will attempt to restore non-corrupt files from the CD onto  the computer)._
  4. Once completed, restart the computer.

If none of the fixes above work, try the following:

  1. Click Start
  2. Click Run
  3. Type:  devmgmt.msc _(This will open Device Manager, which lists your devices)_
  4. In the list, go to System devices
  5. Right Click ACPI Fixed Features
  6. Choose Uninstall
  7. Restart the computer
