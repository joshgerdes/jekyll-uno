---
title: Shutdown Batch Script
date: 2013-01-18 04:38:04 +13:00
permalink: "/misc/shutdown-batch-script/"
categories:
- Misc
- Windows
id: 2642
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2642
dsq_thread_id:
- '2527421407'
mfn-post-love:
- '0'
post_views_count:
- '8'
---

Save the following into a notepad document and name it with .bat at the end &#8211; for example shutdown.BAT. You can then either set it to the desktop or add it to a scheduled task to turn your computer off at a certain time.

`<br />
@echo off<br />
shutdown.exe -s -t 00<br />
exit<br />
` 

Note: Changing &#8220;-s&#8221; to &#8220;-r&#8221; will restart the computer, instead of turning it off and adjusting the &#8220;-t&#8221; will change the time in seconds till it shuts down. Useful if you are wanting the computer to shutdown after an hour or so.