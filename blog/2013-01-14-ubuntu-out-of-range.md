---
title: Ubuntu – Out of range
date: 2013-01-14T08:40:11+00:00
authors: [Luke]
tags:
  - Linux
---

This issue is commonly caused by the screen resolution settings in Ubuntu becoming too high for the actual monitor. This guide is written with the Ubuntu Live CD and version 12.10 in mind.

  1. During start-up select your language when prompted.
  2. Press **F6** (Other Options)
  3. At the end of the command line type: **vga=791**
  4. Press Enter

_Ubuntu should now boot with a resolution of 1024 by 768 (32bit). Click &#8220;<a title="VESA Video Modes" href="http://en.wikipedia.org/wiki/VESA_BIOS_Extensions#Linux_video_mode_numbers" target="_blank">here</a>&#8221; for a Wikipedia link to other Video display choices._

If that doesn&#8217;t work:

Start the Live CD process

  1. **Unplug** the **VGA** port for the monitor for about **5 minutes** &#8211; _allowing Ubuntu to properly start._
  2. **Plug** the monitor back **in** and Ubuntu should automatically select the right resolution and display.