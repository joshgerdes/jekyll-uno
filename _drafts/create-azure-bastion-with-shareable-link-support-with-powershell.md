---
date: 2023-03-16 00:00:00 +1300
title: Create Azure Bastion with Shareable Link support with PowerShell
author: Luke
categories: []
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

Because the service is in Public Preview - native PowerShell cmdlet support, enabling and configuring this feature isn't available - but you can easily enable it via the [Azure Portal](https://learn.microsoft.com/en-us/azure/bastion/shareable-link?WT.mc_id=AZ-MVP-5004796#enable-shareable-link-feature "Enable Shareable Link feature").

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
 2. Open a Terminal or PowerShell prompt, navigate to the folder containing the script
 3. Dot source the script so that you can run it from the session: . .\\New-AzBastionSharedLinkEnabled.ps1
 4. ![. .\\New-AzBastionSharedLinkEnabled.ps1](/uploads/windowsterminal_new-azbastionsharedlinkenabled.png ". .\New-AzBastionSharedLinkEnabled.ps1")
 5. Once it's imported - we can now run it; make sure you replace your parameters that match your environment:

        New-AzBastionSharedLinkEnabled -RGName BastionTest -VNetName vnet-aue-dev -addressPrefix 10.2.1.0/26 -region AustraliaEast -BastionPubIPName VNet1-ip -BastionResourceName net-aue-dev-bastion
 6. The script will then prompt for your credentials to authenticate
 7. You will then need to select the Azure subscription containing your Azure Virtual Network, then select Ok
 8. ![Select Azure subscription](/uploads/select-azsubscription_outgridview.png "Select Azure subscription")
 9. The script will then go and provision Azure Bastion and enable Shared Links. It will take a few minutes to run while it provisions Bastion. Then you will get JSON output, indicating it has been completed.
10. ![Windows PowerShell - New Azure Bastion](/uploads/windowsterminal_new-azbastionsharedlinkenabledrun.png "Windows PowerShell - New Azure Bastion")
11. s
12. s