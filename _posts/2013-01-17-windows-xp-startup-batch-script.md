---
title: Windows XP Startup Batch Script
date: 2013-01-18 04:20:41 +13:00
permalink: "/misc/windows-xp-startup-batch-script/"
categories:
- Misc
- Windows
id: 2640
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2640
dsq_thread_id:
- '2427617853'
mfn-post-love:
- '0'
post_views_count:
- '12'
---

Save the following into a notepad document and name it with .bat at the end &#8211; for example WinXPStartup.BAT. You can then run the batch script directly from the recovery console on a Windows XP CD.

`<br />
@echo off<br />
CD ..<br />
ATTRIB -H C:boot.ini<br />
ATTRIB -S C:boot.ini<br />
ATRIB -R C:boot.ini<br />
del boot.ini<br />
BOOTCFG /Rebuild<br />
CHKDSK /R /F<br />
FIXBOOT<br />
`