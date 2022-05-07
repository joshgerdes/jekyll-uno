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