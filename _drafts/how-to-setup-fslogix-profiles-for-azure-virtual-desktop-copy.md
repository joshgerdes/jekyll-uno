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