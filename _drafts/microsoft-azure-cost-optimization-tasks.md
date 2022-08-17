---
date: 2022-08-18 00:00:00 +1200
title: Microsoft Azure - Operational Cost Optimization Tasks
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/cost_pillar_overview.png"

---
Like doing service on your car, the [Microsoft Azure](https://azure.microsoft.com/en-us/?WT.mc_id=AZ-MVP-5004796 "Microsoft Azure") platform is not a set-and-forget ecosystem! 

There are no one-size-fits when it comes to cost optimization, but there are some general tasks that can be done or considered on a Monthly/Quarterly/Annual basis to keep on top of the resources you are running in Azure and to keep them lean.

#### Overview

Although Microsoft takes a lot of traditional infrastructure management and security concerns off your hand, you are still responsible for the spending and making sure the value of the technologies and services you consume, match your business goals and agility.

Today we are going to go back to basics and look at the [Cost Optimization](https://docs.microsoft.com/en-us/azure/architecture/framework/?WT.mc_id=AZ-MVP-5004796#cost-optimization "Cost optimization") pillar of the Microsoft [Well-Architected Framework](https://docs.microsoft.com/en-us/azure/architecture/framework/?WT.mc_id=AZ-MVP-5004796 "Microsoft Azure Well-Architected Framework").

> “The cost optimization pillar provides principles for balancing business goals with budget justification to create a cost-effective workload while avoiding capital-intensive solutions. Cost optimization is about looking at ways to reduce unnecessary expenses and improve operational efficiencies.”
>
> “Use the pay-as-you-go strategy for your architecture, and invest in scaling out, rather than delivering a large investment-first version. Consider opportunity costs in your architecture and the balance between first-mover advantage versus fast follow.”

The right governance and oversight can help prevent Cloud sprawl and wasted consumption costs.

To help get you started, I have put together a list of some optimization opportunities, that should be run regularly, items such as reviewing unassociated public IPs should be done Monthly _(along with Azure Advisor checks)_, and [Azure Reservation reviews](https://docs.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations?WT.mc_id=AZ-MVP-5004796 "What are Azure Reservations?") at least quarterly.

> **_This is not an exhaustive list_**, and the use of [Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Policy?") and [Azure Advisor](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview?WT.mc_id=AZ-MVP-5004796 "Introduction to Azure Advisor") help supplement these tasks.
>
> If you have other tasks that you run, feel free to share them with the community in the page comments below.

The [Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview?WT.mc_id=AZ-MVP-5004796 "Overview of Microsoft Graph") and [KQL queries](https://luke.geek.nz/azure-resource-graph-explorer-and-the-powershell-azure-resource-graph "Azure Resource Graph Explorer and the PowerShell Azure Resource Graph ") can also be used in conjunction with PowerShell to pull recommendations straight out of Advisor, which can then be fed into reports, and the use of community tools such as the [Azure Optimization Engine](https://luke.geek.nz/azure/azure-optimization-engine "Azure Optimization Engine ") cannot be undervalued.

#### Design

![Azure - Monitor & optimize](/uploads/cost_pillar_overview.png "Azure - Monitor & optimize")

##### Keep within the cost constraints

Every design choice has cost implications. Before choosing an architectural pattern, Azure service, or a price model for the service, consider the budget constraints set by the company. As part of the design, identify acceptable boundaries on scale, redundancy, and performance against cost. After estimating the initial cost, set budgets and alerts at different scopes to measure the cost.

One of the cost drivers can be unrestricted resources. These resources typically need to scale and consume more cost to meet demand.

##### Aim for scalable costs

A key benefit of the cloud is the ability to scale dynamically. The workload cost should scale linearly with demand.

You can save costs through automatic scaling. Consider the usage metrics and performance to determine the number of instances. Choose smaller instances for a highly variable workload and scale out to get the required level of performance, rather than up. This choice will enable you to make your cost calculations and estimates granular.

##### Pay for the consumption

Adopt a leasing model instead of owning infrastructure. Azure offers many SaaS and PaaS resources that simplify the overall architecture. The cost of hardware, software, development, operations, security, and data center space is included in the pricing model. Also, choose pay-as-you-go over fixed pricing. That way, as a consumer, you're charged for only what you use.

##### Right resources, the right size

Choose the right resources that are aligned with business goals and can handle the performance of the workload.

An inappropriate or misconfigured service can impact the cost.

For example, building a multi-region service when the service levels don't require high availability or geo-redundancy will increase cost without any reasonable business justification. Certain infrastructure resources are delivered as fix-sized building blocks. Ensure that these blocks are adequately sized to meet capacity demand, and deliver expected outcomes.

##### Monitor and optimize

Treat cost monitoring and optimization as a process, rather than a point-in-time activity. Conduct regular cost reviews and measure and forecast the capacity needs so that you can provision resources dynamically and scale with demand. Review the cost management recommendations and take action.

Today, we will focus on **Monitor and optimize**.

#### Review Underutilized Resources

Optimize and improve efficiency by identifying idle and underutilized resources across the Azure ecosystem.

##### Review Azure App Service Plans

Review [Azure App Service Plans](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2FserverFarms "Azure Portal - App Service plan") to determine if:

1. The Azure App Service Plan is ‘Standard’ or ‘Premium’ pricing and has an Application associated with it.
2. If the Azure App Service actually is getting utilized _(by looking at the Metrics/CPU)_ and doesn’t need to be downscaled to a smaller plan.

##### Review shutdown workloads

Because you pay for Azure Resources as ‘Pay As You Go’ a quick win can be to review [Virtual Machines](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Compute%2FVirtualMachines "Azure Portal - Virtual Machines") to determine if the workload actually needs to be on 24/7!

For example, you have automation configured to automatically start up and shut down workloads based on the following schedule: 7 AM Start – 7 PM Stop _(& off Weekends)_.

You can add servers to this automated schedule by adding the following Tag to the Virtual Machine, or trigger automation when a workload is ‘Shutdown’ and not deallocated, see my article on "[Turn on an Azure Virtual Machine using Azure Automation](https://luke.geek.nz/azure/turn-on-a-azure-virtual-machine-using-azure-automation/ "Turn on a Azure Virtual Machine using Azure Automation ")" for a potential place to start.

##### Review Azure Advisor

The Azure Advisor is an inbuilt tool that is critical to optimizing the Azure Environment. The [Azure Advisor](https://portal.azure.com/#blade/Microsoft_Azure_Expert/AdvisorMenuBlade/Cost "Azure Portal - Azure Advisor") needs to be reviewed for Cost recommendations.

1. The Azure Advisor will recommend Reserved Instances
2. The Azure Advisor will recommend if a Virtual Machine is running on a VM size GREATER than what it needs _(based on CPU utilization under 5% in the last 14 days)_. If the Azure Advisor reports an overprovisioned machine, you need to investigate its use and then resize it down to a more suitable size.

##### Review Azure SQL Databases

Review [Azure SQL Databases](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Sql%2Fservers%2Fdatabases "Azure Portal - Azure SQL databases") to determine if:

1. The SQL Database Pricing Tier is ‘Standard’ and is actually using the DTUs (usually found by looking at the Compute utilization on the databases), if not downsize the DTU limit.
2. Check Geo-Replication to make sure that the SQL Database is not replicating across Regions if it doesn’t need to be.

#### Review Azure Reserved Instances

Azure reserved instances significantly reduce costs—up to 72 percent compared to pay-as-you-go prices—with one-year or three-year terms on Windows and Linux virtual machines (VMs). What's more, you can now improve budgeting and forecasting with a single upfront payment (i.e. Pay for a VM Upfront for 1/3 Year or 5 Years) making it easy to calculate your investments. Or, lower your upfront cash outflow with monthly payment options at no additional cost.

![Azure Reserved Instance](/uploads/azure-ri.png "Azure Reserved Instance")

The Azure Advisor is an inbuilt tool that is critical to optimizing the Azure Environment. The Azure Advisor needs to be reviewed for Reserved Instance recommendations.

1. When reviewing Reserved Instances you need to take into consideration:
2. What workloads are they used for?
3. Is there a project that may replace or resize the workloads in the next year?
4. Who is paying for the workloads?

#### Review unused files and VHDs

Save Azure costs by cleaning up unused VHDs in your Azure storage Azure stores Azure Virtual Machine OS and data disks in Azure storage accounts.

When a VM is deleted from the Azure portal, the underlying OS and data disks may not get deleted. Such disks continue to consume Azure storage and account for the cost of storing them. These disks are called Orphaned Disks.

As mentioned above, some Virtual Machines with unmanaged disks when deleted will keep the VHDs around.

Using a PowerShell [script](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/find-unattached-disks?WT.mc_id=AZ-MVP-5004796 "Find and delete unattached Azure managed and unmanaged disks") _(provided by Microsoft)_ you can report on any disks that are not in use by a VM, and then delete them.

_Note: Be VERY cautious doing this, solutions such as Citrix and Azure Image Builder use unmanaged disks to create new Session hosts, etc, so context is key._

With the Azure Storage accounts, using Blob data – such as Diagnostic Accounts, it is a good idea to implement [Azure Blob Storage Lifecycle](https://docs.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview?tabs=azure-portal&WT.mc_id=AZ-MVP-5004796 "Azure Blob Storage Lifecycle") on the storage accounts so we are only retaining recent and relevant data.

![Azure Blob Storage Lifecycle Management](/uploads/azureblogstglifecyclemgmnt.PNG "Azure Blob Storage Lifecycle Management")

The lifecycle management policy lets you:

1. Transition blobs to a cooler storage tier _(hot to cool, hot to archive, or cool to archive)_ to optimize for performance and cost
2. Delete blobs at the end of their lifecycles
3. Define rules to be run once per day at the storage account level.

#### Review budgets

Budgets in Cost Management help you plan for and drive organizational accountability. With budgets, you can account for the Azure services you consume or subscribe to during a specific period.

Budgets help you inform others about their spending to proactively manage costs and monitor how spending progresses over time.

When the budget thresholds you've created are exceeded, notifications are triggered. None of your resources are affected and your consumption isn't stopped, however, you can use Budget alerts as a trigger to run Azure Logic Apps, or Functions to automate the shutdown and resize resources. You can use budgets to compare and track spending as you analyze costs.

Make sure you have [Azure Budget](https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?WT.mc_id=AZ-MVP-5004796 "Azure Budget") notifications configured to email Product Owners or other Stakeholders once a Resource Group or Subscription reaches a specific threshold.

This is set up in the Azure Portal, on the Resource Group under Budgets, and set to email the Application Owner.

Examples of budgets that could be configured:

Generally, I recommend that 3 budgets should be configured, to give enough notice:

* 50%
* 60%
* 70%

#### Review Tags

You apply tags to your Azure resources, resource groups, and subscriptions to logically organize them into a taxonomy. Each tag consists of a name and a value pair. For example, you can apply the name "Environment" and the value "Production" to all the resources in production.

Tags can be used to determine things like:

* Who to bill?
* Who supports it?

The right tags can mean that the right owners get charged internally and have more ownership of their resource costs. Examples below:

| Tag Name | Value | Comment |
| --- | --- | --- |
| Dept | Finance | Name of the department who owns the resources. |
| Environment | UAT | What environment the Resource is used for such as Production, UAT and Development |
| Application Owner | Luke Murray | The name of the Product Owner for the service sitting inside the Resource Group |
| Support Team | Platform Team | What team is responsible for the resources/site for support reasons |
| Billing Code | Operational | Purchase order or project billing code |

For further examples and a base tagging convention, check out a blog article I wrote on [Microsoft Azure Tagging conventions](https://luke.geek.nz/azure/microsoft-azure-tagging-conventions/ "Microsoft Azure Tagging Conventions ").

#### Review Hub (Hybrid Use Benefit)

The [Azure Hybrid Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/?WT.mc_id=AZ-MVP-5004796 "Azure Hybrid Benefit") is a pricing benefit for customers who have licenses with Software Assurance, which helps maximize the value of existing on-premises Windows Server and/or SQL Server license investments when migrating to Azure.

Eligible customers can save up to 40% on Azure Virtual Machines _(infrastructure as a service, or IaaS)_, and save up to 55% on Azure SQL Database _(platform as a service, or PaaS)_ and SQL Server on Azure Virtual Machines _(IaaS)_ with Azure Hybrid Benefit, which increases to up to 80% when combined with Azure Reserved Instances.

To verify if a server is using the Azure Hybrid Benefit Log in to the Azure Portal and navigate to the Virtual Machine Blade Make sure that the: OS Licensing Benefit column is selected.

If a Virtual Machine Already has HUB it will have: Azure hybrid benefit listed in the column, any non-supported workloads _(such as Linux)_ will have ‘Not Supported’.

If any are eligible for HUB, click on the Virtual Machine…

1. Click the **Configuration blade**
2. Select **Licensing, Already have a Windows server license?**
3. **Yes** and **Save**

_Note: This is a non-intrusive change that will take effect on the billing immediately and doesn’t cause any impact on the Virtual Machine._

#### Review Backups

[Azure Backup](https://docs.microsoft.com/en-us/azure/backup/backup-overview?WT.mc_id=AZ-MVP-5004796 "Azure Backup") is simple because it’s built into the platform. It has one-click backup support for SQL databases and virtual machines running in Azure.

Azure Backup is cost-effective and less complex than other cloud backup solutions while keeping your data safe from ransomware and human errors. Sometimes there will be workloads that have been backed up to migrate, test, or clone and that you no longer need to retain the data for.

> Note: This can be a tricky one as you will need to talk to product owners to confirm the workloads were just Dev/Test workloads, and not required, there may be legal implications for keeping workloads in the backup. But if someone stood up something to play with, particularly in a Sandbox or Development subscription there may not be a reason to keep it around.

Log in to the Azure Portal and navigate to the [Recovery Services Vault](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.RecoveryServices%2Fvaults "Azure Portal - Recovery Services") page Navigate to each one and click on:

Backup:

1. Under **Usage**, click on **Backup Items**
2. Click on **Azure Virtual Machines**
3. **Sort** the **Backup** items by **Latest Restore Point** _(so the older restore points are at the top)_

   Using the Latest Restore Point as a guide, IF there are any servers that can have their Backups deleted:
4. Click on the **Name** of the Backup Item
5. Click on **Stop Backup**
6. Select **Delete Backup Data** _(this is non-reversible)_
7. Type in the name of the **Backup Item** and select **Stop Backup**

#### Review unused Public IPs

Public IP addresses allow Internet resources to communicate inbound to Azure resources. Public IP addresses enable Azure resources to communicate to the Internet and public-facing Azure services. 

This is also a great opportunity to inspect what Public IP addresses you have and make sure there are resources, that have public IP that does not need to have them assigned! Tip setup an Azure Policy that prevents the creation of Public IPs.

The address is dedicated to the resource until it’s unassigned by you. A resource without a public IP assigned can communicate outbound. Azure dynamically assigns an available IP address that isn’t dedicated to the resource. 

When resources get created, sometimes they will create a Public IP, these can be removed as part of the build but left in the Resource Groups. 

We want to remove unattached Public IP to save money. 

_Note: In some cases, the Product Owner may need to be consulted before any changes are made, as some of the resources may be inflight projects or required._ 

1. Log in to the **Azure Portal** and navigate to the [**Public IP Addresses **](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Network%2FPublicIpAddresses "Azure Portal - Public IP Addresses")blade
2. Look in the ‘**Associated to**’ column and if not required click on the **Public IP**
3. Click **Delete**