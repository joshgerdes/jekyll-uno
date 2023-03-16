---
date: 2023-03-16 00:00:00 +1300
title: Create Azure Bastion with Shareable Link support with PowerShell
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
[Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Bastion?") is a service you deploy that lets you connect to a virtual machine using your browser and the Azure portal or via the native SSH or RDP client installed on your local computer.

#### Overview

> The Azure Bastion service is a fully platform-managed PaaS service you provision inside your virtual network. It provides secure and seamless RDP/SSH connectivity to your virtual machines directly from the Azure portal over TLS.

Because of this, if you don't have line-of-sight access to your Virtual Machines (_via express route, Site-to-Site VPN etc.)_, Bastion becomes your jump box, allowing secure access to your virtual machines without needing a public IP.

There is a downside, though. To connect to a Virtual Machine secured by Bastion, you need access to the Azure Portal, or command line connectivity to Azure, to create the tunnel; this means that you may need to grant people elevated rights and access they may not need to connect.

As of November 2022[,]() Microsoft introduced shareable links into public preview, solving two key pain points:

* Administrators will no longer have to provide full access to their Azure accounts to one-time VM users—helping to maintain their privacy and security.
* Users without Azure subscriptions can seamlessly connect to VMs without exposing RDP/SSH ports to the public internet.

> The Bastion **Shareable Link** feature lets users connect to a target resource (virtual machine or virtual machine scale set) using Azure Bastion without accessing the Azure portal.

At the time of this writing, there are some [scenarios ](https://learn.microsoft.com/en-us/azure/bastion/shareable-link?WT.mc_id=AZ-MVP-5004796#considerations "Create a shareable link for Bastion")where shareable links won't work - particularly across Network peering across subscriptions and regions.

Because the service is in Public Preview - native PowerShell cmdlet support, enabling and configuring this feature isn't available - but you can easily allow it via the [Azure Portal](https://learn.microsoft.com/en-us/azure/bastion/shareable-link?WT.mc_id=AZ-MVP-5004796#enable-shareable-link-feature "Enable Shareable Link feature").

To get around that, we will leverage the [Azure Rest API](https://learn.microsoft.com/rest/api/azure/?WT.mc_id=AZ-MVP-5004796 "Azure REST API reference") directly, using PowerShell to enable the Shareable Link feature and create and obtain a shareable link for a Virtual Machine.

#### Create Azure Bastion

I will assume there is already an Azure Virtual Network created; if not, you can follow the [Microsoft documentation](https://learn.microsoft.com/azure/virtual-network/quick-create-portal?WT.mc_id=AZ-MVP-5004796 "Quickstart: Create a virtual network using the Azure portal") to get it up and running!

Also, make sure you have the [Az Module](https://learn.microsoft.com/powershell/azure/new-azureps-module-az?view=azps-9.5.0&WT.mc_id=AZ-MVP-5004796 "Introducing the Azure Az PowerShell module") installed.

The PowerShell function we will run will require a few parameters to create the Azure Bastion resource and enable Shared Link functionality; these parameters are:

|  |  |
| --- | --- |
| Parameters | Note |
| RGName | The Resource Group of your Virtual Network |
| VNetName | The Virtual Network name |
| addressPrefix | The address prefix for your new Bastion subnet. For Azure Bastion resources deployed on or after November 2, 2021, the minimum AzureBastionSubnet size is /26 or larger (/25, /24, etc.). |
| region | The region, that Azure Bastion is deployed into (this needs to match your Virtual Network) |
| BastionPubIPName | The name of the Public IP, used by the Azure Bastion resource (this is the Azure resource name, it doesn't have an external DNS alias, so doesn't need to be globally unique) |
| BastionResourceName | The name of your Azure Bastion resource |

 1. Copy the script below into a file named: New-AzBastionSharedLinkEnabled.ps1

        function New-AzBastionSharedLinkEnabled {
            <#
              .SYNOPSIS
              Creates an Azure Bastion resource with shared link enabled, on an already existing Azure Virtual Network.
            #>
            [CmdletBinding()]
            param
            (
              [Parameter(Mandatory = $false, Position = 0)]
              [System.String]
              $RGName = "BastionTest",
              
              [Parameter(Mandatory = $false, Position = 1)]
              [System.String]
              $VNetName = 'vnet-aue-dev',
              
              [Parameter(Mandatory = $false, Position = 2)]
              [System.String]
              $addressPrefix = '10.2.1.0/26',
              
              [Parameter(Mandatory = $false, Position = 3)]
              [System.String]
              $region = 'AustraliaEast',
              
              [Parameter(Mandatory = $false, Position = 4)]
              [System.String]
              $BastionPubIPName = 'VNet1-ip',
              
              [Parameter(Mandatory = $false, Position = 5)]
              [Object]
              $BastionResourceName = "$VNetName-bastion"
            )
            
            # Set variable values for Resource Group name, Virtual Network name, address prefix, region, and bastion-related resources.
          
            # Connect to Azure using Get-AzAccount cmdlet.
            Connect-AzAccount
            
            # Use Get-AzSubscription cmdlet to get all the subscriptions that the account has access to and allow the user to choose one using Out-GridView.
            Get-AzSubscription | Out-GridView -PassThru | Select-AzSubscription
            $token = (Get-AzAccessToken).Token
            $subscription = Get-AzContext | Select-Object Subscription
            
            # Use Get-AzVirtualNetwork cmdlet to get the virtual network object and then use Add-AzVirtualNetworkSubnetConfig cmdlet to create a new subnet for Azure Bastion service. Finally, use Set-AzVirtualNetwork cmdlet to update the virtual network configuration.
            $VNET = Get-AzVirtualNetwork -ResourceGroupName $RGName -Name $VNetName 
            Add-AzVirtualNetworkSubnetConfig -VirtualNetwork $VNET -Name "AzureBastionSubnet" -AddressPrefix $addressPrefix | Set-AzVirtualNetwork
            $VNET = Get-AzVirtualNetwork -ResourceGroupName $RGName -Name $VNetName 
            
            # Note: If there is an error message, it could indicate that the address prefix for the new subnet overlaps with existing address ranges or is too small.
            
            # Use New-AzPublicIpAddress cmdlet to create a new public IP address resource for the Bastion service.
            $publicip = New-AzPublicIpAddress -ResourceGroupName $RGName -name $BastionPubIPName -location $region -AllocationMethod Static -Sku Standard
            $publicip = Get-AzPublicIpAddress -ResourceGroupName $RGName -Name $BastionPubIPName
            # Use New-AzBastion cmdlet to create a new Azure Bastion resource with the specified configuration, including the virtual network and public IP address resources created earlier.
            New-AzBastion -ResourceGroupName $RGName -Name $BastionResourceName -PublicIpAddressRgName $publicip.ResourceGroupName -PublicIpAddressName $publicip.Name  -VirtualNetwork $VNET -Sku 'Standard' 
            
            #Enable Shareable links for VMs in Azure Bastion.
            $BastionSubnet = Get-AzVirtualNetworkSubnetConfig -Name 'AzureBastionSubnet' -VirtualNetwork $VNET
            
            $Body = [PSCustomObject]@{
              location   = $region
              properties = @{
                enableShareableLink = "true"
                ipConfigurations    = @(
                  @{
                    name       = "bastionHostIpConfiguration"
                    properties = @{
                      subnet          = @{
                        id = $BastionSubnet.id
                      }
                      publicIPAddress = @{
                        id = $publicip.Id
                      }
                    }
                  }
                )
              }
              
            }  | ConvertTo-Json -Depth 6
            
            $params = @{
              Uri         = "https://management.azure.com/subscriptions/" + $subscription.Subscription.Id + 
              "/resourceGroups/$($RGName)/providers/Microsoft.Network/bastionHosts/$($BastionResourceName)?api-version=2022-07-01"
              Headers     = @{ 'Authorization' = "Bearer $token" }
              Method      = 'Put'
              Body        = $body
              ContentType = 'application/json'
            }
            
            # Invoke the REST API and store the response
            Invoke-RestMethod @Params
          }
 2. Open a Terminal or PowerShell prompt, and navigate to the folder containing the script.
 3. Dot source the script so that you can run it from the session: **. .\\New-AzBastionSharedLinkEnabled.ps1**
 4. ![. .\\New-AzBastionSharedLinkEnabled.ps1](/uploads/windowsterminal_new-azbastionsharedlinkenabled.png ". .\New-AzBastionSharedLinkEnabled.ps1")
 5. Once it's imported - we can now run it; make sure you replace your parameters that match your environment:

        New-AzBastionSharedLinkEnabled -RGName BastionTest -VNetName vnet-aue-dev -addressPrefix 10.2.1.0/26 -region AustraliaEast -BastionPubIPName VNet1-ip -BastionResourceName net-aue-dev-bastion
 6. The script will then prompt for your credentials to authenticate
 7. You will then need to select the Azure subscription containing your Azure Virtual Network, then select Ok
 8. ![Select Azure subscription](/uploads/select-azsubscription_outgridview.png "Select Azure subscription")
 9. The script will then go and provision Azure Bastion and enable Shared Links. It will take a few minutes to run while it provisions Bastion. Then you will get JSON output, indicating it has been completed.
10. ![Windows PowerShell - New Azure Bastion](/uploads/windowsterminal_new-azbastionsharedlinkenabledrun.png "Windows PowerShell - New Azure Bastion")
11. ![Azure Bastion - Shareable Link](/uploads/azureportal_azurebastion_shareablelinkconfig.png "Azure Bastion - Shareable Link")

#### Create Shareable Link

Now that we have an Azure Bastion instance and have Shareable Links enabled - it's time to create a Shareable Link for a Virtual Machine; this triggers 2 API endpoints - creating the shareable link and then retrieving the shareable link.

The same assumptions are made, so make sure you have the [Az Module](https://learn.microsoft.com/powershell/azure/new-azureps-module-az?view=azps-9.5.0&WT.mc_id=AZ-MVP-5004796 "Introducing the Azure Az PowerShell module") installed.

The script relies on the following parameters:

| Parameters | Note |
| --- | --- |
| BastionResourceName | The name of your Azure Bastion resource |
| RGName | The Resource Group of your Bastion resource |
| VMRGName | The Resource Group of your Virtual Machine, you want a Shareable Link for |
| Vmname | The name of the Virtual Machine you want a shareable link for |

 1. Copy the script below into a file named: New-AzBastionShareableLink.ps1

        function New-AzBastionShareableLink {
          <#
            .SYNOPSIS
              Creates an Azure Bastion shareable link.
          #>
          [CmdletBinding()]
          param
          (
            [Parameter(Mandatory = $false, Position = 0)]
            [System.String]
            $BastionResourceName = 'vnet-aue-dev-bastion',
            
            [Parameter(Mandatory = $false, Position = 1)]
            [System.String]
            $RGName = "BastionTest",
            
            [Parameter(Mandatory = $false, Position = 1)]
            [System.String]
            $VMRGName = "BastionTest",
        
            [Parameter(Mandatory = $false, Position = 2)]
            [System.String]
            $VMname = "2022ServerVM-2"
          )
          
          # Connect to Azure using Get-AzAccount
          Connect-AzAccount
          
          # Get all subscriptions that the account has access to
          Get-AzSubscription | Out-GridView -PassThru | Select-AzSubscription
          
          $subscription = Get-AzContext | Select-Object Subscription
          # Get the access token for the authenticated user
          $token = (Get-AzAccessToken).Token
          
          $ID = Get-AzVM -ResourceGroupName $VMRGName -Name $VMName | Select-Object Id -ExpandProperty id
          
          $body = @{
            
            vms = @(
              @{
                vm = @{
                  id = $ID.Id
                }
              }
            )
            
          }  | ConvertTo-Json -Depth 3
          
            #creates the shareable link for the VM
          $params = @{
            Uri         = "https://management.azure.com/subscriptions/" + $subscription.Subscription.Id + 
            "/resourceGroups/$RGName/providers/Microsoft.Network/bastionHosts/$BastionResourceName/createShareableLinks?api-version=2022-07-01"
            Headers     = @{ 'Authorization' = "Bearer $token" }
            Method      = 'POST'
            Body        = $body
            ContentType = 'application/json'
          }
          
          # Invoke the REST API and store the response
          Invoke-RestMethod @Params
          
          #Gets the shareable link for the VM
            
         $params = @{
            Uri         = "https://management.azure.com/subscriptions/" + $subscription.Subscription.Id + 
            "/resourceGroups/$($RGName)/providers/Microsoft.Network/bastionHosts/$BastionResourceName/getShareableLinks?api-version=2022-09-01"
            Headers     = @{ 'Authorization' = "Bearer $token" }
            Method      = 'POST'
            # Body        = $body
            ContentType = 'application/json'
          }
          
          # Invoke the REST API and store the response
          $ShareableLink = Invoke-RestMethod @Params
          Write-Output $ShareableLink.value.bsl 
        }
 2. Open a Terminal or PowerShell prompt, and navigate to the folder containing the script.
 3. Dot source the script so that you can run it from the session: **. .\\New-AzBastionShareableLink.ps1**
 4. s
 5. Once it's imported - we can now run it; make sure you replace your parameters that match your environment:

        New-AzBastionShareableLink -BastionResourceName net-aue-dev-bastion -RGName BastionTest -VMRGName BastionTest -VMname 2022ServerVM-2
 6. ![Azure Bastion - Create Shared Link](/uploads/windowsterminal_new-azbastionsharedlink.png "Azure Bastion - Create Shared Link")
 7. The script will then prompt for your credentials to authenticate
 8. You will then need to select the Azure subscription containing your Azure Virtual Network, then select Ok
 9. ![Select Azure subscription](/uploads/select-azsubscription_outgridview.png "Select Azure subscription")
10. The script will then go and collect the ID of the Virtual Machine, pass that through to the Create a Shareable Link, then wait 10 seconds for the Bastion Resource to update properly, then collect the Shareable Link and output it to the terminal.
11. ![Azure Bastion - Shared Link](/uploads/windowsterminal_azurebastionsharedlink.png "Azure Bastion - Shared Link")
12. I can then copy the URL into my favourite browser and connect to your Virtual Machine securely!
13. ![Microsoft Azure Bastion - Connect](/uploads/azurebastionshareablelink_vmconnect.gif "Microsoft Azure Bastion - Connect")

The scripts can also be found directly on GitHub here: [https://github.com/lukemurraynz/Azure](https://github.com/lukemurraynz/Azure "https://github.com/lukemurraynz/Azure")