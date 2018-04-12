---
id: 1533
title: How to stop SysPrep from starting
date: 2012-09-30T02:24:30+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1533
permalink: /win/stop-sysprep-starting/
dsq_thread_id:
  - "4823069105"
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
mfn-post-love:
  - "0"
post_views_count:
  - "25"
categories:
  - Windows
---
_Having issues with sysprep popping up all the time? Follow the instructions below to stop that annoyance from happening._

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type: <strong><span style="text-decoration: underline;">regedit</span></strong>
  </li>
  <li>
    Once the <strong>Registry</strong> Editor loads, navigate to: <strong><em>HKEY_LOCAL_MACHINESYSTEMSetup</em></strong>
  </li>
  <li>
    Now to the right you should see some registry entries which you need to edit.
  </li>
  <li>
    <strong>Change AuditInProgress to “0”</strong>
  </li>
  <li>
    <strong>Change cmdLine to “setup –newsetup”</strong>
  </li>
  <li>
    <strong>Change FactoryPreInstallInProgress to “0”</strong>
  </li>
  <li>
    <strong>Change MiniSetupInProgress to “0”</strong>
  </li>
  <li>
    <strong>Change SetupType to “0”</strong>
  </li>
  <li>
    <strong>Change SystemSetupInProgress to “0”</strong>
  </li>
</ol>

_You are pretty much changing Yes I do want to run SysPrep to No I don’t want to._

<ol start="1">
  <li>
    Finally, <strong>navigate</strong> to: <strong><em>HKEY_LOCAL_MACHINEMicrosoftFactory</em></strong> and <strong>delete</strong> <strong>Factory</strong>.
  </li>
</ol>

_You are now safe to delete the SYSPREP folder where it may be (ie C:SYSPREP)_