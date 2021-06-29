---
date: 2021-06-29 00:00:00 +1200
title: Azure Virtual Desktop Optimisations
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
If you are running Azure Virtual Desktop, you want to get the most performance and stability out of them as possible, to reduce cost and increase user experience.

These are a few recommended policies and optimisations to apply to your Azure Virtual Desktop setup.

### Configure Timezone Redirection

Timezone redirection will allow you to pass through the time from the local device through to the Azure Virtual Desktop host, this is useful to keep consistent time between the device you are connecting from and by default the timezone in Azure is UTC.

 1. **Connect to** your Azure Active Directory **Utility server**, that has **Group Policy management** installed using an account in the: AAD DC Administrators group
 2. **Open Group Policy Management**
 3. **Navigate** to your **Hosts OU**
 4. Right click the OU and select: **Create a GPO in this domain, and Link it here…**
 5. Name it according to your naming standards (this is a Computer based policy) - in my example I am using: AVD_ComputerPolicy
 6. Click **Ok**
 7. ![FSLogix - Group Policy](/uploads/gpo_management_createpolicy.png "FSLogix - Group Policy")
 8. Right click the GPO you have just created and select **Edit…**
 9. Because this is a Computer based policy, to speed up processing, **right click** the **Policy heading** and select **Properties**
10. Tick: **Disable User Configuration Settings**
11. Confirm that you want to do it and select **Yes**
12. Click **Apply**
13. While you have the screen open, **click on**: **Comment**, and **add** in some **details** about the GPO for future reference then click **Apply** and **Ok**
14. ![FSLogix - Group Policy](/uploads/gpo_avd_computerpolicy.png "FSLogix - Group Policy")
15. Now its time to actually configure the FSLogix Group Policy settings.
16. **Navigate** to: Computer Configuration\\Policies\\Administrative Templates\\FSLogix\\**Profile Containers**
17. Open up **Enabled** and select: **Enabled** and **Apply**
18. Open: **VHD Location** and **copy** in your Profiles **UNC share** _(for example, mine is:_ \[_\\\\fslogixprofileslgnz.file.core.windows.net\\fslogixprofiles_\](file://fslogixprofileslgnz.file.core.windows.net/fslogixprofiles)_)_ click **Ok**
19. Select: **Delete local profile when FSLofix profile should apply**, click **Enabled** and check **Delete local profile when FSLogix Profile should apply** _(don't blindly follow this, I am making the assumption this is a new farm, with no user based profile stored on it. You may need to create a separate GPO to test this setting on, or you could lose valuable data)_.
20. Open: **Set Outlook cached mode on successful container attach** to **Enabled**.
21. Now in Group Policy Management console, click on: **Container and Directory Naming** and select **Virtual Disk type**
22. Click **Enabled** and change the Option to **VHDX**, click **Ok**
23. Click on: S**wap directory name components setting** and click **Enabled**, **check** the s**wap directory name components** and click **Apply**
24. **Restart** the Azure Virtual Desktop **session hosts** to pickup the new policies.
25. **You have now setup FSLogix profiles! If you map the drive you should see your user profile folders!**
26. ![FSLogix - Mapped Profiles](/uploads/computermappingdrivelast.png "FSLogix - Mapped Profiles")