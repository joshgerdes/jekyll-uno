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

Be aware of the delay with the Cost & Usage data, as there may be a difference between what you end up seeing in the Portal and the Budget itself - so make sure you account for this to be advised as early as possible:

> Cost and usage data is typically available within 8-24 hours and budgets are evaluated against these costs every 24 hours.
>
> Be sure to get familiar with [Cost and usage data update](https://learn.microsoft.com/azure/cost-management-billing/costs/understand-cost-mgt-data?WT.mc_id=AZ-MVP-5004796#cost-and-usage-data-updates-and-retention "Cost and usage data updates and retention") specifics. When a budget threshold is met, email notifications are normally sent within an hour of the evaluation.

Note: Azure Budgets are not supported on Subscriptions, where you can't access Microsoft Cost Management, i.e. [Azure Sponsorship](https://www.microsoftazuresponsorships.com/ "Azure Sponsorship") subscriptions.

##### A view outside the school windows, into Scopes

When creating an Azure Budget, you can specify a Scope. A scope is the level of your hierarchy _(i.e., if it's a Resource Group Budget, it cannot report on resources at the Subscription, you would have to create a Subscription or Management Group scoped Budget)._

When you create an Azure Budget, they can be made at the following Scopes:

![Microsoft Azure Budget Scopes](/uploads/azurebudget_scope.png "Microsoft Azure Budget Scopes")

Most people, when creating scopes, will create a Scope at the Subscription and/or Resource Group level - there is no right or wrong answer when it comes to your Azure Budget Scope - this needs to work for you and your organisation, ie if you have a Project per Resource Group - then it would make sense to create a Budget per Resource Group, the same for Subscriptions.

**You can also have multiple Azure Budgets** at the same or different scopes, so a **combination of Budgets may be the most effective**. An example could be a Subscription Budget that may go to a Product Owner, but a Management Group could go to Finance or the Technology teams.

Keep in mind, that Budgets on their own are just a forecasting and alerting tool, they won't stop resources from running, if it goes over an alert threshold, out of the box - the Budget doesn't touch your resources, merely gives you an opportunity to proactively react to them, before costs become a problem.

##### Pen on paper, let's start taking notes

Let's go through the process of creating an Azure Budget, using the Azure Portal.

 1. Log in to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
 2. In the Search bar above, search for **Budgets**
 3. Click on [**Budgets**](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/Menu/\~/budgets/open/budgets/openedBy/AzurePortal "Cost Management: Tenant Root Group | Budgets")
 4. **Change** the **Scope**
 5. ![Cost Management - Azure Budget](/uploads/azureportal_costmanagement_root.png "Cost Management - Azure Budget")
 6. You can select a Management Group, Subscription, or Resource Group for the Scope, by clicking on each - in my example, I have a Management Group named: _mg-landingzones_, which I am going to select.
 7. Click **Select**
 8. Now that the Scope has been set, we can add our Budget to the specified Scope, click **+ Add**
 9. We will come back to Filters, in another section - but for the Budget details you will need:
    * **Name** (this is the name of your Budget, make sure its something meaningful _(ie Monthly-Budget_MG-LandingZones)_
    * **Reset period** _(Monthly/Quarterly or Annual, this is the period that the Budget resets back to $0 - you can't go wrong with Monthly)_
    * **Creation date** _(the date that the Budget will start)_
    * **Expiration date** _(the date that the Budget will stop)_
10. **Budget Amount **_(this is the overall; amount that you are planning on your resources to spend)_
11. ![Azure Portal - Create budget](/uploads/azureportal_createbudget_scoping.png "Azure Portal - Create budget")
12. Once you have entered in your Budget details, click Next to configure your Alert conditions. The alert conditions are where you can specify, what you want to alert on ie 50% or 80% of the overall budget amount. Actual - is when it financially reaches that point and Forecasted - is when current consumption is forecasted to reach that budget.
13. Specify an email address to send the Alert to and click **Create**.
14. ![Azure Budget Conditions](/uploads/azureportal_createbudget_conditions.png "Azure Budget Conditions")

#### Time to highlight those notes

By default, Scoping the Budget to the Subscription or Resource Group is good enough for 95% of the use cases - but using Budget filters, you can enable a bit more flexibility - for scenarios such as:

* Product-centric alerts
* Service centric alerts

While the scope is your level of the Azure hierarchy, your filter is your handrail to stop you from falling, currently, Microsoft offers the following filters:

| Property | When to use | Notes |
| --- | --- | --- |
| Availability zones | Break down AWS costs by availability zone. | Applicable only to AWS scopes and management groups. Azure data doesn't include availability zone and will show as No availability zone. |
| Billing period | Break down PAYG costs by the month that they were, or will be, invoiced. | Use Billing period to get a precise representation of invoiced PAYG charges. Include two extra days before and after the billing period if filtering down to a custom date range. Limiting to the exact billing period dates won't match the invoice. Will show costs from all invoices in the billing period. Use Invoice ID to filter down to a specific invoice. Applicable only to PAYG subscriptions because EA and MCA are billed by calendar months. EA/MCA accounts can use calendar months in the date picker or monthly granularity to accomplish the same goal. |
| BillingProfileId | The ID of the billing profile that is billed for the subscription's charges. | Unique identifier of the EA enrollment, pay-as-you-go subscription, MCA billing profile, or AWS consolidated account. |
| BillingProfileName | Name of the EA enrollment, pay-as-you-go subscription, MCA billing profile, or AWS consolidated account. | Name of the EA enrollment, pay-as-you-go subscription, MCA billing profile, or AWS consolidated account. |
| Charge type | Break down usage, purchase, refund, and unused reservation and savings plan costs. | Reservation purchases, savings plan purchases, and refunds are available only when using actual costs and not when using amortized costs. Unused reservation and savings plan costs are available only when looking at amortized costs. |
| Department | Break down costs by EA department. | Available only for EA and management groups. PAYG subscriptions don't have a department and will show as No department or unassigned. |
| Enrollment account | Break down costs by EA account owner. | Available only for EA billing accounts, departments, and management groups. PAYG subscriptions don't have EA enrollment accounts and will show as No enrollment account or unassigned. |
| Frequency | Break down usage-based, one-time, and recurring costs. | Indicates whether a charge is expected to repeat. Charges can either happen once OneTime, repeat on a monthly or yearly basis Recurring, or be based on usage UsageBased. |
| Invoice ID | Break down costs by billed invoice. | Unbilled charges don't have an invoice ID yet and EA costs don't include invoice details and will show as No invoice ID. |
| InvoiceSectionId | Unique identifier for the MCA invoice section. | Unique identifier for the EA department or MCA invoice section. |
| InvoiceSectionName | Name of the invoice section. | Name of the EA department or MCA invoice section. |
| Location | Break down costs by resource location or region. | Purchases and Marketplace usage may be shown as unassigned, or No resource location. |
| Meter | Break down costs by usage meter. | Purchases and Marketplace usage will show as unassigned or No meter. Refer to Charge type to identify purchases and Publisher type to identify Marketplace charges. |
| Operation | Break down AWS costs by operation. | Applicable only to AWS scopes and management groups. Azure data doesn't include operation and will show as No operation - use Meter instead. |
| Pricing model | Break down costs by on-demand, reservation, or spot usage. | Purchases show as OnDemand. If you see Not applicable, group by Reservation to determine whether the usage is reservation or on-demand usage and Charge type to identify purchases. |
| PartNumber | The identifier used to get specific meter pricing. |  |
| Product | Name of the product. |  |
| ProductOrderId | Unique identifier for the product order |  |
| ProductOrderName | Unique name for the product order. |  |
| Provider | Break down costs by the provider type: Azure, Microsoft 365, Dynamics 365, AWS, and so on. | Identifier for product and line of business. |
| Publisher type | Break down Microsoft, Azure, AWS, and Marketplace costs. | Values are Microsoft for MCA accounts and Azure for EA and pay-as-you-go accounts. |
| Reservation | Break down costs by reservation. | Any usage or purchases that aren't associated with a reservation will show as No reservation or No values. Group by Publisher type to identify other Azure, AWS, or Marketplace purchases. |
| ReservationId | Unique identifier for the purchased reservation instance. | In actual costs, use ReservationID to know which reservation the charge is for. |
| ReservationName | Name of the purchased reservation instance. | In actual costs, use ReservationName to know which reservation the charge is for. |
| Resource | Break down costs by resource. | Marketplace purchases show as Other Marketplace purchases and Azure purchases, like Reservations and Support charges, show as Other Azure purchases. Group by or filter on Publisher type to identify other Azure, AWS, or Marketplace purchases. |
| Resource group | Break down costs by resource group. | Purchases, tenant resources not associated with subscriptions, subscription resources not deployed to a resource group, and classic resources don't have a resource group and will show as Other Marketplace purchases, Other Azure purchases, Other tenant resources, Other subscription resources, $system, or Other charges. |
| ResourceId | Unique identifier of the Azure Resource Manager resource. |  |
| Resource type | Break down costs by resource type. | Type of resource instance. Not all charges come from deployed resources. Charges that don't have a resource type will be shown as null or empty, Others, or Not applicable. For example, purchases and classic services will show as others, classic services, or No resource type. |
| ServiceFamily | Type of Azure service. For example, Compute, Analytics, and Security. |  |
| ServiceName | Name of the Azure service. | Name of the classification category for the meter. For example, Cloud services and Networking. |
| Service name or Meter category | Break down cost by Azure service. | Purchases and Marketplace usage will show as No service name or unassigned. |
| Service tier or Meter subcategory | Break down cost by Azure usage meter subclassification. | Purchases and Marketplace usage will be empty or show as unassigned. |
| Subscription | Break down costs by Azure subscription and AWS linked account. | Purchases and tenant resources may show as No subscription. |
| Tag | Break down costs by tag values for a specific tag key. | Purchases, tenant resources not associated with subscriptions, subscription resources not deployed to a resource group, and classic resources cannot be tagged and will show as Tags not supported. Services that don't include tags in usage data will show as Tags not available. Any remaining cases where tags aren't specified on a resource will show as Untagged. Learn more about tags support for each resource type. |
| UnitOfMeasure | The billing unit of measure for the service. For example, compute services are billed per hour. |  |

One or a[ combination of these filters](https://learn.microsoft.com/azure/cost-management-billing/costs/group-filter?WT.mc_id=AZ-MVP-5004796 "Group and filter options in Cost analysis and budgets") can be used to create your own meaningful Budgets! You can target specific resources, an example is if you have resources in a Shared Resource Group - for example, Networking, and you have a VPN Gateway, that is used for a Site to Site VPN, for a specific application, that is sitting in another resource group or subscription - you can add the Resource directly into the filter of your Budget for the Azure Gateway, and then include a Tag - that may reference the rest of the application dependencies.

Budgets can be created with all sorts of various tools, from the Azure Portal to:

* [Quickstart: Create a budget with Bicep](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-create-budget-bicep?tabs=CLI&WT.mc_id=AZ-MVP-5004796 "Quickstart: Create a budget with Bicep")
* PowerShell ([New-AzConsumptionBudget](https://learn.microsoft.com/en-us/powershell/module/az.billing/new-azconsumptionbudget?view=azps-9.5.0&WT.mc_id=AZ-MVP-5004796 "New-AzConsumptionBudget") &[ Set-AzConsumptionBudget](https://learn.microsoft.com/powershell/module/az.billing/set-azconsumptionbudget?view=azps-9.5.0&WT.mc_id=AZ-MVP-5004796 "Set-AzConsumptionBudget"))

#### Homework time

Finished the school day! But you still have your homework to finish! Your homework for today is a few tricks and tips to help!

* You can use the [**Azure Mobile Application**](https://azure.microsoft.com/get-started/azure-portal/mobile-app?WT.mc_id=AZ-MVP-5004796 "Get the Azure mobile app") **to display your Cost and Budgets** so keep on top of your consumption on the go!
* The Microsoft Cost Management team are working on new features all the time, including improvements to Cost Management and Budgets! If you like living on the edge - be sure to check out [the Preview porta](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-preview-features-cost-management-labs?WT.mc_id=AZ-MVP-5004796#recommendationinsights "Enable preview features in Cost Management Labs")l (and add your feedback)!