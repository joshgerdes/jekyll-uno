---
title: Entra ID login to a CIS Level 1 Ubuntu Azure Virtual Machine
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/ChangeDefaultManagementGroup.png
date: '2023-07-27 00:00:00 +1300'
---

Currently, [CIS](https://www.cisecurity.org/) (Center for Internet Security) [Azure Marketplace images](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=CIS&page=1?WT.mc_id=AZ-MVP-5004796), do not support being Entra ID (Azure Active Directory) Joined.

Although this article is about allowing Entra ID login to a Ubuntu machine, its worth noting the current decisions around Windows as well currently:

>'The Windows CIS Benchmarks are written for Active Directory domain-joined systems using Group Policy, not standalone/workgroup systems. Adjustments/tailoring to some recommendations will be needed to maintain functionality if attempting to implement CIS hardening on standalone systems or a system running in the cloud.
>'Currently, we do not support Azure Active Directory and it is not compatible with our EXISTING Hardened Images.

In fact when you, attempt to create a CIS Level 1 Ubuntu image in the Azure Portal, you get:

"This image does not support Login with Azure AD."

![CIS Image does not support Login with Azure AD](/images/posts/AzurePortal_CIS_Level1_Ubuntu_NoEntraIDLogin.png)

sd

