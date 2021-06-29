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

Timezone redirection will allow you to pass through the time from the local device through to the Azure Virtual Desktop host, this is useful to keep the consistent time between the device you are connecting from and the session host and by default the timezone in Azure is UTC.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Device** and **Resource Redirection**.
5. **Enable** the setting **Allow time zone redirection**.
6. **Close** the **Group Policy Management console**, as this is a Computer-based policy it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

### Configure Session Time Limit Policies

You can use this policy to specify the maximum amount of time that a disconnected session remains active on the server. By default, Remote Desktop Services allows users to disconnect from a Remote Desktop Services session without logging off and ending the session. This means that sessions users sessions may remain open for an extended period of time, taking up usable resources.

When configuring these, take into consideration a users normal work time, the time they have for lunch etc, the sweet spot to disconnect their session is not during their lunch break, but after they have finished for the day, usually 8-12 hours is recommended, but is dependant on how Azure Virtual Desktop is used.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Session Time Limits**.
5. Configure the below settings, in accordance with your organisation policies:

* **Set time limit for active but idle Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that an active Remote Desktop Services sessions can be idle (without user input) before it is automatically disconnected._
* **Set time limit for active Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that a Remote Desktop Services session can be active before it is automatically disconnected._
* **Set time limit for disconnected sessions**
* _This policy allows you to configure a time limit for disconnected Terminal Services sessions._
* **End session when time limits are reached**
* _This policy allows you to specify whether to terminate a timed-out Terminal Services session instead of disconnecting it._
* **Set a time limit for log off of RemoteApp sessions**
* _This policy allows you to specify how long a user's RemoteApp session will remain in a disconnected state after closing all RemoteApp programs before the session is logged off from the RD Session Host server._
* **Close** the **Group Policy Management console**, as this is a Computer-based policy it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

_Note: Taken from:_ [_https://kb.parallels.com/en/123638_](https://kb.parallels.com/en/123638 "https://kb.parallels.com/en/123638")

### DeleteUserAppContainersOnLogoff

Back in March 2019, there were issues with slow server performance, caused by numerous Windows Firewall Rules getting created on user login. A patch was released, however, to enable this '_fix_' a registry key needs to be set. You could eventually run into host performance/hang issues if this key is not configured. See: [https://support.microsoft.com/en-us/help/4490481](https://support.microsoft.com/en-us/help/4490481 "https://support.microsoft.com/en-us/help/4490481")

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
12. **Close** the **Group Policy Management console**, as this is a Computer-based policy it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

![](/uploads/deleteuserapp.png)

### Configure RDP Shortpath

RDP Shortpath is a feature of Azure Virtual Desktop that establishes a direct UDP-based transport between Remote Desktop Client and Session host. RDP uses this transport to deliver Remote Desktop and RemoteApp while offering better reliability and consistent latency. RDP Shortpath establishes the direct connectivity between Remote Desktop client and Session Host. Direct connectivity reduces the dependency on the Azure Virtual Desktop gateways, improves the connection's reliability, and increases the bandwidth available for each user session. You can read more about it here: [Azure Virtual Desktop RDP Shortpath](https://docs.microsoft.com/en-us/azure/virtual-desktop/shortpath "Azure Virtual Desktop RDP Shortpath").

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

### Implement Windows Defender FSLogix exclusions

Make sure to configure antivirus exclusions for FSLogix Profiles.

For a list of exclusions, along with a PowerShell script to implement them please refer to the following Microsoft documentation: [FSLogix for the enterprise](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/wvd/windows-virtual-desktop-fslogix "FSLogix for the enterprise")