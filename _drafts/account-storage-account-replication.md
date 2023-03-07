---
date: 2023-03-07 00:00:00 +1300
title: Object Block replication for Azure Storage Accounts
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
You can change [your current Azure Storage account replication type](https://learn.microsoft.com/azure/storage/common/redundancy-migration?tabs=portal&WT.mc_id=AZ-MVP-5004796#perform-a-conversion "Change how a storage account is replicated") from LRS _(Locally-Redundant Storage)_ to ZRS _(Zone-Redundant Storage)_ or GRS by using a self-initiated request can also replicate your block files from 1 storage account to another, using [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview?WT.mc_id=AZ-MVP-5004796 "Object replication for block blobs").

> Object replication asynchronously copies block blobs between a source storage account and a destination account. Some scenarios supported by object replication include:
>
> * **Minimizing latency.** Object replication can reduce latency for read requests by enabling clients to consume data from a region that is in closer physical proximity.
> * **Increase efficiency for compute workloads.** With object replication, compute workloads can process the same sets of block blobs in different regions.
> * **Optimizing data distribution.** You can process or analyze data in a single location and then replicate just the results to additional regions.
> * **Optimizing costs.** After your data has been replicated, you can reduce costs by moving it to the archive tier using life cycle management policies.
>
> The following diagram shows how object replication replicates block blobs from a source storage account in one region to destination accounts in two different regions.
>
> ![Diagram showing how object replication works](https://learn.microsoft.com/en-us/azure/storage/blobs/media/object-replication-overview/object-replication-diagram.svg)
>
> ![](/uploads/object-replication-diagram.svg)