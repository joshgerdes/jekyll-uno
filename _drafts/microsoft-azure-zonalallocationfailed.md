---
date: 2022-07-27 00:00:00 +1200
title: 'Microsoft Azure - ZonalAllocationFailed '
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
> **Error code**: AllocationFailed or ZonalAllocationFailed
>
> **Error message**: "Allocation failed. We do not have sufficient capacity for the requested VM size in this region. Read more about improving likelihood of allocation success at [https://aka.ms/allocation-guidance](https://aka.ms/allocation-guidance?WT.mc_id=AZ-MVP-5004796 "https://aka.ms/allocation-guidance")"

When you create a virtual machine (VM), start stopped (deallocated) VMs, or resize a VM, Microsoft Azure allocates compute resources to your subscription. 

Microsoft is continually investing in additional infrastructure and features to ensure that they always have all VM types available to support customer demand. However, you may occasionally experience resource allocation failures because of unprecedented growth in demand for Azure services in specific regions.

**Waiting for more Compute to be added to the Azure server clusters may not be an option, so what can you do?**

The first thing is to:

* Take a screenshot of the error
* Copy the Activity/Deployment ID
* Take note of the Region 
* Take note of the Availability Zone.

Let [Azure Support](https://azure.microsoft.com/en-us/support/?WT.mc_id=AZ-MVP-5004796 " Azure support") know; Microsoft may already be aware, but raising a support request helps to identify potentially impacted customers, and if you have any 