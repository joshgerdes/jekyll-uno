---
id: 3065
title: 'Virtual Box   &#8216;Failed, trying without DKMS&#8221;'
date: 2012-03-08T07:28:53+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1058
permalink: /linux/virtual-box-failed-trying-without-dkms/
dsq_thread_id:
  - "2703398883"
  - "2703398883"
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
  - "23"
categories:
  - Linux
---
This means simply, you are missing the <a title="Dynamic Kernel Module Support" href="http://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support" target="_blank">dkms </a>package.

**Ubuntu**

  1. **Open** a **Terminal** type: **apt-get install dkms**
  2. Press **Enter**
  3. Wait for it to **download** & **install**. Try **opening** **Virtual** **Box** Again

**Fedora**

  1. **Open** a **Terminal** type: **yum install dkms**
  2. Press **Enter**
  3. Wait for it to **download** & **install**. Try **opening** **Virtual** **Box** Again

&nbsp;

&nbsp;