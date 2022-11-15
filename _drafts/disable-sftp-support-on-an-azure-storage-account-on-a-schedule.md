---
date: 2022-11-16 00:00:00 +1300
title: Disable SFTP support on an Azure Storage account on a Schedule
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Azure Storage account [SFTP functionality](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support?WT.mc_id=AZ-MVP-5004796#pricing-and-billing "SSH File Transfer Protocol (SFTP) support for Azure Blob Storage") has now gone GA _(Generally Available)_ across most regions as part of the GA release - SFTP support for Azure Storage accounts was free while it was in preview - but now that the service is GA - there is an additional charge for SFTP functionality.

> Enabling the SFTP endpoint has a cost of $0.30 per hour. We will start applying this hourly cost on or after December 1, 2022.

This service has worked for me without a hitch for months, but as with most resources in Microsoft Azure - you pay for what you use! Therefore, there may be instances where you do not need SFTP support 24 hours a day, seven days a week! This is where the following Azure Automation runbook can help.

_Feel free to check out a_ [_previous article_](https://luke.geek.nz/azure/sftp-in-microsoft-azure-using-azure-blob-storage/ "SFTP in Microsoft Azure using Azure Blob Storage ") _on setting up SFTP support for an Azure storage account._

#### Overview

Using an [Azure Automation](https://learn.microsoft.com/en-us/azure/automation/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Automation?") PowerShell runbook and Schedules _(as part of the Azure Automation account)_  - we can turn on the SFTP endpoint - when we need it and disable it - the rest of the time - which is excellent from a security and cost perspective.

#### Prerequisites

To do this, we will need an:

* Azure Automation Account
* System Managed Identity set with Storage Account Contributor rights
* PowerShell runbook _(supplied below)_

For this article, I will assume you already have an Azure Automation account - if you do not - then follow the Microsoft documentation: [Create a standalone Azure Automation account](https://learn.microsoft.com/en-us/azure/automation/automation-create-standalone-account?tabs=azureportal&WT.mc_id=AZ-MVP-5004796 "Create a standalone Azure Automation account").

#### Deploy & Configure

Now that the Azure Automation account has been configured and set up - we need to add the Runbook, but before we can do that - there are some dependencies. For example, SFTP is a new service that the currently installed Az Modules in the Azure Automation don't have visibility on - so to configure the SFTP service - we need to update 2 Modules to the most recent version.

These modules are:

* Az.Accounts _(≥ 2.10.3)_
* Az.Storage

Az.Accounts are a dependent service of the latest Az.Storage account, so let us import that first.

##### Update Az.Accounts module

1. In the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"), navigate to [**Azure Automation accounts**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Automation%2FAutomationAccounts "Azure Automation Accounts").
2. Find your Azure Automation account and, click on it, navigate to **Modules** _(under Shared resources)_.
3. Select **Browse Gallery**
4. Search for: **Az.Accounts**
5. ![Import Az.Accounts](/uploads/azautomation_gallery_azaccounts.png "Az.Accounts")
6. Click '**Az.Accounts**' and select **Select.**
7. Set the **runtime** version to: **5.1** & select impor**t**
8. Wait for 5 minutes while the module imports.

##### Update Az.Storage module

_Note: the Az.The accounts module will need to finish its import before the Az.The storage module is updated._

1. In the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"), navigate to [**Azure Automation accounts**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Automation%2FAutomationAccounts "Azure Automation Accounts").
2. Find your Azure Automation account and, click on it, navigate to **Modules** _(under Shared resources)_.
3. Select **Browse Gallery**
4. Search for: **Az.Storage**
5. ![Import  Az.Storage](/uploads/azautomation_gallery_azstorage.png " Az.Storage")
6. Click '**Az.Storage**' and select **Select.**
7. Set the **runtime** version to: **5.1** & select impor**t**
8. Wait for 5 minutes while the module imports.