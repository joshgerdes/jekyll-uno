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

> The Azure Bastion service is a fully platform-managed PaaS service you provision inside your virtual network. It provides secure and seamless RDP/SSH connectivity to your virtual machines directly from the Azure portal over TLS.

Because of this, if you don't have line-of-sight access to your Virtual Machines (_via express route, Site-to-Site VPN etc.)_, Bastion becomes your jump box, allowing secure access to your virtual machines without needing a public IP.

There is a downside, though. To connect to a Virtual Machine secured by Bastion, you need access to the Azure Portal, or command line connectivity to Azure, to create the tunnel; this means that you may need to grant people elevated rights and access they may not need to connect.

As of November 2022[,]() Microsoft introduced shareable links into public preview, solving two key pain points:

* Administrators will no longer have to provide full access to their Azure accounts to one-time VM users—helping to maintain their privacy and security.
* Users without Azure subscriptions can seamlessly connect to VMs without exposing RDP/SSH ports to the public internet.

> The Bastion **Shareable Link** feature lets users connect to a target resource (virtual machine or virtual machine scale set) using Azure Bastion without accessing the Azure portal. 