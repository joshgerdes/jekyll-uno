---
date: '2022-10-05 00:00:00 +1300'
title: Application cost analysis in Microsoft Azure with cm-resource-parent tag
authors: [Luke]
tags:
  - Azure
toc: false
header:
  teaser: /uploads/azureportal_costanalysis_aznamingtool.png

---

Cost Analysis in Microsoft Azure allows you to analyse the cost of your services; these services can be scoped into Resource Groups, Resources and Services; you can also group your services by [Tags](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Use tags to organize your Azure resources and management hierarchy").

Azure tags are name-value pairs used to organize resources. You can apply tags for individual resources, display show back or ownership and can be used for automation - but what assigning parent/child relationships to your resources?

[Tags](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json&WT.mc_id=AZ-MVP-5004796 "Resource naming and tagging decision guide") work well for most used cases, but there may be times when you want to get a more in-depth view of the service and dependencies - this is where the "_cm-resource-parent_" tag comes in.

Introduced in [Cost Analysis preview](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-preview-features-cost-management-labs?WT.mc_id=AZ-MVP-5004796#group-related-resources-in-the-cost-analysis-preview "Group related resources in the cost analysis preview"), Q3 of 2022, the 'cm-resource-parent tag' allows you to Group related resources together - to help give you a quick view of the solution's total cost in a parent/child relationship. The 'cm' in the tag stands for: Cost Management.

![cm-resource-parent Child Relationship](/uploads/parentchild.png "cm-resource-parent Child Relationship")

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

_Note: You cannot have a multi-hierarchy, i.e. a Parent, then Child and Child off that - it is purely a Parent and Child relationship at this stage. Also, the Resource ID will change if the Parent resources are moved to another Resource group or subscription._

These Tags can work easily with other cost management tags you may be using _(but you cannot have more than one cm-resource-parent tag)_, so it doesn't replace but supplements your visibility. They are supported on any resource that is Tag-capable.

You may have to wait up to a day _(24 hours)_ before the changes are visible in Azure Cost Analysis.

I have the [Azure Naming Tool](https://luke.geek.nz/azure/deploy-azure-naming-tool-into-an-azure-webapp-as-a-container/ "Azure Naming Tool") deployed in my example and would like to see the overall cost; these resources are deployed across multiple resources in the same subscription.

Choosing my WebApp as my parent resource, I tagged all child resources _(App Service Plan, Container Registry, Storage Account)_ with the relevant tag and resource ID as seen below:

![Azure Portal - Child resource](/uploads/azureportal_cmtags_child.png "Azure Portal - Child resource")

After 24 hours, I then went to the [**Cost Analysis (Preview)**](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/Menu/\~/costanalysisv3 "Cost analysis (preview)") and selected **Resources** and could view the current cost of my service after a few days of use.

![Azure Cost Analysis](/uploads/azureportal_costanalysis_aznamingtool.png "Azure Cost Analysis")

And another example can be seen below - where I have added a Public IP as a child resource of the Azure storage account, which, although the parent in this relationship, is a child in the Azure Naming Tool.

![Azure Cost Analysis](/uploads/azureportal_costanalysis_example2.png "Azure Cost Analysis")

As you can see, the 'cm-resource-parent' is another way to group related resources of different types from a cost analysis angle; still, in preview, this tag opens up the door for various other initiatives across observability, security stacks etc. 

Although not tested, you also should be able to output the resource ID of your Bicep code and add that as a variable for any resources deployed via Infrastructure as Code.

It's worth noting that this feature is still in Preview at the time of this article, so if you incur any bugs or have feature requests, you can use the 'Rate the Cost Analysis Preview' feature in the Azure Portal to supply feedback to the product teams.
