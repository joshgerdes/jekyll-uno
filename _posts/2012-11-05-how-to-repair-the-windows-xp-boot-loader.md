---
id: 2508
title: How to repair the Windows XP boot loader
date: 2012-11-05T14:11:23+00:00
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2508
permalink: /win/how-to-repair-the-windows-xp-boot-loader/
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
dsq_thread_id:
  - "1055398697"
mfn-post-love:
  - "0"
post_views_count:
  - "12"
categories:
  - Windows
---
What you need.

  * Windows XP CD _(doesn’t matter whether Home or Professional)_

&nbsp;

  1.  Boot the computer from the Windows XP disk at start-up
  2. Once greeted with the Welcome to Windows XP setup screen select Recovery Console.
  3. Select your Windows installation _(if prompted)_.
  4. Type:  _fixboot_ 
  5. Press Enter
  6. Press Y
  7. Type: _fdisk /mbr_
  8. Press Enter
  9. Restart the computer and remove the Windows XP CD.