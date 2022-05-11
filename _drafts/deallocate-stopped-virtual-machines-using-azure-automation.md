---
date: 2022-05-12 00:00:00 +1200
title: Deallocate 'Stopped' Virtual Machines using Azure Automation
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
[Virtual Machines](https://azure.microsoft.com/en-us/overview/what-is-a-virtual-machine/?WT.mc_id=AZ-MVP-5004796#overview " What is a virtual machine (VM)?") in Microsoft Azure have different states and depending on what state the Virtual Machine is in, depends on whether you get billed or not.

| Power state  | Description                                                                                                                                                                                                                                                                                                                                  | Billing      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Starting     | Virtual Machine is powering up.                                                                                                                                                                                                                                                                                                              | Billed       |
| Running      | Virtual Machine is fully up. This is the standard working state.                                                                                                                                                                                                                                                                             | Billed       |
| Stopping     | This is a transitional state between running and stopped.                                                                                                                                                                                                                                                                                    | Billed       |
| Stopped      | The Virtual Machine is allocated on a host but not running. Also called PoweredOff state or _Stopped (Allocated)_. This can be result of invoking the PowerOff API operation or invoking shutdown from within the guest OS. The Stopped state may also be observed briefly during VM creation or while starting a VM from Deallocated state. | Billed       |
| Deallocating | This is the transitional state between running and deallocated.                                                                                                                                                                                                                                                                              | Not billed |
| Deallocated  | The Virtual Machine has released the lease on the underlying hardware and is completely powered off. This state is also referred to as _Stopped (Deallocated)_.                                                                                                                                                                              | Not billed |

sd