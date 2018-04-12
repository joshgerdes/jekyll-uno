---
id: 1125
title: OSX Freezing when accessing Network Preferences
date: 2012-03-21T12:36:07+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1125
permalink: /osx/osx-freezing-accessing-network/
dsq_thread_id:
  - "865073041"
  - "865073041"
omc_review_enable:
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "5"
categories:
  - Mac OSX
---
This usually happens, when some of the OSX settings become corrupted. OSX can regenerate new settings, which should resolve your problem. Follow the settings below:

  1. Open **Finder**
  2. **Navigate** to your **hard****drive**
  3. **Go** to /**Library**/**Prefences**
  4. Drag **System****Configuration** folder to **Trash**
  5. Now **open****Network****Preferences**, the System Configuration folder should reappear and OSX should not freeze.

If the above doesn&#8217;t work then delete these files:

_Library/Preferences/com.apple.systempreferences.plist_

_Library/Preferences/com.apple.NetworkUtility.plist_