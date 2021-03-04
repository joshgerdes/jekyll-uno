---
title: Using PowerShell to remove App-V packages from a Windows workstation
permalink: /win/using-powershell-remove-app-v-packages-windows-workstation/
categories:
  - Windows
  - PowerShell
---
App-V applications, usually store their data locally if they are not streamed. Sometimes an Application will have problems, either hasn't been downloaded or some other reason.

One of the solutions that can be ran is to clear the App-V package store of a workstation, allowing you to reevaluate and download the packages back to the affected computer.

This script is pretty simple and something I made a year ago for some colleagues experiencing App-V application cache issues so decided to share it here. This requires the App-VClient PowerShell module to be installed which is installed by default as part of the App-V client.

{% gist 9fe9be2c307615c773fe3648f7ca3f9c %}