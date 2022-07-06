---
date: 2022-07-06 00:00:00 +1200
title: Migrating Resources between regions using Azure Resource Mover
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/azureresourcemover_header.png"

---
With over 70+ Microsoft Azure [regions](https://azure.microsoft.com/en-us/global-infrastructure/geographies/?WT.mc_id=AZ-MVP-5004796#overview " Azure geographies") across the globe and new regions popping up all the time _(for example new New Zealand North region coming in 2023)_!

Migrating resources between regions is something that you may want to consider. Let's look at migrating workloads between them, by using [Azure Resource Mover](https://docs.microsoft.com/en-us/azure/resource-mover/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Resource Mover?").

### Overview

![](/uploads/azureresourcemover_header.png)

Azure Resource Mover helps you to move Azure resources between Azure regions, offering a single pane of glass to migrate different resource types, such as Virtual Machines or Azure SQL databases from a single portal without having to know how to migrate the individual underlying resources, or trying to work out the dependencies for each resource.

#### Why would you migrate resources between Regions?

Let’s start with why would you migrate resources between regions? Common scenarios include:

* Taking advantage of new Azure region expansions to be closer to customers and reduce latency _(such as migrating from Australia East to New Zealand North)_.
* Increasing availability and resilience by moving to Azure Availability Zones, from regions that don’t currently support it.
* Meeting data residential and compliance requirements.
* Consolidating workloads for mergers and acquisitions.
* The cost of resources in one region may also be cheaper than in another.

#### So, what are the risks of migrating resources?

Whatever your reason, moving your applications from Point A to Point B is often no easy task. Here are common reasons why:

* Moving resources can pose a risk of an outage.
* Workloads are often made up of multiple services, each requiring its own method and tools to move.
* Interdependencies are often not understood.
* Testing and rollback of these complex scenarios can be daunting.

#### So, what are the benefits of using Azure Resource Mover?

So, what are some of the benefits that Azure Resource Mover offers us?

* The ability to plan with ease, reducing the time and complexity of your move.
* Streamline your move process by identifying dependencies.
* Plan and test your move multiple times.
* Stage your move as part of scheduled downtime.
* Azure Resource Mover helps you orchestrate seamlessly with a consistent experience across common Azure resources​:
* Move multiple resources through a single pane of glass.
* Reduce manual touchpoints, which could increase the change of services being missed.
* Reduce overall time for your move from months to weeks or days* (based on the service and data being consumed).
* Azure Resource Mover helps you move with confidence by planning, testing, and moving related resources together and validating and testing your move before final commitment _(by testing your migrated services, while having the peace of mind that your source resources are left intact until you commit to the migration)_.

> So to recap, Azure Resource Mover offers you a unified experience to move multiple resource types across regions while validating dependencies between services and giving you the flexibility to adjust resources such as the Names, SKUs and Availability Zones during the migration to the destination region.

#### What can Azure Resource Mover move?

The currently supported resources _(as of July 2023)_ are:

* Azure Virtual Machines
* Azure SQL Database
* Azure Virtual Network
* SQL elastic pools
* Azure Load balancer
* Public IP
* Resource group
* Network security group
* Network interfaces
* Azure Availability Sets

And Azure Storage account region replication support is scheduled in the next 6-9 months to be released so the storage account migration should be ready by the time the NZ North comes live.

An updated list of Resources currently supported by Azure Resource Mover can be found here: [What resources can I move across regions using Resource Mover?](https://docs.microsoft.com/en-us/azure/resource-mover/common-questions?WT.mc_id=AZ-MVP-5004796#what-resources-can-i-move-across-regions-using-resource-mover "https://docs.microsoft.com/en-us/azure/resource-mover/common-questions?WT.mc_id=AZ-MVP-5004796#what-resources-can-i-move-across-regions-using-resource-mover")

#### Azure Resource Mover - The 6-Step Process!

![Azure Resource Mover - 6 Step Process](/uploads/azure-resource-mover-6-step-process.png "Azure Resource Mover - 6 Step Process")

k