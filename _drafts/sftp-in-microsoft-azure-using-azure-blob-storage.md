---
date: 2021-12-27 00:00:00 +1300
title: SFTP in Microsoft Azure using Azure Blob Storage
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
SSH File Transfer Protocol _(SFTP)_ support is now in Preview for Azure Blob Storage accounts with hierarchical namespace enabled. 

Although tools such as Storage Explorer and AzCopy allows a copy to and from Azure storage accounts, sometimes your applications need more traditional integration, so SFTP is a welcome addition to the Microsoft Azure ecosystem, which in some cases removes the need for additional Virtual Machine(s).

This support enables traditional SFTP connectivity to an Azure Storage account, which as an Azure PaaS _(Platform as a Service)_ resource, offers additional flexibility, reduce operational overhead and redundancy. 

We will run through the initial setup of the Azure Storage account using the Microsoft Azure Portal, then connect to it.