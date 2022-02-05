---
date: 2022-02-03 00:00:00 +1300
title: Datto Remote Management Azure VM Application Deployment
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
The Azure Compute Gallery _(superseded the Shared Image Gallery)_ offers more than just Azure Image management and replication, you can deploy Applications to your Virtual Machines.

### Overview

> An Azure Compute Gallery helps you build structure and organization around your Azure resources, like images and [applications](https://docs.microsoft.com/en-us/azure/virtual-machines/vm-applications). An Azure Compute Gallery provides:
>
> * Global replication.
> * Versioning and grouping of resources for easier management.
> * Highly available resources with Zone Redundant Storage _(ZRS)_ accounts in regions that support Availability Zones. ZRS offers better resilience against zonal failures.
> * Premium storage support _(Premium_LRS)_.
> * Sharing across subscriptions, and even between Active Directory _(AD)_ tenants, using Azure RBAC.
> * Scaling your deployments with resource replicas in each region.

Along with images, Azure VM applications that support both Linux and Windows operating systems gets these benefits.

> While you can create an image of a VM with apps pre-installed, you would need to update your image each time you have application changes. Separating your application installation from your VM images means there’s no need to publish a new image for every line of code change.
>
> Application packages provide benefits over other deployment and packaging methods:
>
> * Grouping and versioning of your packages
> * VM applications can be globally replicated to be closer to your infrastructure, so you don’t need to use AzCopy or other storage copy mechanisms to copy the bits across Azure regions.
> * Sharing with other users through Azure Role Based Access Control (RBAC)
> * Support for virtual machines, and both flexible and uniform scale sets
> * If you have Network Security Group (NSG) rules applied on your VM or scale set, downloading the packages from an internet repository might not be possible. And with storage accounts, downloading packages onto locked-down VMs would require setting up private links.
> * VM applications can be used with the [DeployIfNotExists](https://docs.microsoft.com/en-us/azure/governance/policy/concepts/effects) policy.

Azure VM Application packages _(stored in an Azure Storage account)_, uses multiple resources, as below:

| Resource | Description |
| --- | --- |
| Azure compute gallery | A gallery is a repository for managing and sharing application packages. Users can share the gallery resource and all the child resources will be shared automatically. The gallery name must be unique per subscription. For example, you may have one gallery to store all your OS images and another gallery to store all your VM applications. |
| VM application | This is the definition of your VM application. This is a logical resource that stores the common metadata for all the versions under it. For example, you may have an application definition for Apache Tomcat and have multiple versions within it. |
| VM Application version | This is the deployable resource. You can globally replicate your VM application versions to target regions closer to your VM infrastructure. The VM Application Version must be replicated to a region before it may be deployed on a VM in that region. |

* There is no extra charge for using VM Application Packages, but you will be charged for the following resources:
  * Storage costs of storing each package and any replicas.
  * Network egress charges for replication of the first image version from the source region to the replicated regions. Subsequent replicas are handled within the region, so there are no additional charges.

Before we deploy our first VM application, there are a few things we need to be aware of:

* VM Application requires an Azure Compute Gallery
* VM Application requires an Azure storage account to store your applications
* The VM Application gets downloaded to the VM using the name of the VM application _(not the actual name and extension of your file in the storage account)_
* Currently, in order to retry a failed installation, you need to remove the application from the profile and add it back
* No more than 5 applications per Virtual Machine deployed at a time
* The maximum size of the application is 1 GB
* You can't have multiple versions of the same application installed on a Virtual Machine, a newer version will supersede an older version either via an upgrade command or complete reinstall.

In this article, we are going to deploy the Datto Remote Management & Monitoring Agent to a Windows Server 2022 Virtual Machine, this agent is a simple executable that installs on a virtual machine and allows remote access and management of a virtual machine, without requiring any other form of connectivity _(Azure Bastion, RDP via Public IP, Site to Site VPN etc)_ for an MSP _(Managed Service Provider)_ using the Datto toolset, the same concept can be applied to any application. 

> It's worth noting the VM Applications are currently in Public Preview, there is a good chance there will be changes in the way these operate and are configured when it becomes Generally Available.

### Setup Azure VM Application Deployment

#### Prerequisites

In order to use VM Applications, we need:

* A storage account
* Azure Compute gallery
* VM application definition and version _(in my example: the Datto RMM agent)_

Following the guide, we will run through the creation of everything from scratch, I am however assuming you already have the executable or application package and know the instructions to install/uninstall it - as each application is different. The Microsoft[ VM Applications docs](https://docs.microsoft.com/en-us/azure/virtual-machines/vm-applications#exe-installer "VM Applications overview") give a few good examples for getting started with various different applications.

#### Setup Storage Account

The Storage account is where your application will be placed, it uses blobs, depending on the importance of your application deployments, you may want to go for geo-replication etc, but in this example, I will be going with a locally redundant, StorageV2 general-purpose account.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
 2. Click on **+ Create a Resource**
 3. Search for: **Storage account**, and **select** it
 4. Click [**Create**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM "Create a storage account")
 5. **Select** your **subscription**
 6. **Select** a **Resource Group** for your storage account, **or create** a new **one**
 7. **Enter** your storage account **name** _(this needs to be globally unique)_
 8. **Select** your **region** that your application will be in, although the application can be replicated to other regions, it's better to select your primary region here.
 9. **Select** the **performance** and **redundancy** to match your requirements and click **Next: Advanced**
10. ![](/uploads/create-a-storage-account-microsoft-azure.png)
11. You can **leave** most **settings** here as **default**, the application executable will need to be able to be accessed directly, make sure the **Minimum TLS** is at least **1.2**.
12. You don't need hierarchical namespace etc, unselect 'Allow cross-tenant replication' unless this is a feature you use.
13. ![](/uploads/create-a-storage-account-advanced-microsoft-azure.png)
14. Click **Review + Create** to skip to the last blade, most defaults are fine, but if you wanted to adjust the blob retainment and soft delete settings, go to the Data Protection tab, set them, then review your configuration and select **Create**.

#### Setup Azure Compute Gallery

Now that we have the Storage account to store your application binaries, we now need an Azure Compute Gallery _(previously the Shared Image Gallery)_ to store your application definition and version metadata

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
 2. Click on **+ Create a Resource**
 3. Search for: **Azure Compute Gallery** and **select** it
 4. Click [**Create**](https://portal.azure.com/#create/microsoft.sharedImageGallery "Create Azure compute gallery")
 5. **Select** your **subscription** and **resource group** _(in this case, I am going to use the same resource group as the Storage account I created earlier)_
 6. Type in a **name**, and **select** your **region**
 7. Although not mandatory, use the opportunity to fill in a description for the purpose of the Compute Gallery for future reference
 8. ![](/uploads/create-azure-compute-gallery-microsoft-azure.png)
 9. Select **Review + Create**
10. Verify everything is correct and click on: **Create**

#### Create Application Definition

VM application definitions are created within a gallery and carry information about the application and requirements for using it internally. This includes the operating system type for the VM application versions contained within the application definition. The name of your Application definition defines the name of the file that will be downloaded to your virtual machines.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
 2. Navigate to '**All Resources'**
 3. **Find and click on** your **Azure Compute Gallery** you created earlier
 4. On the overview pane, select **+ Add**
 5. Click on +**VM application definition**
 6. Your subscription and resource group should be automatically selected to the location of the Compute Gallery, type in the **name of** your **Application**
 7. Select your **region**
 8. Select the **OS type** - in my case, I select **Windows**
 9. ![](/uploads/create-a-vm-application-definition-microsoft-azure.png)
10. Click **Next: Publishing Options**
11. 