---
date: 2022-09-30 00:00:00 +1300
title: Application cost analysis in Microsoft Azure with cm-resource-parent tag
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Cost Analysis in Microsoft Azure allows you to analyse the cost of your services; these services can be scoped into Resource Groups, Resources and Services; you can also group your services by [Tags](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Use tags to organize your Azure resources and management hierarchy") - but what assigning parent/child relationships to your resources?

Tags work well for most used cases, but there may be times when you want to get a more in-depth view of the service and dependencies - this is where the "cm-resource-parent" tag comes in.