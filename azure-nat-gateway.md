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
* Virtual Machine Scale Set with 4 instances (each with Windows Server 2019)

_Note: Each VM has RDP opened to allow inbound traffic from my network using the Public IP, and a NAT rule allowing RDP traffic on the Load Balancer. There is no point-to-site or site-to-site VPN, RDP connections are directly over the internet to Australia East, from New Zealand._

I had connectivity to all 3 VMs at the same time.

![NAT Gateway - Test](/uploads/natgw_test.png "NAT Gateway - Test") 

Once the resources were created, I then connected to each machine using RDP/SSH on their Public IP address and tested:

### Linux Machine with Public IP for RDP

* Inbound Public IP: 20.53.92.19
* Outbound IP: 20.53.73.184

![Linux Azure NAT Gateway](/uploads/linux_ubuntu_nat_test.png "Linux Azure NAT Gateway")

As you can see, I had connected to the public IP of the Linux VM via SSH and did a curl to: [https://ifconfig.me/](https://ifconfig.me/ "https://ifconfig.me/") to grab my public IP. The public IP of my Linux box was my NAT Gateway Public IP prefix!

### Windows Machine with Public IP for RDP

* Inbound Public IP: 20.70.228.211
* Outbound IP: 20.53.73.184

![Windows Azure NAT Gateway](/uploads/window_nat_test.png "Windows Azure NAT Gateway")

Using RDP to the public IP of the Windows Server, I navigated to: [https://www.whatismyip.com/](https://www.whatismyip.com/  "https://www.whatismyip.com/"), as you can see the Public IP of my outbound IP address was my NAT Gateway Public IP prefix!

### Windows Machine behind an Azure Load Balancer

* Inbound Public IP: 20.211.100.67
* Outbound IP: 20.53.73.185

![](/uploads/windows_nat_test_loadbalancer.png)

This was the last of the 3 test machines, I stood up. Using RDP to the public IP of the Azure Load BalancerI navigated to: [https://www.whatismyip.com/](https://www.whatismyip.com/ "https://www.whatismyip.com/"), as you can see the Public IP of my outbound IP address was my NAT Gateway Public IP prefix, however, this was '20.53.73.18**5**', which was the second IP address available in my /31 IP address prefix.

### Windows Machine behind a VM Scale Set

Although, not in the diagram, I decided to add a VM Scale Set of 4 Virtual Machines into my testing _(to save on cost they are just Standard_B2ms machines but more than enough for my testing)_.

![Azure NAT Gateway - VM Scale Set](/uploads/vmss_nat_test.png "Azure NAT Gateway - VM Scale Set")

As you can see from the mess that is my screenshot above, all machines had completely different inbound Public IP addresses, but the outbound public IP addresses came from the NAT Gateway as expected.

### Findings and Observations

* The outbound public IP did seem to change between the workloads if I refreshed '_whatismyip_' and '_ifconfig_', the public IP changed between 184 and 185, although no loss of connectivity occurred to the Virtual Machines. This was linked to the '4-minute idle timeout' configured on the NAT Gateway, I saw no reason to change the default timeout value, if I was that worried about the exact same IP address - I would have chosen with a Public IP vs a Public IP prefix on the NAT Gateway.
* Any Public IP that is used on the same subnet as a NAT Gateway, needs to be Standard.
* If I had both a Public IP address and a Public IP prefix on my NAT gateway, the Prefix seemed to take precedence.
* A single [NAT gateway resource](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-gateway-resource) supports from 64,000 up to 1 million concurrent flows. Each IP address provides 64,000 SNAT ports to the available inventory. You can use up to 16 IP addresses per NAT gateway resource. The SNAT mechanism is described [here](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-gateway-resource#source-network-address-translation) in more detail.

## Create a NAT Gateway

To create my NAT Gateway, I used the ARM Quickstart template, located here: [https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template "https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/quickstart-create-nat-gateway-template")

Then I created the additional Virtual Machines and Load Balancers and added them to the same VNET created as part of the NAT Gateway.

To create a NAT Gateway using the Azure Portal

1. Log in to the **Azure Portal** and navigate to **Create a resource**, **NAT Gateway** (this link will get you there: [Create-NATGateway](https://portal.azure.com/#create/Microsoft.NatGateway-ARM "Create network address translation (NAT) gateway")).
2. Select your **Subscription**
3. **Enter** your NAT **Gateway name**
4. Enter your **Region**
5. Enter your availability zone
6. Set your idle timeout _(I suggest leaving this at 4 minutes, you can change it later if it presents issues)_

![](/uploads/create_natgateway1.png)

7. Click Next: Outbound IP

## Resources

* [What is Virtual Network NAT?]()


* [Design Virtual Networks that use NAT gateway resources]()