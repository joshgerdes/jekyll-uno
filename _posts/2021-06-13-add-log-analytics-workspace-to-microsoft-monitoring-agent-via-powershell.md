---
date: 2021-06-13 00:00:00 +1200
title: Add a Log Analytics workspace to Microsoft Monitoring Agent using PowerShell
author: Luke
categories:
- PowerShell
toc: false
header:
  teaser: "images/powershell-blog-feature-banner.png"
---
Have you ever wanted to add a Log Analytics workspace to multiple Microsoft Monitoring Agent (MMA)'s before? 

Maybe you are setting up Windows Defender or wanting to redirect to collect event or performance logs. 

This little quick script will help get you started on automating adding a Log Analytics workspace to the MMA agent, even through a proxy.

_Note:  It is recommended to have the latest MMA Agent installed, this is not compatible with SCOM 2012 R2 agents, but the latest agent is supported by SCOM._

{% gist 3f0fa72c545aaa4caef54e66934a7f83 %}
