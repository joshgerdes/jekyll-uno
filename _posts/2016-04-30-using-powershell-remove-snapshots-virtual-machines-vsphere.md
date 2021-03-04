---
title: Using PowerShell to remove Snapshots from Virtual Machines in vSphere
permalink: /win/using-powershell-remove-snapshots-virtual-machines-vsphere/
categories:
  - Windows
  - PowerShell
---
Although vSphere 5.5 has a scheduled task to create Snapshots, it appears to be missing a scheduled task to remove them.

I had to find a way of automating the removal of the Snapshots for specific Virtual Machines at a specific time _(ie not during business hours)_.

To do this required 3 things, a Scheduled Task and a PowerShell script using the VMWare Snapin and a TXT document with the hostname of the Virtual Machine that needs the Snapshot to be removed.

This script is quite simple – it connects to the vSphere server, checks for a VM name under a TXT document that people add their servers to and then when the scheduled task runs it removes the Snapshot for that VM and clears the TXT document ready for the next day.

{% gist 7931cfa391b7562879b383f5dab829ba %}

Note: You can add Credentials for the vSphere connection to the script, however, I am running the script under a Service Account that has been granted Remove Snapshot rights.
