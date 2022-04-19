---
date: 2022-04-19 00:00:00 +1200
title: Azure Arc Bridge - Implementing and Testing
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
[Azure Arc Bridge](https://docs.microsoft.com/en-us/azure/azure-arc/resource-bridge/overview "What is Azure Arc resource bridge ") _(currently in preview)_, is part of the core Azure Arc Hybrid Cloud platform.

### Overview

The Azure Arc resource bridge allows for VM (Virtual Machine) self-servicing and management of on-premises Azure Stack HCI and VMWare virtualized workloads, supporting both Linux and Windows.

Along with normal integration of Azure Arc workloads, such as support for Azure Policy. The Azure Arc resource bridge offers the following self-service functionality direct from the Microsoft Azure portal, offering a single pane of a glass of your workloads, whether they exist on-premises or in Azure:

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

![](/uploads/arc-bridge-architecture-overview.png)

> Azure Arc resource bridge currently supports the following Azure regions:
>
> * East US
> * West Europe

These regions, hold the Resource Bridge metadata for the resources.

Today, we are going to stand up an Azure Arc Bridge, that supports VMWare vSphere.

I will be running vSphere 6.7, on a single host in my home lab, connected to my Visual Studio subscription.

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
* A workstation, with rights to run PowerShell, and install Python and the Azure CLI, with a line of sight to vCenter.

#### Networking

* The Arc resource bridge communicates outbound securely to Azure Arc over TCP port 443
* At least one free IP _(Internet Protocol)_ address on the on-premises network _(or 3 if there isn't a DHCP server)._ Make sure this isn't a used IP, you will need to enter this during the bridge provisioning script.

### Create Azure Arc Resource Bridge

#### Create Resource Bridge

 1. Log in to the [**Azure Portal**]()
 2. In the search box up the top, type in: **Azure Arc**
 3. Click **Azure Arc**
 4. Click on: **VMware vCenters (preview)**
 5. Click **Add**
 6. ![](/uploads/azure_arc_vmware_portal.png)
 7. Click: **Create a new resource bridge**
 8. ![](/uploads/azure_arc_vmware_portal_createresourcebridge.png)
 9. Click **Next: Basics**
10. **Enter** the **following** information to suit your environment:

* **Name** _(of the Resource Bridge resource)_
* Select the **region** for your Metadata
* Create a [**Custom location **](https://docs.microsoft.com/en-us/azure/azure-arc/kubernetes/custom-location "Create and manage custom locations on Azure Arc-enabled Kubernetes")_(that matches your on-premises location, where your resources are stored, ie could be a data centre prefix that matches your naming convention)_
* Enter in the **name** of your **vCenter** resource _(this will represent your vCenter in Azure, so make sure it is easily identifiable)_

 1. ![](/uploads/azure_arc_vmware_portal_createresourcesbridge.png)
 2. Click **Next: Tags**
 3. A list of default tags has been supplied, feel free to enter or change these to suit your environment.
 4. ![](/uploads/azure_arc_vmware_portal_createresourcesbridgetags.png)
 5. Click **Next: Download and run the script**
 6. Click on **Register**, to register the Azure Arc Provider, to your subscription. Wait for this process to complete _(it may take a minute or two, you will see: Successfully register your subscription(s) when completed)_.
 7. Once completed, **download** the **onboarding** PowerShell **script**
 8. **Run** the PowerShell **script** from a computer that has access to Azure and vCenter, this script will download the necessary dependencies _(Azure CLI, Python)_ and if necessary authenticate to Azure.

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
10. sdsd

#### Link vCenter to Azure Arc

1. Log in to the [**Azure Portal**]()
2. In the search box up the top, type in: **Azure Arc**
3. Click **Azure Arc**
4. Click on: **Resource bridges (preview)**
5. Click on your Azure Arc Bridge and **verify** the **status** is '**Running**' _(if it is not make sure it has been started on-premises)_
6. In the Azure Portal, click on **VMWare vCenters (preview)**
7. Click **Add**
8. 

### Troubleshooting

* The 'resource-bridge-onboarding-script.ps1' script contains an output file, named: arcvmware-output.log. This log file exists in the same directory as the script and is useful for an investigation into any errors.
* If you get no Folders, listed when the script prompts you to select a folder _(ie Please select folder)_:

1. Right-click the Datacenter in vSphere
2. Select New Folder
3. Select New VM and Templates folder
4. Create a folder

* If your Center, becomes unavailable, it is most likely because you specified the same IP for the Azure Arc Appliance, if this is the case, log in to the host containing your Azure Arc Bridge and stop/delete the resources from the disk and remove from inventory. Then rerun deployment again, this time selecting an appropriate IP.