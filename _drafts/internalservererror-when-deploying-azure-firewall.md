---
date: 2022-09-06 00:00:00 +1200
title: InternalServerError when deploying Azure Firewall
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
When attempting to deploy an [Azure Firewall](https://docs.microsoft.com/en-us/azure/firewall/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Firewall?"), you may get a error: Conflict, DeploymentFailed error.

    "code": "InternalServerError",
    "message": "An error occurred."

![Deployment Failed - Azure Firewall](/uploads/deploymentfailedazurefirewall.png "Deployment Failed - Azure Firewall")

If you click Input in the deployment, you may notice your vnetName, vnetAddressSpace and subnetAddressSpace are blank.

![Azure Firewall deployment](/uploads/deploymentfailedazurefirewallinputs.png "Azure Firewall deployment")

Even though the Azure Firewall, will appear as deployed. You will notice that it won't have a Private IP assigned.

To resolve this error:

1. **Delete** the **Azure Firewall** that has been **partially deployed**
2. **Create** a **User Defined route**:

| Name | Address Prefix | Next hop type |
| --- | --- | --- |
| Internet | 0.0.0.0/0 | Internet |

1. Link it to the **AzureFirewallSubnet**
2. **Redeploy**

This error may occur as your internet route may be flowing via BGP routes from on-premises.