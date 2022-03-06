---
date: 2022-03-06 00:00:00 +1300
title: Azure Optimisation Engine
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
This post is part of [Azure Spring Clean](https://www.azurespringclean.com/ "Azure Spring Clean") 2022! 

This article, along with others of its kind _(Articles, Videos etc)_ cover Azure Management topics such as Azure Monitor, Azure Cost Management, Azure Policy, Azure Security Principles or Azure Foundations!

Today I will be covering the Azure Optimization Engine.

### Overview

> The Azure Optimization Engine _(AOE)_ is an extensible solution designed to generate optimization recommendations for your Azure environment, like a fully customizable Azure Advisor. 
>
> The first custom recommendations use-case covered by this tool was augmenting Azure Advisor Cost recommendations, particularly Virtual Machine right-sizing, with a fit score based on VM metrics and properties.

The Azure Optimization Engine can…

* Enable new custom recommendation types
* Augment Azure Advisor recommendations with richer details that better drive action
* Add fit score to recommendations
* Add historical perspective to recommendations _(the older the recommendation, the higher the chances to remediate it)_
* Drive automated continuous optimization

Azure Optimization Engine combines multiple data sources to give you better data-driven decisions and recommendations, outside of that usually deployed by the inbuilt Azure Advisor, example use-cases and data sources can be seen below:

* Azure Resource Graph (Virtual Machine and Managed Disks properties) 
* Azure Monitor Logs(Virtual Machine performance metrics) 
* Azure Consumption (consumption/billing usage details events) 
* Extracts data periodically to build a recommendations history 
* Joins and queries data in an analytics-optimized repository (Log Analytics) 
* Virtual Machine performance metrics collected with Log Analytics agent 
* Can leverage existing customer set-up 
* Requires only a few metrics collected with a frequency >= 60 seconds