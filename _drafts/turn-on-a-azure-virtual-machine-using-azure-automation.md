---
date: 2022-06-05 00:00:00 +1200
title: Turn on a Azure Virtual Machine using Azure Automation
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
[Virtual Machines](https://azure.microsoft.com/en-us/overview/what-is-a-virtual-machine/?WT.mc_id=AZ-MVP-5004796#overview " What is a virtual machine (VM)?"){:target="_blank"} in Microsoft Azure have different states and, depending on what state the Virtual Machine is in, will determine whether you get billed or not _(for the Compute, storage and network adapters are still billed)_.

| Power state | Description | Billing |
| --- | --- | --- |
| Starting | Virtual Machine is powering up. | Billed |
| Running | Virtual Machine is fully up. This is the standard working state. | Billed |
| Stopping | This is a transitional state between running and stopped. | Billed |
| Stopped | The Virtual Machine is allocated on a host but not running. Also called PoweredOff state or Stopped (Allocated). This can be result of invoking the PowerOff API operation or invoking shutdown from within the guest OS. The Stopped state may also be observed briefly during VM creation or while starting a VM from Deallocated state. | Billed |
| Deallocating | This is the transitional state between running and deallocated. | Not billed |
| Deallocated | The Virtual Machine has released the lease on the underlying hardware and is completely powered off. This state is also referred to as Stopped (Deallocated). | Not billed |

Turning off a Virtual Machine in Microsoft Azure on a schedule can quickly be done using the built-in Shutdown controls in the Virtual Machine blade _(part of_ [_Azure Lab Services_](https://azure.microsoft.com/en-us/services/lab-services/?WT.mc_id=AZ-MVP-5004796 " Azure Lab Services")_, but not a requirement)_, but what about starting it?

You have a few options, Logic Apps, PowerShell, Functions and Runbooks; most of the time, these will run on a standard 7 AM to 5 PM Monday to Friday schedule _(meaning the Virtual Machine is off during off-peak hours and weekends, reducing compute cost)_. 

This works fine for most scenarios, but what happens if a Bank or Public Holiday falls during the week? With the normal schedule, your Virtual Machine starts. 

Because all your users are on Holiday, it wastes money while you and your users drink snicker cocktails at the beach?

This is where using a third party timezone API like '[AbstractApi](https://www.abstractapi.com/ "Automate routine dev work with Abstract's suite of APIs")' comes in handy; incorporating a lookup to check if it's a Public Holiday before starting that Virtual Machine can help reduce unnecessary costs.

I have written a base runbook that does precisely that, every time the runbook runs, it checks if it is a public Holiday. If it is - then the Virtual Machine isn't started; if it isn't, then the virtual machine is started.

### Overview

Today, we are going to set up an Azure Automation runbook, triggered by a scheduled will go through the following steps:

1. On a schedule _(7 AM, it will trigger an Azure Automation runbook)_
2. The Azure Automation runbook will do a lookup to an external API, in this case, AbstractApi.
3. The runbook will check the date and detect if it falls on a Public Holiday; if it is a Public Holiday, it will exit the Azure Automation runbook; if it is a standard workday, it will start the Virtual Machine.

To do this, we need a few resources.

* [Azure Automation](https://docs.microsoft.com/en-us/azure/automation/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Automation?") Account
* Azure Automation [runbook](https://docs.microsoft.com/en-us/azure/automation/automation-runbook-types?WT.mc_id=AZ-MVP-5004796 "Azure Automation runbook types") _(I will supply a PowerShell runbook below)_
* [AbstractAPI ](https://www.abstractapi.com/ "Automate routine dev work with Abstract's suite of APIs")API Key

And, of course, 'Contributor' rights to the Microsoft Azure subscription to create the resources and the schedule, along with setting up the System Managed identity to grant the Azure Automation account access to start the Virtual Machine.

We will set up this from scratch using the Azure Portal and use an already created PowerShell Azure Automation runbook.

### Deploy Start VM Solution

#### Setup Azure Automation Account

##### Create Azure Automation Account

First, we need an [Azure Automation](https://docs.microsoft.com/en-us/azure/automation/automation-create-standalone-account?tabs=azureportal&WT.mc_id=AZ-MVP-5004796 "Create a standalone Azure Automation account"){:target="_blank"} resource.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Click **+ Create a resource.**
 3. Type in **automation**
 4. Select **Create** under Automation, and select **Automation.**
 5. ![Create Azure Automation Account](/uploads/azureportal-create-automation.jpg "Create Azure Automation Account")
 6. Select your **subscription**
 7. Select your **Resource Group** or Create one if you don't already have one _(I recommend placing your automation resources in an Azure Management or Automation resource group, this will also contain your Runbooks)_
 8. Select your **region**
 9. ![Create Azure Automation Account](/uploads/azureportal-create-automation_basics.jpg "Create Azure Automation Account")
10. Select **Next**
11. Make sure: **System assigned** is selected for Managed identities _(this will be required for giving your automation account permissions to deallocate your Virtual Machine, but it can be enabled later if you already have an Azure Automation account)_.
12. Click **Next**
13. Leave Network connectivity as default (**Public access**)
14. Click **Next**
15. **Enter** in appropriate **tags**
16. ![Create Azure Automation Account](/uploads/azureportal-create-automation_tags.jpg "Create Azure Automation Account")
17. Click **Review + Create**
18. After validation has passed, select **Create**

##### Configure System Identity

Now that we have our Azure Automation account, its time to set up the System Managed Identity and grant it the following roles:

* Virtual Machine Contributor _(to deallocate the Virtual Machine)_
* Monitoring Contributor _(to close the Azure Alert)_

You can set up a custom role to be least privileged and use that instead. But in this article, we will stick to the built-in roles.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Navigate to your Azure **Automation account**
 3. Click on: **Identity**
 4. Make sure that the **System assigned** toggle is: **On** and click **Azure role assignments.**
 5. ![Azure Automation Account managed identity](/uploads/azureportal-automation_managedidentity.jpg "Azure Automation Account managed identity")
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

We will use the Azure Runbook and use a few Azure PowerShell Modules; by default, Azure Automation has the base Azure PowerShell modules, but we will need to add [Az.AlertsManagement](https://docs.microsoft.com/en-us/powershell/module/az.alertsmanagement/?WT.mc_id=AZ-MVP-5004796 "Az.AlertsManagement"){:target="_blank"}, and update the Az.Accounts as required as a pre-requisite for Az.AlertsManagement.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Navigate to your Azure **Automation account**
 3. Click on **Modules**
 4. Click on **+ Add a module**
 5. Click on **Browse from Gallery**
 6. Click: **Click here to browse from the gallery**
 7. Type in: **Az.Accounts**
 8. Press **Enter**
 9. Click on **Az.Accounts**
10. Click **Select**
11. ![Import Az.Accounts module](/uploads/azureportal-automation_modules_az-accounts.jpg "Import Az.Accounts module")
12. Make sure that the Runtime version is: **5.1**
13. Click **Import**
14. Now that the Az.Accounts have been updated, and it's time to import Az.AlertsManagement!
15. Click on **Modules**
16. Click on **+ Add a module**
17. Click on **Browse from Gallery**
18. Click: **Click here to browse from the gallery**
19. Type in: **Az.AlertsManagement** _(note its Alert**s)**_
20. Click **Az.AlertsManagement**
21. ![Az.AlertsManagement module](/uploads/azureportal-automation_modules_az-alertsmanagement.jpg "Az.AlertsManagement module")
22. Click **Select**
23. Make sure that the Runtime version is: **5.1**
24. Click **Import** _(if you get an error, make sure that Az.Accounts has been updated, through the Gallery import as above)_
25. Now you have successfully added the dependent modules!

##### Import Runbook

Now that the modules have been imported into your Azure Automation account, it is time to import the Azure Automation runbook.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Navigate to your Azure **Automation account**
 3. Click on **Runbooks**
 4. Click **+ Create a runbook**
 5. Specify a **name** _(i.e. Deallocate-AzureVirtualMachine)_
 6. Select Runbook type of: **PowerShell**
 7. Select Runtime version of: **5.1**
 8. Type in a **Description** that explains the runbook _(this isn't mandatory, but like Tags is recommended, this is an opportunity to indicate to others what it is for and who set it up)_
 9. ![Create Azure Runbook](/uploads/azureportal-runbook-create.jpg "Create Azure Runbook")
10. Click **Create**
11. Now you will be greeted with a blank edit pane; paste in the Runbook from below:
12. {% gist f727d53c027eacc79121d325eeb49d7f %}
13. Click **Save**
14. ![Azure Automation runbook](/uploads/azureportal-runbook-import.jpg "Azure Automation runbook")
15. Click **Publish** _(so the runbook is actually in production and can be used)_
16. You can select View or Edit at any stage, but you have now imported the Azure Automation runbook!

##### Setup Webhook

Now that the Azure runbook has been imported, we need to set up a Webhook for the Alert to trigger and start the runbook.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Navigate to your Azure **Automation account**
 3. Click on **Runbooks**
 4. **Click** on the **runbook** you just imported _(i.e. Deallocate-AzureVirtualMachine)_
 5. Click on **Add webhook**
 6. Click **Create a new webhook**
 7. **Enter** a **name** for the webhook
 8. Make sure it is **Enabled**
 9. You can edit the expiry date to match your security requirements; make sure you **record** the expiry date, as it will need to be renewed before it expires.
10. **Copy** the **URL** and paste it somewhere safe _(you won't see this again! and you need it for the next steps)_
11. ![Create Azure webhook](/uploads/azureportal-webhook-create.jpg "Create Azure webhook")
12. Click **Ok**
13. Click on **Configure parameters and run settings.**
14. Because we will be taking in dynamic data from an Azure Alert, enter in: **\[EmptyString\]**
15. Click **Ok**
16. Click **Create**
17. You have now set up the webhook _(make sure you have saved the URL from the earlier step as you will need it in the following steps)!_

#### Setup Alert & Action Group

Now that the Automation framework has been created with the Azure Automation account, runbook and webhook, we now need a way to detect if a Virtual Machine has been Stopped; this is where a Resource Health alert will come in.

 1. Log into the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal"){:target="_blank"}.
 2. Navigate to: [**Monitor**](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/overview){:target="_blank"}
 3. Click on **Service Health**
 4. Select **Resource Health**
 5. Select **+ Add resource health alert**
 6. Select your **subscription**
 7. Select **Virtual machine** for Resource Type
 8. You can target specific Resource Groups for your alert _(and, as such, your automation)_ or **select all.**
 9. Check **Include all future resource groups**
10. Check **include all future resources**
11. Under the Alert conditions, make sure **Event Status** is: **All selected**
12. Set Current resource status to **Unavailable**
13. Set Previous resource status to **All selected**
14. For reason type, select: **User initiated** and **unknown**
15. ![Create Azure Resource Health Alert](/uploads/azureportal-alert-create.jpg "Create Azure Resource Health Alert")
16. Now that we have the Alert rule configured, we need to set up an Action group. That will get triggered when the alert gets fired.
17. Click **Select Action groups.**
18. Click **+ Create action group**
19. **Select** your subscription and **resource group** _(this is where the Action alert will go, I recommend your Azure Management/Monitoring resource group that may have a Log Analytics workspace as an example)_.
20. Give your Action Group a **name**, i.e. AzureAutomateActionGroup
21. The display name will be automatically generated, but feel free to adjust it to suit your naming convention
22. Click **Next: Notifications**
23. Under **Notifications**, you can trigger an **email alert**, which can be handy in determining how often the runbook runs. This can be modified and removed if it is running, especially during testing.
24. Click **Next: Actions**
25. Under Action Type, select **Webhook**
26. **Paste** in the **URI** created earlier when setting up the Webhook
27. Select **Yes** to enable the **common alert schema** (_this is required as the JSON that the runbook is parsing is expecting it to the in the schema, if it isn't the runbook will fail)_
28. ![Create Azure Action Group](/uploads/azureportal-actiongroup-webhook.jpg "Create Azure Action Group")
29. Click **Ok**
30. Give the **webhook** a **name**.
31. Click **Review + create**
32. Click **Create**
33. Finally, enter in an Alert **name** and **description**, specify the resource group for the Alert to go into and click **Save.**

### Test Deallocate Solution

So now we have stood up our:

* Azure automation account
* Alert
* Action Group
* Azure automation runbook
* Webhook

It is time to test! I have a VM called: VM-D01, running Windows _(theoretically, this runbook will also run against Linux workloads, as its relying on the Azure agent to send the correct status to the Azure Logs, but in my testing, it was against Windows workloads)_ in the same subscription that the alert has been deployed against.

As you can see below, I shut down the Virtual Machine. After a few minutes _(be patient, Azure needs to wait for the status of the VM to be triggered)_, an Azure Alert was fired into Azure Monitor, which triggered the webhook and runbook, and the Virtual Machine was deallocated, and the Azure Alert was closed.

![Azure deallocate testing](/uploads/deallocatevm.gif "Azure deallocate testing")