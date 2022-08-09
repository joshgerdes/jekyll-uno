---
date: 2022-08-09 00:00:00 +1200
title: Create a Public Holidays API using Microsoft Azure
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Using a previous [blog post](https://luke.geek.nz/azure/turn-on-a-azure-virtual-machine-using-azure-automation/tomation "Turn on a Azure Virtual Machine using Azure Automation ") I did on using a third-party API _(Application Programming Interface)_ to start a Virtual Machine, when it wasn't a Public Holiday, I had a thought on what could be an option if I wanted an API only accessible on an internal network or if I wanted to include custom Holidays such as Star Wars day or company holidays? And could I create and query my own API using Microsoft Azure services? You can!

### Overview

> Today we will create a base Public Holidays API using several Microsoft Azure serverless services, such as Azure Function, Azure Storage Account and API Management.

_Note: As this is a demonstration, I will be using a_ [_Consumption-based Azure Function_](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=AZ-MVP-5004796 "Azure Functions hosting options") _and Azure storage account, and although it is a good place to start - depending on your requirements, you may be better off with Azure Function Premium Plan to avoid cold-start times, and if you need a high amount of requests and writes (GET and POSTs) and resiliency, then replace the Storage account table with a_ [_Cosmos DB_](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction?WT.mc_id=AZ-MVP-5004796 "Azure Cosmos DB")_._

#### Pre-requisites

* An Azure subscription, with at least Contributor rights to a Resource Group.
* Azure PowerShell modules _(_[_Az.Accounts_](https://docs.microsoft.com/en-us/powershell/module/az.accounts/?view=azps-8.2.0&WT.mc_id=AZ-MVP-5004796 "Az.Accounts")_,_ [_Az.Storage_](https://docs.microsoft.com/en-us/powershell/module/az.storage/?view=azps-8.2.0&WT.mc_id=AZ-MVP-5004796 "Az.Storage") _&_ [_AzTables_](https://www.powershellgallery.com/packages/AzTable/ "AzTable")_)_

_Note: AzTables is not part of the normal Az PowerShell module set and is a separate module that you will need to install (Install-Module AzTables)._

We will use a mix of the Azure Portal and PowerShell to deploy this solution from start to finish; the source data and code can be found directly in the GitHub repository here: [lukemurraynz/PublicHoliday-API](https://github.com/lukemurraynz/PublicHoliday-API "PublicHoliday-API") for reference.