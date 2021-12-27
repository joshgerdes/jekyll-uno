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
SSH File Transfer Protocol _(SFTP)_ support is now supported in Preview for Azure Blob Storage accounts with hierarchical namespace enabled.

Although tools such as Storage Explorer, Data Factory, AzCopy allows a copy to and from Azure storage accounts, sometimes your applications need more traditional integration, so SFTP is a welcome addition to the Microsoft Azure ecosystem, which in some cases removes the need for additional Virtual Machine(s).

This support enables traditional SFTP connectivity to an Azure Storage account, which as an Azure PaaS _(Platform as a Service)_ resource, offers additional flexibility, reduce operational overhead and increase redundancy and scalability.

We will run through the initial setup of the Azure Storage account using the Azure Portal. 

Azure Storage does not support shared access signature (SAS), or Azure Active Directory (Azure AD) authentication for connecting SFTP clients. Instead, SFTP clients must use either a password or a Secure Shell _(SSH)_ private key credential.

Before we head into the implementation, just a bit of housekeeping, this is currently still in Preview at the time of this post, the functionality MAY change by the time it becomes GA (_Generally Available)_.

> During the public preview, the use of SFTP does not incur any additional charges. However, the standard transaction, storage, and networking prices for the underlying Azure Data Lake Store Gen2 account still apply. SFTP might incur additional charges when the feature becomes generally available. As of the time of the preview SFTP support is only avaliable in certain [regions](https://docs.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support#regional-availability "SSH File Transfer Protocol (SFTP) support for Azure Blob Storage (preview)").

You can connect to the SFTP storage account by using local _(to the SFTP storage account)_ SSH public-private keypair, or password _(or both)_. You can also set up individual HOME directories _(containers)_ for each user _(maximum of 1000 local user accounts_).

SFTP communicates on port: 22, which is the default port usually used by this service.