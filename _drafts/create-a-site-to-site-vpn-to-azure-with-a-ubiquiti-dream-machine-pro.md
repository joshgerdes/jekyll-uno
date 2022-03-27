---
date: 2022-03-26 00:00:00 +1300
title: Create a Site to Site VPN to Azure with a Ubiquiti Dream Machine Pro
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
The Ubiquiti [Dream Machine Pro](https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/udm-pro "Dream Machine Pro") has a lot of functionality built-in, including IPsec Site-to-site VPN _(Virtual Private Network)_ support.

I recently installed and configured a UDM-PRO at home, so now it's time to set up a site-to-vpn to my Microsoft Azure network.

I will create Virtual Network and Gateway resources using Azure Bicep, but please skip ahead.

My address range is as follows _(so make sure you adjust to match your setup and IP ranges)_:

| On-premises | Azure |
| --- | --- |
| 192.168.1.0/24 | 10.0.0.0/16 |

#### Prerequisites

1. The latest [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-7.1.0) modules and [Azure Bicep/Azure CLI](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) for local editing
2. An Azure subscription that you have at least contributor rights to
3. Permissions to the UDM Pro to set up a new network connection

I will be using PowerShell [splatting](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting "Splatting") as it's easier to edit and display. You can easily take the scripts here to make them your own.

#### Deploy - Azure Network

I will assume that you have both [Azure Bicep](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install#windows "Azure Bicep - Install") and[ PowerShell Azure](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps "PowerShell - Azure") modules installed and the know-how to connect to Microsoft Azure.

Azure Bicep deployments _(like ARM)_ have the following command: 'TemplateParameterObject'. 'TemplateParameterObject' allows Azure Bicep to accept parameters from PowerShell directly, which can be pretty powerful when used with a self-service portal or pipeline.

I will first make an Azure Resource Group using PowerShell for my Azure Virtual Network, then use the New-AzResourceGroupDeployment cmdlet to deploy my Virtual Network and subnets from my bicep file.

Update the parameters to match your own needs, and you may need to edit the Bicep file itself to add/remove subnets and change the IP address space to match your standards.

The shared key will be used between the UDM Pro and your Azure network; make sure this is unique.

    #Connects to Azure
    Connect-AzAccount
    #Resource Group Name
    $resourcegrpname = 'network_rg'
    #Creates a resource group for the storage account
    New-AzResourceGroup -Name $resourcegrpname -Location 'AustraliaEast'
    # Parameters splat, for Azure Bicep
    # Parameter options for the Azure Bicep Template, this is where your Azure Bicep parameters go
    $paramObject = @{
    'sitecode' = 'luke'
    'environment' = 'prod'
    'contactEmail' = 'email@luke.geek.nz'
    'sharedkey' = '18d5b51a17c68a42d493651bed88b73234bbaad0'
    'onpremisesgwip' = '123.456.789.101'
    'onpremisesaddress' = '192.168.1.0/24'
    }
    # Parameters for the New-AzResourceGroupDeployment cmdlet goes into.
    $parameters = @{
    'Name' = 'AzureNetwork-S2S'
    'ResourceGroupName' = $resourcegrpname
    'TemplateFile' = 'c:\temp\Deploy-AzVNETS2S.bicep'
    'TemplateParameterObject' = $paramObject
    'Verbose' = $true
    }
    #Deploys the Azure Bicep template
    New-AzResourceGroupDeployment @parameters -WhatIf

Note: The _'_[_-whatif_](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if?tabs=azure-powershell%2CCLI "Bicep deployment what-if operation")' parameter has been added as a safeguard, so once you know the changes are suitable, then remove and rerun.

The Virtual Network Gateway can take 20+ minutes to deploy.