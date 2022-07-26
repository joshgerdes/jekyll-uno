---
date: 2022-07-27 00:00:00 +1200
title: 'Microsoft Azure - ZonalAllocationFailed '
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/zonalallocationfailed.png"

---
> **Error code**: AllocationFailed or ZonalAllocationFailed
>
> **Error message**: "Allocation failed. We do not have sufficient capacity for the requested VM size in this region. Read more about improving likelihood of allocation success at [https://aka.ms/allocation-guidance](https://aka.ms/allocation-guidance?WT.mc_id=AZ-MVP-5004796 "https://aka.ms/allocation-guidance")"

When you create a virtual machine _(VM)_, start stopped _(deallocated)_ VMs, or resize a VM, Microsoft Azure allocates compute resources to your subscription.

![ZonalAllocationFailed](/uploads/zonalallocationfailed.png "ZonalAllocationFailed")

Microsoft is continually investing in additional infrastructure and features to ensure that they always have all VM types available to support customer demand. However, you may occasionally experience resource allocation failures because of unprecedented growth in demand for Azure services in specific regions.

#### **Waiting for more Compute to be added to the Azure server clusters may not be an option, so what can you do?**

##### Raise a Support Case

* Take a screenshot of the error
* Copy the Activity/Deployment ID
* Take note of the Region
* Take note of the Availability Zone.

Let [Azure Support](https://azure.microsoft.com/en-us/support/?WT.mc_id=AZ-MVP-5004796 " Azure Support") know; that Microsoft may already be aware, but raising a support request helps identify potentially impacted customers. If you know of other SKUs you need to deploy, you can let them know.

##### Purchase On-demand Capacity Reservation

On-demand Capacity Reservation enables you to reserve Compute capacity in an Azure region or an Availability Zone for any duration of time. 

Unlike [Reserved Instances](https://azure.microsoft.com/en-us/pricing/reserved-vm-instances/?WT.mc_id=AZ-MVP-5004796 "Reserved Instances"), you do not have to sign up for a 1-year or a 3-year term commitment.

Once the Capacity Reservation is created, the capacity is available immediately and is exclusively reserved for your use until the reservation is deleted.

Capacity Reservations are priced at the same rate as the underlying VM size. 

For example, if you create a reservation for the D2s_v3 VMs, you will start getting billed for the D2s_v3 VMs, even if the reservation is not being used.

So why would you purchase On-demand Capacity reservations?

* You are operating Azure workloads that scale out and run off a fresh image, like a Citrix farm and want to ensure the capacity is available for the minimum workloads you need.
* You have a project coming up where you need the capacity to be available.

##### Redeploy to another Availability Zone

The server cluster that ARM (Azure Resource Manager) attempted to deploy your workload may not have the necessary capacity, but another Availability Zone _(datacenter)_ might.

Make sure your Virtual Machine is not in a Proximtry or Avalibility Group and do the following.

1. Take note of the Availability Zone that your deployment failed _(i.e. Availability Zone 1)_
2. Remove any resources that may have been created as part of the original failed deployment.
3. Redeploy your workload and select another Availability Zone, such as _(2 - if your failed deployment was in Zone 1)_

##### Change the Virtual Machine version.

By version, I don't mean [Generation 1 and Generation 2](https://docs.microsoft.com/en-us/azure/virtual-machines/generation-2?WT.mc_id=AZ-MVP-5004796#features-and-capabilities "Generation 1 vs. generation 2 features") Virtual Machines; I mean the version of underlying Compute; when you look at a VM SKU size, you will see:

> Standard_DC24s_**v3**
>
> \[Family\] + _\[Sub-family\]_* + \[# of vCPUs\] + _\[Constrained vCPUs\]_* + \[Additive Features\] + _\[Accelerator Type\]_* + **\[Version\]**

You can read more about Virtual Machine Naming conversions "[here](https://docs.microsoft.com/en-us/azure/virtual-machines/vm-naming-conventions?WT.mc_id=AZ-MVP-5004796 "Azure virtual machine sizes naming conventions")".

The version of the VM series links to the underlying hardware associated with the Virtual Machine series; with most new hardware releases, the version changes; an example is: from v3 to v4. 

Microsoft may run a promotion on the pricing for early adopters to move to the new version; they can be seen from the Azure Portal with "Promo" in the name.

1. You can change the version of the SKU by looking in the Azure Portal, Sizing, and you should be able to see other versions of the same SKU; if you are at v5, try resizing to v4 - or the other way around. 

Remember that changing the VM SKU will force the Virtual Machine to deallocate _(stop)_, as it triggers ARM to stand up the Virtual Machine on different server clusters/hardware.

I have found that there are no noticeable decreases in performance for most workloads, but keep in mind you may be returning on older hardware - but it should get you going, and then you can update the SKU to the latest version later.