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
22. ![](/uploads/storageaccount_privateendpoint.png)
23. Select Next: Data Protection
24. Untick the Enable soft delete for Blogs and Container's _(we will only be using Azure Files in this storage account)_
25. Soft delete allows you to quickly recover a deleted fileshare, even though we can backup the Azure Fileshare, my recommendation would be to leave this on for additional protection and '7' days is enough for me.
26. ![](/uploads/storageaccount_softdelete.png)
27. Select Review + Create
28. Validate your configuration and select Create

### Configure Storage Account

 1. Once your storage account has been created, go to it.
 2. Navigate down the left hand side Blade and select: Networking

    Make sure: Selected networks is selected and the Private Endpoint connection is displaying.
 3. ![](/uploads/storageaccount_firewalls.png)
 4. ![](/uploads/storageaccount_peapproved.png)
 5. Now its time to join the Storage account to Azure Active Directory Domain Services, on the left hand side Blade, click on Configuration _(under Settings)_
 6. Navigate to: Identity-based access for file shares
 7. Select Enabled
 8. Click Save
 9. ![](/uploads/storageaccount_adds_identity.png)
10. Now its time to create the File Share, On the left hand side Blade, navigate to: File Shares (under Data Storage)
11. Select + File Share
12. Give this File share a name: fslogixprofiles
13. Even though you don't need to have a Quota (the Fileshare will grow), I will add one in stop any surprises and make sure that I have an ongoing task to review and optimize the profiles
14. Because user profiles are generally a lot of read/write activity, select Transaction Optimized (take a look at the [https://azure.microsoft.com/en-us/pricing/details/storage/files/](https://azure.microsoft.com/en-us/pricing/details/storage/files/ "https://azure.microsoft.com/en-us/pricing/details/storage/files/") )
15. Click Create
16. ![](/uploads/storageaccount_newfileshare.png)

### Configure File Share

Now that the Azure Active Directory rights has been assigned and the File Share has been created, we now need to setup the NTFS permissions on the FSLogix share.

 1. Navigate to File Shares _(under Data Storage)_
 2. Click on your fileshare
 3. Click on Properties
 4. Copy the URL
 5. ![](/uploads/storageaccount_fslogixprofiles.png)
 6. Remove http and replace the forward slashes with backslashes so it looks like this: \[\\\\fslogixprofileslgnz.file.core.windows.net\\fslogixprofiles\](file://fslogixprofileslgnz.file.core.windows.net/fslogixprofiles)
 7. Using a user that is a member of the 'AVD Admins' group and can log into the Azure Virtual Desktop farm _(it’s a good chance to test connectivity to the Storage account through the private endpoint from your Azure Virtual Desktop session host)_
 8. Open Computer
 9. Select the Computer Tab and select Map network drive
10. ![](/uploads/computermappeddrive.png)
11. Select a drive letter that isn't in use and paste in the fileshare UNC path created earlier.
12. ![](/uploads/computermappingdrive.png)
13. Hopefully you should successfully have mapped a drive!
14. Once the drive is mapped, open up a Command Prompt

    _Note: Don't run the Command Prompt as Administrator, as this runs in a separate context and doesn't have permissions to the mapped drive._
15. Run the following command to set the necessary NTFS permissions (change the Drive mapping and AVD Users group to your own group):

        icacls z: /grant "AVD Users":(M)
        
        icacls z: /grant "Creator Owner":(OI)(CI)(IO)(M)
        
        icacls z: /remove "Authenticated Users"
        
        icacls z: /remove "Builtin\Users"
16. ![](/uploads/setfslogixpermissions.png)