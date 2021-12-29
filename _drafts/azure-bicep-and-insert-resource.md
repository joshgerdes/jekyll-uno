---
date: 2021-12-29 00:00:00 +1300
title: Azure Bicep and Insert Resource
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Azure Bicep is a Domain Specific Language (DSL) for deploying Azure resources declaratively. Azure Bicep is a **transparent abstraction** over ARM and ARM templates, which means anything that can be done in an ARM Template can be done in Bicep.

Azure Bicep has recently _(December 2021)_ been updated to: v0.4.1124, along with various other hotfixes and enhancements, this version supports ‘Insert Resource’ functionality.

Insert Resource simplifies ARM to Bicep conversion without having to export entire ARM templates then compile them to Bicep when you are only after export for a single resource.