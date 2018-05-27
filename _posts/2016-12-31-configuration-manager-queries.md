---
title: Configuration Manager Queries
layout: post
permalink: /win/configuration-manager-queries/
categories:
  - Windows
---
One of the best uses of Configuration Manager is its ability to query and actually make use of the data in a dynamic and automated way.

This is just a quick post with a few Configuration Manager WQL queries I have created or collected that may be useful to someone.

Feel free to use them, change them to suit your needs and share your own!

If you don't know how to use these – check the bottom of the post for links to TechNet.

   
### <span id="Collection_Based_Dynamic_Rules">Collection Based Dynamic Rules:</span>

##### <span id="Get_Windows_7_Enterprise_x64_Devices_matching_a_specific_naming_convention">Get Windows 7 Enterprise x64 Devices matching a specific naming convention:</span>

{% highlight sql %}

select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System inner join SMS_G_System_SYSTEM on SMS_G_System_SYSTEM.ResourceID = SMS_R_System.ResourceId inner join SMS_G_System_OPERATING_SYSTEM on SMS_G_System_OPERATING_SYSTEM.ResourceID = SMS_R_System.ResourceId inner join SMS_G_System_COMPUTER_SYSTEM on SMS_G_System_COMPUTER_SYSTEM.ResourceId = SMS_R_System.ResourceId where SMS_G_System_OPERATING_SYSTEM.Caption = "Microsoft Windows 7 Enterprise" and SMS_G_System_COMPUTER_SYSTEM.SystemType = "x64-based PC" and SMS_G_System_SYSTEM.Name like "HOSTNAME%"

{% endhighlight %}

##### <span id="Devices_in_a_specific_OU">Devices in a specific OU:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true ">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System where SMS_R_System.SystemOUName = "Atlantis.local/Atlantis/WORKSTATIONS/PRODUCTION"
</pre>

##### <span id="Devices_that_have_a_specific_Hotfix_installed">Devices that have a specific Hotfix installed:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System inner join SMS_G_System_QUICK_FIX_ENGINEERING on SMS_G_System_QUICK_FIX_ENGINEERING.ResourceId = SMS_R_System.ResourceId where SMS_G_System_QUICK_FIX_ENGINEERING.HotFixID = "KB2520155"</pre>

##### <span id="Devices_which_are_Bitlocker_encrypted">Devices which are Bitlocker encrypted:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System inner join SMS_G_System_BITLOCKER_DETAILS on SMS_G_System_BITLOCKER_DETAILS.ResourceID = SMS_R_System.ResourceId inner join SMS_G_System_OPERATING_SYSTEM on SMS_G_System_OPERATING_SYSTEM.ResourceId = SMS_R_System.ResourceId where SMS_G_System_BITLOCKER_DETAILS.ProtectionStatus = 1</pre>

##### <span id="Devices_which_have_ran_a_Software_Metering_Rule_in_the_last_x60_days">Devices which have ran a Software Metering Rule in the last x60 days:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_SYSTEM inner join SMS_MonthlyUsageSummary on SMS_R_SYSTEM.ResourceID = SMS_MonthlyUsageSummary.ResourceID    INNER JOIN SMS_MeteredFiles ON SMS_MonthlyUsageSummary.FileID = SMS_MeteredFile.MeteredFileID    WHERE DateDiff(day, SMS_MonthlyUsageSummary.LastUsage, GetDate()) &lt; 60  AND SMS_MeteredFiles.RuleID = 16777421</pre>

##### <span id="Devices_that_have_Visual_Studio_Premium_2013_installed">Devices that have Visual Studio Premium 2013 installed:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System inner join SMS_G_System_ADD_REMOVE_PROGRAMS on SMS_G_System_ADD_REMOVE_PROGRAMS.ResourceID = SMS_R_System.ResourceId where SMS_G_System_ADD_REMOVE_PROGRAMS.DisplayName like "Microsoft Visual Studio Premium 2013" order by SMS_R_System.Name</pre>

##### <span id="Devices_that_are_a_member_of_a_specific_Active_Directory_group">Devices that are a member of a specific Active Directory group:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System where SMS_R_System.SecurityGroupName = 'ATLANTIS\\GROUPNAME'</pre>

### <span id="Query_Based_Dynamic_Rules">Query Based Dynamic Rules:</span>

##### <span id="Devices_which_are_Bitlocker_encrypted-2">Devices which are Bitlocker encrypted:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select SMS_R_System.Name, SMS_G_System_OPERATING_SYSTEM.Caption, SMS_G_System_COMPUTER_SYSTEM.Model, SMS_R_System.LastLogonUserName from  SMS_R_System inner join SMS_G_System_BITLOCKER_DETAILS on SMS_G_System_BITLOCKER_DETAILS.ResourceID = SMS_R_System.ResourceId inner join SMS_G_System_OPERATING_SYSTEM on SMS_G_System_OPERATING_SYSTEM.ResourceID = SMS_R_System.ResourceId inner join SMS_G_System_COMPUTER_SYSTEM on SMS_G_System_COMPUTER_SYSTEM.ResourceID = SMS_R_System.ResourceId where SMS_G_System_BITLOCKER_DETAILS.ProtectionStatus = 1 order by SMS_R_System.Name</pre>

##### <span id="Get_users_Primary_devices_from_User_based_group">Get users Primary devices from User based group:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">Select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client, SMS_R_User.UniqueUserName
FROM SMS_R_System
JOIN SMS_UserMachineRelationship ON SMS_R_System.Name=SMS_UserMachineRelationship.MachineResourceName
JOIN SMS_R_User ON SMS_UserMachineRelationship.UniqueUserName=SMS_R_User.UniqueUserName
Where SMS_R_User.UniqueUserName in (select UniqueUserName from SMS_R_User where UserGroupName = "ATLANTIS\\UsersGroupName")</pre>

##### <span id="Show_Devices_and_Users_of_a_limited_Collection">Show Devices and Users of a limited Collection:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select distinct SMS_R_System.LastLogonUserName, SMS_R_System.Name, SMS_R_System.LastLogonUserDomain, SMS_R_System.LastLogonTimestamp, SMS_R_System.IPAddresses from  SMS_R_System order by SMS_R_System.IPAddresses</pre>

##### <span id="Get_Identical_MAC_addresses">Get Identical MAC addresses:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select distinct *  from  SMS_R_System where SMS_R_System.MACAddresses = "50:1a:c5:ff:10:88"</pre>

##### <span id="Get_a_list_of_hardware_Models_that_exist">Get a list of hardware Models that exist:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true">select distinct SMS_G_System_COMPUTER_SYSTEM.Manufacturer, SMS_G_System_COMPUTER_SYSTEM.Model from  SMS_R_System inner join SMS_G_System_COMPUTER_SYSTEM on SMS_G_System_COMPUTER_SYSTEM.ResourceID = SMS_R_System.ResourceId</pre>

##### <span id="Get_a_list_of_Webcam_models">Get a list of Webcam models:</span>

<pre class="nums:false nums-toggle:false wrap:true lang:default decode:true ">select SMS_R_System.Name, SMS_G_System_USB_DEVICE.Caption from  SMS_R_System inner join SMS_G_System_USB_DEVICE on SMS_G_System_USB_DEVICE.ResourceID = SMS_R_System.ResourceId where SMS_G_System_USB_DEVICE.Caption like "%CAM%" order by SMS_R_System.Name</pre>

### <span id="Resources">Resources:</span>

How to Create Queries in Configuration Manager &#8211; <a href="https://technet.microsoft.com/en-us/library/gg712323.aspx" target="_blank">https://technet.microsoft.com/en-us/library/gg712323.aspx</a>

How to Create Collections in Configuration Manager &#8211; <a href="https://technet.microsoft.com/en-us/library/gg712295.aspx" target="_blank">https://technet.microsoft.com/en-us/library/gg712295.aspx</a>
