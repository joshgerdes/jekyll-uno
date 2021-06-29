---
date: 2021-06-29 00:00:00 +1200
title: How to setup FSLogix profiles for Azure Virtual Desktop
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
If you have a few Azure Virtual Desktop machines, you need some way to keep user persistence's and application customisations, which would usually be stored in the user profile locally across multiple machines _(or even the same machine if using Ephemeral OS)_, this is where FSLogix Profile Containers can assist.

We are going to implement FSLogix using an Azure File Share, to store the profiles.

I am going to assume you already have an Azure Virtual Desktop farm _(and Azure ADDS)_, if not you can check out my guide [here](https://luke.geek.nz/azure/create-a-azure-virtual-desktop-farm/ "How to create a Azure Virtual Desktop farm ").

This article will be based on the Azure Virtual Desktop farm created in a previous article, however, you can just still along and replace the resource names and groups with your own.

### Setup Storage Account

 1. Log in to the Azure Portal
 2. Click on Create a resource
 3. Type in Storage Account and press Enter to search
 4. Select Storage account
 5. ![FSLogix - Azure Storage Account](/uploads/storageaccount.png "FSLogix - Azure Storage Account")
 6. Click Create
 7. If you already have a Resource Group, then select it, if not you can create a new resource group. I am going to put my resources user profiles in the same resource group as my utility server: aad_infra _(this is just personal preference, keeping the session hosts in their own resource groups)_.
 8. Type in a Storage Account Name _(the name needs to be globally unique across all of Azure, the field can contain only lowercase letters and numbers. Name must be between 3 and 24 characters.)_, in my case I have gone with: fslogixprofileslgnz.
 9. Select your Region _(the same region you have your Azure Virtual Desktop session hosts and Virtual Network)_
10. Select Standard performance _(Microsoft have recommendations, based on users on what Tier to select -_ [_https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile_](https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile "https://docs.microsoft.com/en-us/azure/virtual-desktop/store-fslogix-profile")_)_
11. For Redundancy, I am going to select LRS storage _(I haven't built have any redundancy in my Azure Virtual Desktop farm)_.
12. _Note: Just a heads up, don't select Geo-Redundant if you are looking to create File Shares on this Storage account over 100TiB, it is only supported in LRS. If you do need this kind of large file size, I recommend using a completely different storage account from the one you are using for user profiles. My screenshot below has GRS, just ignore it!_
13. ![FSLogix - Azure Storage Account](/uploads/storageaccount_projectdetails.png "FSLogix - Azure Storage Account")
14. Click Next: Advanced
15. Leave everything as default and select Next: Networking
16. Now we need to configure a Private Endpoint for the Azure storage account to add onto the Virtual Network directly.
17. Select Private endpoint and click + Add Private endpoint
18. Verify that your Location is correct and type in a Name for your Private Endpoint

    service, in my case: fslogixprofileslgnzPE
19. Select the drop down for Storage sub-resource and select file
20. Select your Virtual Network and subnet _(I will be selecting my main resource subnet of aadds-subnet, where the Azure Virtual Desktop hosts are)_
21. Click Ok
22. ![FSLogix - Azure Storage Account](/uploads/storageaccount_privateendpoint.png "FSLogix - Azure Storage Account")
23. Select Next: Data Protection
24. Untick the Enable soft delete for Blogs and Container's _(we will only be using Azure Files in this storage account)_
25. Soft delete allows you to quickly recover a deleted fileshare, even though we can backup the Azure Fileshare, my recommendation would be to leave this on for additional protection and '7' days is enough for me.
26. ![FSLogix - Azure Storage Account](/uploads/storageaccount_softdelete.png "FSLogix - Azure Storage Account")
27. Select Review + Create
28. Validate your configuration and select Create

### Configure Storage Account

 1. Once your storage account has been created, go to it.
 2. Navigate down the left hand side Blade and select: Networking

    Make sure: Selected networks is selected and the Private Endpoint connection is displaying.
 3. ![FSLogix - Azure Storage Account](/uploads/storageaccount_firewalls.png "FSLogix - Azure Storage Account")
 4. ![FSLogix - Azure Storage Account](/uploads/storageaccount_peapproved.png "FSLogix - Azure Storage Account")
 5. Now its time to join the Storage account to Azure Active Directory Domain Services, on the left hand side Blade, click on Configuration _(under Settings)_
 6. Navigate to: Identity-based access for file shares
 7. Select Enabled
 8. Click Save
 9. ![FSLogix - Azure Storage Account](/uploads/storageaccount_adds_identity.png "FSLogix - Azure Storage Account")
10. Now its time to create the File Share, On the left hand side Blade, navigate to: File Shares (under Data Storage)
11. Select + File Share
12. Give this File share a name: fslogixprofiles
13. Even though you don't need to have a Quota (the Fileshare will grow), I will add one in stop any surprises and make sure that I have an ongoing task to review and optimize the profiles
14. Because user profiles are generally a lot of read/write activity, select Transaction Optimized (take a look at the [https://azure.microsoft.com/en-us/pricing/details/storage/files/](https://azure.microsoft.com/en-us/pricing/details/storage/files/ "https://azure.microsoft.com/en-us/pricing/details/storage/files/") )
15. Click Create
16. ![FSLogix - File Share](/uploads/storageaccount_newfileshare.png "FSLogix - File Share")
17. One last thing we can do on the Storage Account, is enable backups for your Azure File Share - [https://docs.microsoft.com/en-us/azure/backup/backup-afs](https://docs.microsoft.com/en-us/azure/backup/backup-afs "https://docs.microsoft.com/en-us/azure/backup/backup-afs")

### Configure File Share

Now that the Azure Active Directory rights has been assigned and the File Share has been created, we now need to setup the NTFS permissions on the FSLogix share.

 1. Navigate to File Shares _(under Data Storage)_
 2. Click on your fileshare
 3. Click on Properties
 4. Copy the URL
 5. ![FSLogix - File Share](/uploads/storageaccount_fslogixprofiles.png "FSLogix - File Share")
 6. Remove http and replace the forward slashes with backslashes so it looks like this: \[\\\\fslogixprofileslgnz.file.core.windows.net\\fslogixprofiles\](file://fslogixprofileslgnz.file.core.windows.net/fslogixprofiles)
 7. Using a user that is a member of the 'AVD Admins' group and can log into the Azure Virtual Desktop farm _(it’s a good chance to test connectivity to the Storage account through the private endpoint from your Azure Virtual Desktop session host)_
 8. Open Computer
 9. Select the Computer Tab and select Map network drive
10. ![FSLogix - Mapped Drive](/uploads/computermappeddrive.png "FSLogix - Mapped Drive")
11. Select a drive letter that isn't in use and paste in the fileshare UNC path created earlier.
12. ![FSLogix - Mapped Drive](/uploads/computermappingdrive.png "FSLogix - Mapped Drive")
13. Hopefully you should successfully have mapped a drive!
14. Once the drive is mapped, open up a Command Prompt

    _Note: Don't run the Command Prompt as Administrator, as this runs in a separate context and doesn't have permissions to the mapped drive._
15. Run the following command to set the necessary NTFS permissions (change the Drive mapping and AVD Users group to your own group):

        icacls z: /grant "AVD Users":(M)
        
        icacls z: /grant "Creator Owner":(OI)(CI)(IO)(M)
        
        icacls z: /remove "Authenticated Users"
        
        icacls z: /remove "Builtin\Users"
16. ![FSLogix - Security Permissions](/uploads/setfslogixpermissions.png "FSLogix - Security Permissions")
17. The permissions should look similar to:
18. ![FSLogix - Security Permissions](/uploads/setfslogixpermissions2.png "FSLogix - Security Permissions")

### Configure FSLogix policies

Now that you have successfully created a Storage Account and granted it the proper permissions, we now need to configure Group Policy to for FSLogix.

 1. Connect to your Azure Active Directory Utility server, that has Group Policy management installed using an account in the: AAD DC Administrators group
 2. Download the latest FSLogix Agent - [https://aka.ms/fslogix_download](https://aka.ms/fslogix_download "https://aka.ms/fslogix_download") onto the Utility server
 3. Extract the FSLogix agent zip file to a folder
 4. Now we will create a Central Store to manage the Group Policy from consistantly
 5. On your Utility server, browse to: C:\\Windows (If you are primarily using Azure Virtual Desktop, it may be best to copy the PolicyDefinitions folder from a Azure Virtual Desktop sessionhost to make sure you can edit all the latest Windows 10 policies)
 6. Copy the PolicyDefinitions folder
 7. Copy the PolicyDefinitions folder to your Policies folder on your domain: [\\\\luke.geek.nz\\SYSVOL\\luke.geek.nz\\Policies](file://luke.geek.nz/SYSVOL/luke.geek.nz/Policies) _(replace luke.geek.nz, with your ADDS DNS name)_
 8. ![FSLogix - Group Policy](/uploads/sysvolpolicies.png "FSLogix - Group Policy")
 9. Go to your extracted FSLogix folder and copy:
    * fslogix.admx to: [\\\\luke.geek.nz\\SYSVOL\\luke.geek.nz\\Policies\\PolicyDefinitions](file://luke.geek.nz/SYSVOL/luke.geek.nz/Policies/PolicyDefinitions)
    * fslogix.adml to: [\\\\luke.geek.nz\\SYSVOL\\luke.geek.nz\\Policies\\PolicyDefinitions\\en-US](file://luke.geek.nz/SYSVOL/luke.geek.nz/Policies/PolicyDefinitions/en-US)
10. This will allow us to use Group Policy to manage FSLogix using Group Policy, Open Group Policy Management
11. Navigate to your Hosts OU
12. Right click the OU and select: Create a GPO in this domain, and Link it here…
13. Name it according to your naming standards (this is a Computer based policy) - in my example I am using: AVD_ComputerPolicy
14. Click Ok
15. ![FSLogix - Group Policy](/uploads/gpo_management_createpolicy.png "FSLogix - Group Policy")
16. Right click the GPO you have just created and select Edit…
17. Because this is a Computer based policy, to speed up processing, right click the Policy heading and select Properties
18. Tick: Disable User Configuration Settings
19. Confirm that you want to do it and select Yes
20. Click Apply
21. While you have the screen open, click on: Comment, and add in some details about the GPO for future reference then click Apply and Ok
22. ![FSLogix - Group Policy](/uploads/gpo_avd_computerpolicy.png "FSLogix - Group Policy")
23. Now its time to actually configure the FSLogix Group Policy settings.
24. Navigate to: Computer Configuration\\Policies\\Administrative Templates\\FSLogix\\Profile Containers
25. Open up Enabled and select: Enabled and Apply
26. Open: VHD Location and copy in your Profiles UNC share _(for example, mine is:_ [_\\\\fslogixprofileslgnz.file.core.windows.net\\fslogixprofiles_](file://fslogixprofileslgnz.file.core.windows.net/fslogixprofiles)_)_ click Ok
27. Select: Delete local profile when FSLofix profile should apply, click Enabled and check Delete local profile when FSLogix Profile should apply (don't blindly follow this, I am making the assumption this is a new farm, with no user based profile stored on it. You may need to create a separate GPO to test this setting on, or you could lose valuable data).
28. Open: Set Outlook cached mode on successful container attach to Enabled.
29. Now in Group Policy Management console, click on: Container and Directory Naming and select Virtual Disk type
30. Click Enabled and change the Option to VHDX, click Ok
31. Click on: Swap directory name components setting and click Enabled, check the swap directory name components and click Apply
32. Restart the Azure Virtual Desktop session hosts to pickup the new policies.
33. **You have now setup FSLogix profiles! If you map the drive you should see your user profile folders!**
34. ![FSLogix - Mapped Profiles](/uploads/computermappingdrivelast.png "FSLogix - Mapped Profiles")