---
date: 2021-12-27 00:00:00 +1300
title: SFTP in Microsoft Azure using Azure Blob Storage
author: Luke
categories:
- Azure
toc: true
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

#### Fill out the SFTP Public Preview Interest Form

Because the SFTP functionality is currently in Private Preview, Microsoft has asked that anyone interested in the SFTP Preview fill out a Microsoft Forms: 

* [SFTP Public Preview Interest Form](https://forms.office.com/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbRxE4mlJMX2FKhD4ROGugH69URjBGVVdNSVRRWVUxSFA3WkM5OVk4STJFQS4u "SFTP Public Preview Interest Form")

This MAY be required before proceeding to the next steps, initially I believe this was required - but there appears to have been a few people who I know have registered the feature without the form - either way, the SFTP Public Preview Interest form, is a good opportunity to supply your use-case information to Microsoft directly, to help improve the nature of the service going forward.

#### Registering the Feature

In order to create an Azure Storage account, that supports SFTP - we need to enable the Preview Feature.

1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
2. Navigate to: **Subscriptions**
3. **Select** the **subscription** that you want to enable **SFTP** preview for
4. Click on: **Preview features**
5. Search for: **SFTP**
6. Click on: **SFTP support for Azure Blob Storage** and click **Register** - _this may take from minutes to a few days to be registered, as each preview request may need to be manually approved by Microsoft personnel based on the Public Preview Interest form - my feature registration occurred quite quickly, so there is a chance that they either have automated the approvals or I was just lucky._ 

   _As you can see in the screenshot below, I had already registered mine:_
7. ![Azure Portal SFTP Preview Feature](/uploads/azureportal_sftppreview.png "Azure Portal SFTP Preview Feature")
8. You can continue to hit refresh until it changes from: Registering to Registered.
9. While we are here, let's check that the Microsoft.Storage resource provider is registered _(it should already be enabled, but it is a good opportunity to check before attempting to create a resource and get a surprise_), by clicking on REsource providers in the left-hand side menu and search for: Storage, if it is set to NotRegistered - click on Microsoft.Storage and click Register.

To register the SFTP feature using PowerShell you can run the following cmdlet:

    Register-AzProviderFeature -FeatureName "AllowSFTP" -ProviderNamespace "Microsoft.Storage"

#### Create the Azure Storage Account

Now that the Preview feature has been registered, we can now create a new Storage account.

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Click on **+Create a resource**
 3. Type in: **Storage account** and click on the Microsoft Storage account resource and click Create
 4. ![Azure Portal - Storage account](/uploads/azureportal_createresourcestorageaccount.png "Azure Portal - Storage account")
 5. Select your **Subscription** you enabled the SFTP feature in earlier
 6. Select your **Resource Group** _(or create a new resource group)_ to place your storage account into.
 7. **Select** your **storage account name **_(_[_this needs to be globally unique and a maximum of 24 characters_](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules#microsoftstorage "Naming rules and restrictions for Azure resources")_), in my example, I am going with: sftpstorageacc1337_
 8. **Select** your **Region**, remember that only specific regions currently have SFTP support at the time of this article _(luckily for me - the closest Azure region for me (Australia East) is supported)_.
 9. **Select** your **performance tier**, Premium isn't supported so I will select Standard
10. **Select** your **Redundancy**, remember that GRS-R, GRS isn't supported at this time, I will select Zone-redundant storage (ZRS) so that my storage account is replicated between the 3 availability zones, but you can also select LRS _(Locally Redundant Storage)._
11. ![Azure Portal - Create v2 Storage Account](/uploads/azureportal_createstorageaccount.png "Azure Portal - Create v2 Storage Account")
12. Click **Next: Advanced**
13. Leave the Security options, as-is and check: **Enable hierarchical namespace**, under the Data Lake Storage Gen2 subheading
14. Click **Enable SFTP**
15. ![](/uploads/azureportal_createstorageaccountenablesftp.png)
16. Click: **Next: Networking**
17. SFTP supports Private Endpoints (_as a blob storage sub-resource)_, but in this case, I will be keeping Connectivity as a **Public endpoint (all networks)**
18. ![](/uploads/azureportal_createstorageaccountnetwork.png)
19. Click **Next: Data Protection**
20. Here you can enable [soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview "Soft delete for blobs") for your blobs and containers, so if a file is deleted, it is retained for 7 days, until it's permanently deleted, I am going to leave mine set as the default of 7 days and click: **Next: Tags**
21. Add in any applicable Tags, ie who created it, when you created it, what you created it for and click **Review + Create**
22. Review your configuration, make sure that Enable SFTP is enabled with Hierarchical namespace and click **Create**.

In case you are interested in Infrastructure as Code, here is an Azure Bicep file I created to create a storage account ready for SFTP here that can be deployed to a Resource Group, ready for the next steps: [https://gist.github.com/lukemurraynz/e2e087010c73167fdb2ce4a44ad660e9](https://gist.github.com/lukemurraynz/e2e087010c73167fdb2ce4a44ad660e9 "https://gist.github.com/lukemurraynz/e2e087010c73167fdb2ce4a44ad660e9")

#### Setup SFTP

Now that you have a compatible Azure storage account, it is time to enable SFTP!

1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
2. Navigate to the Storage account you have created for SFTP and click on it
3. On the Storage account blade, under Settings, you will see: SFTP