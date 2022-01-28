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

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Navigate to the Virtual Machine you would like to enable Defender for Cloud on and enable Just in Time Access for
 3. Click on Configuration
 4. Click on: Upgrade your Security Center subscription to enable a just-in-time access
 5. ![](/uploads/azureportal-configurationinitialjit.png)
 6. Select the Subscription that holds your VM and select Upgrade
 7. If you want to make use of the rest of the Cloud Defender offerings (and you should), then make sure you install the Log Analytics agent, however for Just In Time Access, you don't need it.
 8. Navigate back to your Virtual Machine
 9. Click on Configuration
10. Now you should see: Enable for Just-in-Time VM access, select this to enable Just in Time.

Now if you go to the Network Security Group attached to the network interface of the VM, you should see a Deny Rule for 3389 that's been created with a priority lower than the allowed rules, forcing the block.

![](/uploads/azureportal-justintime_nsgblock.png)

### Configure Just In Time

Now that we have enabled Defender for Cloud, it's time to configure what ports (can be used for more than just RDP and SSH access) and the length of time that access is allowed. 

1. Click on Microsoft Defender for Cloud
2. Select Workload Protections
3. Select Just-In-Time VM access
4. ![](/uploads/azureportal-defenderforcloud.png)
5. Select the VM you have configured
6. Click the ellipsis on the right-hand side
7. Select Edit
8. Azure has automatically added the port for RDP (3389) and set a maximum 3 hour request time (that I am allowed to connect to the VM), I can also restrict Just In TIme access from certain IP addresses and IP ranges, to avoid anyone being able able to RDP from their home IP.
9. ![](/uploads/azureportal-configurationports.png)

### Request Access for Just In Time Access to RDP

You can [programmatically ](https://docs.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-powershell "Secure your management ports with just-in-time access")request JiT access to Azure VM through PowerShell and the REST API, but we are going to use the Azure Portal.

1. Open the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
2. Navigate to the Virtual Machine you would like to enable Defender for Cloud on and enable Just in Time Access for
3. Click Connect
4. You should see an information alert at the top of the blade "This VM has a just-in-time access policy. Select "Request access" before connecting."
5. ![](/uploads/azureportal-requestaccess.png)
6. Click Request access
7. You should now have access to RDP to the machine!
8. If you look at the Network Security Group, you should be able to see a new 'Allow' rule has been created with a priority lower than the block rule.
9. ![](/uploads/azureportal-justintime_nsgallow.png)

### Additional Resources