---
id: 2493
title: The network password needs to be 128 bits or 256 bits depending on your network configuration
date: 2012-10-29T09:36:43+00:00
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2493
permalink: /win/the-network-password-needs-to-be-128-bits-or-256-bits-depending-on-your-network-configuration/
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
  - "4818550060"
mfn-post-love:
  - "0"
post_views_count:
  - "91"
categories:
  - Windows
---
Attempting to enter in your wireless passkey and getting “The network password needs to be 128bits or 256bits depending on your network configuration “error? This usually occurs when the networking stack has been damaged/corrupted. Follow the instructions below to repair:

  1. Click **Start**
  2. Click **Run**
  3. Type in: _**cmd**_
  4. Press **Enter**
  5. The windows Command Prompt should launch, type in: **_netsh winsock reset_**
  6. Press **Enter**
  7. **Restart** your **computer** and attempt wireless connectivity.