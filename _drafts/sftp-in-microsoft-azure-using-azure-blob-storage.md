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

### Creating an Azure Storage account for SFTP

This article, assumes you have an Azure subscription and rights to create a new Storage account resource, and the following pre-requisites:

* A standard general-purpose v2 or premium block blob storage account. You can also enable SFTP as you create the account. For more information on these types of storage accounts, see [Storage account overview](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview).
* The account redundancy option of the storage account is set to either locally-redundant storage (LRS) or zone-redundant storage (ZRS), GRS is not supported at this time.
* The hierarchical namespace feature of the account must be enabled for existing storage accounts. To enable the hierarchical namespace feature, see [Upgrade Azure Blob Storage with Azure Data Lake Storage Gen2 capabilities](https://docs.microsoft.com/en-us/azure/storage/blobs/upgrade-to-data-lake-storage-gen2-how-to).
* If you're connecting from an on-premises network, make sure that your client allows outgoing communication through port 22. The SFTP uses that port.

#### Registering the Feature

In order to create an Azure Storage account, that supports SFTP - we need to enable the Preview Feature.

 1. Log in to the Azure Portal
 2. Navigate to: Subscriptions
 3. Select the subscription that you want to enable SFTP preview for
 4. Click on: Preview features
 5. Search for: SFTP
 6. Click on: SFTP support for Azure BLob Storage and click Register - this may take 5-10 minutes to be registered.
 7. _As you can see in the screenshot below, I had already registered mine:_
 8. ![Azure Portal SFTP Preview Feature](/uploads/azureportal_sftppreview.png "Azure Portal SFTP Preview Feature")
 9. You can continue to hit refresh until it changes from: Registering to Registered.
10. While we are here, let's check that the Microsoft.Storage resource provider is registered _(it should already be enabled, but it is a good opportunity to check before attempting to create a resource_), by clicking on REsource providers in the left-hand side menu and search for: Storage, if it is set to NotRegistered - click on Microsoft.Storage and click Registered.