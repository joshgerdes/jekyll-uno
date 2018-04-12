---
id: 3815
title: 'BgInfo Configuration &amp; User Deployment using Group Policy'
date: 2016-12-13T02:00:47+00:00
author: Luke
layout:
  - ""
guid: http://luke.geek.nz/?p=3815
permalink: /win/bginfo-configuration-user-deployment-using-group-policy/
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
dsq_thread_id:
  - "5375562190"
post_views_count:
  - "0"
categories:
  - Windows
---
<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Introduction"><span class="toc_number toc_depth_1">1</span> Introduction</a>
    </li>
    <li>
      <a href="#How_do_I_create_a_BGInfo_package"><span class="toc_number toc_depth_1">2</span> How do I create a BGInfo package?</a>
    </li>
    <li>
      <a href="#How_do_I_deploy_BGInfo_package"><span class="toc_number toc_depth_1">3</span> How do I deploy BGInfo package?</a>
    </li>
  </ul>
</div>

## <span id="Introduction">Introduction</span>

BgInfo is beneficial for Endpoint device support by displaying the Asset number, IP address and logged on username overlaid on top of the wallpaper, it is OS independent and can be used across other Windows Desktop and Windows Server environments.

BGInfo is a free Windows Sysinternals utility created by Microsoft engineer, Mark Russinovich.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi1.jpg?w=1500" alt="" data-recalc-dims="1" />

This utility runs under the user&#8217;s context. This does not need admin rights. As such this we will create this as a User Based group policy which runs upon logon.

## <span id="How_do_I_create_a_BGInfo_package">How do I create a BGInfo package?</span>

Use the following guide to create the BG Info package&#8230;

  1. <div style="text-align: justify">
      Download BGInfo &#8211; <a href="https://technet.microsoft.com/en-us/sysinternals/bginfo.aspx" target="_blank">https://technet.microsoft.com/en-us/sysinternals/bginfo.aspx</a>
    </div>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi2.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      Run and extract it to a folder – for example c:\temp\bginfo
    </div>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi3.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      Run BGInfo, you will be prompted with the default configuration
    </div>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi4.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      You can delete the Fields from the Black window, as applicable in this example we are just going to use x3 fields:
    </div>

Host Name:    <Host Name>

IP Address:    <IP Address>

User Name:    <User Name>

  1. <div style="text-align: justify">
      To add more you can select Fields, and Add. If there is a field that you may need, that isn&#8217;t selectable from the defaults you can also query Environment Variables, Registry and WMI by clicking on the Custom button. We are sticking with the defaults so click Apply to review changes.
    </div>

  2. <div style="text-align: justify">
      We want to also replace the Background so it isn&#8217;t the default – Black color – so click on Background…
    </div>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi5.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      Because this will be rolled out to multiple users, we either need to have a BMP or JPG that will be on every single computer in the same location or accessible to all authenticated users on the network. We will be going with option 2 – using the domains namespace, and net logon folder to store BGInfo and the wallpaper. Copy the Wallpaper you want to an easily accessible share that authenticated users have Read access too. I am using a Wallpaper folder, under the Net Logon folder.
    </div>

  2. <div style="text-align: justify">
      Select navigate to: \\DOMAIN\netlogon\Wallpaper\Desktop.jpg and select Stretch as the Wallpaper position and click Ok.
    </div>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi6.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      For future wallpaper changes. This will need to be modified again to point towards the newest wallpaper. Click Apply
    </div>

  2. <div style="text-align: justify">
      Verify that the settings are correct and it looks ok. If so now we need to save the configuration so it can be reused – click on File and select Save As.
    </div>

  3. <div style="text-align: justify">
      Name it: config.bgi
    </div>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi7.png?w=1500" alt="" data-recalc-dims="1" />

  1. <div style="text-align: justify">
      Restart your computer to lose the changes and you can now test the configuration file from the Command Line, open PowerShell or Command Prompt <em>(as a normal user)</em> and navigate to the place where the BGInfo executable and you have saved the configuration file too and type:
    </div>

bginfo.exe config.bgi /accepteula /silent /timer 0

  1. <div style="text-align: justify">
      Press Enter and that should force BGInfo to load with your changes without any user prompt.
    </div>

## <span id="How_do_I_deploy_BGInfo_package">How do I deploy BGInfo package?</span>

Use the following guide to deploy the BG Info package. Because this is a user based application and needs to run under user context on login, we are going to use a logon script using a user based group policy – for specific users only.

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Open Active Directory Users and Computers and create an application group to assign users too that you want to have the BGInfo wallpaper – for example _APP_BGInfo and add your user account to that group.
    </div>
  </li>
  
  <li>
    Open Group Policy Management tool using an account that has access to create Group Policies and right click on the OU with your user account or Computer – if you have Loopback enabled and select Create a GPO in this domain, and Link it here…
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi8.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    Specify a name for the Group Policy, such as BgInfo-UserPolicy –and click Ok
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi9.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Right click and Policy and select Edit…
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Navigate to: User Configuration\Policies\Windows Settings\
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Click on: Scripts (Logon/LogOff)
    </div>
  </li>
  
  <li>
    Double click Logon to open the Logon Properties
  </li>
  <li>
    I prefer to keep my scripts, source files replicated across Domain Controllers and located in the same location as my Group Policy – so click Show Files…
  </li>
</ol>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi10.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Copy your BGInfo executable and configuration file into the folder. If you get errors, you may need to launch Explorer or map a drive using Domain Admin credentials which usually has write access to the SYSVOL.
    </div>
  </li>
</ol>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi11.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Now we need to create a batch script, that will be ran by the group policy to launch BGInfo. Right click a blank space in the folder and select New, Text Document
    </div>
  </li>
</ol>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi12.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Rename file to: Run_BGInfo.bat
    </div>
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi13.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Right click bat file and Open with, Notepad
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Go back to Windows Explorer; we now need to get the Group Policy location/path. Right Click on the Address pane and select &#8216;Copy as Text&#8217;
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Enter in the following detail (the <a href="///\\DOMAIN">\\DOMAIN</a> till the Logon path is the location of your Group Policy, copied from Step 13) and click Save:
    </div>
  </li>
</ol>

@echo off

<p style="margin-left: 21pt">
  \\DOMAIN\SysVol\luke.geek.nz\Policies\{8BBCd98E-4907-4D45-B662-8034A55B0352}\User\Scripts\Logon\Bginfo.exe \\DOMAIN\SysVol\luke.geek.nz\Policies\{8BBCd98E-4907-4D45-B662-8034A55B0352}\User\Scripts\Logon\config.bgi /accepteula /silent /timer 0
</p>

<p style="margin-left: 21pt">
  Exit
</p>

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Double click the Run_BGInfo.bat to confirm it works, and if not modify the batch script to work – it needs to point towards the exact BGInfo and configuration file and to avoid extra spaces it may be best to run it on the same line with a space between BgInfo.exe and the path to the configuration file only.
    </div>
  </li>
</ol>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi14.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Once it has confirmed working, go back to the Group Policy created in Step 3 and before we add the script we need to set the Scope so the policy doesn&#8217;t affect users that are not supposed to be get the BGInfo wallpaper.
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Under the Scope tab, remove Authenticated Users from the Security Filtering and add the Active Directory group created earlier – ie _APP_BGInfo – also check the Delegation Tab and make sure Authenticated Users is added for Read Rights.
    </div>
  </li>
</ol>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi15.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt">
  <li>
    <div style="text-align: justify">
      Now right click the BGInfo group policy – select Edit and navigate back to: User Configuration\Policies\Windows Settings\
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Click on: Scripts (Logon/Logoff)
    </div>
  </li>
  
  <li>
    Double click Logon to open the Logon Properties
  </li>
  <li>
    <div style="text-align: justify">
      Click Add and Browse
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Select Run_BGInfo.bat and click Open and click Ok
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      You have now successfully created the User base policy that will run the Run_BGInfo.bat script on user logon
    </div>
  </li>
  
  <li>
    <div style="text-align: justify">
      Restart and verify that your Desktop wallpaper has now been changed. Other users of the Active Directory group will need to restart or Log off and back in &#8211; to pick up the changes.
    </div>
  </li>
</ol>

<p style="text-align: justify">
  <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi16.png?w=1500" alt="" data-recalc-dims="1" />
</p>