---
title: .NET Framework not installing through SCCM
tags:
  - Windows
authors: [Luke]
date: 2014-03-28 00:00:00 +1300
---

1. Click **Start**
2. Click **Run** and type in: **services.msc**
3. **Stop** the **Automatic Update** service
4. **Navigate** to: **C:\Windows**
5. **Delete** the: SoftwareDistribution folder
6. **Start** the **Automatic Update** service
7. Double click on the SCCM Update icon in the notification tray and select Install & Install now.
