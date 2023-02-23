---
date: 2023-02-23 00:00:00 +1300
title: Azure Availability Zone Peering
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
In most [regions ](https://learn.microsoft.com/azure/reliability/availability-zones-service-support?WT.mc_id=AZ-MVP-5004796 "Availability zone service and regional support")_(and odds are, if your region doesn't have Avalibility Zones, it's on the roadmap to be set up)_, Microsoft Azure has [Availability Zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview?WT.mc_id=AZ-MVP-5004796 "What are Azure regions and availability zones?").

Each Azure region features data centres deployed within a latency-defined perimeter. At a high level, these zones consist of 3 separate data centres with independent cooling, power, switching etc.

![Azure availability zones](/uploads/availability-zones.png "Azure availability zones")

> Azure availability zones are connected by a high-performance network with a round-trip latency of less than 2ms. They help your data stay synchronized and accessible when things go wrong. Each zone is composed of one or more datacenters equipped with independent power, cooling, and networking infrastructure. Availability zones are designed so that if one zone is affected, regional services, capacity, and high availability are supported by the remaining two zones.
>
> With availability zones, you can design and operate applications and databases that automatically transition between zones without interruption. Azure availability zones are highly available, fault tolerant, and more scalable than traditional single or multiple datacenter infrastructures.

Today we are going to look into Availability Zone peering:

> Each data centre is assigned to a physical zone. Physical zones are mapped to logical zones in your Azure subscription. Azure subscriptions are automatically assigned this mapping at the time a subscription is created.

There are a few things to be aware of here that I will call out:

* **Physical zones** are mapped to **logical zones** in your Azure subscription.
* Azure subscriptions are automatically **assigned** this **mapping** **at the time** a **subscription** is **created**.

**So what does this mean?**

We know we have three separate data centres within a single region:

| Zone | Region |
| --- | --- |
| 1 | Australia East |
| 2 | Australia East |
| 3 | Australia East |

In fact, we can see these zones in the Azure Portal when we create resources:

![Azure Avalibility Zone - Selection](/uploads/avalibilityzone_selection_azportal.png "Azure Avalibility Zone - Selection")

This is great for making your solutions redundant against a single data centre failure and spreading your workloads across different zones; services such as Virtual Networks are zone-redundant by default, allowing access to resources across multiple zones out of the box.

One reason you may have all your resources in a single zone could be latency.