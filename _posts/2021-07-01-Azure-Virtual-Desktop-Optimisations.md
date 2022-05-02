---
date: 2021-07-01 00:00:00 +1200
title: Azure Virtual Desktop Optimisations
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/avddesktopfull.png"

---
If you are running Azure Virtual Desktop, you want to get the most performance and stability out of them as possible, to reduce cost and increase user experience.

These are a few recommended policies and optimisations to apply to your Azure Virtual Desktop setup. These are in no particular order; they are just recommendations.

### Configure Timezone Redirection

Timezone redirection will allow you to pass through the time from the local device to the Azure Virtual Desktop host. This is useful to keep the consistent time between the device you are connecting from and the session host, and by default, the timezone in Azure is UTC.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Device** **and Resource Redirection**.
5. **Enable** the setting **Allow time zone redirection**.
6. **Close** the **Group Policy Management console**; as this is a Computer-based policy, it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

### Configure Session Time Limit Policies

You can use this policy to specify the maximum amount of time that a disconnected session remains active on the server. By default, Remote Desktop Services allows users to disconnect from a Remote Desktop Services session without logging off and ending the session. Unfortunately, this means that sessions users sessions may remain open for an extended period of time, taking up usable resources.

When configuring these, take into consideration a users normal work time, the time they have for lunch etc., the sweet spot to disconnect their session is not during their lunch break, but after they have finished for the day, usually 8-12 hours is recommended, but is dependant on how Azure Virtual Desktop is used.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Session Time Limits**.
5. Configure the below settings per your organisation policies:

* **Set time limit for active but idle Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that an active Remote Desktop Services session can be idle (without user input) before it is automatically disconnected._
* **Set time limit for active Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that a Remote Desktop Services session can be active before it is automatically disconnected._
* **Set time limit for disconnected sessions**
* _This policy allows you to configure a time limit for disconnected Terminal Services sessions._
* **End session when time limits are reached**
* _This policy allows you to specify whether to terminate a timed-out Terminal Services session instead of disconnecting it._
* **Set a time limit for log off of RemoteApp sessions**
* _This policy allows you to specify how long a user's RemoteApp session will remain in a disconnected state after closing all RemoteApp programs before the session is logged off from the RD Session Host server._
* **Close** the **Group Policy Management console**; as this is a Computer-based policy, it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

_Reference: Taken from:_ [_https://kb.parallels.com/en/123638_](https://kb.parallels.com/en/123638 "https://kb.parallels.com/en/123638"){:target="_blank"}

### DeleteUserAppContainersOnLogoff

Back in March 2019, there were issues with slow server performance caused by numerous Windows Firewall Rules getting created on user login. A patch was released; however, to enable this '_fix_', a registry key needs to be set. You could eventually run into host performance/hang issues if this key is not configured. See: [https://support.microsoft.com/en-us/help/4490481](https://support.microsoft.com/en-us/help/4490481 "https://support.microsoft.com/en-us/help/4490481"){:target="_blank"}

 1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
 2. **Expand** your **domain** and **Group Policy Objects**.
 3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
 4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Preferences**> **Windows Settings** > **Registry**.
 5. Right-click in the window and select **New**, **Registry Item**
 6. Select **Update** as the Action
 7. Make sure **HKEY_LOCAL_MACHINE** is set to **Hive**
 8. Enter in the following for the Key Path: **SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy**
 9. For the Value name type: **DeleteUserAppContainersOnLogoff**
10. Change the Value type to **REG_DWORD**
11. Put: '**1**' to enable the option and click **Apply**
12. **Close** the **Group Policy Management console**. As this is a Computer-based policy, it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

![Delete user Apps](/uploads/deleteuserapp.png)

### Configure RDP Shortpath

RDP Shortpath is a feature of Azure Virtual Desktop that establishes a direct UDP-based transport between Remote Desktop Client and Session host. RDP uses this transport to deliver Remote Desktop and RemoteApp while offering better reliability and consistent latency. RDP Shortpath establishes the direct connectivity between Remote Desktop client and Session Host. Direct connectivity reduces the dependency on the Azure Virtual Desktop gateways, improves the connection's reliability, and increases the bandwidth available for each user session. You can read more about it here: [Azure Virtual Desktop RDP Shortpath](https://docs.microsoft.com/en-us/azure/virtual-desktop/shortpath?WT.mc_id=AZ-MVP-5004796 "Azure Virtual Desktop RDP Shortpath"){:target="_blank"}.

 1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
 2. **Expand** your **domain** and **Group Policy Objects**.
 3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
 4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Preferences**> **Windows Settings** > **Registry**.
 5. Right-click in the window and select **New**, **Registry Item**
 6. Select **Update** as the Action
 7. Make sure **HKEY_LOCAL_MACHINE** is set to **Hive**
 8. Enter in the following for the Key Path: **SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\WinStations**
 9. For the Value name type: **fUseUdpPortRedirector**
10. Change the Value type to **REG_DWORD**
11. Put: '**1**' to enable the option and click **Apply**
12. Right-click in the window and select **New**, **Registry Item**
13. Select **Update** as the Action
14. Make sure **HKEY_LOCAL_MACHINE** is set to **Hive**
15. Enter in the following for the Key Path: **SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\WinStations**
16. For the Value name type: **UdpPortNumber**
17. Change the Value type to **REG_DWORD**
18. Put: '**3390**' as the UDP report and click **Apply**
19. **Close** the **Group Policy Management console**. Restart the session hosts.

### Virtual-Desktop-Optimization-Tool

Automatically apply a range of optimisations for pooled and personal Azure Desktop hosts, this is a good resource to add to your initial image creation builds. 

[Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool "Virtual-Desktop-Optimization-Tool"){:target="_blank"}

### Implement Windows Defender FSLogix exclusions

Make sure to configure antivirus exclusions for FSLogix Profiles.

For a list of exclusions, along with a PowerShell script to implement them, please refer to the following Microsoft documentation: [FSLogix for the enterprise](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/wvd/windows-virtual-desktop-fslogix?WT.mc_id=AZ-MVP-5004796 "FSLogix for the enterprise")

### Implement FSLogix Profile Exclusions

By default, FSLogix will capture a lot of user profile data, including Teams Cache, Chrome cache and save it to the profile VHD/VHDX; this causes profile size bloat and can decrease the performance of your applications.

It is recommended to implement exclusions to reduce storing user profile data that you don't need.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **FSLogix** > **Profile Containers** > **Advanced**
5. **Enable** the setting **Provide RedirXML file to customize directions**.
6. Point the path to a **UNC path** that is **accessible** to all session hosts that **contains** are '**redirections.xml**' file. This just needs the folder; it will automatically pick up the redirections.xml file.
7. **Close** the **Group Policy Management console**. As this is a Computer-based policy, it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

An example redirections.xml can be found here:

{% gist 376bd6eeda9d33172a8442e2d76054a2 %}

_Note: Make sure you test and adjust this for your own environment. The Desktop/Documents have been excluded as the assumption is these are redirected or covered by OneDrive._

### DeleteUserAppContainersOnLogoff

Back in March 2019, there were issues with slow server performance caused by numerous Windows Firewall Rules getting created on user login. A patch was released; however, to enable this '_fix_', a registry key needs to be set. You could eventually run into host performance/hang issues if this key is not configured. See: [https://support.microsoft.com/en-us/help/4490481](https://support.microsoft.com/en-us/help/4490481 "https://support.microsoft.com/en-us/help/4490481"){:target="_blank"}

 1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
 2. **Expand** your **domain** and **Group Policy Objects**.
### Implement Storage Sense

On Windows 10, Storage sense is a built-in tool designed to free up space automatically. When it's enabled, the feature monitors your device. When it's running low on space, it deletes temporary files, empties the Recycle Bin, cleans up the Downloads folder, removes previous installation files, and more to make space to install new updates or store more important data. Storage Sense can also help dehydrate files that are available locally and do not need to be stored locally anymore, helping to reduce profile space and OneDrive processing.

_Note: If you find that Storage Sense is missing, it is because it is mainly a client setting and may be missing from the Windows Server; you can copy the PolicyDefinitions folder from an Azure Virtual Desktop host to your domains Central Store, i.e. in my case \\\\luke.geek.nz\\SYSVOL\\luke.geek.nz\\Policies\\PolicyDefinitions. Or just look for StorageSense.admx and StorageSense.adml and copy it (the ADML goes in the language directory, i.e. en-US)._

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **System** > **Storage Sense**.
5. **Enable** the setting **Allow Storage Sense**.
6. **Enable** the setting **Configure Storage Sense Cloud Content dehydration threshold**
7. Now we can provide the minimum number of days a cloud-backed file can remain unopened before Storage Sense dehydrates it back to Files on Demand, for example, **30** days since it was last accessed.
6. **Enable** the setting **Configure Storage Storage Downloads cleanup threshold**
7. **Type** in a minimum number of **days**, that files sit in the Downloads before before Storage sense will delete it.
8. **Close** the **Group Policy Management console**. As this is a Computer-based policy, it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

![Storage Sense - Group Policy](/uploads/storagesense_gpo.png "Storage Sense - Group Policy")

### Configure Microsoft Teams Optimisations

You can run Microsoft Teams in Azure Virtual Desktop. To do so, you need to install as a Machine installer and set the WVD environment variable.

**Install as Machine:**

    msiexec /i Teams_windows_x64 /l*v teams_install.log ALLUSER=1

**Set IsWVDEnvironment key**:

 1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
 2. **Expand** your **domain** and **Group Policy Objects**.
 3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
 4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Preferences**> **Windows Settings** > **Registry**.
 5. Right-click in the window and select **New**, **Registry Item**
 6. Select **Update** as the Action
 7. Make sure **HKEY_LOCAL_MACHINE** is set to **Hive**
 8. Enter in the following for the Key Path: **SOFTWARE\\Microsoft\\Teams**
 9. For the Value name type: **IsWVDEnvironment**
10. Change the Value type to **REG_DWORD**
11. Put: '**1**' to enable the option and click **Apply**
12. **Close** the **Group Policy Management console**. Restart the session hosts.

**Install the Remote Desktop WebRTC Redirector**

1. The Remote Desktop WebRTC Redirector onto the Sessions Hosts: [https://docs.microsoft.com/en-us/azure/virtual-desktop/teams-on-AVD#install-the-teams-websocket-service](https://docs.microsoft.com/en-us/azure/virtual-desktop/teams-on-AVD#install-the-teams-websocket-service "hhttps://docs.microsoft.com/en-us/azure/virtual-desktop/teams-on-AVD?WT.mc_id=AZ-MVP-5004796#install-the-teams-websocket-service"){:target="_blank"}

### Configure Auto Close Apps on Logoff

When users may go to logoff, open applications may halt or prolong the logoff process and prompts for users to close applications, this can leave to sessions being left connected, if a user hits logoff or shutdown and walks away. To stop the prompt about open Applications we need to set a registry key - this is not an 'optimisation' to be treated lightly, as it won't ask users to double check some of the apps they have open, as soon as they hit the logoff button - that it is, any open apps will be closed!

 1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
 2. **Expand** your **domain** and **Group Policy Objects**.
 3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
 4. In the Group Policy Management Editor, **navigate to User Configuration** > **Preferences**> **Windows Settings** > **Registry**.
 5. Right-click in the window and select **New**, **Registry Item**
 6. Select **Update** as the Action
 7. Make sure **HKEY_CURRENT_USER** is set to **Hive**
 8. Enter in the following for the Key Path: **Control Panel\\Desktop**
 9. For the Value name type: **AutoEndTasks**
10. Change the Value type to **REG_SZ**
11. Put: '**1**' to enable the option and click **Apply**
12. **Close** the **Group Policy Management console**. Restart the session hosts.

This is a user-based policy, so will take effect on next logon.

### Hide the Shutdown button

This is not so much of an optimization, but it is one of my favourite group policy configurations, something I implement in server base policies; it prevents that "Oops!" moment when someone clicks Shutdown on a server, especially with multi-session VDI machines, this just removes the shortcuts to shutdown and restart the server from the Start Menu.

_Note: You can still restart and shut down the server from the Command Prompt with the 'shutdown' command._

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to User Configuration** > **Policies** > **Administrative Templates** > **Start Menu and Taskbar**
5. **Enable** the setting **Remove and prevent access to Shut Down, Restart, Sleep, and Hibernate commands.**
6. **Close** the **Group Policy Management console**; as this is a User-based policy, it should take effect on the next user login.
