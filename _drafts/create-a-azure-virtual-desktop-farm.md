---
date: 2021-06-27 00:00:00 +1200
title: How to create a Azure Virtual Desktop farm
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
## Overview

Previously known as Windows Virtual Desktop, [Azure Virtual Desktop](https://docs.microsoft.com/en-us/azure/virtual-desktop/overview "What is Azure Virtual Desktop?") is the successor of Microsoft Remote Desktop, although compatible with Server OS (Operating System), it is the first to support Windows 10 _(and soon Windows 11)_ multisession, reducing application compatibility issues and giving consistent user experience.

In this guide, I am going to run you through creating Azure Virtual Desktop from scratch, along with some prerequisites that will help you manage AVD after you create it.

Before I begin, I recommend reading the Azure Virtual Desktop Azure product page "[here](https://azure.microsoft.com/en-us/services/virtual-desktop/ " Azure Virtual Desktop -   Enable a secure remote desktop experience from virtually anywhere.")" to get an understanding of the pricing model,  Features and additional resources that could help you in your journey.

Before we begin, when selecting a region for your Session Hosts (Virtual Machines), I recommend you have a look at the: [Azure Virtual Desktop Experience Estimator](https://azure.microsoft.com/en-us/services/virtual-desktop/assessment/ " Azure Virtual Desktop Experience Estimator") to help valid the proper region for your Session Hosts and the round trip time _(I am in New Zealand, so my recommended region is: Australia East, which is what I will be using for this guide)_.

_If you don't already have a Microsoft Azure subscription, you can sign up for a Free subscription "_[_here_](https://azure.microsoft.com/en-us/free/ "Create your Azure free account today")_"._

Assuming you already have an Azure subscription and the appropriate access to create resources in that subscription, gets begin!

## Create Azure Active Directory Domain Services

1. Log in to the Azure Portal
2. Click on Create a resource
3. Search for: Azure AD Domain Services

_Note: You can change the Publisher Type to Microsoft, so it doesn't display any other marketplace offerings._

![](/uploads/azureaddssearch.png)

![](/uploads/azureaddsmarketplace.png)

4. Click Create
5. If you already have a Resource Group, select it - in this Demo, we are going to create one: aad_prod
6. Type in the DNS domain name - this is the FQDN of your domain, in my demo, I am going to choose: internal.luke.geek.nz.
7. Because I am in New Zealand, the closest region to me at the moment is Australia East, so that’s the region I am going to select, make sure you select the appropriate region for where your Azure Virtual Desktop workloads are.
8. Select the SKU and Resource Type, you can see the Pricing Calculator and the "Help Me choose.." links to verify your SKU and Forest type _(however in most cases, such as Azure Virtual Desktop, your Forest Type will be 'User')_. 

![](/uploads/adds_basics.png)

 9. Click Next
10. Now we will set up the Networking, if you have an already existing Virtual Network then select it

    _Azure AD Domain Services uses a dedicated subnet within a virtual network to hold all of its resources. If using an existing network, ensure that the network configuration does not block the ports required for Azure AD Domain Services to run._ [_Learn more_](https://docs.microsoft.com/azure/active-directory-domain-services/create-instance?WT.mc_id=Portal-Microsoft_AAD_DomainServices)
11. In my case, I am starting from scratch so will let it create a Virtual Network and its Subnet (/24), click Next

![](/uploads/adds_networking.png)

12. Azure AD Domain Services, will create a new Azure AD Group called: AAD DC Administrators - this group will be used for Administrator level permissions on the Azure AD Domain Services domain (it automatically adds the account you are using to create Azure AD Domain Services into this group). You can configure Membership of this group now and configure who gets alerted if there are issues with Azure AD Domain Services, when you are ready select Next

![](/uploads/adds_admin.png)

13. Depending on the amount of Azure Active Directory users you have in your organisation and whether they will need Azure AD Domain Services, you can choose to synchronise ALL Azure AD Groups and Users, or specific groups of users (this can be changed later), because my Azure AD Organisation is fairly low, I am going to Sync everything, click Next.

_One thing to note here is the recommendation on the number of Objects (Users, Groups) that will get synced to Azure AD Domain Services, for the Standard SKU the suggested Object Count is 0 to 25,000 - for the Enterprise SKU, it is 25,000 to 100,000. Although there is no hard limit, if fit in the Enterprise space, it might be worth upgrading the SKU you are running for the additional backups and authentication._

![](/uploads/adds_sync.png)

14. We can now configure the Security Settings, the only setting I am going to change here is TLS 1.2 Only Mode to Enable

![](/uploads/adds_securitysettings.png)

15. Enter any applicable Tags and click Review & Create to validate your configuration
16. Review your configuration and if you are happy with it: Select Create.
17. Confirm that you are happy with the following and click Ok

![](/uploads/adds_youshouldknow.png)

Note: Azure AD Domain Services can take up to an hour to provision.