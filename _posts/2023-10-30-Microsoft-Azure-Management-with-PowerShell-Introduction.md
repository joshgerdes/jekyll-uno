---
title: Microsoft Azure Management with PowerShell - Introduction
author: Luke
categories:
  - Azure
  - PowerShell
toc: true
header:
  teaser: /images/posts/BlogHeading-BlogHeading-Microsoft-Azure-Management-with-PowerShell.gif
date: 2023-10-30 00:00:00 +1300
keywords:
  - azure
  - powershell
  - landing zones
description: Delve into the common ways to work with Microsoft Azure, using PowerShell.
slug: azure-management-powershell
---

# Introduction to PowerShell in Azure

> To see a video of these commands in action, take a look at the following YouTube-hosted video: [Microsoft Azure Management with PowerShell - Introduction](https://youtu.be/a4gehHwlwBQ)

## PowerShell

PowerShell is a powerful scripting and automation framework developed by Microsoft. It is designed for task automation and configuration management and is particularly useful for managing and automating Microsoft Windows environments. PowerShell uses a command-line interface with a scriptable approach, and it's built on the .NET Framework.

* [What is PowerShell?](https://learn.microsoft.com/powershell/scripting/overview?WT.mc_id=AZ-MVP-5004796)

## PowerShell and Microsoft Azure

When it comes to Microsoft Azure, PowerShell provides a robust set of cmdlets (pronounced "command-lets") that enable you to interact with and manage Azure resources, making it a valuable tool for working with Azure services.

When you run a PowerShell cmdlet to, for example, create a virtual machine or retrieve information about an Azure resource, the cmdlet translates your request into an HTTP request to the relevant Azure REST API endpoint.

* [Azure PowerShell Documentation](https://learn.microsoft.com/powershell/azure/?view=azps-10.4.1&WT.mc_id=AZ-MVP-5004796)

> There is an assumption, that you have access to an Azure environment, and the ability to create resources, within that environment.

![Microsoft Azure Management with PowerShell](/images/posts/BlogHeading-BlogHeading-Microsoft-Azure-Management-with-PowerShell.gif)

First up, let's verify the version of PowerShell we have, open a Powershell terminal and run:

``` powershell
$PSVersionTable
```

A supported version of PowerShell version 7 or higher is the recommended version of PowerShell for use with the Az PowerShell module on all platforms including Windows, Linux, and macOS.

The Az PowerShell module is preinstalled in [Azure Cloud Shell](https://learn.microsoft.com/azure/cloud-shell/overview?WT.mc_id=AZ-MVP-5004796) and in [Docker](https://learn.microsoft.com/powershell/azure/azureps-in-docker?view=azps-10.4.1&tabs=amd64&WT.mc_id=AZ-MVP-5004796) images.

### Setting up your Azure environment for PowerShell

First thigs first, lets installed the Azure ([Azure Az PowerShell module](https://learn.microsoft.com/powershell/azure/new-azureps-module-az?view=azps-10.4.1&WT.mc_id=AZ-MVP-5004796))modules.

``` powershell
# Install Azure Modules
# The Set-PSRepository cmdlet is used to set values for a registered repository. 
# The Install-Module cmdlet is used to download one or more modules from an online gallery and installs them on the local computer. In this case, the command is installing the Az module, which provides cmdlets for managing Azure resources.
Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
Install-Module Az 
```

If you don't have local administrator rights, you can install it into your user profile like below:

``` powershell
# Install Azure Module as Current User (as opposed to System)
# '-Scope CurrentUser` specifies that the module should be installed only for the current user. If you don't specify a scope, the default is `AllUsers`, which requires administrator permissions.

Install-Module -Name Az -Repository PSGallery -Scope CurrentUser
```

You can install a specific version of the Az module by specifying RequiredVersion, like below:

``` powershell
# Install specific version of Azure Modules

Install-Module -Name Az -RequiredVersion 7.1.0
```

You will find that the Azure powershell cmdlets will constantly get updated, to resolve bugs, offer new functionality, to update the modules to the ltest you can use:

``` powershell
# Update Azure Module
# The command Get-InstalledModule -Name Az* | Update-Module is used to update all installed PowerShell modules that start with "Az".
Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
Get-InstalledModule -Name Az* | Update-Module
```

Az is a collection of different cmdlets, across multiple Azure resource types, to view a list of avaliable commands you use 'Get-Command', like below:

``` powershell
# Gets Az Commands
# Note: Will take a while for all the cmdlets to list.
Get-Command -Noun Az*
```

### Getting started with Azure PowerShell module

Lets connect to Microsoft Azure

``` powershell
# Connect to Azure - Interactive will prompt for credentials
Connect-AzAccount
```

If your wanting to connect to Azure, from a device that doesn't supoport the credential prompt, like Azure Cloudshell you can connect using another device, using a device code:

``` powershell
# Connect to Azure
Connect-AzAccount -UseDeviceAuthentication
```

If you have a Service principal, you can use this to authenticate, commonly used for automation scripts, Azure DevOps agents and GitHub runners.

``` powershell
# Connect to Azure using Service Principal authentication
$SecurePassword = ConvertTo-SecureString -String "Password123!" -AsPlainText -Force
$TenantId = 'yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyy'
$ApplicationId = 'zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzz'
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $ApplicationId, $SecurePassword
Connect-AzAccount -ServicePrincipal -TenantId $TenantId -Credential $Credential
```

Once, connected - its time to check what Azure subscriptions you can use.

``` powershell
# Get Azure Subscriptions
Get-AzSubscription
```

Once you have selected the right Azure subscription to connect to, you can set your Subscription context (modify/delete resources). Add your subscription ID, from the earlier step in between ''.

``` powershell
# Select Azure Subscription
$subid = ''
Set-AzContext -SubscriptionId $subid
```

Now you have connected to your, Azure subscription, it is time to get your Azure resources and Resource Groups

``` powershell
# Get Azure resource groups and resources
Get-AzResourceGroup | Format-Table
Get-AzResource | Format-Table
```

``` powershell
# Get Azure resource
Get-AzResource
```

``` powershell
# Get Azure resource by ResourceType
Get-AzResource | Where-Object {$_.ResourceType -eq 'Microsoft.Network/virtualNetworks'} 
```

``` powershell
# Sort Azure resource by Name and Resource Group
Get-AzResource | Where-Object {$_.ResourceType -eq 'Microsoft.Storage/storageAccounts'} | Sort-Object Name
Get-AzResource | Sort-Object ResourceGroupName 
```

``` powershell
# Working with Variables

# Working with variables and data types in PowerShell
$resourceType = 'Microsoft.Network/virtualNetworks'
Get-AzResource | Where-Object {$_.ResourceType -eq $resourceType}
```

``` powershell
# Using PowerShell operators for comparisons and calculations

$resources = Get-AzResource
$count = $resources.Count
Write-Host "You have $count resources in your Azure subscription."
```

``` powershell
# Scripting constructs: loops and conditional statements
$resources = Get-AzResource

foreach ($resource in $resources) {
    if ($resource.ResourceType -eq 'Microsoft.Network/virtualNetworks') {
        Write-Host "Found a virtual network: $($resource.Name)"
        Write-Host "This virtual network is in $($resource.ResourceGroupName)" -ForegroundColor Green
    }
}
```

``` powershell
# Scripting constructs: loops and conditional statements
$subscriptions = Get-AzSubscription

foreach ($subscription in $subscriptions) {
$resource = Get-AzResource | Where-Object {$_.ResourceType -eq 'Microsoft.Network/virtualNetworks'} 

    if ($resource.ResourceType -eq 'Microsoft.Network/virtualNetworks') {
        Write-Host "Found a virtual network: $($resource.Name)" -BackgroundColor Black -ForegroundColor White
        Write-Host "This virtual network is in $($resource.ResourceGroupName)" -ForegroundColor Green
        Write-Host "This Virtual Network is in $($subscription.Name)" -ForegroundColor Green
    }
}
```

``` powershell
# Error handling in PowerShell
try {
    Get-AzResource -ResourceGroupName "NonexistentResourceGroup" -ErrorAction Stop
} catch {
    Write-Host "An error occurred: $_. Make sure you have selected the right Resource Group" -ForegroundColor Red
}
```

### Resource Creation

``` powershell
# Import Module
Import-Module Az -Verbose
```

``` powershell
#Create Azure Resource Group
New-AzResourceGroup -Name "MyResourceGroup" -Location "West US"
```

``` powershell
# Get Regions
Get-AzLocation | Select-Object -First 1
Get-AzLocation | Select-Object DisplayName, Location, PhysicalLocation, GeographyGroup | Format-Table
```

``` powershell
ate Azure Resource Group
$region = 'AustraliaEast'
New-AzResourceGroup -Name "MyResourceGroup$region" -Location $region
```

``` powershell
# Create a storage account
$uniqueId = [guid]::NewGuid().ToString().Substring(0,4)
$region = 'AustraliaEast'
$ResourceGroupName = "MyResourceGroup$region"
New-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name "mystgacc$uniqueId" -Location $region -SkuName Standard_LRS -AllowBlobPublicAccess $false -verbose
```

``` powershell
#Remove Azure Storage account
$region = 'AustraliaEast'
$ResourceGroupName = $ResourceGroupName
Remove-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name "mystgacc$uniqueId" -Force -verbose
Get-AzStorageAccount -ResourceGroupName $ResourceGroupName -Name "mystgacc$uniqueId" -verbose
```

``` powershell
# Create an Azure Virtual Network
$region = 'AustraliaEast'
$ResourceGroupName = 'network-prod-rg'
$VNetname = 'vnet-prod'
$subnetname = 'infraservers'
$subnetAddressPrefix = '10.0.0.0/24'

# Create a resource group
$ResourceGroup = Get-AzResourceGroup -Name $ResourceGroupName -ErrorAction SilentlyContinue

if ($null -eq $ResourceGroup)
{
    Write-Host "Creating Resource Group $ResourceGroupName in $region" -ForegroundColor Yellow
    $ResourceGroup = New-AzResourceGroup -Name $ResourceGroupName -Location $region -Force
}
else
{
    Write-Host "Resource Group $ResourceGroupName already exists in $region" -ForegroundColor Green
}

# Create a virtual network
$AzVNET = New-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name $VNetname -AddressPrefix '10.0.0.0/16' -Location $region

# Create a subnet
$subnetConfig = Add-AzVirtualNetworkSubnetConfig -Name $subnetname -AddressPrefix $subnetAddressPrefix -VirtualNetwork $AzVNET
```

``` powershell
# Get full object output
# Alias (This is a pipeline to the Format-List cmdlet (fl is an alias for Format-List). It formats the output as a list of properties for each object. This can make it easier to read the details of the virtual network.)

Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name $VNetname # | fl
```

``` powershell
# Alias

Get-Alias  | Select-Object -First 2
```

``` powershell
#splat

$configData = @{
    ResourceGroupName = "MyResourceGroup"
    Location = "West US"
    StorageAccountName = "stgacctest100"
}

try {
    New-AzStorageAccount -ResourceGroupName $configData.ResourceGroupName -Name $configData.StorageAccountName -Location $configData.Location -SkuName Standard_LRS
} catch {
    Write-Error "Failed to create storage account: $_"
}
```

``` powershell
#splat as parameters

$configData = @{
    "ResourceGroupName" = "MyResourceGroup"
    "Location" = "West US"
    "StorageAccountName" = "stgacctest100"
    "SkuName" = "Standard_LRS"

}

try {
    New-AzStorageAccount @configData
} catch {
    Write-Error "Failed to create storage account: $_"
}
```

``` powershell
# Tags
$ResourceGroupName = 'TagTestRG'
New-AzResourceGroup -Name $ResourceGroupName -Location 'AustraliaEast'
Set-AzResourceGroup -Name $ResourceGroupName -Tag @{ Department = "Finance"; Project = "Q1" }
```

``` powershell
# Get Tag Resource Group
$ResourceGroupName = 'TagTestRG'
(Get-AzResourceGroup -Name $ResourceGroupName).Tags
```

``` powershell
$ResourceGroupName = 'TagTestRG'
$tags = (Get-AzResourceGroup -Name $ResourceGroupName).Tags
$tags.Remove("Project")
Set-AzResourceGroup -Name $ResourceGroupName -Tag $tags
```
