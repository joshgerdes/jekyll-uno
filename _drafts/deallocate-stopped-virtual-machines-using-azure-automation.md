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
[Virtual Machines](https://azure.microsoft.com/en-us/overview/what-is-a-virtual-machine/?WT.mc_id=AZ-MVP-5004796#overview " What is a virtual machine (VM)?") in Microsoft Azure have different states and, depending on what state the Virtual Machine is in, will determine whether you get billed or not _(for the Compute, storage and network adapters are still billed)_.

| Power state | Description | Billing |
| --- | --- | --- |
| Starting | Virtual Machine is powering up. | Billed |
| Running | Virtual Machine is fully up. This is the standard working state. | Billed |
| Stopping | This is a transitional state between running and stopped. | Billed |
| Stopped | The Virtual Machine is allocated on a host but not running. Also called PoweredOff state or Stopped (Allocated). This can be result of invoking the PowerOff API operation or invoking shutdown from within the guest OS. The Stopped state may also be observed briefly during VM creation or while starting a VM from Deallocated state. | Billed |
| Deallocating | This is the transitional state between running and deallocated. | Not billed |
| Deallocated | The Virtual Machine has released the lease on the underlying hardware and is completely powered off. This state is also referred to as Stopped (Deallocated). | Not billed |

Suppose a Virtual Machine is not being used. In that case, turning off a Virtual Machine from the Microsoft Azure Portal _(or programmatically via_ [_PowerShell_](https://docs.microsoft.com/en-us/powershell/azure/?view=azps-7.5.0&WT.mc_id=AZ-MVP-5004796 "Azure PowerShell Documentation")_/_[_Azure CLI_](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796 "How to install the Azure CLI")_)_ is recommended to ensure that the Virtual Machine is deallocated and its affinity on the host has been released.

![Microsoft Azure - Virtual Machine Power States](/uploads/azvm-power-states.png "Microsoft Azure - Virtual Machine Power States")

However, you need to know this, and those new to Microsoft Azure, or users who don't have [Virtual Machine Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles?WT.mc_id=AZ-MVP-5004796 "Azure built-in roles") rights to deallocate a Virtual Machine, may simply shut down the operating system, leaving the Virtual Machine in a 'Stopped' state, but still tied to an underlying Azure host and incurring cost.

This is where our solution can help; by triggering an Alert when a Virtual Machine becomes unavailable due to a user-initiated shutdown, we can then start an [Azure Automation]() runbook to deallocate the Virtual Machine.

Today, we are going to set up an Azure Automation runbook, triggered by a Resource Health alert that will go through the following steps:

1. User shutdowns Virtual Machine from within the Operating System
2. The Virtual Machine enters an unavailable state
3. A Resource Alert is triggered when the Virtual Machine becomes unavailable (after being available) by a user initiated event
4. The Alert triggers a Webhook to an Azure Automation runbook
5. Using permissions assigned to the Azure Automation account through a System Managed Identity connects to Microsoft Azure and checks the VM state; if the Virtual Machine state is still 'Stopped', then deallocate the virtual machine.
6. Then finally, resolve the triggered alert.

To do this, we need a few resources.

* Azure Automation Account
* Az.AlertsManagement module in the Azure Automation account
* Az.Accounts module _(updated in the Azure Automation account)_
* Azure Automation runbook _(I will supply this below)_
* Resource Health Alert
* Webhook _(to trigger to the runbook and pass the JSON from the alert)_

And, of course, 'Contributor' rights to the Microsoft Azure subscription to provide the resources and the alerts and resources and set up the system managed identity.

We will run through setting up this from scratch using the Azure Portal and an already created PowerShell Azure Automation runbook.