---
id: 3254
title: Windows cannot connect to the domain
date: 2014-04-27T15:52:41+00:00
author: Luke
layout: post
guid: http://localhost/techremedy/?p=3254
permalink: /win/windows-cannot-connect-to-the-domain/
slide_template:
  - default
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4987895630"
mfn-post-love:
  - "0"
post_views_count:
  - "9"
categories:
  - Windows
---
  1. Open **Active Directory Users & Computers**
  2. Right click **Computers**
  3. **Search** for the **computer** **name** you would like to remove and **right** **click** and select **Reset**
  4. Now on the **computer** **logon **using a local computer account.
  5. **Right** **click** Computer/My **Computer**
  6. Select **Properties**
  7. **Click** **Computer** **Name** tab and select **Change**
  8. **Click** on **Member of** &#8211; and **change** from **Domain** to **Workgroup** and click Ok
  9. Windows will prompt you to restart your Computer &#8211; select **Restart** **later**
 10. **Select** **Domain** and enter in the domain name you wish to reconnect to and click **Ok**
 11. **Enter** in your domain **credentials** to add the workstation back to the domain and click **Ok** **to** **restart** the computer.

&nbsp;

Note: The benefit of doing the Reset in Active Directory first &#8211; allows you to maintain the computer groups and security identifier without loosing it.

&nbsp;

You can also use the following Powershell command on the local PC to restore the secure channel to the domain: `Test-ComputerSecureChannel -Repair`