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

The Azure Arc resource bridge allows for VM self-servicing and management of on-premises Azure Stack HCI and VMWare virtualized workloads, supporting both Linux and Windows.

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

Today, we are going to stand up an Azure Arc Bridge, that supports VMWare vSphere _(supported on a version greater than VMware vSphere version 6.7)_.

I will be running vSphere 7.0.3, on a single host in my home lab, connected to my Visual Studio subscription.

### Prerequisites

#### Private cloud environments

The following private cloud environments and their versions are officially supported for the Azure Arc resource bridge:

* VMware vSphere version 6.7
* Azure Stack HCI

#### Required Azure permissions

* Contributor rights to the Resource Group that the Azure Arc bridge resource will be created to
* The Arc resource bridge communicates outbound securely to Azure Arc over TCP port 443

### Create Azure Arc Resource Bridge

#### Create Resource Bridge

1. Log in to the [**Azure Portal**]()
2. In the search box up the top, type in: **Azure Arc**
3. Click **Azure Arc**
4. Click on: **VMware vCenters (preview)**
5. Click **Add**
6. ![](/uploads/azure_arc_vmware_portal.png)
7. 