---
title: Enabling Remote Desktop connections remotely
categories:
  - Windows
date: 2014-12-23 00:00:00 +1300
---
Enabling remote desktop remotely can be done from an elevated command prompt. This will set your Remote Desktop settings to &#8220;Allow connections from computers running any version of Remote Desktop (less secure).

  1. Open an elevated Command Prompt _(one with the permissions of the local administrator on the remote machine)_
  2. Type in:  `reg add "\\<servername>\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0`
  3. Where <Servername> is your Remote machine host-name or IP address. Once filled out press Enter to remotely set Remote Desktop.
