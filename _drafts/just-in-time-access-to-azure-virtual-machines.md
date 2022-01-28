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

This article assumes you have the authority and permissions (_at least Security Administrator role)_ to configure and pay for Defender for Cloud

### Configure Defender for Cloud

 1. Open the [Azure Portal](https://portal.azure.com/#home "Azure Portal")
 2. Navigate to the Virtual Machine you would like to enable Defender for Cloud on and enable Just in Time Access for
 3. Click on Configuration
 4. Click on: Upgrade your Security Center subscription to enable a just-in-time access
 5. ![](/uploads/azureportal-configurationinitialjit.png)
 6. Select the Subscription that holds your VM and select Upgrade
 7. If you want to make use of the rest of the Cloud Defender offerings (and you should), then make sure you install the Log Analytics agent, however for Just In Time Access, you don't need it.
 8. Navigate back to your Virtual Machine
 9. Click on Configuration
10. Now you should see: Enable for Just-in-Time VM access, select this to enable Just in Time.

Now if you go to the Network Security Group attached to the network interface of the VM, you should see a Deny Rule for: 3389 that's been created with a priority lower than the allow rules, forcing the block.

![](/uploads/azureportal-justintime_nsgblock.png)