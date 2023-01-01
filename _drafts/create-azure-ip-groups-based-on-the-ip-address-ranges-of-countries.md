---
date: 2023-01-01 00:00:00 +1300
title: Create Azure IP Groups based on the IP address ranges of countries
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
An [IP Group](https://learn.microsoft.com/azure/firewall/ip-groups?WT.mc_id=AZ-MVP-5004796 "IP Groups in Azure Firewall") in Microsoft Azure can be used as a logical container of IP address ranges for private and public addresses.

> IP Groups allow you to group and manage IP addresses for Azure Firewall rules in the following ways:
>
> * As a source address in DNAT rules
> * As a source or destination address in network rules
> * As a source address in application rules
>
> An IP Group can have a single IP address, multiple IP addresses, one or more IP address ranges or addresses and ranges in combination.

The IP Group allows you to define an IP address that can be used in conjunction with Azure Firewall, to allow or deny internal or external traffic from a perspective set of IP addresses.

> The following IPv4 address format examples are valid to use in IP Groups:
>
> * Single address: 10.0.0.0
> * CIDR notation: 10.1.0.0/32
> * Address range: 10.2.0.0-10.2.0.31

By default, the Azure Firewall blocks 