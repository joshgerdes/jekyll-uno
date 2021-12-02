---
date: 2021-12-03 00:00:00 +1300
title: Azure NAT Gateway
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''
published: false

---
## Overview

With most Cloud resources being accessible over the internet, each publically accessible resource has its own public IP address, this makes it a lot more difficult to administer the security and access rules to access third party services _(think along the lines of - you or your organisation might use software-as-a-service CRM product and that product is only accessible from your organisations IP for compliance/security reasons, you might access the CRM product from various Azure Virtual Desktop hosts, each with its own public IP, or you want to control Multifactor authentication for users using Azure services)_.

The administration of this, particularly in scenarios where others may be enabled to create and manage resources can be difficult, sure you can use Standard Load Balancers which would help, but you have to manage and pay for it.

Tunnelling outbound traffic through to a specific IP address or IP addresses to _'known controllable IP addresses_' for Azure resources _(both IaaS and PaaS)_ which sit in the same Virtual Network is where the Azure NAT Gateway comes in, allowing you to easily whitelist and control what IPs your traffic is coming from.

"The Azure NAT gateway is a fully managed, highly resilient service built into the Azure fabric, which can be associated with one or more subnets in the same Virtual Network, that ensures that all outbound Internet-facing traffic will be routed through the gateway. The NAT gateway gives you a static predictable public IP for outbound Internet-facing traffic. It also significantly increases the available [SNAT ports](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-intermittent-outbound-connection-errors) in scenarios where you have a high number of concurrent connections to the same public address/port combination."

## My Testing

Knowing that the Azure NAT gateway existed, and could in theory solve some issues I may run into wasn't enough! I wanted to get hands-on and actually test that it would work - the way I thought it would, so I wanted to test it, in order to test a NAT Gateway, I created:

* Virtual Network
* NAT Gateway
* IP Public Address prefix
* 1 Windows VM (Windows Server 2019) with Public IP
* 1 Linux (Ubuntu 18.04) VM with Public IP
* 1 Windows VM (Windows Server 2019) as a backend pool for an Azure Load Balancer

_Note: Each VM has RDP opened to allow inbound traffic from my network using the Public IP, and a NAT rule allowing RDP traffic on the Load Balancer._

![NAT Gateway - Test](/uploads/natgw_test.png "NAT Gateway - Test") 

## Create a NAT Gateway

To create my NAT Gateway, I used the ARM Quickstart template, located here: [https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template "https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template")

Then I created the additional Virtual Machines and Load Balancers and added it to the same VNET created as part of the NAT Gateway.

## Resources

* [What is Virtual Network NAT?]()


* [Design Virtual Networks that use NAT gateway resources]()