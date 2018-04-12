---
id: 2815
title: Outlook 2010 – Cannot process RSS Feed
date: 2013-12-03T21:02:52+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2815
permalink: /win/outlook-2010-cannot-process-rss-feed/
mfn-post-love:
  - "0"
dsq_thread_id:
  - "3658675786"
post_views_count:
  - "7"
categories:
  - Windows
---
  1. Open regedit 
  2. Navigate to: <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">HKCUSoftwareMicrosoftOffice12.0OutlookOptionsRSS<br /> </span>
  3. <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">In the: DWORD: Disable<br /> </span>
  4. <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">Change the value from 1 to 0 to enable RSS functionality.</span>