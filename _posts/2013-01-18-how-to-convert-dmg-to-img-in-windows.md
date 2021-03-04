---
title: How to convert DMG to IMG in Windows
date: 2013-01-18 21:00:16 +13:00
permalink: "/osx/how-to-convert-dmg-to-img-in-windows/"
categories:
- Mac OSX
- Windows
id: 2645
author: Luke
layout:
- ''
guid: http://localhost/incinerate/?p=2645
dsq_thread_id:
- '4810402629'
omc_review_enable:
- '0'
omc_user_ratings_visibility:
- '0'
omc_review_type:
- stars
omc_criteria_display:
- n
omc_featured_post:
- '0'
omc_comment_type:
- wp
sidebar:
- ''
header:
- 'yes'
footer:
- ''
mfn-post-love:
- '0'
post_views_count:
- '107'
---

Downloaded that DMG and want to burn it to a CD/DVD but you’re in a Windows based system? Not a problem! Thanks to the guys at vu1tur for making a cool little utility for doing the conversion.

&nbsp;

  1. First download the software “<a title="DMG to IMG" href="http://vu1tur.eu.org/tools/" target="_blank">here</a>” (_go down to win32 binary to download)_ and extract it to an easy accessible folder, in this guide I am going to use the Desktop.
  2. Click Start
  3. Click Programs/All Programs
  4. Click Accessories
  5. Click Command Prompt
  6. Now you need to type: cd %userprofile%Desktop
  7. Now navigate to the location you saved dmg2img in my case I type: cd dmg_convert
  8. Copy the DMG you would like to convert to IMG into the folder or location you put DMG to IMG and make sure you copy down the name of the DMG file as you will need this in the conversion process.
  9. Back in the command prompt type: _**dmg2img <input.dmg> <output.img>**_ _(for example:  dmg2img OSX.DMG OSX.IMG)_ and press Enter
 10. The DMG will now start to convert to IMG, once completed you will be back at the blinking cursor and you can now burn the IMG file.

&nbsp;

Note: If the DMG was bootable it will retain the bootable partition information when converted, so you can easily boot from the IMG once burnt to a CD/DVD.