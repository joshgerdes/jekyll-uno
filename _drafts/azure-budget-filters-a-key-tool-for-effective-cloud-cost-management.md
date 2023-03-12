---
date: 2023-03-13 00:00:00 +1300
title: 'Azure Budget Filters: A Key Tool for Effective Cloud Cost Management'
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azurebacktoschool_azurebudgetfilters.png"

---
[Azure Budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?WT.mc_id=AZ-MVP-5004796 "Tutorial: Create and manage Azure budgets") are a vital tool that can be used to keep on top of your Cloud financial management _(FinOps)_ Microsoft Azure platform potential and actual costs.

#### The most effective Azure Budgets - are the ones that you use!

![ Azure Budgets](/uploads/budgets.png " Azure Budgets")

> In the realm of Cost Management, budgets play a pivotal role in facilitating the planning and implementation of organizational accountability. These tools enable proactive communication regarding expenses and support the management of costs by closely monitoring spending trends over extended periods.
>
> One can set up alerts based on current or projected expenditures to maintain adherence to the established organizational spending limit. Upon surpassing the budget thresholds, notifications are promptly triggered. Such occurrences neither impact any of the available resources nor interrupt any consumption processes. 
>
> By leveraging budgets, it becomes possible to perform detailed cost analysis and track expenses effectively.

![Azure Back to School - Azure Budget Filters](/uploads/azurebacktoschool_azurebudgetfilters.png "Azure Back to School - Azure Budget Filters")

Be aware of the delay with the Cost & Usage data, as there may be a difference between what you end up seeing in the Portal and the Budget itself - so make sure you account for this, to be advised as early as possible:

> Cost and usage data is typically available within 8-24 hours and budgets are evaluated against these costs every 24 hours. 
>
> Be sure to get familiar with [Cost and usage data update](https://learn.microsoft.com/azure/cost-management-billing/costs/understand-cost-mgt-data?WT.mc_id=AZ-MVP-5004796#cost-and-usage-data-updates-and-retention "Cost and usage data updates and retention") specifics. When a budget threshold is met, email notifications are normally sent within an hour of the evaluation.

Note: Azure Budgets are not supported on Subscriptions, where you don't have access to Microsoft Cost Management, ie [Azure Sponsorship](https://www.microsoftazuresponsorships.com/ "Azure Sponsorship") subscriptions.

##### A view outside the school windows, into Scopes

When creating an Azure Budget, you can specify a Scope. A scope is the level of your hierarchy _(ie, if it's a Resource Group Budget, it cannot report on resources at the Subscription, you would have to create a Subscription or Management Group scoped budget)._

When you create an Azure Budget, they can be created at the following Scopes:

![Microsoft Azure Budget Scopes](/uploads/azurebudget_scope.png "Microsoft Azure Budget Scopes")

Most people, when creating scopes, will create a Scope at the Subscription and/or Resource Group level - there is no right or wrong answer when it comes to your Azure Budget Scope - this needs to work for you and your organisation, ie if you have a Project per Resource Group - then it would make sense to create a Budget per Resource Group, the same for Subscriptions. 

**You can also have multiple Azure Budgets** at the same or different scopes, so a **combination of Budgets may be the most effective**. An example could be a Subscription Budget that may go to a Product Owner, but a Management Group could go to Finance or the Technology teams. 