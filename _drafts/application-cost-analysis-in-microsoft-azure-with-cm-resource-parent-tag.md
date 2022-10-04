---
date: 2022-10-05 00:00:00 +1300
title: Application cost analysis in Microsoft Azure with cm-resource-parent tag
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Cost Analysis in Microsoft Azure allows you to analyse the cost of your services; these services can be scoped into Resource Groups, Resources and Services; you can also group your services by [Tags](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Use tags to organize your Azure resources and management hierarchy").

Azure tags are name-value pairs used to organize resources. You can apply tags for individual resources, display show back or ownership and can be used for automation - but what assigning parent/child relationships to your resources?

[Tags](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json&WT.mc_id=AZ-MVP-5004796 "Resource naming and tagging decision guide") work well for most used cases, but there may be times when you want to get a more in-depth view of the service and dependencies - this is where the "cm-resource-parent" tag comes in.

Introduced in [Cost Analysis preview](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-preview-features-cost-management-labs?WT.mc_id=AZ-MVP-5004796#group-related-resources-in-the-cost-analysis-preview "Group related resources in the cost analysis preview"), Q3 of 2022, the 'cm-resource-parent tag' allows you to Group related resources together - to help give you a quick view of the solution's total cost in a parent/child relationship.

To use the cm-resource-parent tag, you must choose a parent resource _(an example may be an App Service or an Azure Virtual Desktop host pool)._ No changes will be made to this resource, but you need the ResourceID of the resource to apply to Child resources.

To find the ResourceID of the parent resource, you can use the [Azure Portal](https://portal.azure.com/#home "Azure Portal"), by

1. **Open** the **resource** that you want to be the parent of.
2. Select **Properties** in the resource menu.
3. Find the **Resource ID** property and copy its value.

You can easily use PowerShell to find the ResourceID as well:

    $ResourceName = 'Parent Resource'
    Get-AzResource -Name $ResourceName | Select-Object ResourceId

A resource ID looks like this _(you will need to copy the full thing, this will be used on your child's resources)_:

    /subscriptions/4501c644-74a3-4bfc-a456-16425eccd2a4/resourceGroups/vm-preprod-rg/providers/Microsoft.Network/publicIPAddresses/VM-T01-ip

Once you have the Resource ID of your resource, it is time to tag your Child's resources.

As an Azure Tag is a Key/Value pair - the tags will be similar to:

| Name | Value |
| --- | --- |
| cm-resource-parent | /subscriptions/4501c644-74a3-4bfc-a456-16425eccd2a4/resourceGroups/vm-preprod-rg/providers/Microsoft.Network/publicIPAddresses/VM-T01-ip |

To apply the ResourceID of the parent resource, you can use the [Azure Portal](https://portal.azure.com/#home "Azure Portal"), by

1. **Open** the **resource** you want to be the child of the parent you selected above.
2. Click **Tags**
3. Add in: **cm-resource-parent** in the value and the resource ID of your parent as a value.

_Note: You are unable to have a multi-hierarchy, i.e. a Parent, then Child and Child off that - it is purely a Parent and Child relationship at this stage. Also, the Resource ID will change if the Parent resources are moved to another Resource group or subscription._

These Tags can work easily with other cost management tags you may be using, so it doesn't replace but supplements your visibility.

You may have to wait up to a day _(24 hours)_ before the changes are visible in Azure Cost Analysis.

I have the [Azure Naming Tool](https://luke.geek.nz/azure/deploy-azure-naming-tool-into-an-azure-webapp-as-a-container/ "Azure Naming Tool") deployed in my example and would like to see the overall cost; these resources are deployed across multiple resources in the same subscription.