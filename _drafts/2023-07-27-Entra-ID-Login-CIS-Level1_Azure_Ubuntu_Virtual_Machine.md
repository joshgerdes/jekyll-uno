---
title: Entra ID login to a CIS Level 1 Ubuntu Azure Virtual Machine
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/ChangeDefaultManagementGroup.png
date: '2023-07-27 00:00:00 +1300'
---

Currently, [CIS](https://www.cisecurity.org/) (Center for Internet Security) [Azure Marketplace images](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=CIS&page=1?WT.mc_id=AZ-MVP-5004796), do not support being Entra ID (Azure Active Directory) Joined.

Although this article is about allowing Entra ID login to a Ubuntu machine, its worth noting the current decisions around Windows as well currently:

>'The Windows CIS Benchmarks are written for Active Directory domain-joined systems using Group Policy, not standalone/workgroup systems. Adjustments/tailoring to some recommendations will be needed to maintain functionality if attempting to implement CIS hardening on standalone systems or a system running in the cloud.
>'Currently, we do not support Azure Active Directory and it is not compatible with our EXISTING Hardened Images.

In fact when you, attempt to create a CIS Level 1 Ubuntu image in the Azure Portal, you get:

"This image does not support Login with Azure AD."

![CIS Image does not support Login with Azure AD](/images/posts/AzurePortal_CIS_Level1_Ubuntu_NoEntraIDLogin.png)

However, as I go into below, we can indeed login to the CIS hardened image, using the [Microsoft Azure AD based SSH Login](https://learn.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-linux?WT.mc_id=AZ-MVP-5004796) extension.

> Be wary, that although this works, you may run into issues with operational support of this from CIS, due to the hardening. This is also Entra ID LOGIN (not JOINED!). You won't see the device under Entra ID Devices.

There are many security benefits of using Azure AD with SSH log in to Linux VMs in Azure, including:

1. Use of your Entra ID (Azure AD) credentials to log in to Azure Linux VMs.
1. Get SSH certificate-based authentication without needing to distribute SSH keys to users or provision SSH public keys on any Azure Linux VMs you deploy.
1. Reduce reliance on local administrator accounts, credential theft, and weak credentials.
1. Password complexity and password lifetime policies configured for Azure AD help secure Linux VMs as well.
1. With Azure role-based access control, specify who can login to a VM as a regular user or with administrator privileges. When users join or leave your team, you can update the Azure RBAC policy for the VM to grant access as appropriate. When employees leave your organization and their user account is disabled or removed from Azure AD, they no longer have access to your resources.
1. With Conditional Access, configure policies to require multi-factor authentication and/or require client device you are using to SSH be a managed device (for example: compliant device or hybrid Azure AD joined) before you can SSH to Linux VMs.
1. Use Azure deploy and audit policies to require Azure AD login for Linux VMs and to flag use of non-approved local accounts on the VMs.

So after your CIS Hardened Image, in my case I am using Ubuntu 20.04 has been deployed in Azure. Lets set this up.

You will need to make sure you have a few prerequsites.

### Prerequsites

#### Network

VM network configuration must permit outbound access to the following endpoints over TCP port 443.

[https://packages.microsoft.com](https://packages.microsoft.com): For package installation and upgrades.
[http://169.254.169.254](http://169.254.169.254): Azure Instance Metadata Service endpoint.
[https://login.microsoftonline.com](https://login.microsoftonline.com): For PAM-based (pluggable authentication modules) authentication flows.
[https://pas.windows.net](https://pas.windows.net): For Azure RBAC (Role Based Access Control) flows.

Also make sure you have enabled TCP Port 80 for: ubuntu.com, specifically [http://archive.ubuntu.com](http://archive.ubuntu.com) as the Microsoft Azure AD based SSH Login, will need to download and install the following packages: aadsshlogin and aadsshlogin-selinux as needed.

#### Virtual Machine

The CIS hardened image, will need to have a [System Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview?WT.mc_id=AZ-MVP-5004796#managed-identity-types) setup. This can be easily enabled in the Identity blade of the Virtual Machine.

The Entra ID (Azure Active Directory) users that need to login with to the Linux Virtual Machine are a member of one of the following Azure RBAC (Role Based Access Control) groups, as per their requirements:

| RBAC Role                           | Notes                                                            |
| ----------------------------------- | ---------------------------------------------------------------- |
| Virtual Machine Administrator Login | View Virtual Machines in the portal and login as administrator   |
| Virtual Machine User Login          | View Virtual Machines in the portal and login as a regular user. |

Only one role is required. These roles are supported for both Windows and Linux.

#### Client

On the jumphost, client PC you will be connecting to the Linux virtual machine from, you need the latest [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796) with the Azure CLI extension 'ssh' installed.

    az extension add --name ssh

The minimum version required for the extension is 0.1.4.

    az extension show --name ssh

### Install Extension

## Install using the Azure Portal

Once the pre-requsites have been met, it is time to install the extension.

1. Login to the [Azure Portal](https://portal.azure.com/)
1. Navigate to your CIS Hardened Virtual Machine
1. Click on Extensions + Applications
1. Click + Add
1. ![Azure Portal - Extensions](/images/posts/AzurePortal_CISHardenedVM_Extensions.png)
1. Search for: Azure AD based SSH Login
1. ![Azure Portal - SSH Extension](/images/posts/AzurePortal_CISHardenedVM_SSH_Extension.png)
1. Select the Azure AD base SSH Login extension
1. Click Next
1. Click Review and Create
1. Click Create

After a few m oments, the extension and supporting components, will be installed.

## Install using Terraform

You can use the following Terraform code snippet, to install the extension to a Linux Virtual Machine:

Make sure you assign the extension, to the virtual machine, using the ID.

    resource "azurerm_virtual_machine_extension" "aad_login" {
    name                 = "AADLogin"
    virtual_machine_id   = 
    publisher            = "Microsoft.Azure.ActiveDirectory"
    type                 = "AADSSHLoginForLinux" # For Windows VMs: AADLoginForWindows
    type_handler_version = "1.0"                 # There may be a more recent version
    }

sd