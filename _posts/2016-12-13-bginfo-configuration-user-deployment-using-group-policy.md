---
title: 'BgInfo Configuration &amp; User Deployment using Group Policy'
permalink: /win/bginfo-configuration-user-deployment-using-group-policy/
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


Download BGInfo &#8211; <a href="https://technet.microsoft.com/en-us/sysinternals/bginfo.aspx" target="_blank">https://technet.microsoft.com/en-us/sysinternals/bginfo.aspx</a>


<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi2.png?w=1500" alt="" data-recalc-dims="1" />

Run and extract it to a folder – for example c:\temp\bginfo


<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi3.png?w=1500" alt="" data-recalc-dims="1" />


Run BGInfo, you will be prompted with the default configuration


<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi4.png?w=1500" alt="" data-recalc-dims="1" />


You can delete the Fields from the Black window, as applicable in this example we are just going to use x3 fields:


Host Name:    <Host Name>

IP Address:    <IP Address>

User Name:    <User Name>


To add more you can select Fields, and Add. If there is a field that you may need, that isn&#8217;t selectable from the defaults you can also query Environment Variables, Registry and WMI by clicking on the Custom button. We are sticking with the defaults so click Apply to review changes.


We want to also replace the Background so it isn&#8217;t the default – Black color – so click on Background…


<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi5.png?w=1500" alt="" data-recalc-dims="1" />


Because this will be rolled out to multiple users, we either need to have a BMP or JPG that will be on every single computer in the same location or accessible to all authenticated users on the network. We will be going with option 2 – using the domains namespace, and net logon folder to store BGInfo and the wallpaper. Copy the Wallpaper you want to an easily accessible share that authenticated users have Read access too. I am using a Wallpaper folder, under the Net Logon folder.



Select navigate to: \\DOMAIN\netlogon\Wallpaper\Desktop.jpg and select Stretch as the Wallpaper position and click Ok.


<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi6.png?w=1500" alt="" data-recalc-dims="1" />


For future wallpaper changes. This will need to be modified again to point towards the newest wallpaper. Click Apply

 Verify that the settings are correct and it looks ok. If so now we need to save the configuration so it can be reused – click on File and select Save As.

Name it: config.bgi

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi7.png?w=1500" alt="" data-recalc-dims="1" />


Restart your computer to lose the changes and you can now test the configuration file from the Command Line, open PowerShell or Command Prompt <em>(as a normal user)</em> and navigate to the place where the BGInfo executable and you have saved the configuration file too and type:

bginfo.exe config.bgi /accepteula /silent /timer 0

Press Enter and that should force BGInfo to load with your changes without any user prompt.


## <span id="How_do_I_deploy_BGInfo_package">How do I deploy BGInfo package?</span>

Use the following guide to deploy the BG Info package. Because this is a user based application and needs to run under user context on login, we are going to use a logon script using a user based group policy – for specific users only.


Open Active Directory Users and Computers and create an application group to assign users too that you want to have the BGInfo wallpaper – for example _APP_BGInfo and add your user account to that group.

Open Group Policy Management tool using an account that has access to create Group Policies and right click on the OU with your user account or Computer – if you have Loopback enabled and select Create a GPO in this domain, and Link it here…

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi8.png?w=1500" alt="" data-recalc-dims="1" />

Specify a name for the Group Policy, such as BgInfo-UserPolicy –and click Ok

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi9.png?w=1500" alt="" data-recalc-dims="1" />

Right click and Policy and select Edit…

Navigate to: User Configuration\Policies\Windows Settings\

Click on: Scripts (Logon/LogOff)
 
Double click Logon to open the Logon Properties

 I prefer to keep my scripts, source files replicated across Domain Controllers and located in the same location as my Group Policy – so click Show Files…

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi10.png?w=1500" alt="" data-recalc-dims="1" />

Copy your BGInfo executable and configuration file into the folder. If you get errors, you may need to launch Explorer or map a drive using Domain Admin credentials which usually has write access to the SYSVOL.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi11.png?w=1500" alt="" data-recalc-dims="1" />

Now we need to create a batch script, that will be ran by the group policy to launch BGInfo. Right click a blank space in the folder and select New, Text Document
 
<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi12.png?w=1500" alt="" data-recalc-dims="1" />

Rename file to: Run_BGInfo.bat

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi13.png?w=1500" alt="" data-recalc-dims="1" />

Right click bat file and Open with, Notepad
  
Go back to Windows Explorer; we now need to get the Group Policy location/path. Right Click on the Address pane and select ;Copy as Text

Enter in the following detail (the <a href="///\\DOMAIN">\\DOMAIN</a> till the Logon path is the location of your Group Policy, copied from Step 13) and click Save:

@echo off


\\DOMAIN\SysVol\luke.geek.nz\Policies\{8BBCd98E-4907-4D45-B662-8034A55B0352}\User\Scripts\Logon\Bginfo.exe \\DOMAIN\SysVol\luke.geek.nz\Policies\{8BBCd98E-4907-4D45-B662-8034A55B0352}\User\Scripts\Logon\config.bgi /accepteula /silent /timer 0

Exit

Double click the Run_BGInfo.bat to confirm it works, and if not modify the batch script to work – it needs to point towards the exact BGInfo and configuration file and to avoid extra spaces it may be best to run it on the same line with a space between BgInfo.exe and the path to the configuration file only.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi14.png?w=1500" alt="" data-recalc-dims="1" />

Once it has confirmed working, go back to the Group Policy created in Step 3 and before we add the script we need to set the Scope so the policy doesn&#8217;t affect users that are not supposed to be get the BGInfo wallpaper.
 
 Under the Scope tab, remove Authenticated Users from the Security Filtering and add the Active Directory group created earlier – ie _APP_BGInfo – also check the Delegation Tab and make sure Authenticated Users is added for Read Rights.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi15.png?w=1500" alt="" data-recalc-dims="1" />

Now right click the BGInfo group policy – select Edit and navigate back to: User Configuration\Policies\Windows Settings\
 
Click on: Scripts (Logon/Logoff)
 
Double click Logon to open the Logon Properties

Click Add and Browse
 
Select Run_BGInfo.bat and click Open and click Ok
 
You have now successfully created the User base policy that will run the Run_BGInfo.bat script on user logon
 
Restart and verify that your Desktop wallpaper has now been changed. Other users of the Active Directory group will need to restart or Log off and back in &#8211; to pick up the changes.
   
<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121216_0805_BgInfoConfi16.png?w=1500" alt="" data-recalc-dims="1" />
