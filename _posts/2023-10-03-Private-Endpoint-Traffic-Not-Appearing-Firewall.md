---
title: Private Endpoint traffic not appearing in Azure Firewall
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/BlobHeading_PrivateEndpointtrafficnotappearing.gif
date: 2023-10-03 00:00:00 +1300
keywords:
  - azure
  - firewall
  - private endpoint
slug: private-endpoint-traffic-not-appearing-azure-firewall
description: Private Endpoint traffic can take a different route than your standard traffic and cause some confusion and dropped packets.
---

You may have a situation where you have implemented [Private endpoints](https://learn.microsoft.com/azure/private-link/private-endpoint-overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"} and the traffic from on-premises to those Private Endpoints, either doesn't work, even though on-premises firewalls say otherwise, or is working, but doesn't appear in the Azure Firewall.

I had this recently with [Azure Arc](https://learn.microsoft.com/azure/azure-arc/overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"}, where the endpoints failed to connect once a site-to-site VPN connection _(which was working)_ was replaced with an expressroute connection, but going through the Azure Firewall logs, was unable to see any 443 traffic for Arc, hitting the Firewall even when the connection was working.

![Private Endpoint traffic not appearing in Azure Firewall](/images/posts/BlobHeading_PrivateEndpointtrafficnotappearing.gif)

> Traffic flow: Onpremises -- (ER Circuit) -- ER gateway -- Secured hub Azure Firewall -- (Vnet Connection) -- PE (Private Endpoint)

The issue was related to how private endpoint traffic is routed differently.

If the traffic has reached the Expressroute gateway from on-premises, with routing intent, normal traffic will be forced to the AzFW first before reaching its destination, as you would think and expect.

> However, for the private endpoint scenario, once a Private Endpoint is deployed to any VNET, there will be an automatic system route with the PE IP and prefix /32 installed on all of the linked NICs.
> The next hop for this route will be InterfaceEndpoint.
> This route will allow the traffic to go directly to the PE, bypassing the routing intent and other user-defined routes that are larger than /32. The /32 route propagates to these areas: Any VPN or ExpressRoute connection to an on-premises system.

See: [Considerations for Hub and Spoke topology](https://learn.microsoft.com/en-us/azure/architecture/guide/networking/private-link-hub-spoke-network?WT.mc_id=AZ-MVP-5004796#considerations){:target="*blank"}.

In an Azure Virtual Wide Area Network (VWAN), you could see this route in the virtual hub [effective routes](https://learn.microsoft.com/azure/virtual-wan/effective-routes-virtual-hub?WT.mc_id=AZ-MVP-5004796){:target="*blank"} and which gets propagated to the expressroute gateway.

My traffic from on-premises to the Azure Arc went directly to the private endpoints (bypassing the Azure Firewall). Still, the route back via the Azure Firewall was completely different, leading to asymmetric routing _(a packet traverses from a source to a destination in one path and takes a different path when it returns to the source)_.

**To resolve this**, we need to enable network security policies for User-Defined Routes on the subnet of the private endpoint(s):

![Azure Portal - Private Endpoint - Routes](/images/posts/AzurePortal_RouteTables_PrivateEndpoint.png)

Once enabled, you should see the traffic connect and flow through your Azure Firewall almost immediately.

Reference:

* [Manage network policies for private endpoints](https://learn.microsoft.com/azure/private-link/disable-private-endpoint-network-policy?tabs=network-policy-portal&WT.mc_id=AZ-MVP-5004796){:target="*blank"}
* [Secure traffic destined to private endpoints in Azure Virtual WAN](https://learn.microsoft.com/azure/firewall-manager/private-link-inspection-secure-virtual-hub?WT.mc_id=AZ-MVP-5004796){:target="*blank"}
