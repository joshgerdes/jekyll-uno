---
title: Access denied on an Azure Virtual Machine when using aztfexport
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/aztfexport_access_denied.png
date: '2023-07-10 00:00:00 +1300'
---

When attempting to use [aztfexport](https://github.com/Azure/aztfexport), a tool designed to export currently deployed Azure resources into HashiCorp Configuration Language (HCL) for use with Terraform, you may get: Access denied.

When using aztfexport, the first thing you need to do is make sure you have the [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796) installed, and run an:

    az login

After logging in, you need to verify you are on the right subscription, by running:

    az account show

If you are on the right subscription, you don't need to do anything. If you are in the wrong subscription then run:

    az account list

Find the susbcription ID then use:

    az account set --subscription <name or id>

**You only need Reader rights to be able to export the Terraform configuration.**

If you find you are still running into access denied issues, such as below:

![aztfexport - Access denied](/images/posts/aztfexport_access_denied.png "aztfexport - Access denied")

And you are running the aztfexport program on an Azure Virtual Machine, such as Azure Virtual Desktop or Devbox, what is happening is the [Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview?WT.mc_id=AZ-MVP-5004796) permissions of your Azure Virtual Machine is overriding your own permissions you used to login to Azure using the CLI.

To get around this, you either have to run aztfexport locally, on a device thats not an Azure Virtual Machine, or supply the Managed Identity of the Virtual Machine, Reader rights to the subscription you wish to do the export from.

You can do this, by navigating to your Azure Virtual Machine, in the Azure Portal, click on the Virtual Machine, select Identity, select Azure role assignments and grant it Reader rights to the Resource Group or Subscription you are targeting.

You could try Disabling the System Assigned Managed Identity as well, which appeared to work for me.

For more information about this error, please refer to the following Github issue: [Access Denied during xport on Azure Virtual Desktop](https://github.com/Azure/aztfexport/issues/380).