---
title: Native RDP Client & Azure Bastion
author: Luke
categories:
  - Azure
date: 2022-02-16 00:00:00 +1300
toc: true
header:
  teaser: images/iazure-marketplace-banner.png
---

In early February 2022, Azure Bastion Preview support for the [native Windows SSH and RDP](https://learn.microsoft.com/en-us/azure/bastion/connect-native-client-windows?WT.mc_id=AZ-MVP-5004796 "Connect to a VM using the native client (Preview)"){:target="_blank"} client came out, and this meant that we no longer have to rely on the Azure Portal and the limitations of a web browser - the support also includes File transfer through the clipboard by copying and pasted into the RDP session!

> Azure Bastion is a fully managed service that provides more secure and seamless Remote Desktop Protocol (RDP) and Secure Shell Protocol (SSH) access to virtual machines (VMs) without any exposure through public IP addresses. Provision the service directly in your local or peered virtual network to get support for all the VMs within it.

Let’s test the native RDP client through a secure connection using Azure Bastion!

### Prerequisites

* This configuration requires the [Standard](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings?WT.mc_id=AZ-MVP-5004796 "Azure Bastion documentation"){:target="_blank"} tier for Azure Bastion.
* A Virtual Machine(s) to connect
* Latest [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796 "Azure CLI"){:target="_blank"}
* Reader role on the Virtual Machine
* Read role on the Network Interface Card of the Virtual Machine.
* Reader role on the Azure Bastion resource
* Virtual Machine Administrator _(or User)_ login role _using_ [_Microsoft Entra ID_](https://learn.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-windows?WT.mc_id=AZ-MVP-5004796 "Login to Windows virtual machine in Azure using Microsoft Entra ID authentication"){:target="_blank"}_authentication_.

### Create Azure Bastion

If you have a Virtual Machine but haven't set up Azure Bastion, run through the below to set it up:

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource**
 3. Search for: **Bastion** ![Azure - Bastion](/uploads/bastionmarketplace.png "Azure - Bastion")
 4. Click **Create**
 5. This is a Networking resource to place it in the same Resource Group as my Virtual Network.
 6. Please type in a **Name** for the **Bastion** instance; I will call mine: Bastion
 7. **Select** the **Region** that **matches** the Virtual **Network** region
 8. Select **Standard** Tier
 9. Select the **Virtual Network**
10. It now warns you about creating an: AzureBastionSubnet with a prefix of at least /27, so we need to create one; click on **Manage Subnet Configuration**.
11. Click **+ Subnet**
12. For the Name type in: **AzureBastionSubnet**
13. For the **Subnet** address range: **10.0.1.0/27**, _If you get an error that indicates the address is overlapping with another subnet, it may be because the Address space is only a /24; click Cancel and click on Address Space in the Virtual Network and change the /24 to/16 to increase the address range._
14. Click **Save** to create the subnet ![Azure - Bastion](/uploads/az_subnet.png "Azure - Bastion")
15. Up the Top, click **Create a Bastion**. Your subnet should be selected automatically to go back to the Bastion setup.
16. You do need a **Public IP** for Bastion, so **confirm** the **name** is appropriate, then click **Next: Tags.**
17. ![Azure Bastion](/uploads/2022-02-16-10_44_32-create-a-bastion-microsoft-azure-mozilla-firefox-private-browsing.png)
18. Add in appropriate tags, then click **Next: Advanced**
19. Check the box next to **Native client support (Preview)**
20. ![Azure Bastion](/uploads/2022-02-16-10_46_19-create-a-bastion-microsoft-azure-mozilla-firefox-private-browsing.png)
21. Click **Next: Review + Create**
22. Click on **Create** to create your Bastion instance!

**Note: Bastion may take 10-20 minutes to provision.**

### Check Bastion SKU

If you already have an Azure Bastion instance, let's check the SKU and, if needed, change it to Standard. Just a note:

_Downgrading from a Standard SKU to a Basic SKU is not supported. To downgrade, you must delete and recreate Azure Bastion._

1. Log in to the **Azure Portal**
2. Navigate to your **Bastion** resource
3. Click on: **Configuration**
4. Change Tier to **Standard**
5. Check: **Native client support (Preview)**
6. Click **Apply**
7. ![Azure Bastion](/uploads/2022-02-16-10_58_47-bastion-microsoft-azure-mozilla-firefox-private-browsing.png)

### Connect to VM using Native RDP Support

1. Open command prompt or Terminal
2. Type: **az login**
3. Login to your Azure subscription
4. We need the resource ID of the VM we need to connect to, type in: **az VM show --resource-group 'appserver-rg' --name 'APP-P01' --show-details**
5. _Change the resource group and VM name above to match your VM_
6. Copy the id of the Virtual Machine you want to connect to
7. Because I am running the Azure CLI from a PowerShell terminal, I am going to use the following variables:

       $BastionName = 'Bastion'
       $BastionRG = 'network-rg'
       $VMResourceID= '/subscriptions/000000-0000-0000-0000000/resourceGroups/appserver-rg/providers/Microsoft.Compute/virtualMachines/APP-P01'
       az network bastion rdp --name $BastionName --resource-group $BastionRG --target-resource-id $VMResourceID
8. Run the command, your Remote Desktop window should open up, and the tunnel has been established; if you close the Azure CLI window, your RDP session will be dropped!
9. ![Azure Bastion](/uploads/azurebastiontst.gif)

As you could most likely tell, there are no options to enable drive passthrough, etc. You would usually find when connecting to Remote Desktop, but the copying of files/text, etc., does work!
