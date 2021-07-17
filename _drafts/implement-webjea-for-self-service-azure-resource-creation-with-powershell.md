---
date: 
title: Implement WebJEA for self-service Azure Resource creation with PowerShell
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
WebJEA allows you to dynamically build web forms for any PowerShell script. WebJEA automatically **parses the script at page load for description, parameters and validation**, **then dynamically builds a form to take input and display formatted output! No webpage knowledge is needed!**

Goals

* The main goals for WebJEA:
* Reduce delegation of privileged access to users
* Quickly automate on-demand tasks and grant access to less-privileged users
* Leverage your existing knowledge in PowerShell to build web forms and automate on-demand processes
* Encourage proper script creation by parsing and honouring advanced function parameters and comments

Because WebJEA is simply a Self-Service Portal for PowerShell scripts, anything that you can script with PowerShell can be run through the Portal! Opening a lot of opportunities for automation, without having to learn third party automation toolsets! Anyone who knows PowerShell can use it! Each script can be locked down to specific users and AD groups!

This guide will concentrate on setting up WebJEA for self-service Azure Resource creation, however, can be used to enable much more self-service automation.

### Prerequisites

* Domain Joined server running Windows 2016 Core/Full with PowerShell 5.1   
  _(Windows 2012 R2 or PowerShell 4.0 (perhaps with a recompile) should work, but it hasn't been tested.)_
* CPU/RAM Requirements will depend significantly on your usage.   
  _My testing shows about 40 MB just to spin up a PowerShell thread plus typical ASP.NET consumption. Your usage will vary greatly depending on what your script does. I'm successfully running WebJEA in production on Windows 2016 core, 2-vCPU, 4GB RAM with light usage._