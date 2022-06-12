---
date: 2022-06-12 00:00:00 +1200
title: Microsoft Azure Portal - Global & Advanced Filters
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azureportal_advanced_subscription_filter.png"

---
We've all been there! In the Azure portal, looking for a resource or subscription and cannot find it! Once permissions are ruled out, you are left with the Portal itself, and the filter.

You may see a checkbox or message like the below:

> Show only subscriptions selected in the [global subscriptions filter](https://portal.azure.com/#settings/directory "Portal settings | Directories + subscriptions")
>
> ![Show only subscriptions selected in the global subscriptions filter](/uploads/azureportal_globalfilter.png "Show only subscriptions selected in the global subscriptions filter")

This is because the Microsoft Azure portal has a default filter, which is very handy in hiding subscriptions and resources you don't want to see or use all the time.

The following Microsoft document '[Manage Azure portal settings and preferences](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences?WT.mc_id=AZ-MVP-5004796 "Manage Azure portal settings and preferences")' is a great place to start, but let us take a look ourselves.

### Azure Portal Filters

#### Global Subscription Filter

Let us take a look at the Global subscription filter.

1. Log in to the Microsoft [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
2. Click on '**Settings**' on the top right-hand navigation bar
3. ![](/uploads/azureportal_settings.png)
4. Click on the **dropdown list** under the Default subscription filter
5. Here you can **select** or **de-select** the **subscriptions** you want to display by default in the Microsoft Azure Portal.
6. ![](/uploads/azureportal_default_subscription_filter.png)
7. There is no Save button, the changes will automatically take effect.

#### Advanced Filters

Let us take a look at the Advanced subscription filters.

1. Log in to the Microsoft [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
2. Click on '**Settings**' on the top right-hand navigation bar
3. ![](/uploads/azureportal_settings.png)
4. Toggle **Advanced Filters**
5. Click **Continue** to reload the Azure Portal, your Global subscription filter will be changed to an advanced filter.
6. Click **Modify Advanced filters**
7. Click **+ Create a filter**
8. Here you have the ability to create a filter or filters, to help match your requirements. You can create filters based on subscription ID and subscription name.

| Filter Type | Operator | Value | Note |
| --- | --- | --- | --- |
| Subscription ID | == | Subscription ID array | Equal |
| Subscription name | != | Subscription ID array | Does not Equal |
| Subscription state | contains | String | Contains |
|  | !contains | String | Does not Contain |
|  | startswith | String | Starts with |
|  | !startswith | String | Does not start with |
|  | endswith | String | Ends with |
|  | !endswith | String | Does not end with |

| Subscription State | Description |
| --- | --- |
| Activate/Enabled | Your Azure subscription is active. You can use the subscription to deploy new resources and manage existing ones. |
| Deleted | Your Azure subscription has been deleted along with all underlying resources/data. |
| Disabled | Your Azure subscription is disabled and can no longer be used to create or manage Azure resources. While in this state, your virtual machines are de-allocated, temporary IP addresses are freed, storage is read-only and other services are disabled. |
| Expired | Your Azure subscription is expired because it was canceled. You can reactivate an expired subscription. |
| Past Due | Your Azure subscription has an outstanding payment pending. Your subscription is still active but failure to pay the dues may result in subscription being disabled. |
| Warned | Your Azure subscription is in a warned state and will be disabled shortly if the warning reason isn't addressed. A subscription may be in warned state if its past due, canceled by user, or if the subscription has expired. |

1. Using the logic above, we can easily create filters based on the state of a subscription and name, an example is, creating a filter that displays all subscriptions with 'dev' in its name:
2. ![](/uploads/azureportal_advanced_subscription_filter.png)

You can only have one Filter displayed at once in the Azure Portal, but you can easily switch between them, by clicking **Activate**, next to the filter name.

If you wish to disable Advanced Filters, and go back to the Global Filter, you can deselect the Toggle for Advanced Filters.

### Additional Resources

To get the most out of your Azure Portal experience, the below Microsoft documentation is worth a read _(in no particular order)_.

* [Manage Azure portal settings and preferences](https://docs.microsoft.com/en-us/azure/azure-portal/set-preferences?WT.mc_id=AZ-MVP-5004796 "Manage Azure portal settings and preferences")
* [Azure subscription states](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-states?WT.mc_id=AZ-MVP-5004796 "Azure subscription states")
* [Add, remove, and rearrange favorites](https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-add-remove-sort-favorites?WT.mc_id=AZ-MVP-5004796 "Add, remove, and rearrange favorites")
* [View and filter Azure resource information](https://docs.microsoft.com/en-us/azure/azure-portal/manage-filter-resource-views?WT.mc_id=AZ-MVP-5004796 "View and filter Azure resource information")

#### Send Feedback to Microsoft

On the last note, Microsoft has made it easy to create Feedback, that will get fed back to the Azure Portal and product teams straight in the Microsoft Azure Portal, if you ever see anything that may need changing, or a link out of date don't hesitate to send your feedback to Microsoft, by pressing the little Feedback button on the top right of your navigation bar. 

![](/uploads/azureportal_feedback.png)

The Microsoft Azure portal is in development all the time and is now built with [Azure Resource Graph](https://docs.microsoft.com/en-us/azure/governance/resource-graph/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Resource Graph?") capabilities, it is very easy not to try and see new functionality, so I recommend you keep your eyes out and try new features.