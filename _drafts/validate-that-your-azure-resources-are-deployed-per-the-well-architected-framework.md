---
date: 2021-07-13 00:00:00 +1200
title: Validate that your Azure Resources are deployed per the Well-Architected Framework
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Validate that your Azure Resources are deployed per the Well-Architected Framework.. it is pretty long-winded, but imagine!

Of a way of validating your services are secure and deployed in accordance with your companies governance rules and the Azure Architecture framework, both before and after the resources have been commissioned!

Imagine no longer! There is a PowerShell module designed specifically for that purpose: PSRule for Azure.

PSRule is a suite of rules to validate Azure resources and infrastructure as code (IaC) using PSRule.

Features of PSRule for Azure include:

* Over 200 pre-built rules to validate Azure resources.
* Validate resources and infrastructure code pre or post-deployment using Azure DevOps or Github!
* Runs on macOS, Linux, and Windows.

PSRule for Azure provides two methods for analyzing Azure resources:

* Pre-flight - Before resources are deployed from Azure Resource Manager templates.
* In-flight - After resources are deployed to an Azure subscription.

With over 200 inbuilt rules _(and you can add your own),_ there is a lot of resource types covered such as (but not limited to):

* Azure App Service
* Azure Key vault
* Azure Virtual Machine
* Azure Storage
* Azure Network
* Azure Public IP

Azure PSRules has been in development since 2019 and is under constant updates