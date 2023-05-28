---
title: 'Bytes, Blocks and Elasticity - Getting Started with Azure Elastic SAN'
author: Luke
categories: Azure
description: Deployment and look into Azure Elastic SAN
toc: 'True'
Header: /images/posts/BytesBlocksAzureElasticSAN_Blog_Heading.gif
---

Today we are going to take a look at the [Microsoft Azure Elastic SAN](https://azure.microsoft.com/products/storage/elastic-san/?WT.mc_id=AZ-MVP-5004796). 

#### Introduction

> “Azure Elastic SAN is a unique cloud-native and fully managed storage area network (SAN) service. Combining SAN-like capabilities with the benefits of being a cloud-native service, Azure Elastic SAN offers a massively scalable, cost-effective, high-performance, and resilient storage solution. It can connect to a variety of Azure compute services, enabling you to seamlessly transition your SAN data estate to the cloud without having to refactor your application architectures.”

Azure Elastic SAN provides a storage solution that is highly scalable, cost-effective, high-performing, and resilient. It caters to various storage needs, whether you're migrating your on-premises SAN to the cloud or creating your application directly in the cloud.

> As Azure Elastic SAN is still in the preview stage, as of 28/05/2023, it is important to note that its [features
> and functionality](https://learn.microsoft.com/azure/storage/elastic-san/elastic-san-introduction?WT.mc_id=AZ-MVP-5004796#support-for-azure-storage-features) may undergo changes before it reaches the production phase. Microsoft continues to actively gather feedback from users and refine the offering to ensure a seamless experience when it finally becomes
> generally available. Request access to the Preview by filling out this [form](https://aka.ms/AzureElasticSANPreviewAccess).

A Storage Area Network (SAN) typically comprises one or more physical appliances equipped with multiple drive bays, which are used to create volumes – it is considered a high-performance and low-latency connectivity
storage solution.

The benefits of a SAN are:

* Grow storage footprint independent of Compute
* Low latency and high storage throughput
* Cost efficient with massive scale.
* Built for databases and IOPS-intensive applications.
* Supports large virtualization deployments.

Introducing [Azure Elastic SAN](https://azure.microsoft.com/products/storage/elastic-san/?WT.mc_id=AZ-MVP-5004796#overview).

![Azure Elastic SAN - Overview](/images/posts/AzureElasticSAN.PNG "Azure Elastic SAN - Overview")

With the Azure Elastic SAN, we can the elasticity of the Microsoft Azure block storage systems, to supply expandable block storage capabilities to workloads via [iSCSI](https://learn.microsoft.com/en-gb/azure/storage/elastic-san/elastic-san-planning?WT.mc_id=AZ-MVP-5004796#iscsi-support)(Internet Small Computer Systems Interface), or services such as Azure Kubernetes Services through [Azure Container Storage](https://techcommunity.microsoft.com/t5/azure-storage-blog/azure-container-storage-in-public-preview/ba-p/3819246?WT.mc_id=AZ-MVP-5004796). 

When looking at some of the [benefits ](https://learn.microsoft.com/azure/storage/elastic-san/elastic-san-introduction?WT.mc_id=AZ-MVP-5004796#benefits-of-elastic-san)of an Azure Elastic SAN, over a traditional SAN, we will delve into several
common user stories around SAN provisioning and capacity management, with key differences around time to deployment and skills required. 
![Azure Elastic SAN - User journey](/images/posts/AzureElasticSAN_UserJourney.PNG "Azure Elastic SAN - User journey")

#### Architecture and Components

The Azure Elastic SAN consists of 3 layers:

![Azure Elastic SAN - Overview](/images/posts/AzureElasticSAN_3Layers.PNG "Azure Elastic SAN - Overview")

The Elastic SAN
The Elastic SAN itself, the Elastic SAN consists of the control plane, where you create and manage your Volume Groups from. The Elastic SAN where the resources are provisioned, and the Cost Management takes place (i.e.,Tags on the Elastic SAN resource).

##### Volume Group

An Azure Elastic SAN can have up to 20 volume groups, the volume group is where your security, encryption, and data protection configurations get applied.

The volume group is where is your Network Security rule and service endpoints is applied. Any settings or configurations applied to a volume group, such as virtual network rules, are inherited by any volumes
associated with that volume group.

![Azure Elastic SAN - Volume Group Network Security Rules](/images/posts/AzureElasticSAN_VolumeGroup_NetworkSecurityRule.PNG "Azure Elastic SAN - Volume Group Network Security Rules")

##### Volume

The volume in an Azure Elastic SAN, is the actual storage, that gets delivered and mapped to your workload or service.

Multiple volumes can be a part of a single-volume group, or separate groups – depending on requirements, such as accessibility across different virtual networks.

![Azure Elastic SAN - Volume](/images/posts/AzureElasticSAN_Volume.PNG "Azure Elastic SAN - Volume")

You partition the SAN's storage capacity into individual volumes. These individual volumes can be mounted to your clients with iSCSI. The name of your volume is part of their iSCSI IQD

#### ![Azure Elastic SAN - Volume](/images/posts/AzureElasticSAN_Volume2.PNG "Azure Elastic SAN - Volume")&#xA;&#xA;Deployment and Configuration

Now that we know what Azure Elastic SAN is, lets deploy it using the Azure Portal.

At the time of this article, the Azure Elastic SAN is only available in [specific regions](https://azure.microsoft.com/en-us/updates/regional-expansion-azure-elastic-san-public-preview-is-now-available-in-more-regions/?WT.mc_id=AZ-MVP-5004796) – and whether the SAN is capable of ZRS or LRS [storage redundancy](https://learn.microsoft.com/azure/storage/common/storage-redundancy?WT.mc_id=AZ-MVP-5004796). As I am based in New Zealand, the closest region at this time
to me is Australia East, this region only supports LRS so this is what I will be configuring.

If you haven’t already – as part of Public Preview, your Azure subscription needs to be [enabled](https://aka.ms/AzureElasticSANPreviewAccess) to provision Azure
Elastic SAN.

##### Deployment    

1. Login to the Microsoft Azure [portal](https://portal.azure.com/)
2. In the search box at the top of the portal, type in: Elastic SAN, navigate to the [Elastic SAN](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ElasticSan%2Felasticsans) resource page.
3. Click Create elastic SAN
4.





















#### &#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;

##### &#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;















































