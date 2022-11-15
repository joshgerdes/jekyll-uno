---
date: 2022-11-16 00:00:00 +1300
title: Disable SFTP support on an Azure Storage account on a Schedule
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Azure Storage account [SFTP functionality](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support?WT.mc_id=AZ-MVP-5004796#pricing-and-billing "SSH File Transfer Protocol (SFTP) support for Azure Blob Storage") has now gone GA _(Generally Available)_ across most regions as part of the GA release - SFTP support for Azure Storage accounts was free while it was in preview - but now that the service is GA - there is an additional charge for SFTP functionality.

> Enabling the SFTP endpoint has a cost of $0.30 per hour. We will start applying this hourly cost on or after December 1, 2022.

This service has worked for me without a hitch for months, but as with most resources in Microsoft Azure - you pay for what you use! There may be instances where you do not need SFTP support 24 hours a day, seven days a week! This is where the following Azure Automation runbook can help.

Using an [Azure Automation](https://learn.microsoft.com/en-us/azure/automation/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Automation?") PowerShell runbook and Schedules _(as part of the Azure Automation account)_  - we can turn on the SFTP endpoint - when we need it and disable it - the rest of the time - which is great from a security and cost perspective.

To do this, we will need an:

* Azure Automation Account
* System Managed Identity set with Storage Account Contributor rights
* PowerShell runbook _(supplied below)_

For the purpose of this article, I am going to assume you already have an Azure Automation account - if you do not - then follow the Microsoft documentation: Create a standalone Azure Automation account.