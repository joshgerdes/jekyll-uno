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