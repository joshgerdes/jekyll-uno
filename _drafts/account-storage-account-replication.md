---
date: 2023-03-07 00:00:00 +1300
title: Object Block replication for Azure Storage Accounts
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
Not only can you change [your current Azure Storage account replication type](https://learn.microsoft.com/azure/storage/common/redundancy-migration?tabs=portal&WT.mc_id=AZ-MVP-5004796#perform-a-conversion "Change how a storage account is replicated") from LRS _(Locally-Redundant Storage)_ to ZRS _(Zone-Redundant Storage)_ or GRS by using a self-initiated request, but you can also replicate your block files from 1 storage account to another, using [Object replication for block blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview?WT.mc_id=AZ-MVP-5004796 "Object replication for block blobs").