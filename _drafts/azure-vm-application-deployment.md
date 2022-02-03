---
date: 2022-02-03 00:00:00 +1300
title: Azure VM Application Deployment
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
The Azure Compute Gallery _(superseded the Shared Image Gallery)_ offers more than just Azure Image management and replication, you can deploy Applications to your Virtual Machines. 

> An Azure Compute Gallery helps you build structure and organization around your Azure resources, like images and [applications](https://docs.microsoft.com/en-us/azure/virtual-machines/vm-applications). An Azure Compute Gallery provides:
>
> * Global replication.
> * Versioning and grouping of resources for easier management.
> * Highly available resources with Zone Redundant Storage (ZRS) accounts in regions that support Availability Zones. ZRS offers better resilience against zonal failures.
> * Premium storage support (Premium_LRS).
> * Sharing across subscriptions, and even between Active Directory (AD) tenants, using Azure RBAC.
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