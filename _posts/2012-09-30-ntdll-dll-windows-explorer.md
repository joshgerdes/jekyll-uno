---
title: ntdll.dll Windows Explorer
date: 2012-10-01 02:42:29 +13:00
permalink: "/win/ntdll-dll-windows-explorer/"
categories:
- Windows
id: 1438
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1438
dsq_thread_id:
- '2756255649'
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
- '15'
---

Having problems with Windows Explorer with the “ntdll.dll” error? This usually occurs when you are running an AMD system.

&nbsp;

<ol start="1">
  <li>
    <strong>Right</strong> <strong>click</strong> My <strong>Computer</strong>
  </li>
  <li>
    Click <strong>Properties</strong>
  </li>
  <li>
    Click on <strong>Advanced</strong>
  </li>
  <li>
    Click <strong>Environment Variables</strong>
  </li>
  <li>
    Look for “<strong><em>NLSPATH</em></strong>” and <strong>delete</strong>/rename it
  </li>
  <li>
    Press <strong>Ok</strong>
  </li>
</ol>

_Another issue is with Data Execution Prevention, follow the prompts below_:

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Control Panel</strong>
  </li>
  <li>
    Click <strong>System</strong>
  </li>
  <li>
    Click the <strong>Advanced</strong> Tab
  </li>
  <li>
    Click <strong>Settings</strong>
  </li>
  <li>
    <strong>Click</strong> on <strong>Data Execution Prevention</strong>
  </li>
  <li>
    Click on “<strong><em>Turn on DEP for all Programs and Services Except Those I Select</em></strong>”
  </li>
  <li>
    Click <strong>Add</strong>
  </li>
  <li>
    Browse to <strong><em>c:Windowsexplorer.exe</em></strong>
  </li>
  <li>
    Click <strong>Add</strong>
  </li>
  <li>
    Click <strong>Ok</strong>
  </li>
  <li>
    <strong>Restart</strong> your machine.
  </li>
</ol>