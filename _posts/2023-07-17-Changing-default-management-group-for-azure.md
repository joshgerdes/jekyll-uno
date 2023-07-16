---
title: Changing the default Management Group in Azure for your new subscriptions
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/ChangeDefaultManagementGroup.png
date: '2023-07-17 00:00:00 +1300'
---

By default, when a [Management Group](https://learn.microsoft.com/azure/governance/management-groups/overview?WT.mc_id=AZ-MVP-5004796){:target="_blank"} gets created, it goes under the Root Management Group, the same is true for [Subscriptions](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/organize-subscriptions?WT.mc_id=AZ-MVP-5004796){:target="_blank"}.

This works fine, when you have a simple Microsoft Azure environment, but as soon as you start expanding into areas such as [Subscription vending](https://learn.microsoft.com/azure/architecture/landing-zones/subscription-vending?WT.mc_id=AZ-MVP-5004796){:target="_blank"} or limited access to who can see the Root Management Group and start to look into Visual Studio Enterprise subscriptions, you may want to consider moving new subscriptions, under its own Management Group, away from any policies or RBAC controls, essentially into a Management Group that acts as a shopping cart, to then be picked up and moved later.

If we refer to a [recommendation](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups?WT.mc_id=AZ-MVP-5004796#management-group-recommendations){:target="_blank"} on the Microsoft Cloud Adoption Framework:

> Configure a default, dedicated management group for new subscriptions. This group ensures that no subscriptions are placed under the root management group. This group is especially important if there are users eligible for Microsoft Developer Network (MSDN) or Visual Studio benefits and subscriptions. A good candidate for this type of management group is a sandbox management group.

So, how can we change the default Management Group, that new Subscriptions go into?

Lets take a look at the different ways we could use to update the default management group, that new subscriptions go into.

{% tabs defaultmgmtgrp %}

{% tab defaultmgmtgrp AzurePortal %}

1. Use the search bar to search for and select 'Management groups'.
1. On the root management group, select details next to the name of the management group.
1. Under Settings, select Hierarchy settings.
1. Select the Change default management group button.

{% endtab %}

{% tab defaultmgmtgrp Terraform %}

    resource "azurerm_management_group_subscription_association" "example" {
    management_group_id = data.azurerm_management_group.example.id
    subscription_id     = data.azurerm_subscription.example.id
    }

{% endtab %}

{% tab defaultmgmtgrp PowerShell %}

```PowerShell
$root_management_group_id = "Enter the ID of root management group"
$default_management_group_id = "Enter the ID of default management group (or use the same ID of the root management group)"

$body = '{
     "properties": {
          "defaultManagementGroup": "/providers/Microsoft.Management/managementGroups/' + $default_management_group_id + '",
          "requireAuthorizationForGroupCreation": true
     }
}'

$token = (Get-AzAccessToken).Token
$headers = @{"Authorization"= "Bearer $token"; "Content-Type"= "application/json"}
$uri = "https://management.azure.com/providers/Microsoft.Management/managementGroups/$root_management_group_id/settings/default?api-version=2020-05-01"

Invoke-RestMethod -Method PUT -Uri $uri -Headers $headers -Body $body
```

{% endtab %}

{% endtabs %}
