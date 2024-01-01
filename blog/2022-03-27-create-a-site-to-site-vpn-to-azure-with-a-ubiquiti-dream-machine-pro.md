---
date: '2022-03-27 00:00:00 +1300'
title: Create a Site to Site VPN to Azure with a Ubiquiti Dream Machine Pro
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---

The Ubiquiti [Dream Machine Pro](https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/udm-pro "Dream Machine Pro") has a lot of functionality built-in, including IPsec Site-to-site VPN_(Virtual Private Network)_ support.

I recently installed and configured a UDM-PRO at home, so now it's time to set up a site-to-vpn to my Microsoft Azure network.

I will create Virtual Network and Gateway resources using Azure Bicep, but please skip ahead.

My address range is as follows _(so make sure you adjust to match your setup and IP ranges)_:

| On-premises | Azure |
| --- | --- |
| 192.168.1.0/24 | 10.0.0.0/16 |

#### Prerequisites

* The latest [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-7.1.0?WT.mc_id=AZ-MVP-5004796) modules and [Azure Bicep/Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install?WT.mc_id=AZ-MVP-5004796) for local editing
* An Azure subscription that you have at least contributor rights to
* Permissions to the UDM Pro to set up a new network connection

I will be using PowerShell [splatting](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting?WT.mc_id=AZ-MVP-5004796 "Splatting") as it's easier to edit and display. You can easily take the scripts here to make them your own.

#### Deploy - Azure Network and Virtual Network Gateway

I will assume that you have both [Azure Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install#windows?WT.mc_id=AZ-MVP-5004796 "Azure Bicep - Install") and[PowerShell Azure](https://learn.microsoft.com/en-us/powershell/azure/install-az-ps?WT.mc_id=AZ-MVP-5004796 "PowerShell - Azure") modules installed and the know-how to connect to Microsoft Azure.

Azure Bicep deployments _(like ARM)_ have the following command: 'TemplateParameterObject'. 'TemplateParameterObject' allows Azure Bicep to accept parameters from PowerShell directly, which can be pretty powerful when used with a self-service portal or pipeline.

I will first make an Azure Resource Group using PowerShell for my Azure Virtual Network, then use the New-AzResourceGroupDeployment cmdlet to deploy my Virtual Network and subnets from my bicep file.

Along with the Virtual Network, we will also create 2 other Azure resources needed for a Site to Site VPN, a [Local Network Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-site-to-site-portal?WT.mc_id=AZ-MVP-5004796 "Tutorial: Create a site-to-site VPN connection in the Azure portal") _(this will represent your on-premises subnet and external IP to assist with routing)_and a [Virtual Network Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways?WT.mc_id=AZ-MVP-5004796 "What is VPN Gateway?") _(which is used to send encrypted traffic over the internet between your on-premises site(s) and Azure)_.

Update the parameters of the PowerShell script below, to match your own needs, and you may need to edit the Bicep file itself to add/remove subnets and change the IP address space to match your standards.

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

Note: The _'_[_-whatif_](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if?tabs=azure-powershell%2CCLI?WT.mc_id=AZ-MVP-5004796 "Bicep deployment what-if operation")' parameter has been added as a safeguard, so once you know the changes are suitable, then remove and rerun.

The Virtual Network Gateway can take 20+ minutes to deploy, leave the Terminal/PowerShell window open, you can also check the Deployment in the Azure Portal _(Under Deployments panel in the Resource Group)_.

![Azure Portal - Resource Group Deployments](/uploads/vnet-deployments2svpnazportal.png "Azure Portal - Resource Group Deployments")

The Azure Bicep file is located here:

{% gist 4399d36266e8be79afc62db7edf31d8c %}

Once deployed, run the following command to capture and copy the Gateway Public IP: 

    Get-AzPublicIPAddress | Select-Object Name, IpAddress 

Copy the Public IP, we will need this for configuring the UDM Pro, this would have been generated dynamically.

#### Configure - Ubiquiti Dream Machine Pro

 1. **Login** to the **UDM-Pro**
 2. ![Unifi OS](/uploads/udm-pro_unifi-os.png "UDM Pro Unifi OS")
 3. Click on **Network** _(under Applications heading)_
 4. Click **Settings** _(Gear icon)_
 5. ![Unifi OS - Network](/uploads/udm-pro_networksettings.png "UDM Pro Unifi OS")
 6. Click **VPN**
 7. ![UDM Pro Unifi OS - VPN](/uploads/udm-pro_vpn_s2svpn.png "UDM Pro Unifi OS - VPN")
 8. Scroll down and click **+ Create Site-to site-VPN**
 9. Fill in the following information:
    * **Network Name**_(ie Azure - SYD)_
    * **VPN Protocol** _(select Manual IPsec)_
    * **Pre-shared Key** _(enter in the SAME key that was used by Azure Bicep to create the Connection - if you have lost it, it can be updated in Azure, under Shared key on the connection attached to the Virtual network gateway, but will stop any other VPN connections using the old key)_
    * **Server Address** _(make sure you select the interface for your WAN/External IP)_
    * **Remote** Gateway/**Subnets** _(Enter in the Address Prefix of your Azure virtual network or subnets, remember to add any peered virtual networks and Press Enter)_
    * **Remote IP Address** _(Enter in the Public IP of the Virtual Network gateway, the same IP retrieved by Get-AzPublicIPAddress cmdlet )_
10. ![UDM Pro - Azure S2S VPN](/uploads/udmpro_s2svpnsettings1.png "UDM Pro - Azure S2S VPN")
11. Select **Manual**
12. ![UDM Pro - Azure S2S VPN](/uploads/udmpro_s2svpnsettings2.png "UDM Pro - Azure S2S VPN")

    Select **IPSec Profile**, and select **Azure Dynamic Routing**
13. Click **Apply Changes**

After a few minutes, the VPN should become connected and you should be able to connect to devices on the Azure Network using their private IP address.

If you have problems, make sure that the Gateway IPs line up and are correct, along with the pre-shared key.  You can also Pause the Network from the UDM-Pro and Resume to reinitiate the connection.

You can also troubleshoot the VPN connection, from the Azure Portal, by navigating the Virtual network gateway and selecting VPN Troubleshoot.

![Azure Portal - VPN Troubleshoot](/uploads/azureportal_vpntroubleshoot.png "Azure Portal - VPN Troubleshoot")
