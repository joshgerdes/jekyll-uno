---
id: 3703
title: Using PowerShell to remove Snapshots from Virtual Machines in vSphere
date: 2016-04-30T16:46:37+00:00
author: Luke
layout:
  - ""
guid: http://luke.geek.nz/?p=3703
permalink: /win/using-powershell-remove-snapshots-virtual-machines-vsphere/
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
post_views_count:
  - "58"
dsq_thread_id:
  - "4790226402"
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
categories:
  - Windows
---
Although vSphere 5.5 has a scheduled task to create Snapshots, it appears to be missing a scheduled task to remove them.

I had to find a way of automating the removal of the Snapshots for specific Virtual Machines at a specific time _(ie not during business hours)_.

To do this required 3 things, a Scheduled Task and a PowerShell script using the VMWare Snapin and a TXT document with the hostname of the Virtual Machine that needs the Snapshot to be removed.

This script is quite simple – it connects to the vSphere server, checks for a VM name under a TXT document that people add their servers to and then when the scheduled task runs it removes the Snapshot for that VM and clears the TXT document ready for the next day.

<div class="oembed-gist">
  <noscript>
    View the code on <a href="https://gist.github.com/lukemurraynz/7931cfa391b7562879b383f5dab829ba">Gist</a>.
  </noscript>
</div>

Note: You can add Credentials for the vSphere connection to the script, however I am running the script under a Service Account that has been granted Remove Snapshot rights.

Feel free to add any comments, suggestions to the comments section below.