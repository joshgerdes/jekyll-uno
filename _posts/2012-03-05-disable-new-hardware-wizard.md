---
id: 2626
title: Disable New Hardware Wizard in Windows XP to Enable Automatic Device Driver Installation
date: 2012-03-05T18:17:55+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1016
permalink: /win/disable-new-hardware-wizard/
dsq_thread_id:
  - "4915608189"
  - "4915608189"
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
  - "21"
categories:
  - Windows
---
Want to skip straight to automatic hardware installation? Follow the instructions below to edit the registry.

  1. Click **Start**
  2. Click **Programs**
  3. Click Accessories
  4. Click **Notepad**
  5. Copy the script below:

<div>
  <p>
    <em>REGEDIT4</em>
  </p>
  
  <p>
    <em>[HKEY_LOCAL_MACHINESOFTWAREPoliciesMicrosoftWindowsDriverSearching]</em><br /> <em> &#8220;DontSearchWindowsUpdate&#8221;=dword:00000001</em><br /> <em> &#8220;DontPromptForWindowsUpdate&#8221;=dword:00000001</em><br /> <em> &#8220;DontSearchCD&#8221;=dword:00000001</em><br /> <em> &#8220;DontSearchFloppies&#8221;=dword:00000001</em>
  </p>
  
  <p>
    <em>[HKEY_CURRENT_USERSoftwarePoliciesMicrosoftWindows NTDriver Signing]</em><br /> <em> &#8220;behaviorOnFailedVerify&#8221;=dword:00000000</em>
  </p>
  
  <p>
    <em>[HKEY_USERS.DEFAULTSoftwarePoliciesMicrosoftWindows NTDriver Signing]</em><br /> <em> &#8220;behaviorOnFailedVerify&#8221;=dword:00000000</em>
  </p>
</div>

  1. **Paste** into Notepad
  2. Click File
  3. Click **Save As**
  4. Name the file &#8220;**_DisableHardware.bat_**&#8220;
  5. **Run** the file & accept all changes.