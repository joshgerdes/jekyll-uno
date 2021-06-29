---
date: 2021-06-29 00:00:00 +1200
title: How to setup FSLogix profiles for Azure Virtual Desktop
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
If you have a few Azure Virtual Desktop machines, you need some way to keep user persistence's and application customisations, which would usually be stored in the user profile locally across multiple machines (or even the same machine if using Ephemeral OS), this is where FSLogix Profile Containers can assist.

We are going to implement FSLogix using an Azure File Share, to store the profiles.

I am going to assume you already have an Azure Virtual Desktop farm (and Azure ADDS), if not you can check out my guide [here](https://luke.geek.nz/azure/create-a-azure-virtual-desktop-farm/ "How to create a Azure Virtual Desktop farm ").

This article will be based on the Azure Virtual Desktop farm created in a previous article, however, you can just still along and replace the resource names and groups with your own.

### Setup Storage Account

 1. Log in to the Azure Portal
 2. Click on Create a resource
 3. Type in Storage Account and press Enter to search
 4. Select Storage account
 5. ![](/uploads/storageaccount.png)
 6. Click Create
 7. If you already have a Resource Group, then select it, if not you can create a new resource group. I am going to put my resources user profiles in the same resource group as my utility server: aad_infra _(this is just personal preference, keeping the session hosts in their own resource groups)_.
 8. Type in a Storage Account Name _(the name needs to be globally unique across all of Azure, the field can contain only lowercase letters and numbers. Name must be between 3 and 24 characters.)_, in my case I have gone with: fslogixprofileslgnz.
 9. Select your Region _(the same region you have your Azure Virtual Desktop session hosts and Virtual Network)_
10. Select Standard performance _(Microsoft have recommendations, based on users on what Tier to select -_ [_https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile_](https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile "https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile")_)_
11. For Redundancy, I am going to select LRS storage _(I haven't built have any redundancy in my Azure Virtual Desktop farm)_.
12. _Note: Just a heads up, don't select Geo-Redundant if you are looking to create File Shares on this Storage account over 100TiB, it is only supported in LRS. If you do need this kind of large file size, I recommend using a completely different storage account from the one you are using for user profiles. My screenshot below has GRS, just ignore it!_
13. ![](/uploads/storageaccount_projectdetails.png)
14. Click Next: Advanced
15. Leave everything as default and select Next: Networking
16. Now we need to configure a Private Endpoint for the Azure storage account to add onto the Virtual Network directly.
17. Select Private endpoint and click + Add Private endpoint
18. Verify that your Location is correct and type in a Name for your Private Endpoint

    service, in my case: fslogixprofileslgnzPE
19. Select the drop down for Storage sub-resource and select file
20. Select your Virtual Network and subnet _(I will be selecting my main resource subnet of aadds-subnet, where the Azure Virtual Desktop hosts are)_
21. Click Ok