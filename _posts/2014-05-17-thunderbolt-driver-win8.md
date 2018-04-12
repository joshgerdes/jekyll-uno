---
id: 3312
title: ASUS thunderbolt driver working in Windows 8
date: 2014-05-17T13:30:10+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3312
permalink: /win/thunderbolt-driver-win8/
dsq_thread_id:
  - "4822974866"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
mfn-post-love:
  - "0"
post_views_count:
  - "22"
categories:
  - Windows
---
Unfortunately ASUS hasn&#8217;t released driver updates for the Rampage 3 Black edition for Windows 8 or Windows 8.1 and although the on-board Realtek chipset drivers are available through Windows Update &#8211; one of the selling points of this motherboard combo was the Thunderboard audio interface!

Note: Tested in Windows 8.1 64 bit.

  1. First you need to download the Windows 7 thunderbolt drivers &#8211; &#8220;<a style="font-family: sans-serif;font-style: normal" title="ASUS Rampage 3 Black Edition Drivers/Utilities" href="http://support.asus.com/download.aspx?SLanguage=en&m=Rampage%20III%20Black%20Edition&os=30" target="_blank">here</a>&#8220;
  2. Download and extract the drivers to a folder
  3. Press the Windows Key + Pause/Break at the same time to open up your computers System properties
  4. Click Device Manager on the left hand menu (you need full Administrator rights)
  5. Navigate down to the Thunderbolt device &#8211; _it should have an exclamation on it to indicate driver problems_ &#8211; Right click and select Update Driver Software
  6. Select Browse my computer for driver software
  7. Select Let me pick from a list of device drivers on my computer and click Next
  8. Navigate down to Sound Devices and click next
  9. Click Have Disk and navigate to the extracted driver path and select &#8220;USBUAA.inf&#8221; and click Next
 10. Select USB device in the Model window and select Next to force Windows 8 to install the Windows 7 Thunderbolt audio driver
 11. Once installed &#8211; restart your computer and you should now have Thunderbolt audio.