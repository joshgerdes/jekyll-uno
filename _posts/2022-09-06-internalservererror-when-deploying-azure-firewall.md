---
date: 2022-09-06 00:00:00 +1200
title: InternalServerError when deploying Azure Firewall
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/deploymentfailedazurefirewall.png"

---
When attempting to deploy an [Azure Firewall](https://docs.microsoft.com/en-us/azure/firewall/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Firewall?"){:target="_blank"}, you may get an error: Conflict, DeploymentFailed error. This error can occur when you have an expressroute connection, and the Firewall is not deployed in Force Tunneled mode, as the routes from the BGP link will be replacing the default Azure internet route, required for the Azure Firewall.

    "code": "InternalServerError",
    "message": "An error occurred."

![Deployment Failed - Azure Firewall](/uploads/deploymentfailedazurefirewall.png "Deployment Failed - Azure Firewall")

If you click Input in the deployment, you may notice your vnetName, vnetAddressSpace and subnetAddressSpace are blank.

![Azure Firewall deployment](/uploads/deploymentfailedazurefirewallinputs.png "Azure Firewall deployment")

Even though the Azure Firewall will appear as deployed. You will notice that it won't have a Private IP assigned.

To resolve this error:

1. **Delete** the **Azure Firewall** that has been **partially deployed**
2. **Create** a **[User Defined route]**(https://docs.microsoft.com/en-us/azure/virtual-network/manage-route-table?WT.mc_id=AZ-MVP-5004796 "Create, change, or delete a route table"){:target="_blank"} for the internet:

| Name | Address Prefix | Next hop type |
| --- | --- | --- |
| Internet | 0.0.0.0/0 | Internet |

1. Link it to the **AzureFirewallSubnet**
2. **Redeploy**

This error may occur as your internet route may flow via BGP routes from on-premises; the user-defined route will override this route.
