---
date: 2022-08-18 00:00:00 +1200
title: Microsoft Azure - Cost Optimization Tasks
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/cost_pillar_overview.png"

---
Like doing service on your car, the [Microsoft Azure](https://azure.microsoft.com/en-us/?WT.mc_id=AZ-MVP-5004796 "Microsoft Azure") platform is not a set-and-forget ecosystem!

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