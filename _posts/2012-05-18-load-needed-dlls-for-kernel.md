---
id: 1325
title: Load needed DLLs for Kernel
date: 2012-05-18T12:00:24+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1325
permalink: /win/load-needed-dlls-for-kernel/
dsq_thread_id:
  - "866276773"
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
  - "24"
categories:
  - Windows
---
  1. First thing you need to have a Windows XP CD
  2. Put CD in drive and **boot** from it, you may have to press ESC or F8 to open Boot Prompt to select CD Drive.
  3. Once it has loaded choose Recovery Console
  4. Type: **_chkdsk /r /f c:_**
  5. Press Y
  6. This may take an hour or two to complete, once it has completed type: BOOTCFG /rebuild (Press Enter for prompt)
  7. Type: **_fixboot_** and press Enter
  8. Type: **_fixmbr_** and press Enter
  9. Restart your computer which should now be loading Windows properly.