---
date: 2022-09-02 00:00:00 +1200
title: Azure Point to Site VPN and Private DNS Resolver
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
You might access resources such as [Azure SQL databases](https://azure.microsoft.com/products/azure-sql/database/?WT.mc_id=AZ-MVP-5004796 "Azure SQL Database") or [Azure Storage accounts](https://docs.microsoft.com/azure/storage/?WT.mc_id=AZ-MVP-5004796 "Azure Storage documentation") if you're connecting to a Microsoft Azure network; if you operate Cloud-only services and don't have an external DNS provider, such as Active Directory - connecting to [private link](https://azure.microsoft.com/services/private-link/?WT.mc_id=AZ-MVP-5004796 "Private Link") resources, you may have to edit your local host's file, and override local DNS to point to the IP of the [private endpoint]() for each service.

This is not sustainable, not scaleable, and you might end up throwing your hands in the air and switching back to public-facing services and just whitelisting other users' Public IPs to gain access to Azure resources - which can lead to its own set of issues, such as unmanaged IPs left with access to resources after contractors or users leave or have finished their work, IP address changes if not managed correctly can allow any user or company to have a direct line of sight to your company resources.

Today we will concentrate on DNS resolution of Private Endpoints, using [Azure DNS Private Resolver](https://docs.microsoft.com/azure/dns/dns-private-resolver-overview?WT.mc_id=AZ-MVP-5004796 "What is Azure DNS Private Resolver?") when connecting to Azure using a [Point to Site VPN](https://docs.microsoft.com/azure/vpn-gateway/point-to-site-about?WT.mc_id=AZ-MVP-5004796 "About Point-to-Site VPN").

For this article, I assume you have an Azure Point to Site already set up; if you don't, you can refer to a previous article I wrote for [Creating an Azure Point to Site VPN using Azure Active Directory authentication](https://luke.geek.nz/azure/create-azure-point-to-site-vpn-using-azure-active-directory-authentication/ "Create Azure Point to Site VPN using Azure Active Directory authentication").