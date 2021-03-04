---
title: Plug &#038; Play Software Enumerator No Sound Win XP
date: 2012-10-01 14:52:56 +13:00
permalink: "/win/pnp-enum-no-sound/"
categories:
- Windows
id: 1504
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1504
dsq_thread_id:
- '4967548225'
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
- '21'
---

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Programs</strong>
  </li>
  <li>
    Click <strong>Accessories</strong>
  </li>
  <li>
    Click <strong>Command Prompt</strong>
  </li>
  <li>
    <strong>Type</strong>:  <strong><em>md temp</em></strong> | press Enter
  </li>
  <li>
    Now we need to change to it type: <strong>Type</strong>:  <strong><em>cd temp</em></strong> | press Enter
  </li>
  <li>
    <strong>Type</strong>:  <strong><em>copy %windir%infmachine.inf tempallmachine.inf</em></strong> <em>(That will copy the “machine.inf to our newly created folder”)</em>
  </li>
  <li>
    <strong>Type</strong>:  <strong><em>copy %windir%system32driversswenum.sys temp</em></strong>
  </li>
  <li>
    <strong>Type</strong>: <strong><em>copy %windir%system32streamci.dll temp</em></strong>
  </li>
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>My Computer/Computer</strong>
  </li>
  <li>
    Click on <strong>C</strong>:
  </li>
  <li>
    <strong>Navigate</strong> into <strong>Temp</strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> “<strong><em>allmachine.inf</em></strong>”
  </li>
  <li>
    Left click <strong>Open</strong> With, <strong>Notepad</strong>
  </li>
  <li>
    Click <strong>Edit</strong>
  </li>
  <li>
    Click <strong>Go</strong> To..
  </li>
  <li>
    Type in “<strong><em>22</em></strong>” > press Enter
  </li>
  <li>
    Select and <strong>delete</strong>: <strong><em>ExcludeFromSelect=*</em></strong>
  </li>
  <li>
    Click File, <strong>Save</strong>.
  </li>
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> My Computer/<strong>Computer</strong>
  </li>
  <li>
    Left click <strong>Properties</strong>
  </li>
  <li>
    Click <strong>Hardware</strong>
  </li>
  <li>
    Click <strong>Device</strong> <strong>Manager</strong>
  </li>
  <li>
    Click <strong>Add</strong> <strong>Hardware</strong> <em>(may be under ActionsAdd Hardware)</em>
  </li>
  <li>
    Click <strong>Have</strong> <strong>Disk</strong>
  </li>
  <li>
    <strong>Browse</strong> to c:/<strong>Temp</strong>
  </li>
  <li>
    A list of devices should now appear select Plug and Play Software Enumerator and click <strong>Install</strong>
  </li>
</ol>