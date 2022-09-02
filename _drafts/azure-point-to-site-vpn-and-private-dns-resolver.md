---
date: 2022-09-02 00:00:00 +1200
title: Azure Point to Site VPN and Private DNS Resolver
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
You might access resources such as Azure SQL databases or Azure Storage accounts if you're connecting to a Microsoft Azure network; if you operate Cloud-only services and don't have an external DNS provider, such as Active Directory - connecting to private link resources, you may have to edit your local host's file, and override local DNS to point to the IP of the private endpoint for each service.

This is not sustainable, not scaleable, and you might end up switching back to Public facing services and just whitelisting your and other users' Public IPs to gain access to Azure resources.