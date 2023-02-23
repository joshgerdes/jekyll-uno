---
date: 2023-02-23 00:00:00 +1300
title: Azure Availability Zone Peering
author: Luke
categories: []
toc: false
header:
  teaser: "/uploads/availability-zones.png"

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

Lets us go back to the paragraphs around physical and logical zones and mapping - what does this mean?

What this means is that each of the three datacenters is assigned a physical **AND** logical mapping, so your Azure datacentres look like this:

| Zone (Physical) | Region | Zone (Logical) |
| --- | --- | --- |
| 1 | Australia East | 3 |
| 2 | Australia East | 2 |
| 3 | Australia East | 1 |

When you **deploy a resource into an Azure Avalibility Zone and select Zone 1** - you are **selecting the Logical Zone, NOT** a **physical zone**.

This means that **FOR EACH** Microsoft **Azure subscription,** whether in the same Azure Active Directory tenancy or not, **Zone 1** can be a **different physical data center**.

So if you have resources deployed across multiple subscriptions, and all your resources are deployed to Zone 1 - they **MAY NOT** be in the same physical datacenter.

| Azure Subscriptions | Region | Zone (Logical) | Zone (Physical) |
| --- | --- | --- | --- |
| Sub A | Australia East | 1 | 1 |
| Sub B | Australia East | 1 | 3 |
| Sub B | Australia East | 1 | 1 |

In an example like the above, you have three separate Azure subscriptions, and you have deployed your Virtual Machines and other resources across all Azure subscriptions into Zone 1, 2 of your subscriptions are using the same physical zone for zone 1, and another subscription is using a separate availability zone altogether. 