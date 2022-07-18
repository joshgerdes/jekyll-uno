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

In Microsoft Azure, you can make changes to the Primary Network interface; these changes include manually setting the IP settings to changing the MAC address - these settings are managed by the underlying Network Interface and Azure host.

> _If you do inadvertently make changes to this, you will lose connection to the Azure Virtual Machine, however, don't panic! Until its rebooted and the configuration is reset by the Azure fabric._ 

This causes issues when you have software licensed to a specific MAC address; you could reissue the license to the new MAC address OR create a Secondary Interface in Microsoft Azure and update the MAC address on the Secondary network interface.

    $MACAddress = '000000000000'
    $NetAdapter = Get-NetAdapter -InterfaceDescription "*#2"
    Set-NetAdapter $NetAdapter.Name -MacAddress $MACAddress