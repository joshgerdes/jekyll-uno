---
title: Ubuntu &#8211; Wireless is disabled by hardware switch
date: 2012-11-14 01:45:07 +13:00
permalink: "/linux/ubuntu-wireless-is-disabled-by-hardware-switch/"
categories:
- Linux
id: 2539
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2539
mfn-post-love:
- '0'
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
dsq_thread_id:
- '2490779993'
post_views_count:
- '8'
---

This commonly occurs right after an upgrade/update to the operating system.

  1. First thing is first – your laptop will probably have a Wireless On & Off feature which is either on the side of the laptop chassis or front usually in the form of a button or switch. If it’s off, turn it on!
  2. If the wireless is turned on and you are still getting an issue open a Terminal and type: `sudo rfkill unblock wifi`
  3. Press Enter
  4. You should now be able to access the wireless.

If neither of the above work – then the problem most likely is you’re wireless on & off switch and it might need to be rewired to be permanently on.