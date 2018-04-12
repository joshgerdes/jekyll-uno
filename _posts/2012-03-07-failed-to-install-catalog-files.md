---
id: 1056
title: Failed to install catalog files
date: 2012-03-07T13:04:02+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1056
permalink: /win/failed-to-install-catalog-files/
dsq_thread_id:
  - "601394346"
  - "601394346"
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
Getting the Failed to install catalog files error? This is how you fix it. The issue is related to registry key security settings.

  1. Click **Start**
  2. Click **Run**
  3. Type in: **command**
  4. Press **enter**
  5. In the command prompt **type**: **secedit /configure /cfg c:Windowsrepairsecsetup.inf /db secsetup.sdb /verbose /areas regkeys**
  6. Press **Enter **

If it reports an error about not knowing where secedit is then you can download it from &#8220;here&#8221;. You need to download it and put it in My Computer/C.