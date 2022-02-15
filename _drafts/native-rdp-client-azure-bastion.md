---
date: 2022-02-16 00:00:00 +1300
title: Native RDP Client & Azure Bastion
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
In early February 2022, Azure Bastion Preview support for the [native Windows SSH and RDP](https://docs.microsoft.com/en-us/azure/bastion/connect-native-client-windows "Connect to a VM using the native client (Preview)") client came out, this meant that we didn't have to rely on the Azure Portal and the limitations of a web browser.

> Azure Bastion is a fully managed service that provides more secure and seamless Remote Desktop Protocol (RDP) and Secure Shell Protocol (SSH) access to virtual machines (VMs) without any exposure through public IP addresses. Provision the service directly in your local or peered virtual network to get support for all the VMs within it.

Let's create an Azure Virtual Machine and test the native RDP client!

### Prerequisites

* This configuration requires the Standard SKU tier for Azure Bastion.
* A Virtual Machine to connect to 
* Reader role on the Virtual Machine
* Read role on the Network Interface Card of the Virtual Machine
* Reader role on the Azure BAstion resource
* Virtual Machine Administrator _(or User)_ login role - _if using_ [_Azure Active Directory_](https://docs.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-windows "Login to Windows virtual machine in Azure using Azure Active Directory authentication") _authentication_.

### Create Azure Bastion