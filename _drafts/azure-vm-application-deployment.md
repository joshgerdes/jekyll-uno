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