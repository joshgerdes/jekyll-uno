---
id: 1416
title: Howto repair Windows Boot Loader
date: 2012-09-29T09:03:55+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1416
permalink: /win/repair-win-boot-loader/
dsq_thread_id:
  - "5061530904"
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
  - "22"
categories:
  - Windows
---
First things first! In order to repair the Windows boot loaders you need the appropriate Windows CD/DVD for example: _Windows XP Home/Professional CD for the Windows XP installation & Windows 7 DVD for Windows 7 install._

**Windows XP**

The instructions on repairing this are similar to the [DDL Kernel fix](http://http://luke.geek.nz//load-needed-dlls-for-kernel/ "Load needed DLLs for Kernel").

To access the recover console follow the prompts below:

<ol start="1">
  <li>
    First thing you need to have a Windows XP <strong>CD</strong>
  </li>
  <li>
    Put CD in drive and <strong>boot</strong> from it, you may have to press ESC or F8 to open Boot Prompt to select CD Drive.
  </li>
  <li>
    Once it has loaded choose <strong>Recovery Console</strong>
  </li>
  <li>
    Type: <strong><em>bootcfg /rebuild </em></strong>(This will generate a new Boot.ini file)
  </li>
  <li>
    Press Enter twice at the prompts that follow.
  </li>
  <li>
    Type: <strong><em>fixboot</em></strong>
  </li>
  <li>
    Press Enter
  </li>
  <li>
    Type: <strong><em>fixmbr</em></strong>
  </li>
  <li>
    Press Enter
  </li>
  <li>
    Type: <em>exit </em>(This will restart your computer, eject your CD)
  </li>
</ol>

**Windows Vista/Windows 7**

The bootloader fix for both Windows Vista and Windows 7 is luckily similar.

<ol start="1">
  <li>
    First thing you need to do is get your Windows Vista/Windows 7 <strong>DVD</strong>
  </li>
  <li>
    Put DVD in drive and <strong>boot</strong> from it, once prompted select Repair This Computer (lower left hand side of the Windows dialog)
  </li>
  <li>
    Select your Windows install you want to repair and select Next
  </li>
  <li>
    Now you should be greeted with the <strong>Advanced System Recovery</strong> dialog box, select <strong>Command Prompt</strong>
  </li>
  <li>
    Type: <strong><em>bootrec.exe /FixMbr</em></strong>
  </li>
  <li>
    Press Enter
  </li>
  <li>
    Type: <strong><em>bootrec.exe /FixBoot</em></strong>
  </li>
  <li>
    Press Enter
  </li>
  <li>
    Type: <em>exit </em>(to close the Command Prompt)
  </li>
  <li>
    Restart your machine & eject the CD/DVD ROM.
  </li>
</ol>