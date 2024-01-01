---
title: Mastering CIDRs With Azure Bicep
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: /images/posts/BlogHeading_Mastering-CIDRs-with-Azure-Bicep.gif
date: 2023-11-18 00:00:00 +1300
slug: azure/Working-with-CIDR-Azure-Bicep
---

[Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) *(CIDR)* is a method of allocating IP addresses and routing Internet Protocol *(IP)* packets.

![Mastering CIDRs With Azure Bicep](/images/posts/BlogHeading_Mastering-CIDRs-with-Azure-Bicep.gif)

This article includes sample Bicep functions for working with CIDR, for Azure Virtual Network and Subnet creation.

<!-- truncate -->


    // This function parses the CIDR notation and returns an object with the network address, subnet mask, and other details.
    output v6addressspace object = parseCidr('2001:db8:1234::/48')

    // This function generates an array of subnets within the specified CIDR block. The subnet size is 64, and the index calculates the subnet.
    // The 'range(0, 5)' function generates an array of numbers from 0 to 4. The 'for' loop iterates over these numbers.
    // For each number 'i', the 'cidrSubnet' function calculates a subnet within the '2001:db8:1234::/48' CIDR block.
    // The subnet size is 64, and 'i' is used as the index. The resulting array contains the calculated subnets.
    output v6subnets array = [for i in range(0, 5): cidrSubnet('2001:db8:1234::/48', 64, i)]

    // This function generates an array of host addresses within the specified CIDR block. The index is used to calculate the host address.
    // Similar to the 'v6subnets' array, the 'range(0, 5)' function generates an array of numbers from 0 to 4.
    // For each number 'i', the 'cidrHost' function calculates a host address within the '2001:db8:1234::/48' CIDR block.
    // The resulting array contains the calculated host addresses.
    output v6hosts array = [for i in range(0, 5): cidrHost('2001:db8:1234::/48', i)]

    // This function generates a string within the specified CIDR block. The host index is always 3 (Azure Reserved).
    // The 'cidrHost' function calculates a host address within the '2001:db8:1234::/48' CIDR block.
    // The host index is '0 + 3', which is 3. This is because the first three addresses in a subnet are reserved in Azure.
    output v6hostsazure string = cidrHost('2001:db8:1234::/48', 0 + 3)

References:

* [IPv6 in Microsoft Azure](https://luke.geek.nz/azure/IPv6-on-Azure/)
* [CIDR functions for Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/bicep-functions-cidr?WT.mc_id=AZ-MVP-5004796)
* [CIDR math functions for Azure Networking calculations #3975](https://github.com/Azure/bicep/issues/3975)
