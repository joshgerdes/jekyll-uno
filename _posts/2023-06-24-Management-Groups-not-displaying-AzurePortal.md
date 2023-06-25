---
title: Azure Management Groups not displaying in the Azure Portal
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/azure-management-group-notloading.png
date: '2023-06-24 00:00:00 +1300'
---

When logging into the Microsoft Azure Portal, to view your [Management Group](https://learn.microsoft.com/azure/governance/management-groups/overview?WT.mc_id=AZ-MVP-5004796 "What are Azure management groups?"){:target="blank"} You might have found it blank or constantly attempting to load.

![Azure Management Group - Not loading](/images/posts/azure-management-group-notloading.png "Azure Management Group - Not loading")

It looks like a potential bug in the Portal interface, especially  if you have the correct permissions to see those Management Groups. Here is a few things to look for:

### Elevated rights - Global Administrator

By default, if you are a Global Administrator, it does not allow you to see Azure Resources and manage Azure management groups.

If you have a Global Administrator role, and this is the first time you are setting up Management Groups, then you can [elevate](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?WT.mc_id=AZ-MVP-5004796#elevate-access-for-a-global-administrator){:target="blank"} your rights, to manage the Azure Management Groups.

Note: Because of the elevated nature of this role, it is recommended to enable it only for the period you need to do your work, and make sure you have [specific roles assigned to](https://learn.microsoft.com/azure/role-based-access-control/role-assignments-portal?WT.mc_id=AZ-MVP-5004796) manage your Azure infrastructure, as necessary.

If this is not the first time you set up Management Groups, ensure you have the right to see the Management Groups.

### Create an Azure Management Group using PowerShell

One of the fixes (workaround) discovered is that creating a Management Group triggers the Azure Portal to update, allowing management.

You can do this using the [Azure PowerShell](https://learn.microsoft.com/powershell/azure/install-azure-powershell?view=azps-10.0.0&WT.mc_id=AZ-MVP-5004796){:target="blank"} cmdlets, by running:

         New-AzManagementGroup -GroupName 'Contoso'

Once the Management Group is created, you should be able to refresh the [Azure Management Group](https://portal.azure.com/#view/Microsoft_Azure_ManagementGroups/ManagementGroupBrowseBlade/%7E/MGBrowse_overview){:target="blank"} page in the Portal and view your Management Groups, if that doesn't work then log out and back into the Portal.

You can then use the Remove cmdlet to delete the new Management Group you created.

         Remove-AzManagementGroup -GroupName 'Contoso'

Note: This article was based on findings from the Microsoft Q&A article: [Management Groups Unavailable in Tenant: Limited Account Control and Organization](https://learn.microsoft.com/en-us/answers/questions/1315218/management-groups-unavailable-in-tenant-limited-ac?WT.mc_id=AZ-MVP-5004796){:target="blank"}
