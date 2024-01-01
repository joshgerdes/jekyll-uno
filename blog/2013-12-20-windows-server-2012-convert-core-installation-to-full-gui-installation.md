---
title: Windows Server 2012 – Convert Core installation to full GUI installation
tags:
  - Windows
date: 2013-12-20 00:00:00 +1300
---

  1. You have to have administration rights for this – open an elevated powershell prompt and type: **Install-WindowsFeature Server-Gui-Mgmt-Infra, Server-Gui-Shell –Restart** press Enter for the cmdlet to install the Server 2012 user interface.
