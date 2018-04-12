---
id: 3471
title: Enabling Remote Desktop connections remotely
date: 2014-12-23T18:53:43+00:00
author: Luke
layout:
  - ""
guid: http://techremedy.co.nz/?p=3471
permalink: /win/enabling-remote-desktop-connections-remotely/
mfn-post-love:
  - "0"
dsq_thread_id:
  - "4987888180"
post_views_count:
  - "43"
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
categories:
  - Windows
---
Enabling remote desktop remotely can be done from an elevated command prompt. This will set your Remote Desktop settings to &#8220;Allow connections from computers running any version of Remote Desktop (less secure)&#8221;

&nbsp;

  1. Open an elevated Command Prompt _(one with the permissions of the local administrator on the remote machine)_
  2. Type in:  `reg add "\\<servername>\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0`
  3. Where <Servername> is your Remote machine host-name or IP address. Once filled out press Enter to remotely set Remote Desktop.

&nbsp;