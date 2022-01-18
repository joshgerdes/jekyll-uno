---
date: 2022-01-19 00:00:00 +1300
title: Application Security Groups in Microsoft Azure
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Azure Application Security Groups, allow you to define what workloads _(Virtual Machines)_ you are running in Azure, has access to what resource - without being tied by managing complex IP address rules inside a Network Security Group.

> Application security groups enable you to configure network security as a natural extension of an application's structure, allowing you to group virtual machines and define network security policies based on those groups. You can reuse your security policy at scale without manual maintenance of explicit IP addresses.

These Azure Application Security groups allow you to define your workloads, for example, Azure Virtual Desktop Session Hosts as a 'group' and what they may have access to in your Azure Virtual Network without opening up the service to everything inside of that VNET, or creating overly complex rules that could make it hard to troubleshoot.

There are a few things to be mindful of:

* Azure Application Security Groups are Virtual Network-specific, so can work to allow resources across subnets, but not in separate Virtual Networks, even if they have peered.
* As with most Azure resources, there are Subscription level[ limits](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits?toc=/azure/virtual-network/toc.json#azure-resource-manager-virtual-networking-limits "Networking limits - Azure Resource Manager"), you cannot have more than 3,000 Azure Application Security groups in a single subscription and region.