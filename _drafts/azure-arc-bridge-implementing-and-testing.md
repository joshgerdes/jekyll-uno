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
Azure Arc Bridge (currently in preview), is part of the core Azure Arc Hybrid Cloud platform.

The Azure Arc resource bridge allows for VM self-servicing and management of on-premises Azure Stack HCI and VMWare virtualized workloads, supporting both Linux and Windows. 

> The resource bridge is a packaged virtual machine, which hosts a _management_ Kubernetes cluster that requires no user management. This virtual appliance delivers the following benefits:
>
> * Enables VM self-servicing from Azure without having to create and manage a Kubernetes cluster
> * It is fully supported by Microsoft, including update of core components.
> * Designed to recover from software failures.
> * Supports deployment to any private cloud hosted on Hyper-V or VMware from the Azure portal or using the Azure Command-Line Interface (CLI).
>
> All management operations are performed from Azure, no local configuration is required on the appliance.