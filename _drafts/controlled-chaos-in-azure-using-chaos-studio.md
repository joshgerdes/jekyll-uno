---
date: 2021-12-30 00:00:00 +1300
title: Controlled Chaos in Azure using Chaos Studio
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Chaos engineering has been around for a while; Netflix runs their own famous [Chaos Monkey](https://netflix.github.io/chaosmonkey/), supposedly running 24/7, taking down their resources and pushing them to the limit continuously; it almost sounds counter-intuitive – but it's not.

> Chaos engineering is a methodology that helps developers attain consistent reliability by hardening services against failures in production. Another way to think about chaos engineering is that it's about embracing the inherent chaos in complex systems and, through experimentation, growing confidence in your solution's ability to handle it.
>
> A common way to introduce chaos is to deliberately inject faults that cause system components to fail. The goal is to observe, monitor, respond to, and improve your system's reliability under adverse circumstances. For example, taking dependencies offline (stopping API apps, shutting down VMs, etc.), restricting access (enabling firewall rules, changing connection strings, etc.), or forcing failover (database level, Front Door, etc.), is a good way to validate that the application is able to handle faults gracefully.

Introducing controlled Chaos by tools such as Chaos Monkey and now – [Azure Chaos Studio](https://azure.microsoft.com/en-us/services/chaos-studio/) allows you to put pressure and, in some cases, take down your services to teach you how your services will react under strain and identity areas of improvement as resiliency and scalability to improve your systems.

Azure Chaos Studio _(currently in Preview and only supported in several_ [_regions_](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=chaos-studio) _now)_ is an enabler for 'controlled Chaos' in the Microsoft Azure ecosystem. Using that same tool that Microsoft uses to test and improve their services – you can as well!

Chaos Studio works by creating Experiments _(i.e., Faults/Capabilities)_ that run against Targets _(your resources, whether they are agent or service-based)_.

There are two types of methods you can use to target your resources:

* Service-direct
* Agent-based

Service-direct is tied into the Azure fabric and puts pressure on your resources from outside them _(i.e., supported on most resources that don't need agent-based, PaaS resources, such as Network Security Groups)._ For example, a service-direct capability may be to add or remove a security rule from your network security group for faulty findings.

Agent-based relies on an agent installed; these are targeted at resources such as Virtual Machine and Virtual Machine scale sets; agent-based targets use a user-assigned managed identity to manage an agent on your virtual machines and wreak havoc by running capabilities such as stopping services and putting memory and disk pressure on your workloads.

Just a word of warning, before you proceed to allow Chaos to reign in your environment, make sure it is done out of hours or, better yet – against development or test resources, also make sure that any resources that support autoscaling are disabled – or you might suddenly find ten more instances of that resource you were running _(unless of course you're testing that autoscaling is working)_! 😊

In my test setup, I have the following already pre-created that I will be running my experiments against:

* Virtual Machine Scale set _(running Windows with two instances)_
* Single Virtual Machine _(running Windows)_ to test shutdown against

The currently supported resource types of Azure Chaos Studio can be found '[here](https://docs.microsoft.com/en-us/azure/chaos-studio/chaos-studio-fault-providers)'.

### Setup Azure Chaos Studio

#### Create Managed Identity

Because we will use Agent-based capabilities to generate our Faults, I needed to create a Managed Identity to give Chaos Studio the ability to wreak havoc on my resources!

 1. In the **Azure Portal,** search for [**Managed Identities**](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities)
 2. Click on **Create**
 3. **Select** the **subscrSubscription**ng the resources that you want to test against
 4. **Select** your **Resource Group** to place the managed identity in (_I suggest creating a new Resource Group, as your Chaos experiments may have a different lifecycle than your resources, but it's just a preference, I will be placing mine in the Chaos Studio resource group so I can quickly delete it later)_.
 5. **Select** the **RegionRegion**ur resources
 6. Type in a **name** (_this will be the identity that you will see in logs running these experiments, so make sure its something you can identify with)_
 7. ![](/uploads/azure_userassignedmanageidentity.png)
 8. Click **Next: Tags**
 9. Make sure you enter appropriate tags to make sure that the resource can be identified and tracked, and click **Review + Create**
10. ![](/uploads/azuretags_chaos.png)
11. Verify that everything looks good and click **Create** to create your User Assigned Managed identity.

#### Create Application Insights

Now, it's time to create an Application Insights resource. Applications Insights is for the logs of the experiments to go into, so you can see the faults and their behaviours.

 1. In the **Azure Portal**, search for [**Application Insights**](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/microsoft.insights%2Fcomponents)
 2. Click on **Create**
 3. **Select** the **Subscription** the resources that you want to test against
 4. **Select** your **Resource Group** to place the Application Insights resource into (_I suggest creating a new Resource Group, as your Chaos experiments may have a different lifecycle than your resources, but it's just a preference, I will be placing mine in the Chaos Studio resource group so I can easily delete it later)_.
 5. **Select** the **Region** the resources are in
 6. Type in a **name**
 7.  **Select** your **Log Analytics workspace** you want to link Application Insights to _(if you don't have a Log Analytics workspace, you can create one '_[_here_](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.OperationalInsights%2Fworkspaces)_')_.
 8. ![](/uploads/azure_applicationinsights.png)
 9. Click **Tags**
10. Make sure you **enter appropriate tags** to make sure that the resource can be identified and tracked, and click **Review + Create**
11. Verify that everything looks good and click **Create** to create your Application Insights.

#### Setup Chaos Studio Targets

It is now time to add the resources targets to Chaos Studio

 1. In the **Azure Portal**, search for [**Chaos Studio**](https://portal.azure.com/#blade/Microsoft_Azure_Chaos/ChaosStudioMenuBlade/overview)
 2. On the left band side Blade, select **Targets**
 3. ![](/uploads/azure_chaosstudio_targets.png)
 4. As you can see, I have a Virtual Machine Scale Set and a front-end Network Security Group.
 5. **Select** the **checkbox** next to Name to **select all** the Resources 
 6. Select **Enable Targets**
 7. ![](/uploads/azure_chaosstudio_targets2.png)
 8. Select **Enable service-direct targets (All resources)**
 9. Enabling the service-direct targets will then add the capabilities supported by Service-direct targets into Chaos Studio for you to use.
10. Once completed, I will **select** the scale set and click **Enable Target**
11. Then finally, **Enable agent-based targets (VM, VMSS)**
12. This is where you link the user-managed identity, and Application Insights created earlier
13. **Select** your **Subsccription**
14. Select your **managed identity**
15. Select Enabled for Application Insights and select your Application Insights account. The instrumentation key should be selected manually.
16. ![](/uploads/azure_chaosstudio_enableagenttargets.png)
17. _If your instrumentation key isn't filled in, you can find it on the Overview pane of the Application Insights resource._
18. Click **Review + Enable**
19. **Review** the **resources** you want to enable Chaos Studio to target and select **Enable**
20. You should now be back at the Targets pane and should see that your services are currently enabled.

### Configure and run Azure Chaos Studio

#### Action exclusions

There may be actions that you don't want to be run against specific resources; an example might be you don't want anyone to kill any processes on a Virtual Machine.

1. In the Target pane of Chaos Studio, select **Actions** next to the resource 
2. **Unselect** the **capability** you don't want to run on that resource
3. Select **Save**
4. ![](/uploads/azure_chaosstudio_manageactions.png)

#### Configure Experiments

An experiment is a collection of capabilities to create faults, put pressure on your resources, and cause Chaos that will run against your target resources. These experiments are saved so you can run them multiple times and edit them later, although currently, you cannot reassign the same experiments to other resources.

Note: If you name an Experiment the same as another experiment, it will replace the older Experiment with your new one and retain the previous history.

 1. In the **Azure Portal,** search for [**Chaos Studio**](https://portal.azure.com/#blade/Microsoft_Azure_Chaos/ChaosStudioMenuBlade/overview).
 2. On the left band side Blade, select **Experiments**
 3. Click **+ Create**
 4. **Select** your **Subscription**
 5. **Select** your **Resource Group** to save the Experiment into
 6. **Type** in a **name** for your **Experiment** that makes sense; in this case, we will put some Memory pressure on the VM scale set.
 7. **Select** your **Region**
 8. Click **Next: Experiment Designer**
 9. **Using** Experiment **Designer**, you can **design** your **Faults**; you can have multiple capabilities hit a resource with expected delays, _i.e., you can have Memory pressure on a VM for 10 minutes, then CPU pressure, then shutdown._
10. We are going to select **Add Action**
11. Then **Add Fault**
12.  I am going to select **Physical Memory** pressure
13. Leave the duration to **10 minutes**
14. Because this will go against my VM scale set, I will add in the instances I want to target _(if you aren't targeting a VM Scale set, you can leave this blank, you can find the instance ID by going to your VM Scale set click on Instances, click on the VM instance you want to target and you should see the Instance ID in the Overview pane)_
15. ![](/uploads/azure_chaosstudio_createexperimentaddfault.png)
16. Select **Next: Target resources**
17. **Select** your **resources** _(you will notice as this is an Agent-based capability, only agent supported resources are listed)_
18.  Select **Add**
19. I am then going to **Add delay for 5 Minutes**
20. Then add an **abrupt VM shutdown** for 10 minutes _(Chaos Studio will automatically restart the VM after the 10-minute duration)_.
21. ![](/uploads/azure_chaosstudio_createexperimentaddfault2.png)
22. As you can see with the Branches _(items that will run in parallel)_ and actions, you can have multiple faults running at once in parallel by using branches or one after the other sequentially.
23. Now that we are ready with our faulty, we are going to click **Review + Create**
24. Click **Create**

_Note: I had an API error; after some investigation, I found it was having problems with the '?' in my experiment name, so I removed it and continued to create the Experiment._

#### Assign permissions for the Experiments

Now that the Experiment has been created, we need to give rights to the Managed User account created earlier _(and/or the System managed identity that was created when the Experiment was created for service-direct experiments)_.

I will assign permissions to the Resource Group that the VM Scale set exists in, but for more granular control, you might be better off applying the rights to the individual resource. You can see suggested roles to give resources: [Supported resource types and role assignments for the Chaos Studio](https://docs.microsoft.com/en-us/azure/chaos-studio/chaos-studio-fault-providers) Microsoft page.

 1. In the **Azure Portal**, click on the **Resource Group** containing your resources you want to run the Experiment against
 2. Select **Access control (IAM)**
 3. Click **+ Add**
 4. Click **Add Role Assignment**
 5. Click **Reader**
 6. Click **Next**
 7. Select **Assign access to Managed identity**
 8. Click on **+ Select Members**
 9. **Select** the **User** assigned **management identit**y
10. Click **Review** and **assign**.
11. Because the shutdown is a service-direct, **go back and give the experiment system managed identity Virtual Machine Contributor rights**, so it has access to shutdown the VM.

#### Run Experiments

Now that the Experiment has been created, it should appear as a resource in the resource group you selected earlier; if you open it, you can see the Experiment's History, Start, and Edit buttons.

1. Click **Start**
2. ![](/uploads/azure_chaosstudio_whatmemory.png)
3. Click **Ok** to **start** the **Experiment** _(and place it into the queue)_
4. **Click** on **Details** to see the **experiment progress** _(and any errors)_, and if it fails one part, it may move to the next step depending on the fault.
5. ![](/uploads/azure_chaosstudio_whatmemoryrun.png)
6. **Azure Chaos studio should now run rampant and do best – cause Chaos**!

This service is still currently in Preview. If you have any issues, take a look at the: [Troubleshoot issues with Azure Chaos Studio](https://docs.microsoft.com/en-us/azure/chaos-studio/troubleshooting).

### Monitor and Auditing of Azure Chaos Studio

Now that Azure Chaos Studio is in use by your organization, you may want to know what auditing is available, along with reporting to Application Insights.

#### Azure Activity Log

When an Azure Chaos Studio experiment has touched a resource, there will be an audit trail in the Azure activity log of that resource; here, you can see that 'WhatMemory', which is the Name of my Chaos Experiment, has successfully powered off and on my VM.

![](/uploads/azure_chaosstudio_activitylog.png)

#### Azure Alerts

It is easy to set up alerts when a Chaos experiment kicks off; to create an Azure, do the following.

 1. In the **Azure Portal**, click on **Azure Monito**r
 2. Click on **Alerts**
 3. Click **+ Create**
 4. Select **Alert Rule**
 5. Click **Create resource**
 6. **Filter** your resource **type** to **Chaos Experiments**
 7. **Filter** your **alert** to **Subscription** and click **Done**
 8. Click **Add Condition**
 9. Select: **Starts a Chaos Experiment**
10. Make sure that: **Event initiated by is set to *(All services and users)**
11. Click **Done**
12. Click **Add Action Group**
13. If you have one, **assign** an **action group** _(these are who and how the alerts will get to you)_. If you don't have one click: + Create an action group.
14. Specify a resource group to hold your action groups _(usually a monitor or management resource group)_
15. Type the Action Group name
16. Type the Action group Display name
17. Click Next: Notifications
18. Select Notification Type
19. Select email
20. Select Email
21. Type in your email address to be notified
22. Click ok
23. Type in the Name of the mail to be a reference in the future _(i.e. Help Desk)_
24. Click Review + Create
25. Click Create to create your Action group
26. Type in your rule name (i.e. Alert – Chaos Experiment – Started)
27. Type in a description
28. Specify the resource group to place the alert in (again, usually a monitor or management resource group)
29. Check Enable alert rule on creation
30. Click Create alert rule

    Note: Activity Log alerts are hidden types; they are not shown in the resource group by default, but if you check the: Show hidden types box, they will appear.
31. ![](/uploads/azure_chaosstudio_alert.png)