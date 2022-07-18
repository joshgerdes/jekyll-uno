---
date: 2022-07-19 00:00:00 +1200
title: Azure Virtual Machine and MAC address software licensing
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
You may need an Azure Virtual Machine to install or license software bound to a media access control address _(MAC address)_.

In Microsoft Azure, you can make changes to the Primary Network interface; these changes include manually setting the IP settings to changing the MAC address - these settings are managed by the underlying Network Interface and Azure host _(if you do inadvertently make changes to this, you will lose connection to the Azure Virtual Machine, until its rebooted and the configuration is reset)_. 

$MACAddress = '000000000000'

$NetAdapter = Get-NetAdapter -InterfaceDescription "*#2"

Set-NetAdapter $NetAdapter.Name -MacAddress $MACAddress