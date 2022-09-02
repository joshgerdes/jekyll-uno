---
date: 2022-09-02 00:00:00 +1200
title: Azure Private DNS Resolver and Azure Point to Site VPN
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azureprivatednsresolver.png"

---
You might access resources such as [Azure SQL databases](https://azure.microsoft.com/products/azure-sql/database/?WT.mc_id=AZ-MVP-5004796 "Azure SQL Database"){:target="_blank"} or [Azure Storage accounts](https://docs.microsoft.com/azure/storage/?WT.mc_id=AZ-MVP-5004796 "Azure Storage documentation"){:target="_blank"} if you're connecting to a Microsoft Azure network externally _(_[_from a non-Azure VM_](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances?WT.mc_id=AZ-MVP-5004796#azure-provided-name-resolution "Name resolution for resources in Azure virtual networks"){:target="_blank"} _or VPN)_; mainly if you operate Cloud-only services and don't have an external DNS provider, such as Active Directory - connecting to [private link](https://azure.microsoft.com/services/private-link/?WT.mc_id=AZ-MVP-5004796 "Private Link"){:target="_blank"} resources, you may have to edit your local host's file and override local DNS to point to the IP of the [private endpoint](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview?WT.mc_id=AZ-MVP-5004796){:target="_blank"} for each service.

This is not sustainable, not scalable, and you might end up throwing your hands in the air and switching back to public-facing services and just whitelisting other users' Public IPs to gain access to Azure resources - which can lead to its own set of issues, such as unmanaged IPs left with access to resources after contractors or users leave or have finished their work, IP address changes if not managed correctly can allow any user or company to have a direct line of sight to your company resources.

### Overview

> Today we will concentrate on DNS resolution of Private Endpoints, using [Azure DNS Private Resolver](https://docs.microsoft.com/azure/dns/dns-private-resolver-overview?WT.mc_id=AZ-MVP-5004796 "What is Azure DNS Private Resolver?"){:target="_blank"} as a DNS proxy when connecting to Azure using a [Point to Site VPN](https://docs.microsoft.com/azure/vpn-gateway/point-to-site-about?WT.mc_id=AZ-MVP-5004796 "About Point-to-Site VPN"){:target="_blank"}.

For this article, I assume you have an Azure Point to Site already set up; if you don't, you can refer to a previous article I wrote for [Creating an Azure Point to Site VPN using Azure Active Directory authentication](https://luke.geek.nz/azure/create-azure-point-to-site-vpn-using-azure-active-directory-authentication/ "Create Azure Point to Site VPN using Azure Active Directory authentication"){:target="_blank"}.

_Disclaimer: Azure Private DNS Resolver is still in Public Preview at the time of this article (02/09/2022). If you aim to use this in a Production scenario, functionality and services may change. This also means there are current_ [_regional restrictions_](https://docs.microsoft.com/en-us/azure/dns/dns-private-resolver-overview?WT.mc_id=AZ-MVP-5004796#regional-availability "Regional availability"){:target="_blank"}_, and Azure Private DNS Resolver is not currently available in all regions._

#### So what is Azure DNS Resolver?

> Azure DNS private resolver is a cloud-native, highly available, and DevOps-friendly service. It provides a simple, zero-maintenance, reliable, and secure Domain Name System (DNS) service to resolve and conditionally forward DNS queries from a virtual network, on-premises, and to other target DNS servers without the need to create and manage a custom DNS solution. Resolve DNS names hosted in Azure Private DNS Zones from on-premises networks as well as DNS queries for your own domain names. This will make your DNS infrastructure work privately and seamlessly across on-premises networks and enable key hybrid networking scenarios.

![Azure Private DNS Resolver](/uploads/azureprivatednsresolver.png "Azure Private DNS Resolver")

Customers will no longer need to provision IaaS-based solutions on their virtual networks to resolve names registered on Azure Private DNS Zones and can do conditional forwarding of domains back to on-premises, across multi-cloud providers, and public DNS servers.

This solution can work with your Azure ExpressRoute, Azure VPN, or Azure Bastion setup.

![Azure Private DNS Resolver](/uploads/dns-private-resolver.png "Azure Private DNS Resolver")

#### Inbound or Outbound?

Name resolution queries for Azure workloads from the on-premises network are conditionally forwarded to the Azure DNS private resolver inbound endpoint, which enables you to perform name resolution of workloads registered on Azure Private DNS Zones from on-premises.

| Inbound Endpoint | Azure DNS private resolver inbound endpoint that receives the name resolution request from Azure & on-premises network and resolve names. |
| --- | --- |
| Outbound Endpoint | Azure DNS private resolver outbound endpoint conditionally forwards the request to on-premises or other target DNS servers. |

The Azure DNS private resolver inbound endpoint has a private IP that is part of a subnet where the endpoint has been created. The IP address of the DNS private resolver inbound endpoint is then set as a DNS server on the on-premises network.

Azure DNS private resolver outbound endpoint conditionally forwards the request to on-premises or other target DNS servers.

**Today, we will connect to private endpoints to concentrate on the Inbound functionality of Azure Private DNS Resolver.**

### Deployment

To deploy Azure Private DNS Resolver, we will need a few things.

* A Virtual Network
* A [subnet](https://docs.microsoft.com/en-us/azure/dns/dns-private-resolver-overview#subnet-restrictions "Subnet restrictions"){:target="_blank"} dedicated to resolving DNS queries _(/28)_
* A private endpoint _(i.e. Storage Account, SQL Database)_ is linked to the virtual network.

#### Deploy DNS Private Resolver

_I assume you already have a Virtual Network tied to your Virtual Network gateway as part of the '_[_Point to Site VPN_](https://luke.geek.nz/azure/create-azure-point-to-site-vpn-using-azure-active-directory-authentication/ "Create Azure Point to Site VPN using Azure Active Directory authentication "){:target="_blank"}_' setup._

 1. Open the **Azure Portal**
 2. Click on **+ Create a resource**
 3. Type in: **DNS Private Resolver**
 4. ![Azure DNS Private Resolver](/uploads/azureportal_creatednsprivateresolver.png "Azure DNS Private Resolver")
 5. Click **Create**
 6. Select your **Subscription**
 7. Select your **Resource Group** _(I recommend placing the DNS Private Resolver in the same resource group as your Virtual Network - but place this service in a Resource Group that makes sense for your environment, i.e. shared services or a specific network team resource group)_
 8. Type in a **name** for your DNS Private Resolver _(this is a regional service, but the name does not need a globally unique )_
 9. **Select** your **region** _(this needs to be the same region as the Virtual Network)_
10. Select your **Virtual Network** _(the same Virtual Network that has your Virtual Network Gateway for the Point to Site VPN and your Private endpoints)_
11. ![Create Azure Private DNS Resolver](/uploads/azureportal_creatednsprivateresolverinitialpane.png "Create Azure Private DNS Resolver")
12. Click **Next: Inbound Endpoints >**
13. Now its time to add our Inbound Endpoint and create the Private DNS Resolver Subnet, click **+ Add an endpoint**
14. Type in your **endpoint name** (_for example, InboundEndpoint)_
15. If you have already created a subnet, select it - else, click **Create New**
16. Enter in your subnet name and address range
17. Click **Save**
18. ![Private DNS Resolver create subnet](/uploads/azureportal_creatednsprivateresolversubnet.png "Private DNS Resolver create subnet")
19. Click **Review + Create**
20. Click **Create**

#### Adjust Point to Site DNS

Now that the DNS Resolver has been created, with an inbound endpoint, allowing the lookup of private endpoints, we need to add the Private Resolver DNS relay to our point-to-site VPN configuration; first, we need the newly created private IP of the inbound endpoint.

 1. Navigate to the [**DNS Private Resolver**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FdnsResolvers "DNS Private Resolvers"){:target="_blank"} in the Azure Portal
 2. **Open** your DNS Private **Resolver service**
 3. Click on **Inbound Endpoints**
 4. Make a note of the **private IP** of your inbound endpoint.
 5. ![Private DNS Resolver](/uploads/azureportal_creatednsprivateresolverinboundendpointip.png "Private DNS Resolver")
 6. Now that the Private Inbound resolver has been configured, we need to add the DNS relay into our Azure VPN configuration so that our DNS queries will respond with a private endpoint; you will need to modify the '[azurevpnconfig.xml](https://docs.microsoft.com/en-us/azure/vpn-gateway/about-vpn-profile-download?WT.mc_id=AZ-MVP-5004796#generate "Generate profile files"){:target="_blank"}' file and reimport the VPN.
 7. Right-click 'azurevpnconfig.xml' and edit in Notepad or Visual Studio Code
 8. Under: </serverlist>
 9. **Add** _(replace the IP listed below with the IP of your Inbound endpoint copied earlier)_:

        <clientconfig>
        <dnsservers>
        <dnsserver>10.0.18.4</dnsserver>
        </dnsservers>
        </clientconfig>
10. **Save** and **reimport** to the Azure VPN Client
11. Once connected, ping a resource behind a private endpoint, and you should get the private IP of that resource back and should be able to connect to that resource privately.
12. ![Azure Private DNS Resolver ping](/uploads/azurevpn_testprivateendpoint.png "Azure Private DNS Resolver ping")

Any future or current private endpoints linked to the same Virtual Network will instantly be accessible without additional changes on the Azure VPN client.

### Additional resources

The third-party resources below include reading and learning about the Azure Private DNS Resolver.

* [Quickstart: Create an Azure private DNS Resolver using the Azure portal](https://docs.microsoft.com/en-us/azure/dns/dns-private-resolver-get-started-portal?WT.mc_id=AZ-MVP-5004796 "Quickstart: Create an Azure private DNS Resolver using the Azure portal"){:target="_blank"}
* [Intro to Azure DNS Private Resolver](https://docs.microsoft.com/en-us/learn/modules/intro-to-azure-dns-private-resolver/?WT.mc_id=AZ-MVP-5004796 "Intro to Azure DNS Private Resolver"){:target="_blank"}
* [Azure DNS Private Resolver - MicroHack](https://github.com/dawlysd/azure-dns-private-resolver-microhack "Azure DNS Private Resolver - MicroHack"){:target="_blank"}
* My Azure Bicep export for reference:

`        param dnsResolvers_PrivateDNSResolver_name string = 'PrivateDNSResolver'
param virtualNetworks_vnettest_externalid string = '/subscriptions/1f0d1466-208f-4810-bb90-8af1b404d549/resourceGroups/pointtositetest/providers/Microsoft.Network/virtualNetworks/vnettest'

resource dnsResolvers_PrivateDNSResolver_name_resource 'Microsoft.Network/dnsResolvers@2020-04-01-preview' = {
  name: dnsResolvers_PrivateDNSResolver_name
  location: 'australiaeast'
  properties: {
    virtualNetwork: {
      id: virtualNetworks_vnettest_externalid
    }
  }
}

resource dnsResolvers_PrivateDNSResolver_name_InboundEndpoint 'Microsoft.Network/dnsResolvers/inboundEndpoints@2020-04-01-preview' = {
  parent: dnsResolvers_PrivateDNSResolver_name_resource
  name: 'InboundEndpoint'
  location: 'australiaeast'
  properties: {
    ipConfigurations: [
      {
        subnet: {
          id: '${virtualNetworks_vnettest_externalid}/subnets/dnsresolvesubnet'
        }
        privateIpAddress: '10.0.18.4'
        privateIpAllocationMethod: 'Dynamic'
      }
    ]
  }
}`
