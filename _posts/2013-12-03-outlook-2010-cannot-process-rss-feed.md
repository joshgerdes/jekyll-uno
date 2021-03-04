---
title: Outlook 2010 – Cannot process RSS Feed
layout: post
permalink: /win/outlook-2010-cannot-process-rss-feed/
categories:
  - Windows
---
  1. Open regedit 
  2. Navigate to: <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">HKCU\Software\Microsoft\Office\12.0\Outlook\Options\RSS<br /> </span>
  3. <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">In the: DWORD: Disable<br /> </span>
  4. <span style="color:#333333;font-family:Segoe UI;font-size:10pt;background-color:white">Change the value from 1 to 0 to enable RSS functionality.</span>
