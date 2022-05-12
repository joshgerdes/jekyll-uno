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

### Overview

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

We will set up this from scratch using the Azure Portal and an already created PowerShell Azure Automation runbook.

### Deploy Deallocate Solution

#### Setup Azure Automation Account

##### Create Azure Automation Account

First, we need an [Azure Automation](https://docs.microsoft.com/en-us/azure/automation/automation-create-standalone-account?tabs=azureportal&WT.mc_id=AZ-MVP-5004796 "Create a standalone Azure Automation account") resource.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal").
 2. Click **+ Create a resource.**
 3. Type in **automation**
 4. Select **Create** under Automation, and select **Automation**
 5. ![](/uploads/azureportal-create-automation.jpg)
 6. Select your **subscription**
 7. Select your **Resource Group** or Create one if you don't already have one _(I recommend placing your automation resources in an Azure Management or Automation resource group, this will also contain your Runbooks)_
 8. Select your **region**
 9. ![](/uploads/azureportal-create-automation_basics.jpg)
10. Select **Next**
11. Make sure: **System assigned** is selected for Managed identities _(this will be required for giving your automation account permissions to deallocate your Virtual Machine, but it can be enabled later if you already have an Azure Automation account)_.
12. Click **Next**
13. Leave Network connectivity as default (**Public access**)
14. Click **Next**
15. **Enter** in appropriate **tags**
16. ![](/uploads/azureportal-create-automation_tags.jpg)
17. Click **Review + Create**
18. After validation has passed, select **Create**

##### Configure System Identity

Now that we have our Azure Automation account, its time to set up the System Managed Identity and grant it the following roles:

* Virtual Machine Contributor _(to deallocate the Virtual Machine)_
* Monitoring Contributor _(to close the Azure Alert)_

You can set up a custom role to be least privileged and use that instead. But in this article, we will stick to the built-in roles. 

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal").
 2. Navigate to your Azure **Automation account**
 3. Click on: **Identity**
 4. Make sure that the **System assigned** toggle is: **On** and click **Azure role assignments**
 5. ![](/uploads/azureportal-automation_managedidentity.jpg)
 6. Click **+ Add role assignments**
 7. Select the **Subscription** _(make sure this subscription matches the same subscription your Virtual Machines are in)_
 8. Select Role: **Virtual Machine Contributor**
 9. Click **Save**
10. Now we repeat the same process for **Monitoring Contributor**
11. lick **+ Add role assignments**
12. Select the **Subscription** _(make sure this subscription matches the same subscription your Virtual Machines are in)_
13. Select Role: **Monitoring Contributor**
14. Click **Save**
15. Click **Refresh** _(it may take a few seconds to update the Portal, so if it is blank - give it 10 seconds and try again)_.
16. You have now set up the System Managed identity and granted it the roles necessary to execute the automation.

##### Import Modules

In the Azure Runbook, we will use - will use a few Azure PowerShell Modules; by default, Azure Automation has the base Azure PowerShell modules, but we will need to add [Az.AlertsManagement](https://docs.microsoft.com/en-us/powershell/module/az.alertsmanagement/?WT.mc_id=AZ-MVP-5004796 "Az.AlertsManagement"), and update the Az.Accounts as its required as a pre-requsite for Az.AlertsManagement.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal").
 2. Navigate to your Azure **Automation account**
 3. Click on **Modules**
 4. Click on **+ Add a module**
 5. Click on **Browse from Gallery**
 6. Click: **Click here to browse from the gallery**
 7. Type in: **Az.Accounts**
 8. Press **Enter**
 9. Click on **Az.Accounts**
10. Click **Select**
11. ![](/uploads/azureportal-automation_modules_az-accounts.jpg)
12. Make sure that the Runtime version is: **5.1** 
13. Click **Import**
14. Now that the Az.Accounts has been updated, it's time to import Az.AlertsManagement!
15. Click on **Modules**
16. Click on **+ Add a module**
17. Click on **Browse from Gallery**
18. Click: **Click here to browse from the gallery**
19. Type in: **Az.AlertsManagement** _(note its Alert**s)**_
20. Click **Az.AlertsManagement**
21. ![](/uploads/azureportal-automation_modules_az-alertsmanagement.jpg)
22. Click **Select**
23. Make sure that the Runtime version is: **5.1** 
24. Click **Import** _(if you get an error, make sure that Az.Accounts has been updated, through the Gallery import as above)_
25. Now you have successfully added the dependant modules!

##### Import Runbook

Now that the modules have been imported into your Azure Automation account, it is time to import the Azure Automation runbook.