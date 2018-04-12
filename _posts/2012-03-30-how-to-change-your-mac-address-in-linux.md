---
id: 1160
title: How to change your MAC address in Linux
date: 2012-03-30T09:47:32+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1160
permalink: /linux/how-to-change-your-mac-address-in-linux/
dsq_thread_id:
  - "4987901036"
  - "4987901036"
mfn-post-love:
  - "0"
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
post_views_count:
  - "5"
categories:
  - Linux
---
  1. Open a **Terminal**
  2. Type: **_ifconfig eth0 down_**
  3. Type: **_ifconfig eth0 hw ether THISISWHEREYOUENTERNEWMACADDRESS_**
  4. Type: **_ifconfig eth0 up_**

The mac address change is only temporary, until you restart