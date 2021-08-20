---
date: 2021-08-21 00:00:00 +1200
title: Update-AdmPwdAdSchema: The requested attribute does not exist
author: Luke
categories:
- PowerShell
toc: false
header:
  teaser: "images/powershell-blog-feature-banner.png"

---
Are you attempting to update the Active Directory Schema for LAPS (Local Administrator Password Solution) and keep getting the error below?

**Update-AdmPwdAdSchema: The requested attribute does not exist**

Here are few things you can check:

* Make sure you are a Schema Admin
* Run PowerShell as Administrator
* Run the PowerShell to update the schema directly from the Schema Master

You can use the snippet below to check which Domain Controller the Schema Master role is running from:

    Get-ADDomainController -Filter * | Select-Object Name, Domain, Forest, OperationMasterRoles | Where-Object {$_.OperationMasterRoles}