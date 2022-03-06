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

> The Azure Optimization Engine _(AOE)_ is an extensible solution designed to generate optimization recommendations for your Azure environment. See it like a fully customizable Azure Advisor. Actually, the first custom recommendations use-case covered by this tool was augmenting Azure Advisor Cost recommendations, particularly Virtual Machine right-sizing, with a fit score based on VM metrics and properties.

The Azure Optimization Engine can…

* Enable new custom recommendation types
* Augment Azure Advisor recommendations with richer details that better drive action
* Add fit score to recommendations
* Add historical perspective to recommendations (the older the recommendation, the higher the chances to remediate it)
* Drive automated continuous optimization