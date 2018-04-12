---
id: 1284
title: You have exceeded your profile space in Windows XP
date: 2012-05-11T22:39:32+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1284
permalink: /win/exceeded-your-profile-space-in-win-xp/
dsq_thread_id:
  - "4859745573"
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
  - "16"
categories:
  - Windows
---
You need to make a registry file and load it to fix the issues causing this problem, follow the instructions below:

  1. Click Start
  2. Click Programs
  3. Click Accessories and click Notepad
  4. Copy and paste the following:

<div>
  <p>
    Windows Registry Editor Version 5.00
  </p>
  
  <p>
    [HKEY_CURRENT_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem]<br /> &#8220;EnableProfileQuota&#8221;=-<br /> &#8220;ProfileQuotaMessage&#8221;=-<br /> &#8220;MaxProfileSize&#8221;=-<br /> &#8220;IncludeRegInProQuota&#8221;=-<br /> &#8220;WarnUser&#8221;=-<br /> &#8220;WarnUserTimeout&#8221;=-
  </p>
</div>

  1. Click File
  2. Click Save
  3. Save as: fix.reg
  4. Run the fix.reg
  5. Restart your computer

&nbsp;

&nbsp;