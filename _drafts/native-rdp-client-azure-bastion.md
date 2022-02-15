---
date: 2022-02-16 00:00:00 +1300
title: Native RDP Client & Azure Bastion
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
In early February 2022, Azure Bastion Preview support for the [native Windows SSH and RDP](https://docs.microsoft.com/en-us/azure/bastion/connect-native-client-windows "Connect to a VM using the native client (Preview)") client came out, this meant that we didn't have to rely on the Azure Portal and the limitations of a web browser.

> Azure Bastion is a fully managed service that provides more secure and seamless Remote Desktop Protocol (RDP) and Secure Shell Protocol (SSH) access to virtual machines (VMs) without any exposure through public IP addresses. Provision the service directly in your local or peered virtual network to get support for all the VMs within it.

Let's create an Azure Virtual Machine and test the native RDP client!

### Prerequisites

* This configuration requires the Standard SKU tier for Azure Bastion.
* A Virtual Machine to connect to 
* Reader role on the Virtual Machine
* Read role on the Network Interface Card of the Virtual Machine
* Reader role on the Azure Bastion resource
* Virtual Machine Administrator _(or User)_ login role - _if using_ [_Azure Active Directory_](https://docs.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-windows "Login to Windows virtual machine in Azure using Azure Active Directory authentication") _authentication_.

### Create Azure Bastion

If you have a Virtual Machine, but haven't setup Azure Bastion, run through the below to set it up:

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource**
 3. Search for: **Bastion**
    ![Azure - Bastion](/uploads/bastionmarketplace.png "Azure - Bastion")
 4. Click **Create**
 5. This is a Networking resource to place it in the same Resource Group as my Virtual Network.
 6. Please type in a **Name** for the **Bastion** instance; I will call mine: Bastion
 7. **Select** the **Region** that **matches** the Virtual **Network** region
 8. Select the **Virtual Network**
 9. It now warns you about creating an: AzureBastionSubnet with a prefix of at least /27, so we need to create one; click on **Manage Subnet Configuration**.
10. Click **+ Subnet**
11. For the Name type in: **AzureBastionSubnet**
12. For the **Subnet** address range: **10.0.1.0/27**
    _If you get an error that indicates the address is overlapping with the aadds-subnet, it may be because the Address space is only a /24; click Cancel and click on Address Space in the Virtual Network and change the /24 to/16 to increase the address range._
13. Click **Save** to create the subnet
    ![Azure - Bastion](/uploads/az_subnet.png "Azure - Bastion")
14. Up the Top, click **Create a Bastion**. To go back to the Bastion setup, your Subnet should be selected automatically.
15. You do need a **Public IP** for Bastion, so **confirm** the **name** is appropriate, then click **Review + Create**
    ![Azure - Bastion](/uploads/bastionsetup.png "Azure - Bastion")
16. Click on **Create** to create your Bastion instance!

**Note: Bastion may take 10-20 minutes to provision.**

### Check Bastion SKU
