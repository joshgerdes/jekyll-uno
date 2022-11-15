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

This service works well!