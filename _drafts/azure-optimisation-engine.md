---
date: 2022-03-06 00:00:00 +1300
title: Azure Optimization Engine
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azurespringclean_2022_aoe.png"

---
This post is part of [Azure Spring Clean](https://www.azurespringclean.com/ "Azure Spring Clean") 2022! 

This article, along with others of its kind _(Articles, Videos etc)_ cover Azure Management topics such as Azure Monitor, Azure Cost Management, Azure Policy, Azure Security Principles or Azure Foundations!

Today I will be covering the [Azure Optimization Engine](https://github.com/helderpinto/AzureOptimizationEngine "Azure Optimization Engine"). 

_Note: Although I had originally planned on having this as a video, due to delay in receiving appropriate equipment, I have fallen to an article, however, plan on making a video on this in the future, feel free to add/ask any questions in the comments section below and I will make sure to cover them in any future video._

![](/uploads/azurespringclean_2022_aoe.png)

### Overview

> The Azure Optimization Engine _(AOE)_ is an extensible solution designed to generate optimization recommendations for your Azure environment, like a fully customizable Azure Advisor. 
>
> The first custom recommendations use-case covered by this tool was augmenting Azure Advisor Cost recommendations, particularly Virtual Machine right-sizing, with a fit score based on VM metrics and properties.

The [Azure Optimization Engine]() can…

* Enable new custom recommendation types
* Augment Azure Advisor recommendations with richer details that better drive action
* Add fit score to recommendations
* Add historical perspective to recommendations _(the older the recommendation, the higher the chances to remediate it)_
* Drive automated continuous optimization

Azure Optimization Engine combines multiple data sources to give you better data-driven decisions and recommendations, outside of that usually deployed by the inbuilt Azure Advisor, example use-cases and data sources can be seen below:

* Azure Resource Graph _(Virtual Machine and Managed Disks properties)_ 
* Azure Monitor Logs _(Virtual Machine performance metrics)_ 
* Azure Consumption _(consumption/billing usage details events)_ 
* Extracts data periodically to build a recommendations history 
* Joins and queries data in an analytics-optimized repository _(Log Analytics)_ 
* Virtual Machine performance metrics collected with Log Analytics agent 
* Can leverage existing customer set-up 
* Requires only a few metrics collected with a frequency >= 60 seconds

> Besides collecting **all Azure Advisor recommendations**, AOE includes other custom recommendations that you can tailor to your needs:
>
> * Cost
>   * Augmented Advisor Cost VM right-size recommendations, with fit score based on Virtual Machine guest OS metrics _(collected by Log Analytics agents)_ and Azure properties
>   * Underutilized VM Scale Sets
>   * Unattached disks
>   * Standard Load Balancers without backend pool
>   * Application Gateways without backend pool
>   * VMs deallocated since a long time ago (_forgotten VMs)_
>   * Orphaned Public IPs
> * High Availability
>   * Virtual Machine high availability _(availability zones count, availability set, managed disks, storage account distribution when using unmanaged disks)_
>   * VM Scale Set high availability _(availability zones count, managed disks)_
>   * Availability Sets structure _(fault/update domains count)_
> * Performance
>   * VM Scale Sets constrained by lack of compute resources
> * Security
>   * Service Principal credentials/certificates without expiration date
>   * NSG rules referring to empty or non-existing subnets
>   * NSG rules referring to orphan or removed NICs
>   * NSG rules referring to orphan or removed Public IPs
> * Operational Excellence
>   * Load Balancers without backend pool
>   * Service Principal credentials/certificates expired or about to expire
>   * Subscriptions close to the maximum limit of RBAC _(Role Based Access Control)_ assignments
>   * Management Groups close to the maximum limit of RBAC assignments
>   * Subscriptions close to the maximum limit of resource groups
>   * Subnets with low free IP space
>   * Subnets with too much IP space wasted
>   * Empty subnets
>   * Orphaned NICs

The Azure Optimization Engine is battle-tested, 

* Providing custom recommendations since Nov 2019 
* Serving Azure customers worldwide
* From smaller 50-500 VMs customers to larger ones with more than 5K VMs
* Several customer-specific developments (custom collectors and recommendation algorithms) • 
* Flexibility options include (multi-subscription and multi-tenant capability)
* Lightweight
*  Based on cheap services _(Azure Automation, Storage, small SQL Database_) 

A few hours after setting up the engine, you will get access to a Power BI dashboard and Log Analytic Workbooks with all Azure optimization opportunities, coming from both Azure Advisor and from custom recommendations included in the engine. 

These recommendations are then updated every 7 days and you can contribute with your own custom ones if needed.

> It is worth noting that Azure Optimisation Engine is **NOT** an official **Microsoft Product,** and as such is under no offical support, it was created and maintened by: Hélder Pinto, a Senior Customer Engineer for Microsoft and would like to take the opportunity to thank Hélder the amazing work he is doing with this product on a continous basis, and giving me his blessing to write this article.

#### Architecture

Azure Optimization Engine, runs on top of Azure Automation and Log Analytics. 

![](/uploads/architecture.jpg)

#### Additional Recommended Reading

* _“Augmenting Azure Advisor Cost Recommendations for Automated Continuous Optimization”_ blog post series:
  1. [Part 1 - Solution Overview](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/augmenting-azure-advisor-cost-recommendations-for-automated/ba-p/1339298 "Augmenting Azure Advisor Cost Recommendations for Automated Continuous Optimization – Part 1")
  2. [Part 2 - Collecting Data](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/augmenting-azure-advisor-cost-recommendations-for-automated/ba-p/1457687 "Augmenting Azure Advisor Cost Recommendations for Automated Continuous Optimization – Part 2")
  3. [Part 3 - Generating & Viewing Recommendations](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/augmenting-azure-advisor-cost-recommendations-for-automated/ba-p/1544796 "Augmenting Azure Advisor Cost Recommendations for Automated Continuous Optimization – Part 3")
  4. [Part 4 - Automating Continous Optimization with the Azure Optimization Engine](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/automating-continuous-optimization-with-the-azure-optimization/ba-p/1851317 "Automating Continuous Optimization with the Azure Optimization Engine")