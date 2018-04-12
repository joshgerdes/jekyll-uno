---
id: 909
title: Change the Windows 7 Logon Background
date: 2012-03-05T18:05:11+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=909
permalink: /win/win7_logon_back/
dsq_thread_id:
  - "5145649556"
  - "5145649556"
  - "5145649556"
omc_review_enable:
  - "0"
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "9"
categories:
  - Windows
---
Want to know how to change your Windows 7 Logon background to something a bit more modern/fancy? Follow the options below.

  1. Launch **Regedit**, and browse to &#8216;**HKEY\_LOCAL\_MACHINESoftwareMicrosoftWindowsCurrentVersionAuthenticationLogonUIBackground**&#8216;.
  2. Double click the dword key called &#8216;**OEM Background**&#8216; (c_reate it if not there_) and set its value to **1**. **Locate** the log-in background image you&#8217;d like to use. It must be a JPG file that&#8217;s less than 245kB in size.
  3. **Copy** the **image** you want to use to **C:Windowssystem32oobeinfobackgrounds** folder.
  4. **Rename** it to **backgroundDefault.jpg**
  5. Restart computer and check out your new handy work.