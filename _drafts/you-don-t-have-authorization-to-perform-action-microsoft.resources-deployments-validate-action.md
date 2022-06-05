---
date: 2022-06-06 00:00:00 +1200
title: You don’t have authorization to perform action 'Microsoft.Resources/deployments/validate/action'.
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
You may be attempting to deploy an Azure Landing Zone, such as the Enterprise Scale Landing Zone and receive the following error:

> You don’t have authorization to perform action 'Microsoft.Resources/deployments/validate/action'.

This is because by default, even if you have Owner right on an Azure subscription, and are a Global Administer, you are unable to assign rights at the root '/' tenant level, to be able to create new Management Groups and move subscriptions between them.

However, users who have the Global Azure Active Directory role can elevate rights to do this.  There are a few steps to enabling this, including using [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/what-is-azure-powershell?WT.mc_id=AZ-MVP-5004796 "Azure PowerShell") to assign rights.

With an account with Global Administrator rights, do the following:

1. Sign in to the **Azure Portal**
2. Open **Azure Active Directory**
3. Click **Properties**
4. Toggle the '**Access management for Azure resources**' to '**Yes**'
5. Click **Save**
6. Open **PowerShell**
7. Run

    Connect-AzAccount
    
8. Run
