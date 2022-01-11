---
date: 2022-01-11 00:00:00 +1300
title: Create Azure Point to Site VPN using Azure Active Directory authentication
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
You may be working remotely, or only have a few devices needing access to your resources in Azure, a solution that can be deployed is a point to site connection straight into your Microsoft Azure network.

This functionality, allows your computer to connect privately to resources over a secure tunnel using your internet connection, using an Azure Virtual Network gateway, you can seamlessly connect to resources without the need of opening up your resources to the internet or having to whitelist your _(or third party vendor)_ IP address, which may change on a daily basis.

Using Azure Active Directory, you know only your specified users have access to your Azure resources.