---
date: 2023-02-23 00:00:00 +1300
title: Azure Availability Zone Peering
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
In most regions _(and odds are, if your region doesn't have Avalibility Zones, it's on the roadmap to be set up)_, Microsoft Azure has Availability Zones.

Each Azure region features data centres deployed within a latency-defined perimeter. At a high level, these zones consist of 3 separate data centres with independent cooling, power, switching etc.

![Azure availability zones](/uploads/availability-zones.png "Azure availability zones")

> Azure availability zones are connected by a high-performance network with a round-trip latency of less than 2ms. They help your data stay synchronized and accessible when things go wrong. Each zone is composed of one or more datacenters equipped with independent power, cooling, and networking infrastructure. Availability zones are designed so that if one zone is affected, regional services, capacity, and high availability are supported by the remaining two zones.
>
> With availability zones, you can design and operate applications and databases that automatically transition between zones without interruption. Azure availability zones are highly available, fault tolerant, and more scalable than traditional single or multiple datacenter infrastructures.