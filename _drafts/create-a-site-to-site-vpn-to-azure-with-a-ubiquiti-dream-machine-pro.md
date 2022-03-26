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
The Ubiquiti [Dream Machine Pro](https://store.ui.com/collections/unifi-network-unifi-os-consoles/products/udm-pro "Dream Machine Pro"), has a lot of functionality built-in, including IPsec Site-to-site VPN _(Virtual Private Network)_ support.

I recently, installed and configured a UDM-PRO at home, so now it's time to set up a site-to-vpn to my Microsoft Azure network.

I am going to create a Virtual Network and Gateway resources using Azure Bicep, but feel free to skip ahead.

My address range is as follows _(so make sure you adjust to match your own setup and IP ranges)_:

| On-premises | Azure |
| --- | --- |
| 192.168.1.0/24 | 10.0.0.0/16 |

#### Prerequisites

1. The latest [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-7.1.0) modules and [Azure Bicep/Azure CLI](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) for local editing
2. An Azure subscription that you have at least contributor rights to