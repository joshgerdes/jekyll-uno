---
id: 3069
title: hal.dll Corrupted/Missing Fix
date: 2012-03-09T13:43:55+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1067
permalink: /win/hal-dll-corruptedmissing-fix/
dsq_thread_id:
  - "865874434"
  - "865874434"
omc_review_enable:
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "9"
categories:
  - Windows
---
_Windows could not start because the following file is missing or corrupt:_
  
 _<Windows root>system32hal.dll._
  
 _Please re-install a copy of the above file._

  1. **Boot** using **Windows** Setup **CD**
  2. Go into the **Recovery** **Console** by pressing &#8220;R&#8221;.
  3. Select the appropriate Windows install
  4. Enter the administrator password
  5. **Type** the **following** in the console and then press enter _(Each line is one different command)_
  6. **Attrib -H -R -S C:Boot.ini**
  7. **Del C:Boot.ini**
  8. **BootCfg /Rebuild**
  9. **Fixboot**
 10. **Restart** PC