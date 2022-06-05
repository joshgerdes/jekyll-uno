---
date: 2022-06-06 00:00:00 +1200
title: You don’t have authorization to perform action 'Microsoft.Resources/deployments/validate/action'.
author: Luke
categories:
- Azure
toc: false
header:
  teaser: images/iazure-marketplace-banner.png

---
You may be attempting to deploy an Azure Landing Zone, such as the Enterprise Scale Landing Zone and receive the following error:

> You don’t have authorization to perform action 'Microsoft.Resources/deployments/validate/action'.

This is because by default, even if you have Owner right on an Azure subscription, and are a Global Administer, you are unable to assign rights at the root '/' tenant level, to be able to create new Management Groups and move subscriptions between them.

However, users who have the Global Azure Active Directory role can elevate rights to do this.  There are a few steps to enabling this, including using [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/what-is-azure-powershell?WT.mc_id=AZ-MVP-5004796 "Azure PowerShell"){:target="_blank"} to assign rights.

With an account with Global Administrator rights, do the following:

 1. Sign in to the **Azure Portal**
 2. Open **Azure Active Directory**
 3. Click **Properties**
 4. Toggle the '**Access management for Azure resources**' to '**Yes**'
 5. Click **Save**
 6. Open **PowerShell**
 7. **Run:**

        Connect-AzAccount
 8. Login with your **account**, and make sure you are in the correct directory _(if you aren't you can use Connect-Az Account - tenantid 'tenantidhere')_.
 9. **Type**:

        Get-AzADUser
10. **Copy** the **ID** of the user you are logged in as, and **run** the following _(replace the ObjectId to match the ID of your user)_:

        $user =  Get-AzADUser -ObjectId f53eaa59-0fc0-4103-b9cb-1650e3069da8
11. Once the user ID has been stored in a variable, its finally time to assign the rights, **run** the following:

        New-AzRoleAssignment -Scope '/' -RoleDefinitionName 'Owner' -ObjectId $user.Id
12. Give Azure Active Directory **10-15 minutes** to **replicate** the Azure AD changes, **log out** and **back in** and you should now be able to **deploy** the **Landing Zone**.

**Note: Remember to go back and change the toggle to 'Allow management of Azure resources' to 'No', or all Global Administrators of Azure Active Directory will be able to manage all Azure resources.**

**Once the Landing Zone is deployed, you should also remove your role assignment at the root level by running:**

    Remove-AzRoleAssignment -Scope '/' -RoleDefinitionName 'Owner' -ObjectId $user.Id
