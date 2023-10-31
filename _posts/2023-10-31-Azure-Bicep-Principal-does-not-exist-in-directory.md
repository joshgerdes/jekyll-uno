---
title: Azure Bicep - Principal does not exist in directory
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlogHeading-PrincipalNotFound.gif
date: 2023-10-31 00:00:00 +1300
keywords:
  - azure
  - bicep
  - identity
  - PrincpalNotFound
description: PrincpalNotFound when doing Role Assignment of a User Assigned Managed identity
slug: PrincpalNotFound-bicep-roleassignment
---

Recently, I was deploying an [User Assigned Managed identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp&WT.mc_id=AZ-MVP-5004796), and assigning the managed identity a role assignment with Azure Bicep, and ran into an issue, where the assignment would fail, but then after a rerun would work.

> Principal e892476361114c90be141d9bf20cc94b does not exist in the directory 73160ae1-aa4a-48b5-a424-d5e43d808f53. Check that you have the correct principal ID. If you are creating this principal and then immediately assigning a role, this error might be related to a replication delay. In this case, set the role assignment principalType property to a value, such as ServicePrincipal, User, or Group. See [https://aka.ms/docs-principaltype](https://learn.microsoft.com/azure/role-based-access-control/troubleshooting?tabs=bicep&WT.mc_id=AZ-MVP-5004796)

![PrincpalNotFound](/images/posts/PrincipalNotExistinDirectory.png)

What was happening, was that the User Assigned Identity was created, and immediately after the role assignment was attempted, leaving no time for the role assignment API to be aware that the User Assigned Managed identity existed, even with a hard coded dependson!

The fix was to Set the: [principalType](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/scenarios-rbac?WT.mc_id=AZ-MVP-5004796#principal) into the Bicep, as ServicePrincipal, making sure that the Azure platform can wait for the replication to complete, before trying the role assignment.

> The principalType property specifies whether the principal is a user, a group, or a service principal. Managed identities are a form of service principal.


``` bicep

resource uami 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: azUserAssignedManagedIdentity
  location: location
}

resource uamiassignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(resourceGroup().id, 'contributor')
  properties: {
    principalId: uami.properties.principalId
    principalType: 'ServicePrincipal' 
    roleDefinitionId: resourceId('Microsoft.Authorization/roleDefinitions', 'b24988ac-6180-42a0-ab88-20f7382dd24c') // Contributor
  }
  scope: resourceGroup()
}


```
