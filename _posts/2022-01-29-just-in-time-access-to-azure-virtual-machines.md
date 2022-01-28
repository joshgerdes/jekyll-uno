---
date: 2022-01-29 00:00:00 +1300
title: Just in Time access to Azure Virtual Machines
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Microsoft Defender for Cloud offers advanced security features, combining functions such as adaptive application controls _(application whitelisting)_, networking hardening _(machine learning that learns the traffic passing through your network security group, which helps you create more restricted rules)_ and advanced antivirus and threat protection; however, a hidden gem of this suite is: Just in Time VM Access.

For a [fee](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ " Microsoft Defender for Cloud pricing") for Microsoft Defender for Cloud, you can use Just In Time or JIT to lock down inbound traffic to your Azure Virtual Machines when you only need it.

This reduces exposure to attacks while providing easy access when you need to connect to a VM.

Today, we will use the Azure Portal and configure Just-in-Time access for RDP for a Windows virtual machine running in Microsoft Azure that has a public IP.

This article assumes you have the authority and permissions (_at least the Security Administrator role)_ to configure and pay for Defender for Cloud.

### Configure Defender for Cloud

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Navigate to the Virtual Machine you would like to enable Defender for Cloud on and enable Just in Time Access for
 3. Click on **Configuration**
 4. Click on: **Upgrade your Security Center subscription** to enable just-in-time access.
 5. ![](/uploads/azureportal-configurationinitialjit.png)
 6. **Select** the **Subscription** that holds your VM and select **Upgrade**
 7. If you want to make use of the rest of the Cloud Defender offerings (and you should), then make sure you install the Log Analytics agent; however, you don't need it for Just In Time Access.
 8. **Navigate** back to your **Virtual Machine**
 9. Click on **Configuration**
10. Now you should see: **Enable for Just-in-Time VM access**; select this to **enable** Just in Time.

Now, if you go to the Network Security Group attached to the network interface of the VM, you should see a Deny Rule for 3389 that's been created with a priority lower than the allowed rules, forcing the block.

![](/uploads/azureportal-justintime_nsgblock.png)

### Configure Just In Time

Now that we have enabled Defender for Cloud, it's time to configure what ports (can be used for more than just RDP and SSH access) and the length of time that access is allowed. 

 1. Click on **Microsoft Defender for Cloud**
 2. Select **Workload Protections**
 3. Select **Just-In-Time VM access**
 4. ![](/uploads/azureportal-defenderforcloud.png)
 5. **Select** the **VM** you have configured.
 6. Click the **ellipsis** on the right-hand side
 7. Select **Edit**
 8. Azure has automatically added the port for RDP (3389) and sets a maximum 3 hour request time (that I am allowed to connect to the VM); I can also restrict Just In TIme access from specific IP addresses, and IP ranges to avoid anyone being able to RDP from their home IP.
 9. ![](/uploads/azureportal-configurationports.png)
10. **Make any adjustments** you feel suits your environment. I am going to leave the configuration as is.

### Request Access for Just In Time Access to RDP

You can [programmatically ](https://docs.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-powershell "Secure your management ports with just-in-time access")request JiT access to Azure VM through PowerShell and the REST API _(see Additional Resources below for a PowerShell script to get you started)_, but we are going to use the Azure Portal.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. **Navigate** to the **Virtual Machine** you would like to enable Defender for Cloud on and enable Just in Time Access for
 3. Click **Connect**
 4. You should see an information alert at the top of the blade "This VM has a just-in-time access policy. Select "Request access" before connecting."
 5. ![](/uploads/azureportal-requestaccess.png)
 6. Select **Source IP (My IP)**
 7. Click **Request access**
 8. You should now have access to RDP to the machine!
 9. If you look at the Network Security Group, you should be able to see a new 'Allow' rule has been created with a priority lower than the block rule.
10. ![](/uploads/azureportal-justintime_nsgallow.png)
11. After 3 hours, the allowed rules will be removed automatically.

Hopefully, this helps keep your environment secure; if you implement this, make sure you read about the custom roles. To prevent the people from just adding in a rule for their public IP in the address manually, it may be better to create a custom role _(see the script in Additional Resources below to create this role)_.

### Additional Resources

* [Secure your management ports with just-in-time access](https://docs.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-usage?tabs=jit-config-asc%2Cjit-request-asc "Secure your management ports with just-in-time access")
* [Understanding just-in-time (JIT) VM access](https://docs.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview "Understanding just-in-time (JIT) VM access")
* [Just in Time Access Policy Script & Custom Role Script](https://github.com/Azure/Microsoft-Defender-for-Cloud/tree/main/Powershell%20scripts/JIT%20Scripts "JIT Scripts")