---
date: 2021-12-14 00:00:00 +1300
title: Whitelisting your Public IP with Azure Bicep and PowerShell
permalink: /azure/whitelisting-your-public-ip-with-azure-bicep/
author: Luke
categories:
- Azure
- PowerShell
toc: false
header:
  teaser: "images/powershell-blog-feature-banner.png"

---
Allowing and restricting Azure resources by being accessible by specific Public IP _(Internet Protocol)_ addresses has been around for years; most Azure resources support it, a Storage account is no different.

In this article, I will be using PowerShell to obtain my current public IP, then parse that variable into my Azure Bicep deployment to create a storage account, with the firewall rule allowing ONLY my public IP address.

I will assume that you have both [Azure Bicep](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install#windows "Azure Bicep - Install"){:target="_blank"} and[ PowerShell Azure](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps "PowerShell - Azure"){:target="_blank"} modules installed and the know-how to connect to Microsoft Azure.

Utilising PowerShell to create dynamic variables in your deployment can open the doors to more flexible deployments, such as including the name of the person deploying the infrastructure into the tags of the resource - or in this case, adding a whitelisted IP automatically to your Azure resource to be secure by default.

I will be using PowerShell [splatting](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting "Splatting"){:target="_blank"} as it's easier to edit and display. You can easily take the scripts here to make them your own.

Azure Bicep deployments *(like ARM)* have the following command: 'TemplateParameterObject'. This allows Azure Bicep to accept parameters from PowerShell directly, which can be pretty powerful when used with a self-service portal or pipeline.

Now we are ready to create the Azure Storage account. I will make an Azure Resource Group using PowerShell for my storage account first, then use the New-AzResourceGroupDeployment cmdlet to deploy my storage account from my bicep file.

    #Connects to Azure
    Connect-AzAccount
    #Grabs the Public IP of the currently connected PC and adds it into a variable.
    $publicip = (Invoke-WebRequest -uri "http://ifconfig.me/ip").Content
    #Resource Group Name
    $resourcegrpname = 'storage_rg'
    #Creates a resource group for the storage account
    New-AzResourceGroup -Name $resourcegrpname -Location "AustraliaEast"
    # Parameters splat, for Azure Bicep
    # Parameter options for the Azure Bicep Template, this is where your Azure Bicep parameters go
    $paramObject = @{
      'storageaccprefix' = 'stg'
      'whitelistpublicip'  = $publicip
    }
    # Parameters for the New-AzResourceGroupDeployment cmdlet goes into.
    $parameters = @{
      'Name'                  = 'StorageAccountDeployBase'
      'ResourceGroupName'     = $resourcegrpname 
      'TemplateFile'          = 'c:\temp\storageaccount.bicep'
      'TemplateParameterObject'    = $paramObject
      'Verbose'               = $true
    }
    #Deploys the Azure Bicep template
    New-AzResourceGroupDeployment @parameters

![Azure Bicep - Parameter](/uploads/storageaccount_publicip.png "Azure Bicep - Parameter")

As you can see above, I am grabbing my current IP Address from the ifconfig website and storing it in a variable *(as a string object)*, then referencing it in the paramObject - which will be passed through to the TemplateParameterObject command as Parameters strings for Azure Bicep, my IP address _(I am running this from an Azure VM)_ is then passed through, to Azure Bicep.

My Azure Bicep is below:

    param storageaccprefix string = ''
    param whitelistpublicip string = ''
    var location = resourceGroup().location
    
    resource storageaccount 'Microsoft.Storage/storageAccounts@2021-06-01' = {
      name: '${storageaccprefix}${uniqueString(resourceGroup().id)}'
      location: location
      sku: {
        name: 'Standard_ZRS'
      }
      kind: 'StorageV2'
      properties: {
        defaultToOAuthAuthentication: false
        allowCrossTenantReplication: false
        minimumTlsVersion: 'TLS1_2'
        allowBlobPublicAccess: true
        allowSharedKeyAccess: true
        isHnsEnabled: true
        networkAcls: {
          resourceAccessRules: []
          bypass: 'AzureServices'
          virtualNetworkRules: []
          ipRules: [
            {
              value: whitelistpublicip
              action: 'Allow'
            }
          ]
          defaultAction: 'Deny'
        }
        supportsHttpsTrafficOnly: true
        encryption: {
          services: {
      
            blob: {
              keyType: 'Account'
              enabled: true
            }
          }
          keySource: 'Microsoft.Storage'
        }
        accessTier: 'Hot'
      }
    }
    

In Azure Bicep - I am accepting the whitelistpublicip variable from PowerShell and have passed that along to the virtualNetworkRules object as an Allow, while the defaultAction is 'Deny'.

If I navigate to the Azure Portal, I can see my newly created storage account; under the Networking blade, I can see that the Firewall has been enabled and my Public IP has been added successfully:

![Azure Storage Account - Network](/uploads/storageaccount_firewall.png "Azure Storage Account - Network")

Hopefully, this helps you be more secure from deployment time and gives you a good framework to work on; in the future, the same process can be used to create inbound RDP rules for Virtual Machines, as an example.