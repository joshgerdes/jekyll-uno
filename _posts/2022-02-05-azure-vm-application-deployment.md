---
date: 2022-02-05 00:00:00 +1300
title: Datto Remote Management Azure VM Application Deployment
author: Luke
categories:
- Azure
toc: true
header:
   teaser: images/iazure-marketplace-banner.png
---
The Azure Compute Gallery _(superseded the Shared Image Gallery)_ offers more than just Azure Image management and replication, and you can deploy Applications to your Virtual Machines.

### Overview

> An Azure Compute Gallery helps you build structure and organization around your Azure resources, like images and [applications](https://learn.microsoft.com/en-us/azure/virtual-machines/vm-applications?WT.mc_id=AZ-MVP-5004796){:target="_blank"}. An Azure Compute Gallery provides:
>
> * Global replication.
> * Versioning and grouping of resources for easier management.
> * Highly available resources with Zone Redundant Storage _(ZRS)_ accounts in regions that support Availability Zones. ZRS offers better resilience against zonal failures.
> * Premium storage support _(Premium_LRS)_.
> * Sharing across subscriptions, and even between Active Directory _(AD)_ tenants, using Azure RBAC.
> * Scaling your deployments with resource replicas in each region.

With images, Azure VM applications that support both Linux and Windows operating systems get these benefits.

> While you can create an image of a VM with apps pre-installed, you would need to update your image each time you have application changes. Separating your application installation from your VM images means there’s no need to publish a new image for every line of code change.
>
> Application packages provide benefits over other deployment and packaging methods:
>
> * Grouping and versioning of your packages
> * VM applications can be globally replicated to be closer to your infrastructure, so you don’t need to use AzCopy or other storage copy mechanisms to copy the bits across Azure regions.
> * Sharing with other users through Azure Role Based Access Control (RBAC)
> * Support for virtual machines, and both flexible and uniform scale sets
> * If you have Network Security Group (NSG) rules applied on your VM or scale set, downloading the packages from an internet repository might not be possible. And with storage accounts, downloading packages onto locked-down VMs would require setting up private links.
> * VM applications can be used with the [DeployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects?WT.mc_id=AZ-MVP-5004796){:target="_blank"} policy.

Azure VM Application packages _(stored in an Azure Storage account)_ uses multiple resources, as below:

| Resource | Description |
| --- | --- |
| Azure compute gallery | A gallery is a repository for managing and sharing application packages. Users can share the gallery resource and all the child resources will be shared automatically. The gallery name must be unique per subscription. For example, you may have one gallery to store all your OS images and another gallery to store all your VM applications. |
| VM application | This is the definition of your VM application. This is a logical resource that stores the common metadata for all the versions under it. For example, you may have an application definition for Apache Tomcat and have multiple versions within it. |
| VM Application version | This is the deployable resource. You can globally replicate your VM application versions to target regions closer to your VM infrastructure. The VM Application Version must be replicated to a region before it may be deployed on a VM in that region. |

There is no extra charge for using VM Application Packages, but you will be charged for the following resources:

* Storage costs of storing each package and any replicas.
* Network egress charges for replication of the first image version from the source region to the replicated regions. Subsequent replicas are handled within the region, so there are no additional charges.

Before we deploy our first VM application, there are a few things we need to be aware of:

* VM Application requires an Azure Compute Gallery
* VM Application requires an Azure storage account to store your applications
* The VM Application gets downloaded to the VM using the name of the VM application _(not the actual name and Extension of your file in the storage account)_
* Currently, in order to retry a failed installation, you need to remove the application from the profile and add it back
* No more than five applications per Virtual Machine deployed at a time
* The maximum size of the application is 1 GB
* You can't have multiple versions of the same application installed on a Virtual Machine, and a newer version will supersede an older version either via an upgrade command or complete reinstall.

In this article, we are going to deploy the Datto Remote Management & Monitoring Agent to a Windows Server 2022 Virtual Machine; this agent is a simple executable that installs on a virtual machine and allows remote access and management of a virtual machine, without requiring any other form of connectivity _(Azure Bastion, RDP via Public IP, Site to Site VPN etc.)_ for an MSP _(Managed Service Provider)_ using the Datto toolset, the same concept can be applied to any application _(theoretically you can also use this to run PowerShell installs or chocolatey installs)_. 

> It's worth noting the VM Applications are currently in Public Preview, there is a good chance there will be changes in the way these operate and are configured when it becomes Generally Available.

### Setup Azure VM Application Deployment

#### Prerequisites

In order to use VM Applications, we need:

* A storage account
* Azure Compute gallery
* VM application definition and version _(in my example: the Datto RMM agent)_

Following the guide, we will run through the creation of everything from scratch; I am, however, assuming you already have the executable or application package and know the instructions to install/uninstall it - as each application is different. The Microsoft[VM Applications docs](https://learn.microsoft.com/en-us/azure/virtual-machines/vm-applications?WT.mc_id=AZ-MVP-5004796#exe-installer "VM Applications overview"){:target="_blank"} give a few good examples for getting started with various applications.

#### Setup Storage Account

The Storage account is where your application will be placed; it uses blobs; depending on the importance of your application deployments, you may want to go for geo-replication etc., but in this example, I will be going with a locally redundant, StorageV2 general-purpose account.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}
 2. Click on **+ Create a Resource**
 3. Search for: **Storage account**, and **select** it
 4. Click [**Create**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM "Create a storage account"){:target="_blank"}
 5. **Select** your **subscription**
 6. **Select** a **Resource Group** for your storage account, **or create** a new **one**
 7. **Enter** your storage account **name** _(this needs to be globally unique)_
 8. **Select** your **region** that your application will be in; although the application can be replicated to other regions, it's better to select your primary region here.
 9. **Select** the **performance** and **redundancy** to match your requirements and click **Next: Advanced**
10. ![Azure Portal - Create Storage Account](/uploads/create-a-storage-account-microsoft-azure.png)
11. You can **leave** most **settings** here as **default**, the application executable will need to be able to be accessed directly; make sure the **Minimum TLS** is at least **1.2**.
12. You don't need hierarchical namespace etc.; unselect '_Allow cross-tenant replication'_ unless this is a feature you use.
13. ![Azure Portal - Create Storage Account](/uploads/create-a-storage-account-advanced-microsoft-azure.png)
14. Click **Review + Create** to skip to the last blade; most defaults are fine, but if you want to adjust the blob retainment and soft delete settings, go to the Data Protection tab, set them, then review your Configuration and select **Create**.
15. Go back to your storage account and click **Configuration**
16. Make sure: Allow storage account key access is: **Enabled**; if it is not, select Enabled and click **Save**.

#### Setup Azure Compute Gallery

Now that we have the Storage account to store your application binaries, we now need an Azure Compute Gallery _(previously the Shared Image Gallery)_ to keep your application definition and version metadata.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}
 2. Click on **+ Create a Resource**
 3. Search for: **Azure Compute Gallery** and **select** it
 4. Click [**Create**](https://portal.azure.com/#create/microsoft.sharedImageGallery "Create Azure compute gallery"){:target="_blank"}
 5. **Select** your **subscription** and **resource group** _(in this case, I am going to use the same resource group as the Storage account I created earlier)_
 6. Type in a **name**, and **select** your **region**
 7. Although not mandatory, use the opportunity to fill in a description for the purpose of the Compute Gallery for future reference
 8. ![Azure Portal - Create Storage Account](/uploads/create-azure-compute-gallery-microsoft-azure.png)
 9. Select **Review + Create**
10. Verify everything is correct and click on: **Create**

#### Create Application Definition

VM application definitions are created within a gallery and carry information about the application and requirements for using it internally. This includes the operating system type for the VM application versions contained within the application definition. The name of your Application definition defines the name of the file that will be downloaded to your virtual machines.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}
 2. Navigate to '**All Resources'**
 3. **Find and click on** your **Azure Compute Gallery** you created earlier
 4. On the overview pane, select **+ Add**
 5. Click on +**VM application definition**
 6. Your subscription and resource group should be automatically selected to the location of the Compute Gallery, type in the **name of** your **applicatio.n**
 7. Select your **region**
 8. Select the **OS type** - in my case, and I select **Windows**
 9. ![Azure Portal - Create Application Definition](/uploads/create-a-vm-application-definition-microsoft-azure.png)
10. Click **Next: Publishing Options**
11. The following fields are not mandatory, but I recommend filling in areas to help report on and manage your applications.
    * Description
    * End of life date
    * Eula link
    * Privacy URI
    * Release notes URI
12. ![Azure Portal - Create Metadata](/uploads/create-a-vm-application-definition-metadata-microsoft-azure.png)
13. Click **Review + create**
14. Verify your Configuration and select **Create**

#### Create Application version

Now that we have the application definition setup, it's time to set up the version and upload our binary file.+

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}
 2. Navigate to '**All Resources'**
 3. **Find and click on** your **Azure Compute Gallery** you created earlier
 4. Click on **Definitions**_(besides the Get Started link)_
 5. **Select** your Application **definition**
 6. Click on: **+Add** 
 7. **Enter** in your **version number**, and this will increment and grow as you adjust and troubleshoot your application; I recommend starting with 0.0.1 then working your way up, with 1.0.0 being potentially your final/production-ready releast.
 8. Select your **Region**
 9. Now we need to select our source application package _(you can enter in your blob URL if you know it)_; we haven't uploaded it to our storage account yet, so we will select **Browse**
10. **Select** your **Storage account**
11. Press **+ Container**
12. **Enter** in the **name** of your **container** _( it has to be in lowercase)_, such as the application name _(to keep things separate, consider a container per application)_
13. Press **Upload**
14. **Browse** to your **file** and select it
15. Expand **Advanced**
16. Make sure that Blob type is: **Blob**
17. ![Azure Portal - Azure Blob](/uploads/upload-blob-microsoft-azure.png)
18. Click **Upload**
19. **Select** your newly uploaded file and click **Select**
20. _Note: You can only upload one file as part of your package, you can upload a ZIP file and have your Install script extract it_
21. The **Install script** is the command to install to your application, by default windows applications are set to install cmd. This already knows the directory your files are in because the file will be uploaded as the application name (i.e. DattoRMM), it needs to be renamed to include .exe and then ran, I will switch to PowerShell for the Install script, so will enter:

        powershell.exe -command "Rename-Item '.\DattoRMM' -NewName 'DattoRMM.exe'; Start-Process '.\DattoRMM.exe'"
22. If you have a script to uninstall the application, enter it _(in my case, I am just going to put a '.' to skip this, as I don't currently have an uninstall script developed)_
23. The rest of the Configuration isn't mandatory; the Update script is used by Azure when a new version of an application is created; by default, the Azure VM extension will treat an upgrade like a completely new install and run the install steps unless an update script is defined.
24. ![Azure Portal - Application Version](/uploads/create-a-vm-application-version-microsoft-azure.png)
25. Click **Next: Replication**
26. Like Azure Compute Images, you can replicate your Azure VM applications across multiple regions _(depending on where your workloads are)_, such as Australia East to West Europe, and store it then Zone Redundant or Local storage. In my example, I am going to leave mine as one replica in Australia East on locally-redundant storage and click **Review + create**
27. Verify everything looks ok and click **Create** to create your application version! This may take a few minutes to create, depending on your configuration and replication.

### Deploy Azure VM Application

#### Deploy Azure VM Application to Virtual Machines using the Azure Portal

Now that your Azure VM Application has been created, it is now time to deploy to a Virtual Machine. I have a Windows Server 2022 Datacenter Azure Gen 2 VM running as a Standard_B2ms as my test machine, and because I am going to use the Datto RMM agent to connect to the machine, I don't need any RDP ports open etc.

 1. Open the [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}
 2. Navigate to **Virtual Machines**
 3. Click on your Virtual Machine
 4. Under Settings, click **Extensions + Applications**
 5. Click **VM Applications**
 6. Click **+ Add application**
 7. **Select** your **application** _(note you can select a particular version, by default, it is the latest)_
 8. Click **Ok**
 9. ![Azure Portal - VM-P01](/uploads/vm-p01-microsoft-azure.png)
10. You can select your Install Order _(i.e. if you had multiple applications, you can select which one installs 1st, 2nd, third and so on)_; I will select No Reference and click Save to start the deployment.
11. If you click Extensions, you should see that a: VMAppExtension has started to be installed; click on Refresh to update the status and click on the Extension to a more detailed status message, hopefully you see ":Operational Install is SUCCESS"
12. My Virtual Machine has now had the Datto Remote Management agent installed successfully and has appeared in the portal for me to connect to!
13. ![Azure - Datto RMM](/uploads/vm-p01-datto-rmm.png)

#### Deploy Azure VM Application to Multiple Virtual Machines using PowerShell

I've created the PowerShell script below to deploy an application to multiple Virtual Machines at once, it can easily be adjusted for a PowerShell Runbook that runs periodically to install software on machines it may be missing. As usual, please make sure you test and run any PowerShell scripts first in a demo environment.

    $allvms = Get-AzVM
    $applicationname = 'DattoRMM'
    $galleryname = 'AzComputeGallery'
    $galleryrg = 'vmapps-prod-rg'
    $appversion = '0.0.1'
    
      
    try
    {
      ForEach ($vm in $allvms)
    
      {
        $AzVM = Get-AzVM -ResourceGroupName $vm.ResourceGroupName -Name $vm.Name
        $appversion = Get-AzGalleryApplicationVersion `
        -GalleryApplicationName $applicationname `
        -GalleryName $galleryname `
        -Name $appversion `
        -ResourceGroupName $galleryrg
        $packageid = $appversion.Id
        $app = New-AzVmGalleryApplication -PackageReferenceId $packageid
        Add-AzVmGalleryApplication -VM $AzVM -GalleryApplication $app
        Update-AzVM -ResourceGroupName $vm.ResourceGroupName -VM $AzVM -ErrorAction Stop
      }
    }
    
    catch [Microsoft.Azure.Commands.Compute.Common.ComputeCloudException]
    {
      #Most likely failed due to duplicate package ID/identical version
      [Management.Automation.ErrorRecord]$e = $_
    
      $info = [PSCustomObject]@{
        Exception = $e.Exception.Message
        Reason    = $e.CategoryInfo.Reason
        Target    = $e.CategoryInfo.TargetName
      }
    
      $info
    }

### Troubleshooting VM Application

If you have problems installing a package, just a reminder that the VM Application, uploads your file based on the name of the Application, to the server and needs to be renamed with a valid extension as part of the install script.

#### Package Location

The package/extension location is here: 

* C:\\Packages\\Plugins\\Microsoft.CPlat.Core.VMApplicationManagerWindows\\{VERSION#}\\

You will find your Application binary under Downloads.

#### Logs

**For the extension status logs, navigate to:** 

* C:\\Packages\\Plugins\\Microsoft.CPlat.Core.VMApplicationManagerWindows\\{VERSION#}\\Status

You should see files such as:

* 0.status

You can right-click these and open them in Notepad, and you should have the timestamp and the last status message, this should be identical to what you see in the Azure Portal.

**For the application install logs, navigate to:** 

* C:\\Packages\\Plugins\\Microsoft.CPlat.Core.VMApplicationManagerWindows\\{VERSION#}\\Downloads\\{APPNAME}\\{APPVERSION}\\

You may see files such as:

* stderr
* stdout

You can right-click these and open them in Notepad, any errors will be noted in these.

#### Troubleshooting during preview

* [Troubleshooting during preview](https://learn.microsoft.com/en-us/azure/virtual-machines/vm-applications?WT.mc_id=AZ-MVP-5004796#troubleshooting-during-preview "Troubleshooting during preview"){:target="_blank"}
