---
date: 2022-01-29 00:00:00 +1300
title: Just in Time access to Azure Virtual Machines
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
Microsoft Defender for Cloud offers advanced security features, combining functions such as adaptive application controls _(application whitelisting)_, networking hardening _(machine learning that learns the traffic passing through your network security group, which helps you create more restricted rules)_ and advanced antivirus and threat protection, however, a hidden gem of this suite is: Just in Time VM Access.

For a [fee](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ " Microsoft Defender for Cloud pricing") for Microsoft Defender for Cloud, you can use Just In Time or JIT to lock down inbound traffic to your Azure Virtual Machines when you only need it.

This reduces exposure to attacks while providing easy access when you need to connect to a VM.

Today we are going to use the Azure Portal, and configure Just-in-Time access for RDP for a Windows virtual machine, running in Microsoft Azure which has a public IP.