---
date: 2022-01-11 00:00:00 +1300
title: Create Azure Point to Site VPN using Azure Active Directory authentication
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
You may be working remotely, or only have a few devices needing access to your resources in Azure, a solution that can be deployed is a point to site connection straight into your Microsoft Azure network.

This functionality, allows your computer to connect privately to resources over a secure tunnel using your internet connection, using an Azure Virtual Network gateway, you can seamlessly connect to resources without the need of opening up your resources to the internet or having to whitelist your _(or third party vendor)_ IP address, which may change on a daily basis.

Using Azure Active Directory, you know only your specified users have access to your Azure resources.

You can have both a site to site and point to site VPN running on the same gateway, today we are going to set up a Point to Site VPN using Windows 11.

Depending on the SKU of your Virtual Network Gateway, depends on the number of concurrent connections and throughput you are allowed, because we are using Azure Active Directory and the OpenVPN protocol, I will be selecting Generation 1, VpnGw1, supporting a max of 250 connections _(you can double the number of throughput and connections if you are running in Active/Active and have a second gateway, or select a higher SKU)_.

> Azure AD authentication is supported for OpenVPN® protocol connections only and requires the Azure VPN client.

A note about Gateway SKUs _(apart from Basic)_ you can resize in the same generation _(ie Generation 1 VpnGw1 to VpnGw3, but you can't go from Generation 1 VpnGw1 to Generation 2 VpnGw5, in order to upgrade you have to delete and recreate the gateway, just keep this in mind when deciding on the SKU of your resources_).

You can read more about the Virtual Network Gateways and VPN SKUs at the official Microsoft documentation '[here'](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways "What is VPN Gateway?"); depending on your requirements your gateway SKU may be different.

### Create Azure Point to Site VPN using Azure Active Directory authentication

#### Prerequisites

* An Azure subscription _(that you have at least contributor rights to and the ability to create Users and Groups)_
* An endpoint device running Windows 10 or 11 that you can install the [Azure VPN client](https://www.microsoft.com/en-us/p/azure-vpn-client-preview/9np355qt2sqb?rtc=2&activetab=pivot:overviewtab " Azure VPN Client") onto

#### Create Virtual Network

First things first, let's create a Virtual Network.

 1. Log in to the [Azure Portal](https://portal.azure.com/#home "Azure Portal")
 2. Click on **+ Create a resource**
 3. Search for: **Virtual Network** and click on it
 4. Click **Create**
 5. **Select** or create your **Resource Group** that you want your network resource to sit in _(I recommend Virtual Network and the gateway resources sit in its own Resource Group away from other resources so that they can be protected by resource locks, RBAC and they are usually classified as a shared resource)_.
 6. ![](/uploads/azureportal-createvirtualnetwork.png)
 7. Click **Next: IP Addresses**
 8. Now we need to **define** the **Address space** and subnets, I will leave the Address space as 10.0.0.0/16, but remove the Default subnet _(select the checkbox next to the subnet and select Delete)_
 9. Click +**Add Subnet**, and add a new subnet with the name of: GatewaySubnet with an IP range of: 10.0.1.0/27 _(this subnet will be used by our Virtual Network Gateway and the name needs to be exactly GatewaySubnet)_.
10. Now I will add a subnet named: app servers, for the Virtual Machines I will need to connect to will be placed.
11. ![](/uploads/azureportal-createvirtualnetworksubnets.png)
12. Click **Next: Security**
13. Leave everything _(BastionHost, DDoS Protection Standard, Firewall)_ as Disabled
14. Click **Next: Tags**
15. Enter in appropriate tags and click **Review + Create**
16. Review your configuration and click **Create**