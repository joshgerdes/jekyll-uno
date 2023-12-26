---
title: Remote assist Xenapp users
categories:
  - Windows
date: 2014-04-27 00:00:00 +1300
---
Due to inconsistencies in Microsoft’s remote assistance and dual monitor technologies – there is an incompatibility between Server 2008 R2 and some Windows client operating systems – not allowing you to use Citrix tools to shadow and control XenApp sessions &#8211; follow the quick guide below to remote assist Xenapp users.

&nbsp;

A way around this is to – publish Remote Assistance for Helpdesk and System administrator access.

&nbsp;

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Configure_Remote_Assistance_in_XenApp"><span class="toc_number toc_depth_1">1</span> Configure Remote Assistance in XenApp</a>
    </li>
    <li>
      <a href="#Using_Remote_Assistance_Citrix_AppCenter_to_Remote_Assist_users"><span class="toc_number toc_depth_1">2</span> Using Remote Assistance & Citrix AppCenter to Remote Assist users</a>
    </li>
  </ul>
</div>

#### <span id="Configure_Remote_Assistance_in_XenApp">Configure Remote Assistance in XenApp</span>


  1. Lal Mohan (<a title="Configure-windows-remote-assistance-in-citrix-xenapp-6-5" href="http://lalmohan.co.nz/2013/07/02/configure-windows-remote-assistance-in-citrix-xenapp-6-5-for-multi-monitor-shadowing/" target="_blank">http://lalmohan.co.nz/2013/07/02/configure-windows-remote-assistance-in-citrix-xenapp-6-5-for-multi-monitor-shadowing/</a> ) has written a great blog post on setting this up – just follow the guide to configure Remote Assistance in the XenApp environment.


#### <span id="Using_Remote_Assistance_Citrix_AppCenter_to_Remote_Assist_users">Using Remote Assistance & Citrix AppCenter to Remote Assist users</span>


  1. Log into the Citrix Application Portal
  2. Launch Citrix **AppCenter**
  3. Select **XenAppFarm**
  4. **Click** the **Users** tab
  5. **Find** the **user** you want to connect to and **check** the **Server** they are on.
  6. Go back to the **Application Portal** and **click** the **Remote Assistance** application
  7. In the Type a computer name or IP address  &#8211; **type** in the **Server** name the user is connected to and press Next
  8. **Select** the name of the **user** you want to connect to and select **Next** to **start** the **Remote Assistance.**
