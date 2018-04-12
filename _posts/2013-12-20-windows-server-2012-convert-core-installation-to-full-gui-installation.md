---
id: 2909
title: Windows Server 2012 – Convert Core installation to full GUI installation
date: 2013-12-20T21:28:04+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2909
permalink: /win/windows-server-2012-convert-core-installation-to-full-gui-installation/
dsq_thread_id:
  - "4830530527"
mfn-post-love:
  - "0"
post_views_count:
  - "23"
categories:
  - Windows
---
  1. You have to have administration rights for this – open an elevated powershell prompt and type: <span style="color:#2a2a2a;font-family:Segoe UI;font-size:10pt;background-color:white"><strong>Install-WindowsFeature Server-Gui-Mgmt-Infra, Server-Gui-Shell –Restart </strong>press Enter for the cmdlet to install the Server 2012 user interface.</span>