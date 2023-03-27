---
date: 2023-03-27 00:00:00 +1300
title: Azure Quick Revuew
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
There are a lot of workbooks that help with Microsoft Azure cost optimization, but when having discussions and looking into SLA/SLO and availability scenarios, there are fewer options to select from - today, we are going to look at the deployment and output of Azure Quick Review.

> Azure Quick Review (azqr) goal is to produce a high level assessment of an Azure Subscription or Resource Group providing the following information for each Azure Service:

[Azure Quick Review](https://github.com/cmendible/azqr "Azure Quick Review") _(created by Microsoft Snr Cloud Solution Architect_ [_Carlos Mendible_](https://www.linkedin.com/in/carlosmendible/)_),_ can supplement other tools - to give you visibility into your Azure services and answer questions such as:

* What is my expected SLA?
* Are my resources protected against zone failures?
* Am I collecting diagnostic logs for my resources?

Using this tool is pretty simple, and today we will look at running it from a windows endpoint, but first, we need some prerequisites.

* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796 "How to install the Azure CLI")
* [AzQr - Windows Release](https://github.com/cmendible/azqr/releases "cmendible/azqr/releases")