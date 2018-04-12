---
id: 3452
title: How to see what users are currently logged into a Windows system
date: 2014-09-06T20:00:53+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3452
permalink: /win/how-to-see-what-users-are-currently-logged-into-a-windows-system/
mfn-post-love:
  - "0"
post_views_count:
  - "17"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4987888782"
categories:
  - Windows
---
<span style="font-size: 1pt;">Bein</span>Being able to determine who is currently logged into a particular Windows system – such as a server can be useful for identify performance problems and notifying the relevant users of an impending restart.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Method_1"><span class="toc_number toc_depth_1">1</span> Method 1</a>
    </li>
    <li>
      <a href="#Method_2"><span class="toc_number toc_depth_1">2</span> Method 2</a>
    </li>
  </ul>
</div>

### <span id="Method_1">Method 1</span>

  1. Open a command prompt on the machine
  2. Type in: **quser**
  3. This will list the users currently logged in and what type of session are they using.

&nbsp;

Note: If you have opened an elevated command prompt you can use: **quser /server:Servername** to show logged on users on remote machines.

### <span id="Method_2">Method 2</span>

  1. Open Task Manager (by clicking CTRL+ALT+DEL) on the PC
  2. Click on the Users Tab – up the top.
  3. This will list the users currently logged in and what type of session are using.