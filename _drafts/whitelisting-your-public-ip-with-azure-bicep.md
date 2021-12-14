---
date: 2021-12-14 00:00:00 +1300
title: Whitelisting your Public IP with Azure Bicep and PowerShell
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Being able to whitelist and restrict Azure resources by being accessible by specific Public IP _(Internet Protocol)_ addresses has been around for years, most Azure resources support it, a Storage account is no different.

In this article, I will be using PowerShell to obtain my current public IP, then parse that variable into my Azure Bicep deployment to create a storage account, with the firewall rule allowing ONLY my public IP address.

I am going to assume that you have both [Azure Bicep ](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install#windows "Azure Bicep - Install")and[ PowerShell Azure](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps "PowerShell - Azure") modules installed, and know-how to connect to Microsoft Azure.

Utilising PowerShell to create dynamic variables in your deployment, can open the doors to more flexible deployments, such as including the name of the person deploying the infrastructure into the tags of the resource - or in this case adding a whitelisted IP automatically to your Azure resource to be secure by default.