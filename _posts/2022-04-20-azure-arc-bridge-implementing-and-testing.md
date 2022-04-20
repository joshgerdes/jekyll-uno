---
date: 2022-04-20 14:00:00 +1300
title: Azure Arc Bridge - Implementation and Testing
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azure_arc_vmware_portal_createresourcebridge.png"

---
[Azure Arc Bridge](https://docs.microsoft.com/en-us/azure/azure-arc/resource-bridge/overview "What is Azure Arc resource bridge "){:target="_blank"} _(currently in preview)_ is part of the core Azure Arc Hybrid Cloud platform.

### Overview

The Azure Arc resource bridge allows for VM _(Virtual Machine)_ self-servicing and managing on-premises Azure Stack HCI and VMWare virtualised workloads, supporting Linux and Windows.

Along with standard integration of Azure Arc workloads, such as support for Azure Policy and Azure extensions, Defender for Cloud support. The Azure Arc resource bridge offers the following self-service functionality direct from the Microsoft Azure portal, offering a single pane of a glass of your workloads, whether they exist on-premises or in Azure:

* Start, stop and restart a virtual machine
* Control access and add Azure tags
* Add, remove, and update network interfaces
* Add, remove, and update disks and update VM size _(CPU cores and memory)_
* Enable guest management
* Install extensions
* Azure Stack HCI - You can provision and manage on-premises Windows and Linux virtual machines _(VMs)_ running on Azure Stack HCI clusters.

> The resource bridge is a packaged virtual machine, which hosts a _management_ Kubernetes cluster that requires no user management. This virtual appliance delivers the following benefits:
>
> * Enables VM self-servicing from Azure without having to create and manage a Kubernetes cluster
> * It is fully supported by Microsoft, including update of core components.
> * Designed to recover from software failures.
> * Supports deployment to any private cloud hosted on Hyper-V or VMware from the Azure portal or using the Azure Command-Line Interface (CLI).
>
> All management operations are performed from Azure, no local configuration is required on the appliance.

![Azure Arc - Overview](/uploads/arc-bridge-architecture-overview.png)

> Azure Arc resource bridge currently supports the following Azure regions:
>
> * East US
> * West Europe

These regions hold the Resource Bridge metadata for the resources.

Today, we will stand up an Azure Arc Bridge that supports VMWare vSphere.

I will be running vSphere 6.7 on a single host in my home lab, connected to my Visual Studio subscription.

### Prerequisites

#### Private cloud environments

The following private cloud environments and their versions are officially supported for the Azure Arc resource bridge:

* VMware vSphere version 6.7
* Azure Stack HCI

_Note: You are unable to set this up on vSphere 7.0.3, as it is not currently supported - I tried!_

#### Permissions

* Contributor rights to the Resource Group that the Azure Arc bridge resource will be created.
* vSphere account _(with at least Read and modify VM rights)_

#### Required Azure resources

* Resource Group for your Azure Arc Resource Bridge

#### Required On-premises resources

* Resource pool with a reservation of at least 16 GB of RAM and four vCPUs. It should also have access to a datastore with at least 100 GB of free disk space.
* A workstation with rights to run PowerShell and install Python and the Azure CLI, with a line of sight to vCenter.

#### Networking

* The Arc resource bridge communicates outbound securely to Azure Arc over TCP port 443
* At least one free IP _(Internet Protocol)_ address on the on-premises network _(or three if there isn't a DHCP server)._ Make sure this isn't a used IP; you will need to enter this during the bridge provisioning script.

### Create Azure Arc Resource Bridge

#### Create Resource Bridge

 1. Log in to the **Azure Portal**
 2. In the search box up the top, type in: **Azure Arc**
 3. Click **Azure Arc**
 4. Click on: **VMware vCenters (preview)**
 5. Click **Add**
 6. ![Azure Arc - Resource Bridge](/uploads/azure_arc_vmware_portal.png "Azure Arc - Resource Bridge")
 7. Click: **Create a new resource bridge**
 8. ![Azure Arc - Resource Bridge](/uploads/azure_arc_vmware_portal_createresourcebridge.png "Azure Arc - Resource Bridge")
 9. Click **Next: Basics**
10. **Enter** the **following** information to suit your environment:

* **Name** _(of the Resource Bridge resource)_
* Select the **region** for your Metadata
* Create a [**Custom Location**](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/custom-locations "Create and manage custom locations on Azure Arc-enabled Kubernetes"){:target="_blank"}_(that matches your on-premises location, where your resources are stored, i.e. could be a data centre prefix that matches your naming convention)_
* Enter in the **name** of your **vCenter** resource _(this will represent your vCenter in Azure, so make sure it is easily identifiable)_

 1. ![Azure Arc - vCenter](/uploads/azure_arc_vmware_portal_createresourcesbridge.png "Azure Arc - vCenter")
 2. Click **Next: Tags**
 3. A list of default tags has been supplied; feel free to enter or change these to suit your environment.
 4. ![Azure Arc - vCenter](/uploads/azure_arc_vmware_portal_createresourcesbridgetags.png "Azure Arc - vCenter")
 5. Click **Next: Download and run the script.**
 6. Click on **Register** to register the Azure Arc Provider to your subscription. Please wait for this process to complete _(it may take a minute or two, you will see: Successfully register your subscription(s) when completed)_.
 7. Once completed, **download** the **onboarding** PowerShell **script**
 8. **Run** the PowerShell **script** from a computer that has access to Azure and vCenter. This script will download the necessary dependencies _(Azure CLI, Python)_ and, if necessary, authenticate to Azure.

        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        ./resource-bridge-onboarding-script.ps1
 9. When the script runs, you will be prompted for the following information.
    * **Proxy** information _(if the Workstation is behind a proxy)_
    * **UAC** _(User Access Control)_ **approval** for the script to install Azure CLI/Python on the workstation
    * **Azure authentication**
    * **vCenter** FQDN/**Address**
    * **vCenter Username** & **Password**
    * **vCenter datastore**
    * **vCenter folder** _(to place the template in)_
    * **IP address**
10. ![Azure Arc - vCenter Onboarding](/uploads/deploy-azurearcbridge.gif "Azure Arc - vCenter Onboarding")

#### Link vCenter to Azure Arc

You may not need to do the below, but my Bridge was in a 'running' state but hadn't added in the connection to vCenter.

 1. Log in to the **Azure Portal**
 2. In the search box up the top, type in: **Azure Arc**
 3. Click **Azure Arc**
 4. Click on: **Resource bridges (preview)**
 5. Click on your Azure Arc Bridge and **verify** the **status** is '**Running**' _(if it is not, make sure it has been started on-premises)_
 6. In the Azure Portal, click on **VMWare vCenters (preview)**
 7. Click **Add**
 8. Click **Use an existing resource bridge**
 9. Click **Next: Basics**
10. Create your **Custom Location**, then **enter** in the on-premises **vCenter** details
11. ![Azure Arc - vCenter Onboarding](/uploads/azure_arc_vmware_portal_bridge_vcenter.png "Azure Arc - vCenter Onboarding")
12. On the next blade, enter in your appropriate **Tags,** then click **Create**
13. Wait for the deployment to complete; this could take 2-5 minutes.
14. In the search box up the top, type in: **Azure Arc**
15. Click **Azure Arc**
16. Click on: **VMware vCenters (preview)**
17. You should now see your vSphere instance in a Connected state.
18. ![Azure Arc - vCenter](/uploads/azure_arc_vmware_portal_bridge_vcenterdeployed.png "Azure Arc - vCenter")

#### Enable vCenter resources to be managed in Microsoft Azure

Now that the Bridge has been created, we need to allow resources _(such as Virtual Machines, Datastores,  Networks)_.

 1. Log in to the **Azure Portal**
 2. In the search box up the top, type in: **Azure Arc**
 3. Click **Azure Arc**
 4. Click on: **VMware vCenters (preview)**
 5. Click on your **vCenter instance**
 6. Under vCenter Inventory, select **Virtual Machines**
 7. ![Azure Arc - vCenter](/uploads/azure_arc_vsphere_vm.png "Azure Arc - vCenter")
 8. Select the Virtual Machines you want to enable for management in Azure and click '**Enable in Azure**'
 9. Select your applicable Subscription and Resource Group (this is where the Azure Arc VM resources will be placed)
10. Make sure '**Enable Guest management**' is selected.
11. Enter in your Administrator _(this is the Admin Username and password of the workloads you want to install the Azure guest management too)_
12. ![Azure Arc - On-premises VM](/uploads/azure_arc_vsphere_vmguestagent.png "Azure Arc - On-premises VM")
13. Click **Enable**
14. It can take a few minutes to onboard these clients. If it fails, pick a single Virtual Machine and attempt to onboard that.
15. You can now repeat the process to onboard Networks, Resource Pools etc.

### Manage Virtual Machines in Microsoft Azure

Now that you have set up an Azure Arc Bridge and onboarded vCenter resources. You can now see and manage your vCenter Virtual Machines in Azure, examples below.

* Ensure that you have VMWare Tools installed and up-to-date to help full functionality, such as Restart, or there may be issues managing these.

#### Stop/Stop Virtual Machines

![Azure Arc - Start/Stop VM](/uploads/startstopvm-azurearcbridge.gif "Azure Arc - Start/Stop VM")

#### Resize Virtual Machines - CPU/Memory

![Azure Arc - Resize VM](/uploads/resizevm-azurearcbridge.gif "Azure Arc - Resize VM")

#### Resize Virtual Machines - Disk

![Azure Arc - Resize Disk](/uploads/resizevmdisk-azurearcbridge.gif "Azure Arc - Resize Disk")

### Troubleshooting

* The 'resource-bridge-onboarding-script.ps1' script contains an output file, named: arcvmware-output.log. This log file exists in the same directory as the script and is useful for investigating any errors.
* If you get no Folders, listed when the script prompts you to select a folder _(i.e. Please select folder)_:

1. Right-click the Datacenter in vSphere
2. Select New Folder
3. Select New VM and Templates folder
4. Create a folder

* If your Center becomes unavailable, it is most likely because you specified the same IP for the Azure Arc Appliance; if this is the case, log in to the host containing your Azure Arc Bridge and stop/delete the resources from the disk and remove from inventory. Then rerun deployment, this time selecting an appropriate IP.
