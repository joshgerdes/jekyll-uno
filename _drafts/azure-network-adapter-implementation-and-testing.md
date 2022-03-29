---
date: 2022-03-29 00:00:00 +1300
title: Azure Network Adapter - Implementation and Testing
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Azure Network Adapter, introduced in Windows Server 2019 _(and available in Windows Server 2022)_, allows standalone servers access to Microsoft Azure, by creating a Point-to-Site connection into an Azure Virtual Network.

Although most organisations will implement expressroute or site-to-site connectivity through a physical or NVA _(Network Virtual Appliance)_ firewall or router, there may be times when you want to limit connectivity, stand up a PoC _(Proof of Concept)_ or need access to Azure services on a single server only, which is where the Azure Network Adapter comes into play.