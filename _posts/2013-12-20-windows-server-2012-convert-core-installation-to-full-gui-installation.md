---
title: Windows Server 2012 – Convert Core installation to full GUI installation
date: 2013-12-20 00:00:00 +13:00
permalink: "/win/windows-server-2012-convert-core-installation-to-full-gui-installation/"
categories:
- Windows
layout: post
---

  1. You have to have administration rights for this – open an elevated powershell prompt and type: <span style="color:#2a2a2a;font-family:Segoe UI;font-size:10pt;background-color:white"><strong>Install-WindowsFeature Server-Gui-Mgmt-Infra, Server-Gui-Shell –Restart </strong>press Enter for the cmdlet to install the Server 2012 user interface.</span>
