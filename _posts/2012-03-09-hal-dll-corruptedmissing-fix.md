---
title: hal.dll Corrupted/Missing Fix
date: 2012-03-09 00:00:00 +13:00
permalink: "/win/hal-dll-corruptedmissing-fix/"
categories:
- Windows
---

Windows could not start because the following file is missing or corrupt:
  
Windows/system32/hal.dll
  
Please re-install a copy of the above file

  1. **Boot** using **Windows** Setup **CD**
  2. Go into the **Recovery** **Console** by pressing &#8220;R&#8221;.
  3. Select the appropriate Windows install
  4. Enter the administrator password
  5. **Type** the **following** in the console and then press enter (Each line is one different command)
  6. **Attrib -H -R -S C:Boot.ini**
  7. **Del C:Boot.ini**
  8. **BootCfg /Rebuild**
  9. **Fixboot**
 10. **Restart** PC
