---
date: 2022-08-09T00:00:00.000+12:00
title: Create a Public Holidays API using Microsoft Azure
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Using a previous [blog post](https://luke.geek.nz/azure/turn-on-a-azure-virtual-machine-using-azure-automation/tomation "Turn on a Azure Virtual Machine using Azure Automation ") I did on using a third-party API _(Application Programming Interface)_ to start a Virtual Machine when it wasn't a Public Holiday, I had a thought on what could be an option if I wanted an API only accessible on an internal network or if I wanted to include custom Holidays such as Star Wars day or company holidays? And could I create and query my API using Microsoft Azure services? You can!

### Overview

> Today we will create a base Public Holidays API using several Microsoft Azure serverless services, such as Azure Function, Azure Storage Account and API Management.

_Note: As this is a demonstration, I will be using a_ [_Consumption-based Azure Function_](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale?WT.mc_id=AZ-MVP-5004796 "Azure Functions hosting options") _and Azure storage account, and although it is a good place to start - depending on your requirements, you may be better off with Azure Function Premium Plan to avoid cold-start times, and if you need a high amount of requests and writes (GET and POSTs) and resiliency, then replace the Storage account table with a_ [_Cosmos DB_](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction?WT.mc_id=AZ-MVP-5004796 "Azure Cosmos DB")_._

The solution will be made up of the following:

| Azure Service | Name | Plan | Note |
| --- | --- | --- | --- |
| Application Insights | ai-nzPublicHolidays-prd-ae |  |  |
| Azure API Management | apims-publicholidays-prd-ae | Developer (No SLA) |  |
| Azure Function | func-nzpublicHolidays-prd-ae | Function App - Consumption |  |
| Azure Storage Account | funcnzpublicholidaystgac | StorageV2 (general purpose v2) - Locally-redundant storage (LRS) | Contains 'PublicHolidays' table |
| Azure Storage Account | rgnzpublicholidayspb4ed | Storage (general purpose v1)  - Locally-redundant storage (LRS) | Contains Azure Functions App Files |
| Resource Group | rg-publicholidays-prd-ae |  | Resource Group - containing above resources. |

#### Pre-requisites

* An Azure subscription _(with at least Contributor rights to a Resource Group)_.
* Azure PowerShell modules _(_[_Az.Accounts_](https://docs.microsoft.com/en-us/powershell/module/az.accounts/?view=azps-8.2.0&WT.mc_id=AZ-MVP-5004796 "Az.Accounts")_,_ [_Az.Storage_](https://docs.microsoft.com/en-us/powershell/module/az.storage/?view=azps-8.2.0&WT.mc_id=AZ-MVP-5004796 "Az.Storage") _&_ [_AzTables_](https://www.powershellgallery.com/packages/AzTable/ "AzTable")_)_

_Note: AzTables is not part of the standard Az PowerShell module set and is a separate module you will need to install (Install-Module AzTables)._

We will use a mix of the Azure Portal and PowerShell to deploy this solution from start to finish; you can find the source data and code directly in the GitHub repository here: [lukemurraynz/PublicHoliday-API](https://github.com/lukemurraynz/PublicHoliday-API "PublicHoliday-API") for reference _(feel free to fork, raise pull requests etc.)._ In this guide, I will try not to assume preexisting knowledge _(other than general Azure and PowerShell knowledge)_.

### Deployment

The deployment steps will be separated into different sections to help simplify implementation.

> First, make sure you adjust the names of your resources and locations to suit your naming conventions and regional locations _(such as Australia East or West Europe)_. Your deployments may fail if a name is already in use. See "[Microsoft Azure Naming Conventions](https://luke.geek.nz/azure/microsoft-azure-naming-conventions/ "Microsoft Azure Naming Conventions ")" for more about Naming conventions.

### Create Resource Group

The Resource Group will contain all resources related to the API that we will deploy today.

_However, I recommend you consider what resources might be shared outside of this API - such as API Management, and put them in a separate Shared or Common Resource Group, to keep the lifecycle of your resources together (ie API resources all in one place, so if it gets decommissioned, it is as easy a deleting the Resource Group)._

1. Log in to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
2. Click **Click on the burger and click** [**Resource groups**](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups "Resource Groups")
3. Click **+ Create**
4. Select your **Subscription**
5. Type in a name for your **Resource Group** _(like 'rg-publicholidays-prd-ae')_
6. Select your **Region** and click **Next: Tags**
7. Enter in applicable **tags** _(ie Application: Public Holidays API)_
8. Click **Next: Review + create**
9. Click **Create**

![Create a resource group](/uploads/azureportal_creatergapi.png "Create a resource group")

If you prefer PowerShell, you can deploy a new Resource Group with the below:

    New-AzResourceGroup -Name 'rg-publicholidays-prd-ae' -Location 'Australia East' -Tag @{Application="Public Holidays API"}

### Create Storage Account

Now that the Resource Group has been created, it's time to import our Storage Account - which will hold our Table of data around Public Holidays.

 1. Log in to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
 2. Click **Click on the burger and click** [**Storage Accounts**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts "Storage accounts")
 3. Click **+ Create**
 4. Select the **Subscription** and **Resource Group** you created earlier
 5. Enter in a **Name** for your **Storage Account** (_like 'funcnzpublicholidaystgac')_
 6. Select your **Region** _(i.e. Australia East)_
 7. For **Performance**, I am going to select: **Standard**
 8. For **Redundancy**, as this is a demo, I will select **Locally-redundant storage (LRS). If** you plan on running this in production, you may consider ZRS for zone redundancy.
 9. If you plan on locking down the Storage Account to your Virtual Network or specific IP addresses, continue to the Networking Tab; we can accept the defaults and click: **Review**.
10. Click **Create**

If you prefer PowerShell, you can deploy a new Storage account with the below:

    New-AzStorageAccount -ResourceGroupName 'rg-publicholidays-prd-ae' -Name 'funcnzpublicholidaystgac' -Location 'Australia East' -SkuName 'Standard_LRS' -Kind StorageV2

### Create Storage Account