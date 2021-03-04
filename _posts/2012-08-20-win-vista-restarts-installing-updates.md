---
title: Windows Vista continuous restarts installing updates
date: 2012-08-21 03:27:36 +12:00
permalink: "/win/win-vista-restarts-installing-updates/"
categories:
- Windows
id: 1560
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1560
dsq_thread_id:
- '920762219'
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
- '7'
---

_One of the common causes of Windows Vista problems is due to Windows Updates; especially when it forces the computer to continuously restart follow the prompts below to repair._

<ol start="1">
  <li>
    First off, you need a Windows Vista DVD or related CD/DVD you can access the files on the Windows installed partition.
  </li>
  <li>
    Using the Windows Vista DVD as an example you need to <strong>Boot</strong> from the <strong>DVD</strong>
  </li>
  <li>
    Once the Windows Vista DVD displays the first dialog Window giving you the options to install click <strong>Repair</strong> <strong>My</strong> <strong>Computer</strong> <em>(below the Install).</em>
  </li>
  <li>
    <strong>Select</strong> the Windows Vista <strong>installation</strong> you would <strong>like</strong> <strong>to</strong> <strong>edit</strong> <em>(you would usually only have one).</em>
  </li>
  <li>
    You should now have the Windows System Recovery dialog window, click <strong>Command Prompt</strong>.
  </li>
  <li>
    Once you are greeted with a blinking cursor <strong>type<em>: del c:WindowsSoftwareDistribution</em></strong><em> </em>> Press <strong>Enter</strong>
  </li>
  <li>
    This will delete the folder that contains all the temp files for Windows Updates <em>(it will regenerate itself, so safe to delete)</em>.
  </li>
  <li>
    Now <strong>type</strong>: <strong>cd Windows</strong>
  </li>
  <li>
    <strong>Type</strong>: <strong><em>cd winsxs</em></strong>
  </li>
  <li>
    <strong>Type</strong>: <strong><em>del pending.xml</em> </strong>> Press <strong>Enter</strong>
  </li>
  <li>
    Now <strong>restart</strong> your computer, it should now load Windows properly.
  </li>
</ol>