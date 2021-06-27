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