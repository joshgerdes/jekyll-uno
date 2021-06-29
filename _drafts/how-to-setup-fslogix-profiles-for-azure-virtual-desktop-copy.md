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

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Device** and **Resource Redirection**.
5. **Enable** the setting **Allow time zone redirection**.
6. **Close** the **Group Policy Management console**, as this is a Computer-based policy it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.

### Configure Session Time Limit Policies

You can use this policy to specify the maximum amount of time that a disconnected session remains active on the server. By default, Remote Desktop Services allows users to disconnect from a Remote Desktop Services session without logging off and ending the session. This means that sessions users sessions may remain open for an extended period of time, taking up usable resources.

1. On a server with the Group Policy Management Console is installed for managing your Azure Virtual Desktop farm, **open** the **Group Policy Management Console**.
2. **Expand** your **domain** and **Group Policy Objects**.
3. **Right**-**click** the **GPO** that you created for the group policy settings and select **Edit**.
4. In the Group Policy Management Editor, **navigate to Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** > **Remote Desktop Services** > **Remote Desktop Session Host** > **Session Time Limits**.
5. Configure the below settings, in accordance with your organisation policies:

* **Set time limit for active but idle Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that an active emote Desktop Services sessions can be idle (without user input) before it is automatically disconnected._
* **Set time limit for active Remote Desktop Services sessions**
* _This policy allows you to specify the maximum amount of time that a Remote Desktop Services session can be active before it is automatically disconnected._
* **Set time limit for disconnected sessions**
* _This policy allows you to configure a time limit for disconnected Terminal Services sessions._
* **End session when time limits are reached**
* _This policy allows you to specify whether to terminate a timed-out Terminal Services session instead of disconnecting it._
* **Set a time limit for log off of RemoteApp sessions**
* _This policy allows you to specify how long a user's RemoteApp session will remain in a disconnected state after closing all RemoteApp programs before the session is logged off from the RD Session Host server._
* **Close** the **Group Policy Management console**, as this is a Computer-based policy it may take up to 90 minutes to take effect unless the session hosts are restarted to force it to pick up the policy sooner.