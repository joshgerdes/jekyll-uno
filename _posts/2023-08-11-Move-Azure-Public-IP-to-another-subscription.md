---
title: Move an Azure public IP to another subscription
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/PublicIP_MoveAnotherSub.png
date: '2023-08-11 00:00:00 +1300'
---

You can move a [Public IP](https://learn.microsoft.com/azure/virtual-network/ip-services/public-ip-addresses?WT.mc_id=AZ-MVP-5004796){:target="_blank"} address in Microsoft Azure, to a new Subscription (BUT NOT A [DIFFERENT REGION](https://learn.microsoft.com/azure/virtual-network/move-across-regions-publicip-portal?WT.mc_id=AZ-MVP-5004796){:target="_blank"}).

There are some limitations as below:

> You can't move a VPN Gateway that is associated with a Standard SKU public IP address to a new subscription.
> Azure Public IPs are region specific and can't be moved from one region to another.

Some resources aren't [supported](https://learn.microsoft.com/azure/azure-resource-manager/management/move-support-resources?WT.mc_id=AZ-MVP-5004796#microsoftnetwork){:target="_blank"} to be moved, but a Public IP is.

Before you move the Public IP, make sure its dissociated (unattached) from a resource.

![Dissociate IP](/images/posts/PublicIP_dissociate.png)

Then once dissociated, you can trigger the move.

![Dissociate IP](/images/posts/PublicIP_MoveAnotherSub.png)
