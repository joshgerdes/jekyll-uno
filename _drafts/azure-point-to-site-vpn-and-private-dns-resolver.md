---
date: 2022-09-02 00:00:00 +1200
title: Azure Point to Site VPN and Private DNS Resolver
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
You might access resources such as [Azure SQL databases](https://azure.microsoft.com/products/azure-sql/database/?WT.mc_id=AZ-MVP-5004796 "Azure SQL Database") or [Azure Storage accounts](https://docs.microsoft.com/azure/storage/?WT.mc_id=AZ-MVP-5004796 "Azure Storage documentation") if you're connecting to a Microsoft Azure network externally _(_[_from a non-Azure VM_](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances?WT.mc_id=AZ-MVP-5004796 "Name resolution for resources in Azure virtual networks")_)_; if you operate Cloud-only services and don't have an external DNS provider, such as Active Directory - connecting to [private link](https://azure.microsoft.com/services/private-link/?WT.mc_id=AZ-MVP-5004796 "Private Link") resources, you may have to edit your local host's file, and override local DNS to point to the IP of the [private endpoint]() for each service.

This is not sustainable, not scalable, and you might end up throwing your hands in the air and switching back to public-facing services and just whitelisting other users' Public IPs to gain access to Azure resources - which can lead to its own set of issues, such as unmanaged IPs left with access to resources after contractors or users leave or have finished their work, IP address changes if not managed correctly can allow any user or company to have a direct line of sight to your company resources.

> Today we will concentrate on DNS resolution of Private Endpoints, using [Azure DNS Private Resolver](https://docs.microsoft.com/azure/dns/dns-private-resolver-overview?WT.mc_id=AZ-MVP-5004796 "What is Azure DNS Private Resolver?") as a DNS proxy when connecting to Azure using a [Point to Site VPN](https://docs.microsoft.com/azure/vpn-gateway/point-to-site-about?WT.mc_id=AZ-MVP-5004796 "About Point-to-Site VPN").

For this article, I assume you have an Azure Point to Site already set up; if you don't, you can refer to a previous article I wrote for [Creating an Azure Point to Site VPN using Azure Active Directory authentication](https://luke.geek.nz/azure/create-azure-point-to-site-vpn-using-azure-active-directory-authentication/ "Create Azure Point to Site VPN using Azure Active Directory authentication").

_Disclaimer: Azure Private DNS Resolver is still in Public Preview at the time of this article (02/09/2022). If you aim to use this in a Production scenario, functionality and services may change._

So what is Azure DNS Resolver?

> Azure DNS private resolver is a cloud-native, highly available, and DevOps-friendly service. It provides a simple, zero-maintenance, reliable, and secure Domain Name System (DNS) service to resolve and conditionally forward DNS queries from a virtual network, on-premises, and to other target DNS servers without the need to create and manage a custom DNS solution. Resolve DNS names hosted in Azure Private DNS Zones from on-premises networks as well as DNS queries for your own domain names. This will make your DNS infrastructure work privately and seamlessly across on-premises networks and enable key hybrid networking scenarios.