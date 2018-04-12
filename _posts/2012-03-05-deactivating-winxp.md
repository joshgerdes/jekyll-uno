---
id: 3063
title: Deactivating Windows XP
date: 2012-03-05T15:30:20+00:00
author: Luke
layout:
  - ""
guid: http://techdrive.co.nz/?p=956
permalink: /win/deactivating-winxp/
dsq_thread_id:
  - "2563286709"
  - "2563286709"
  - "2563286709"
  - "2563286709"
omc_review_enable:
  - "0"
  - "0"
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
  - wp
  - wp
sidebar:
  - ""
header:
  - 'yes'
footer:
  - ""
slide_template:
  - default
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
mfn-post-love:
  - "0"
post_views_count:
  - "5"
header_title_bar:
  - ""
header_transparency:
  - ""
categories:
  - Windows
---
Deactivating Windows XP can be useful especially when moving the Windows XP install from one computer to another as it makes Windows activation easier and more automated.

Follow the simple guide below to make the necessary Registry change to deactivate your Windows XP version.

**Deactivating Windows XP**

<ol style="font-family: sans-serif; font-size: medium; font-style: normal; line-height: normal;">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type &#8216;<strong>regedit</strong>&#8216;
  </li>
  <li>
    Navigate to
  </li>
  <li>
    <strong><em>HKEY_LOCAL_MACHINE/Software/Microsoft/WindowsNT/Current Version/WPAEvents</em></strong>
  </li>
  <li>
    <strong>Double</strong>&#8211;<strong>click <em>OOBETimer</em></strong>, when the box comes up, <strong>change</strong> the <strong>LAST</strong> <strong>TWO</strong> HEX <strong>VALUES</strong> to nulls(<strong><em>00 00</em></strong>)
  </li>
</ol>

&nbsp;

**Reactivating Windows XP**

<ol style="font-family: sans-serif; font-size: medium; font-style: normal; line-height: normal;">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type &#8220;<strong>c:\windows\system32\oobe\msoobe.exe /a</strong>&#8220;
  </li>
  <li>
    Press <strong>Enter</strong>
  </li>
</ol>