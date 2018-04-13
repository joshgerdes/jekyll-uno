---
title: Icons missing in Windows 7
permalink: /win/icons-missing-in-windows-7/
categories:
  - Windows
---
Try the following fixes below:

  1. Open **Task** **Manager** (Ctrl+Shift+Esc)
  2. Click **Process**
  3. **Right** **click** **Explorer**.exe and choose **End** **Task**
  4. Click File
  5. Click **Run**
  6. Type in: **_cmd.exe_** then press Ok
  7. Type:
  8. **_CD /d %USERPROFILE%_**<wbr>**_AppDataLocal_** &#8211; Then press **Enter**</wbr>
  9. **_DEL IconCache.db /a_** &#8211; Then press Enter
 10. EXIT &#8211; Then press Enter
 11. Click File
 12. Click **Run**
 13. Type **Explorer**.exe
