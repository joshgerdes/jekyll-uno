---
id: 1102
title: 'Hybserv2 &#8220;Unable to open SET PATH&#8221;'
date: 2012-03-14T11:00:28+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1102
permalink: /linux/hybserv2-setpath/
dsq_thread_id:
  - "4821789351"
  - "4821789351"
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
  - "32"
categories:
  - Linux
  - Windows
---
Getting the Hybserv2 &#8220;Unable to open SETPATH&#8221; error? Follow the instructions below to repair.

**Windows**

  1. **Right** **click** on My **Computer**
  2. **Left** **click** on **Properties**
  3. Left click on **Advanced** **System** **Settings**
  4. Left click on **Environment** **Variables**.
  5. **Enter** **new** system **variable** with **name** &#8220;**PATH**&#8221; and **value** (The **path** for your **Perl/bin folder**).

**Linux**

  1. **Open** a **Terminal**
  2. **Type**: **cd include**
  3. Press **Enter**
  4. **Type pico config.**h
  5. Type: **\# define SETPATH &#8220;/home/USER/hybserv/etc/settings.conf**
  6. **Save **