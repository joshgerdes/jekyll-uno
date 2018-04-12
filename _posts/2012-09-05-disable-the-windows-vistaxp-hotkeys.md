---
id: 1026
title: Disable the Windows Vista/XP Hotkeys
date: 2012-09-05T18:31:58+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1026
permalink: /win/disable-the-windows-vistaxp-hotkeys/
dsq_thread_id:
  - "865035091"
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
  - "5"
categories:
  - Windows
---
  1. Click **Start**
  2. In the Search box type **_regedit.exe_**
  3. Press Enter
  4. In the registry editor locate to: _**HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesExplorer**_
  5. **Create** a 32-bit DWORD **value** called **_NoWinKeys_** and set the value to **1**.
  6. You’ll need to **log** on and back **off** for the **changes** to take effect.