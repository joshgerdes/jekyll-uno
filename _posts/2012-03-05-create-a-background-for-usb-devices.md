---
id: 946
title: Create a background for USB Devices
date: 2012-03-05T18:01:12+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=946
permalink: /win/create-a-background-for-usb-devices/
dsq_thread_id:
  - "866223407"
  - "866223407"
  - "866223407"
  - "866223407"
  - "866223407"
omc_review_enable:
  - "0"
  - "0"
  - "0"
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
  - "0"
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
  - stars
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
  - 'n'
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
  - "0"
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
  - wp
  - wp
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "6"
categories:
  - Windows
---
Follow the instructions below to assign a picture to a folders background, commonly used to personalise USB flash drives.

  1. First, open notepad. _(Start, Run, type in: notepad, press Enter_
  2. Copy the below coding to the notepad:

[ExtShellFolderViews]
  
{BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}

[{BE098140-A513-11D0-A3A4-00C04FD706EC}]
  
Attributes=1
  
IconArea_Image=back/back.jpg
  
IconArea_Text=0x00ffffff

Save as autorun.inf and exit
  
Edit the:

IconArea_Image=back/back.jpg _(The location of the JPG image you want to use)_
  
IconArea_Text=0x00ffffff _(Edit this colour in hex to display the Icons text colour)_

&nbsp;