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

The main goals for WebJEA:

* Reduce delegation of privileged access to users
* Quickly automate on-demand tasks and grant access to less-privileged users
* Leverage your existing knowledge in PowerShell to build web forms and automate on-demand processes
* Encourage proper script creation by parsing and honouring advanced function parameters and comments

Because WebJEA is simply a Self-Service Portal for PowerShell scripts, anything that you can script with PowerShell can be run through the Portal! Opening a lot of opportunities for automation, without having to learn third party automation toolsets! Anyone who knows PowerShell can use it! Each script can be locked down to specific users and AD groups!

This guide will concentrate on setting up WebJEA for self-service Azure Resource creation, however, can be used to enable much more self-service automation.

We will use a Windows Server 2019, running in Microsoft Azure, to run WebJEA from, and an Azure Keyvault to retrieve the secrets.

### Prerequisites

* Domain Joined server running Windows 2016+ Core/Full with PowerShell 5.1 
* The server must have permission to go out over the internet to Azure and be able to download PowerShell modules.
* CPU/RAM Requirements will depend significantly on your usage, start off low _(2-vCPU/4GB RAM)_ and grow as needed. 

I've created a StandardB2ms (2vCPU, 8GB RAM) virtual machine, called: WEBJEA-P01 in an Azure Resource Group called: webjea_prod.