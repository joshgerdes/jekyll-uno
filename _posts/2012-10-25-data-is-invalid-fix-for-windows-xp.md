---
title: Data Is Invalid fix for Windows XP
date: 2012-10-25 00:00:00 +1300
author: Luke
categories:
  - Windows
---
Having issues trying to install device drivers in Windows XP and its stopping half way through and giving you the “Data is Invalid” error? Following the guide below to repair.

What you need

* Windows XP Home/Professional CD

  1. Open My **Computer**
  2. Navigate to: **C:WINDOWSDRIVERCACHEi386**
  3. **Delete** the **_driver.cab_** file.
  4. Now **copy** the **_driver.cab_** file from the i386 folder from your Windows XP CD into the **_C:WINDOWSDRIVERCACHEi386_** folder.
  5. **Right** click **My Computer**
  6. Left click **Properties**
  7. Click **Hardware**
  8. Click **Device Manager**
  9. **Right** **click** the device you were attempting to install _(should have a yellow exclamation mark next to it)_ select **Uninstall** then restart your computer.

_You should now be able to re-install the device drivers._
