---
date: 2023-01-17 00:00:00 +1300
title: Azure Deployment cleanup with Azure DevOps
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Microsoft Azure has a limit of [800 deployments per resource group](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits?WT.mc_id=AZ-MVP-5004796#resource-group-limits "Resource group limits"). This means that a single resource group can only contain 800 historical deployments at most.

> A deployment in Azure refers to the process of creating or updating resources in a resource group.

When deploying resources in Azure, it is essential to keep track of the number of [historic deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history?tabs=azure-portal&WT.mc_id=AZ-MVP-5004796 "View deployment history with Azure Resource Manager") in a resource group to ensure that the limit is not exceeded. This is because new deployments will fail if the limit is exceeded, and creating or updating resources in that resource group will not be possible.

If you have CI/CD _(Continuous Integration and Continuous Deployment)_ set up to deploy or change your infrastructure or services with code, it can be easy to reach this limit.

To avoid exceeding the deployment limit, it may be necessary to clean up old deployments.

This can be done by using a script to remove deployments that are no longer needed.

So let's build an Azure DevOps pipeline that runs weekly to connect to our Microsoft Azure environment and clean up historical deployments.