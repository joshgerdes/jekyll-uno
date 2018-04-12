---
id: 3350
title: How to clear the local workstations Group Policy cache
date: 2014-07-01T14:16:24+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3350
permalink: /win/clear-local-workstations-group-policy-cache/
dsq_thread_id:
  - "4791012662"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
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
  - "237"
categories:
  - Windows
---
<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Option_1"><span class="toc_number toc_depth_1">1</span> Option 1</a>
    </li>
    <li>
      <a href="#Option_2"><span class="toc_number toc_depth_1">2</span> Option 2</a>
    </li>
    <li>
      <a href="#Option_3"><span class="toc_number toc_depth_1">3</span> Option 3</a>
    </li>
  </ul>
</div>

## <span id="Option_1">Option 1</span>

  1. Open My Computer/Computer
  2. In the URL or address bar paste: %windir%\system32\GroupPolicy
  3. Right click and delete the: Machine and User folders to clear local group policy cache
  4. Restart the computer to reapply the group policies

Note: You can also run: gpupdate /force on the machine to force the policy to reapply.

## <span id="Option_2">Option 2</span>

  1. Delete the &#8220;HKLM\Software\Policies\Microsoft&#8221; Key (looks like a folder).
  2. Delete the &#8220;HKCU\Software\Policies\Microsoft&#8221; Key
  3. Delete the &#8220;HKCU\Software\Microsoft\Windows\CurrentVersion\Group Policy Objects&#8221; Key.
  4. Delete the &#8220;HKCU\Software\Microsoft\Windows\CurrentVersion\Policies&#8221; Key.

## <span id="Option_3">Option 3</span>

  1. Remove the computer from the domain &#8211; (change to a Workgroup)
  2. Restart computer
  3. Run gpupdate /force
  4. Rejoin the domain

&nbsp;