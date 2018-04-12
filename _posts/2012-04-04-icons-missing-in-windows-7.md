---
id: 1184
title: Icons missing in Windows 7
date: 2012-04-04T11:25:49+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1184
permalink: /win/icons-missing-in-windows-7/
dsq_thread_id:
  - "4847486330"
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "11"
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

&nbsp;