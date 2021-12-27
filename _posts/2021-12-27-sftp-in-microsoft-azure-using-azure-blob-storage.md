---
date: 2021-12-27 00:00:00 +1300
title: SFTP in Microsoft Azure using Azure Blob Storage
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
SSH File Transfer Protocol _(SFTP)_ support is now supported in Preview for Azure Blob Storage accounts with hierarchical namespace enabled.

Although tools such as Storage Explorer, Data Factory, AzCopy allows a copy to and from Azure storage accounts, sometimes your applications need more traditional integration, so SFTP is a welcome addition to the Microsoft Azure ecosystem, which in some cases removes the need for additional Virtual Machine(s).

This support enables standard SFTP connectivity to an Azure Storage account. As an Azure PaaS _(Platform as a Service)_ resource, it offers additional flexibility, reduces operational overhead, and increases redundancy and scalability.

We will run through the initial setup of the Azure Storage account using the Azure Portal.

Azure Storage does not support shared access signature (SAS) or Azure Active Directory (Azure AD) authentication for connecting SFTP clients. Instead, SFTP clients must use a password or a Secure Shell _(SSH)_ private essential credential.

Before we head into the implementation, just a bit of housekeeping, this is currently still in Preview at the time this post was written; the functionality MAY change by the time it becomes GA (_Generally Available)_.

> During the public preview, the use of SFTP does not incur any additional charges. However, the standard transaction, storage, and networking prices for the underlying Azure Data Lake Store Gen2 account still apply. SFTP might incur additional charges when the feature becomes generally available. As of the time of the preview SFTP support is only avaliable in certain [regions](https://docs.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-support#regional-availability "SSH File Transfer Protocol (SFTP) support for Azure Blob Storage (preview)"){:target="_blank"}.

You can connect to the SFTP storage account by using local _(to the SFTP storage account)_ SSH public-private keypair or Password _(or both)_. You can also set up individual HOME directories _(because of the hierarchical namespace, these are folders not containers)_ for each user _(maximum 1000 local user accounts_).

![SFTP Azure Storage Account - High Level Diagram](/images/posts/SFTP_Azure_HLDiagram.png "SFTP Azure Storage Account - High Level Diagram")

### Creating an Azure Storage account for SFTP

This article assumes you have an Azure subscription and rights to create a new Storage account resource and the following pre-requisites:

* A standard general-purpose v2 or premium block blob storage account. You can also enable SFTP as you create the account. See Storage account overview for more information on these types of storage accounts.
* The account redundancy option of the storage account is set to either locally-redundant storage (LRS) or zone-redundant storage (ZRS); GRS is not supported.
* The hierarchical namespace feature of the account must be enabled for existing storage accounts. To enable the hierarchical namespace feature, see [Upgrade Azure Blob Storage with Azure Data Lake Storage Gen2 capabilities](https://docs.microsoft.com/en-us/azure/storage/blobs/upgrade-to-data-lake-storage-gen2-how-to){:target="_blank"}.
* If you're connecting from an on-premises network, make sure that your client allows outgoing communication through port 22. The SFTP uses that port.

#### Fill out the SFTP Public Preview Interest Form

Because the SFTP functionality is currently in Private Preview, Microsoft has asked that anyone interested in the SFTP Preview fill out a Microsoft Forms:

* [SFTP Public Preview Interest Form](https://forms.office.com/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbRxE4mlJMX2FKhD4ROGugH69URjBGVVdNSVRRWVUxSFA3WkM5OVk4STJFQS4u "SFTP Public Preview Interest Form"){:target="_blank"}

This MAY be required before proceeding to the following steps; initially, I believe this was required - but there appears to have been a few people who I know have registered the feature without the form - either way, the SFTP Public Preview Interest form, is a good opportunity to supply your use-case information to Microsoft directly, to help improve the nature of the service going forward.

#### Registering the Feature

To create an Azure Storage account that supports SFTP - we need to enable the Preview Feature.

1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
2. Navigate to: **Subscriptions**
3. **Select** the **Subscription** that you want to enable **SFTP** preview for
4. Click on: **Preview features**
5. Search for: **SFTP**
6. Click on: **SFTP support for Azure Blob Storage** and click **Register** - _this may take from minutes to a few days to be registered, as each preview request may need to be manually approved by Microsoft personnel based on the Public Preview Interest form - my feature registration occurred quite quickly, so there is a chance that they either have automated the approvals or I was just lucky._

   _As you can see in the screenshot below, I had already registered mine:_
7. ![Azure Portal SFTP Preview Feature](/uploads/azureportal_sftppreview.png "Azure Portal SFTP Preview Feature")
8. You can continue to hit refresh until it changes from: Registering to Registered.
9. While we are here, let's check that the Microsoft.Storage resource provider is registered _(it should already be enabled, but it is a good opportunity to check before attempting to create a resource and get a surprise_), by clicking on REsource providers in the left-hand side menu and search for: Storage, if it is set to NotRegistered - click on Microsoft.Storage and click Register.

To register the SFTP feature using PowerShell, you can run the following cmdlet:

    Register-AzProviderFeature -FeatureName "AllowSFTP" -ProviderNamespace "Microsoft.Storage"

#### Create the Azure Storage Account

Now that the Preview feature has been registered, we can now create a new Storage account.

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
 2. Click on **+Create a resource**
 3. Type in: **Storage account** and click on the Microsoft Storage account resource and click Create
 4. ![Azure Portal - Storage account](/uploads/azureportal_createresourcestorageaccount.png "Azure Portal - Storage account")
 5. Select your **Subscription** you enabled the SFTP feature in earlier
 6. Select your **Resource Group** _(or create a new resource group)_ to place your storage account into.
 7. **Select__ your **storage account name **_(_[_this needs to be globally unique and a maximum of 24 characters_](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules#microsoftstorage "Naming rules and restrictions for Azure resources"){:target="_blank"}_), in my example; I am going with: sftpstorageacc1337_
 8. **Select** your **Region**; remember that only specific regions currently have SFTP support at the time of this article _(luckily for me - the closest Azure Region (Australia East) is supported)_.
 9. **Select** your **performance tier**; premium is supported but remember to select Blob, select Standard.
10. **Select** your **Redundancy**; remember that GRS-R, GRS isn't supported at this time; I will select Zone-redundant storage (ZRS) so that my storage account is replicated between the three availability zones, but you can also select LRS _(Locally Redundant Storage)._
11. ![Azure Portal - Create v2 Storage Account](/uploads/azureportal_createstorageaccount.png "Azure Portal - Create v2 Storage Account")
12. Click **Next: Advanced**
13. Leave the Security options as-is and check: **Enable hierarchical namespace** under the Data Lake Storage Gen2 subheading.
14. Click **Enable SFTP**
15. ![Azure Portal - Enable SFTP](/uploads/azureportal_createstorageaccountenablesftp.png "Azure Portal - Enable SFTP")
16. Click: **Next: Networking**
17. SFTP supports Private Endpoints (_as a blob storage sub-resource)_, but in this case, I will be keeping Connectivity as a **Public endpoint (all networks)**
18. ![Azure Portal - Enable SFTP](/uploads/azureportal_createstorageaccountnetwork.png "Azure Portal - Enable SFTP")
19. Click **Next: Data Protection**
20. Here you can enable [soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview "Soft delete for blobs"){:target="_blank"} for your blobs and containers, so if a file is deleted, it is retained for seven days until it's permanently deleted; I am going to leave mine set as the default of 7 days and click: **Next: Tags.**
21. Add in any applicable Tags, i.e. who created it, when you created it, what you created it for and click **Review + Create**
22. Review your configuration, make sure that Enable SFTP is enabled with Hierarchical namespace and click **Create**.

In case you are interested in Infrastructure as Code, here is an Azure Bicep file I created to create a storage account ready for SFTP here that can be deployed to a Resource Group, ready for the next steps:

{% gist e2e087010c73167fdb2ce4a44ad660e9 %}

#### Setup SFTP

Now that you have a compatible Azure storage account, it is time to enable SFTP!

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
 2. **Navigate** to the **Storage account** you have created for SFTP and click on it
 3. On the Storage account blade, under **Settings**, you will see: **SFTP**
 4. ![Azure Portal - Enable SFTP](/uploads/azureportal_storageaccountstpblade.png "Azure Portal - Enable SFTP")
 5. Click on **SFTP** and click **+ Add local user.**
 6. Type in the username of the user you would like to use _(remember you can have up to 1000 local users, but there is no integration into Azure AD, Active Directory or other authentication services currently_), in my example I will use: lukeftpuser
 7. You can use either _(and both)_ SSH keys or passwords, in this article - I am simply going to use a password so I select: **SSH Password**.
 8. Click **Next**
 9. Our storage account is empty, we now need to create a top-level container, so I will sect **Create new** and set the name to: ftp
10. I will leave the Public access level to **Private (no anonymous access)**
11. Click **Ok**
12. Now that the ftp container has been created, we need to **set** the **permissions**, I am simply going to give the permissions of Read, Create, Delete, List and Write. _It's worth noting, that if you only need to read or list contents, then that is the only permissions you need, these permissions are for the Container, not the folder, so you may find your users may have permissions to other folders in the same Container if not managed appropriately._
13. Now we set the **Home directory**. This is the directory that the user will be automatically mapped to, this is optional but if you don't have a Home directory filled in for the user, they will need to connect to the appropriate folders when connecting to SFTP manually. The home directory needs to be relative, ie: ftp/files _(the container name and the files folder, located in the ftp container)._
14. ![Azure Portal - Enable SFTP](/uploads/azureportal_sftplocalusercreate.png "Azure Portal - Enable SFTP")
15. Because we specified Password earlier, **Azure** has automatically **created** a new **password** for that account, although you can generate new passwords - you are unable to specify what the Password is, make sure you **copy** this and **store** it in a password **vault** of some kind, the length of the password that was generated for me was: 89 characters.
16. ![Azure Portal - Enable SFTP](/uploads/azureportal_sftp_localusercreatepassword.png "Azure Portal - Enable SFTP")
17. You should see the connection string of the user, along with the Authentication method and container permissions.
18. ![Azure Storage Account SFTP - Local User Created](/uploads/azureportal_sftp_localusercreated.png "Azure Storage Account SFTP - Local User Created")

### Test Connectivity via SFTP to an Azure Storage Account

I will test Connectivity to the SFTP Azure Storage account using Windows 11, although the same concepts apply across various operating systems _(Linux, OSX, etc.)_.

#### Test using SFTP locally.

1. Make sure you have a copy of the Connection String and user password from the SFTP user account created earlier.
2. Open **Command Prompt**
3. Type in **sftp** CONNECTIONSTRING, example below and press Enter:
   * _sftp sftpstorageacc1337.lukeftpuser@sftpstorageacc1337.blob.core.windows.net_
4. If you get a prompt to verify the authenticity of the host matches (i.e. the name/URL of the storage account matches) and type in: Yes, to add the storage account to your known host's list
5. Press **Enter** and paste in the copy of the Password that was generated for you earlier.
6. You should be **connected to the Azure Storage account via SFTP**!
7. As you can see below, I am in the Files folder, which is my users home folder, and there is a file named: Test in it.
8. ![SFTP Windows](/uploads/sftp_windowstest.png "SFTP Windows")

   > Once you have connected to SFTP using the Windows command line you can type in: **?**
   >
   > That will give you a list of all the available commands to run, ie upload files etc 

#### Test using WinSCP

1. Make sure you have a copy of the Connection String and user password from the SFTP user account created earlier.
2. If you haven't already, **download** [**WinSCP **]()and **install** it
3. You should be greeted by the **Login page** _(but if you aren't, click on Session, New Session)_
4. For the hostname, type in the **URL** for the **storage account** _(after the @ in the connection string)_
5. For the **username,** type in everything before the @
6. Type in your **Password**
7. **Verify** that the port is 22 and file protocol is **SFTP** and click **Login**
8. ![Azure SFTP - WinSCP](/uploads/sftp_winscptest.png "Azure SFTP - WinSCP")
9. ![Azure SFTP - WinSCP](/uploads/sftp_winscptest2.png "Azure SFTP - WinSCP")

Congratulations! You have now created and tested Connectivity to the Azure Storage PaaS service SFTP!