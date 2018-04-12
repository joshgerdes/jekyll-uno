---
id: 2918
title: Windows 7 – Authentication prompt for cached credentials in a domain environment
date: 2013-12-23T17:00:58+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2918
permalink: /win/windows-7-authentication-prompt-for-cached-credentials-in-a-domain-environment/
dsq_thread_id:
  - "4987904668"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
mfn-post-love:
  - "0"
post_views_count:
  - "11"
categories:
  - Windows
---
  1. <span style="color: black; font-family: Tahoma; font-size: 12pt;">In order to fix this – you need to close all Internet Explorer windows.<br /> </span>
  2. <span style="color: black; font-family: Tahoma; font-size: 12pt;">Open Credential Manager <em>(start type in: Credential Manager).</em></span>
  3. <span style="color: black; font-family: Tahoma; font-size: 12pt;">Under Windows Credentials – select & remove all associated Username & Passwords.<br /> </span>
  4. <span style="color: black; font-family: Tahoma; font-size: 12pt;">Once removed log the user out and get the user to login again.<br /> </span>
  5. <div>
      <span style="color: black; font-family: Tahoma; font-size: 12pt;">They should now be able to access the Intranet & Internet.</span>
    </div>

&nbsp;

<em style="font-family: sans-serif; font-size: medium;">Note: I have come across this when the users – password has reached expiry so when attempting to login again the user is usually asked to reset his or her password.</em>
  
<em style="font-family: sans-serif; font-size: medium;">Note: Also make sure the proxy details in Internet Explorer are set correctly for your environment.</em>
  
<em style="font-family: sans-serif; font-size: medium;">Note: Also – Windows 8 compatible.</em>