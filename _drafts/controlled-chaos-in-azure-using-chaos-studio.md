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
Chaos engineering has been around for a while, Netflix runs their own famous [Chaos Monkey](https://netflix.github.io/chaosmonkey/) supposedly running 24/7 taking down their resources and pushing them to the limit on a continuous basis, it almost sounds counter-intuitive – but it’s not.

> Chaos engineering is a methodology that helps developers attain consistent reliability by hardening services against failures in production. Another way to think about chaos engineering is that it's about embracing the inherent chaos in complex systems and, through experimentation, growing confidence in your solution's ability to handle it.
>
> A common way to introduce chaos is to deliberately inject faults that cause system components to fail. The goal is to observe, monitor, respond to, and improve your system's reliability under adverse circumstances. For example, taking dependencies offline (stopping API apps, shutting down VMs, etc.), restricting access (enabling firewall rules, changing connection strings, etc.), or forcing failover (database level, Front Door, etc.), is a good way to validate that the application is able to handle faults gracefully.

Introducing controlled chaos by tools such as Chaos Monkey and now – [Azure Chaos Studio](https://azure.microsoft.com/en-us/services/chaos-studio/), allows you to put pressure and in some cases, take down your services to teach you how your services will react under strain and identity areas of improvement such as resiliency and scalability to improve your systems.

Azure Chaos Studio _(currently in Preview and only supported in a number of_ [_regions_](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=chaos-studio) _currently)_ is an enabler for ‘controlled Chaos’ in the Microsoft Azure ecosystem. Using that same tool that Microsoft uses to test and improve their services – you can as well!

Chaos Studio works by creating Experiments _(i.e., Faults/Capabilities)_ that run against Targets _(your resources whether they are agent or service-based)_.

There are 2 types of methods you can use to target your resources:

* Service-direct
* Agent-based

Service-direct is tied into the Azure fabric and puts pressure on your resources from outside them _(i.e., supported on most resources that don’t need agent-based, PaaS resources, such as Network Security Groups)_ A service-direct capability may be to add or remove a security rule from your network security group for faulty finding.

Agent-based relies on an agent installed, these are targeted at resources such as Virtual Machine and Virtual Machine scale sets, Agent-based targets use a user-assigned managed identity to manage an agent on your virtual machines and wreak havoc by running capabilities such as stopping services and putting memory and disk pressure on your workloads.

Just a word of warning, before you proceed to allow Chaos to reign in your environment, make sure it is done out of hours or better yet – against development or test resources, also make sure that any resources that support autoscaling are disabled – or you might suddenly find 10 more instances of that resource you were running _(unless of course you’re testing that autoscaling is actually working)_! 😊

In my test setup, I have the following already pre-created that I will be running my experiments against:

* Virtual Machine Scale set _(running Windows with 2 instances)_
* Single Virtual Machine _(running Windows)_ to test shutdown against

The currently supported resource types can be found ‘[here](https://docs.microsoft.com/en-us/azure/chaos-studio/chaos-studio-fault-providers)’.

### Setup Azure Chaos Studio

#### Create Managed Identity

Because we are going to use Agent-based capabilities to generate our Faults, I needed to create a Managed Identity to give Chaos Studio the ability to wreak havoc on my resources!

 1. In the **Azure Portal** search for [**Managed Identities**](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities)
 2. Click on **Create**
 3. **Select** the **subscription** holding the resources that you want to test against
 4. **Select** your **Resource Group** to place the managed identity in (_I suggest creating a new Resource Group, as your Chaos experiments may have a different lifecycle than your resources, but it’s just a preference, I will be placing mine in the Chaos Studio resource group so I can easily delete it later)_.
 5. **Select** the **Region** of your resources
 6. Type in a **name** (_this will be the identity that you will see in logs running these experiments so make sure its something you can identify with)_
 7. ![](/uploads/azure_userassignedmanageidentity.png)
 8. Click Nex: Tags
 9. Make sure you enter appropriate tags, to make sure that the resource can be identified and tracked and click Review + Create
10. ![](/uploads/azuretags_chaos.png)
11. Verify that everything looks good and click Create to create your User Assigned Managed identity.

#### Create Application Insights

Now, it's time to create an Application Insights resource, this is for the logs of the experiments to go into, so you can see the faults and their behaviours.

 1. In the Azure Portal search for [Application Insights](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/microsoft.insights%2Fcomponents)
 2. Click on Create
 3. Select the subscription holding the resources that you want to test against
 4. Select your Resource Group to place the Application Insights resource into (_I suggest creating a new Resource Group, as your Chaos experiments may have a different lifecycle than your resources, but it’s just a preference, I will be placing mine in the Chaos Studio resource group so I can easily delete it later)_.
 5. Select the Region of your resources
 6. Type in a name
 7.  Select your Log Analytics workspace you want to link Application Insights to (if you don’t have a Log Analytics workspace you can create one ‘[here](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.OperationalInsights%2Fworkspaces)’).
 8. ![](/uploads/azure_applicationinsights.png)
 9. Click Tags
10. Make sure you enter appropriate tags, to make sure that the resource can be identified and tracked and click Review + Create
11. Verify that everything looks good and click Create to create your Application Insights.

#### Setup Chaos Studio Targets

It is now time to add the resources targets to Chaos Studio

 1. In the Azure Portal search for [Chaos Studio](https://portal.azure.com/#blade/Microsoft_Azure_Chaos/ChaosStudioMenuBlade/overview)
 2. On the left band side Blade, select Targets
 3. ![](/uploads/azure_chaosstudio_targets.png)
 4. As you can see, I have a Virtual Machine Scale Set and a front-end Network Security Group.
 5. Select the checkbox next to Name, to select all the Resources Select Enable Targets
 6. ![](/uploads/azure_chaosstudio_targets2.png)
 7. Select Enable service-direct targets (All resources)
 8. This will then add the capabilities supported by Service-direct targets into Chaos Studio for you to use.
 9. Once completed, I will select the scale set and click Enable Target
10. Then finally, Enable agent-based targets (VM, VMSS)
11. This is where you link the user-managed identity and Application Insights created earlier
12. Select your subscription and your managed identity
13. Select Enabled for Application Insights and select your Application Insights account, the instrumentation key should be selected manually.
14. ![](/uploads/azure_chaosstudio_enableagenttargets.png)
15. If for some reason your instrumentation key isn’t filled in, you can find it on the Overview pane of the Application Insights resource.
16. Click Review + Enable
17. Review the resources you want to enable Chaos Studio to target and select Enable
18. You should now be back at the Targets pane and should see that your services are now enabled.

### Configure and run Azure Chaos Studio

#### Action exclusions

There may be actions that you don’t want to be run against certain resources, an example might be you don’t want anyone to kill any processes on a Virtual Machine.

1. In the Target pane of Chaos Studio, select Actions next to the resource and
2. Unselect the capability you don’t want to run on that resource
3. Select Save
4. ![](/uploads/azure_chaosstudio_manageactions.png)

#### Configure Experiments

An experiment is a collection of capabilities to create faults, put pressure on your resources and overall cause Chaos, that will be run against your target resources. These experiments are saved so you can run them multiple times and edit them later, although currently, you cannot reassign the same experiments to other resources.

Note: If you name an Experiment, the same as another experiment, it will replace the older experiment with your new one and retain the previous history.

 1. In the Azure Portal search for [Chaos Studio](https://portal.azure.com/#blade/Microsoft_Azure_Chaos/ChaosStudioMenuBlade/overview)
 2. On the left band side Blade, select Experiments
 3. Click + Create
 4. Select your Subscription
 5. Select your Resource Group to save the Experiment into
 6. Type in a name for your experiment that makes sense, in this case, we are going to put some Memory pressure on the VM scale set.
 7. Select your region
 8. ![](/uploads/azure_chaosstudio_createexperiment.png)
 9. Click Next: Experiment Designer
10. Using Experiment Designer, you can design your Faults, you can have multiple capabilities hit a resource with scheduled delays, i.e., you can have Memory pressure on a VM for 10 minutes, then CPU pressure then shutdown.
11. We are going to select Add Action
12. Then Add Fault
13.  I am going to select Physical Memory pressure
14. Leave the direction to 10 minutes
15. Because this will against my VM scale set, I will add in the instances I want to target _(if you aren’t targeting a VM Scale set you can leave this blank, you can find the instance ID, by going to your VM Scale set, click on Instances, click on the VM instance you want to target and you should see the Instance ID in the Overview pane)_
16. ![](/uploads/azure_chaosstudio_createexperimentaddfault.png)
17. Select Next: Target resources
18. Select your resources (you will notice as this is an Agent-based capability, only agent supported resources are listed)
19.  Select Add
20. I am then going to Add delay for 5 Minutes
21. Then add an abrupt VM shutdown for 10 minutes
22. ![](/uploads/azure_chaosstudio_createexperimentaddfault2.png)
23. As you can see with the Branches (items that will run in parallel) and actions, you can have multiple faults running at once in parallel by using branches or one after the other sequentially.
24. Now that we are ready with our faulty, we are going to click **Review + Create**

    3\. Click Create

Note: I had an API error, after some investigation, I found it was having problems with the ‘?’ in my experiment name, so I removed it and continued to create the Experiment.

#### Assign permissions for the Experiments

Now that the experiment has been created, we need to give rights to the Managed User account created earlier _(and/or the System managed identity that was created when the Experiment was created for service-direct experiments)_.

I am going to assign permissions to the Resource Group that the VM Scale set exists in, but for more granular control, you might be better off applying the rights to the individual resource. You can see suggested roles to give resources at the: [Supported resource types and role assignments for the Chaos Studio](https://docs.microsoft.com/en-us/azure/chaos-studio/chaos-studio-fault-providers) Microsoft page.

 1. In the Azure Portal click on the Resource Group
 2. Select Access control (IAM)
 3. Click + Add
 4. Click Add Role Assignment
 5. Click Reader
 6. Click Next
 7. Select Assign access to Managed identity
 8. Click on + Select Members
 9. Select the User assigned management identity
10. Click Review and assign.
11. Because the shutdown is a service-direct, go back and give the experiment system managed identity Virtual Machine Contributor rights, so it has access to shutdown the VM.

#### Run Experiments

Now that the experiment has been created, it should appear as a resource in the resource group you selected earlier, if you open it – you can see the History, Start, and Edit buttons for the Experiment.

1. Click Start
2. ![](/uploads/azure_chaosstudio_whatmemory.png)
3. Click Ok to start the Experiment _(and place it into the queue)_
4. Click on Details to see the experiment progress, if it fails one part of it due to an error it will progress to the next step.
5. ![](/uploads/azure_chaosstudio_whatmemoryrun.png)
6. Azure Chaos studio should now run rampant and do what it does best – cause Chaos!

This service is still currently in preview, if you have any issues take a look at the: [Troubleshoot issues with Azure Chaos Studio](https://docs.microsoft.com/en-us/azure/chaos-studio/troubleshooting).

### Monitor and Auditing of Azure Chaos Studio

Now that Azure Chaos Studio is in use by your organization, you may want to know what auditing is available, along with reporting to Application Insights.

#### Azure Activity Log

When a resource has been touched by an Azure Chaos Studio experiment, there will be an audit trail in the Azure activity log of that resource, here you can see that ‘WhatMemory’ which is the name of my Chaos Experiment has successfully powered off and on my VM.

![](/uploads/azure_chaosstudio_activitylog.png)

#### Azure Alerts

It is easy to set up alerts when a Chaos experiment kicks off, to create an Azure do the following.

 1. In the Azure Portal click on Azure Monitor
 2. Click on Alerts
 3. Click + Create
 4. Select Alert Rule
 5. Click Create resource
 6. Filter your resource type to Chaos Experiments
 7. Filter your alert to Subscription
 8. ![](/uploads/azure_chaosstudio_createalert.png)
 9. Click Done
10. Click Add Condition
11. Select: Starts a Chaos Experiment
12. Make sure that: Event initiated by is set to *(All services and users)
13. Click Done
14. Click Add Action Group
15. Assign an action group if you have one (these are who and how the alerts will get to you), if you don’t have one click: + Create action group
16. Specify a resource group to hold your action groups _(usually a monitor or management resource group)_
17. Type the Action Group name
18. Type the Action group Display name
19. Click Next: Notifications
20. Select Notification Type
21. Select email
22. Select Email