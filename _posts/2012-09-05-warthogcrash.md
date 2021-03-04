---
title: DCS A10 C Warthog Crashing Windows Vista/Windows 7
date: 2012-09-06 05:58:26 +12:00
permalink: "/win/warthogcrash/"
categories:
- Windows
id: 954
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=954
dsq_thread_id:
- '5328576940'
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
mfn-post-love:
- '0'
post_views_count:
- '11'
---

Having random crashes on DCS A10 C Warthog? With Texture mismatches and Runtime errors? This is usually due to security permissions inside Windows.

  1. Click Start
  2. In the Search field, type: CMD. Then press enter.
  3. Type** _bcdedit /set increaseuserva 3072_** and press enter

_You may need to temporarily disable UAC/run as administrator for this to work_

_If you wish to reverse this command back to default, simply use &#8220;bcdedit /deletevalue increaseuserva&#8221;_