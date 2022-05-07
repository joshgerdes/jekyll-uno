---
date: 2022-05-07 00:00:00 +1200
title: Hidden Tags in Azure
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
[Tags](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Use tags to organize your Azure resources and management hierarchy") in Microsoft Azure are pivotal to resource management, whether it's used for reporting or automation.

But sometimes, you need that extra bit of information to help discover what resources are for, or you may way to add information to a resource that isn't directly displayed in the portal, especially when complex tags are in use that might be used in automation initiatives.

This is where 'hidden' Azure Tags come in handy.

Tags starting with the prefix of _'hidden-'_ will not be displayed under Tags in the Azure Portal; however, they will be displayed in the resource metadata and utilised by PowerShell and Azure CLI for automation initiatives.

Examples are:

| Tags | Value |
| --- | --- |
| hidden-title | Web Server |
| hidden-ShutdownAutomation | Yes |

### hidden-title

As I mentioned above, every tag with 'hidden-' in front of it will be hidden in the Azure Portal. However, 'hidden-title' behaves differently.

You may have noticed that some resources in Azure, especially if the Azure ARM _(Azure Resource Manager)_ creates them and the name is GUID based, has a '(name)' around them after the resource name; this is because of the hidden-title tag.

The hidden-title tag is especially useful for being able to pick resources that belong to a specific service or application.

An example is below:

![Azure Portal - Hidden Title Tag](/uploads/azureportal_hiddentitle.png "Azure Portal - Hidden Title Tag")

In this case, I have used the _hidden-title_ of 'Web Server', allowing me to quickly view what resources may be mapped to my Web Server.

You may notice that the Test-Virtual Machines title, is displayed in the Resource Groups search blade, and not in the actual Resource Group, there are some areas of the Portal that will not display the hidden-title tag currently.

If I navigate to my Virtual Machine and click on the Tags blade, all I see is my CreatedBy tag.

If I navigate to the Tags blade of my Virtual Machine, all I see is my CreatedBy tag![Azure Portal - Tags](/uploads/azureportal-hiddentitle-vmtags.png "Azure Portal - Tags")

However, if I navigate to the Overview page and click on JSON View, I can see the hidden tags in the resource metadata.

![Azure Portal - Resource Tags](/uploads/azureportal-hiddentitle-vmtagsjson.png "Azure Portal - Resource Tags")

### hidden tags

#### Azure Portal

You can use the Azure Portal directly to add the Tags to apply hidden tags.

![Azure Portal - Add Tags](/uploads/azureportal_hiddentagsadd.png "Azure Portal - Add Tags")

You can remove the Tag by adding the hidden-tag again and keeping the value empty _(ie blanking out the hidden-title will remove the title)_, but it will still be against the metadata as a Tag that exists - it is much cleaner to use PowerShell.

![Azure - Resource Tags](/uploads/azureportal_hiddentagsremove.png "Azure - Resource Tags")

#### PowerShell

Get-AzTag and Remove-AzTag, do not display the hidden tags, to add and remove the tags, you need to add them through 'Update-AzTag' and 'Replace' or 'Merge' to overwrite the tags, which needs the Resource targetted by Resource ID.

A handy snippet to use to add/remove the Tags on individual or multiple resources is:

    $replacedTags = @{"hidden-title" = "Web Server"; "hidden-ShutdownAutomation" = "Yes"}
    $resouceGroup = 'vm-dev-rg'
    Get-AzResource -ResourceGroupName $resouceGroup | Select-Object ResourceId | Out-GridView -PassThru | Update-AzTag -Tag $replacedTags -Operation Merge

This will snippet will gather all the resources in your Resource Group, then select their Resource IDs, the script will then prompt with a GUI allowing you to select which resources or resources you want to update your tags on, then once you click Ok, it will update the Tags on the resources you selected.

![PowerShell - Add Azure Tags](/uploads/powershell_hiddentagsadd.png "PowerShell - Add Azure Tags")