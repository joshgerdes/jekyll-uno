---
title: How to disable automatic restarts in Windows 7 due to Windows Updates
date: 2012-10-02 16:47:38 +13:00
permalink: "/win/how-to-disable-automatic-restarts-in-windows-7-due-to-win-updates/"
categories:
- Windows
id: 1470
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1470
dsq_thread_id:
- '912387543'
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
- '5'
---

&nbsp;

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    In the search field <strong>type</strong>: <strong><em>regedit</em></strong>
  </li>
  <li>
    Click the <strong><em>regedit.exe</em></strong> result to open Registry Editor
  </li>
  <li>
    <strong>Navigate</strong> to: <strong><em>HKEY_LOCAL_MACHINE/SOFTWARE/Polices/Microsoft/Windows</em></strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> an empty space in the right area and select <strong>New</strong>
  </li>
  <li>
    Click <strong>Key</strong>
  </li>
  <li>
    <strong>Name</strong> the new key: <strong><em>WindowsUpdate</em></strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> the new WindowsUpdate <strong>key</strong>
  </li>
  <li>
    Select <strong>New</strong>
  </li>
  <li>
    Click <strong>Key</strong>
  </li>
  <li>
    <strong>Name</strong> the new <strong>key</strong>: <strong><em>AU</em></strong>
  </li>
  <li>
    <strong>Select</strong> the key key and <strong>right</strong> <strong>click</strong> and empty area
  </li>
  <li>
    Select <strong>New</strong>
  </li>
  <li>
    Click <strong>DWORD</strong> (32-bit) value
  </li>
  <li>
    <strong>Name</strong> the <strong>DWORD</strong>: <strong><em>NoAutoRebootWithLoggedOnUsers</em></strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> <strong><em>NoAutoRebootWithLoggedOnUsers</em></strong>
  </li>
  <li>
    Select <strong>Modify</strong>
  </li>
  <li>
    Enter “<strong>1</strong>” in the value box
  </li>
  <li>
    Click <strong>Ok</strong>
  </li>
  <li>
    <strong>Close</strong> regedit
  </li>
</ol>

_Restart your computer and Windows should no longer restart due to automatic Windows Updates_