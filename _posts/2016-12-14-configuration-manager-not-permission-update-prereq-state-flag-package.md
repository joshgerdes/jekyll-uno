---

title: Configuration Manager – Does not have permission to update the prereq or state flag of the package
permalink: /win/configuration-manager-not-permission-update-prereq-state-flag-package/
categories:
  - Windows
---
When attempting an upgrade of System Center Configuration Manager v1511 to 1606 I ran into issues relating to the permissions of the Security Scope in Configuration Manager under the account I was doing the upgrade under.

I also had issues enabling Automatic Client upgrade which was grayed out– after some research I found that it was due to the original Full Administrator account which was used by a contractor to do the SCCM environment installation had been deleted from Active Directory and had explicit ownership of All Scopes and Collections which was fixed by taking ownership of the Scope and Collections below.

_ConfigMgr Error Object:instance of SMS\_ExtendedStatus{ Description = &#8220;User \&#8221;DOMAIN\\User\&#8221; does not have permission to update the prereq or state flag of the package. &#8220;;               ErrorCode = 1112017920;      File = &#8220;e:\\nts\_sccm\_release\\sms\\siteserver\\sdk\_provider\\smsprov\\sspupdatepackages.cpp&#8221;;           Line = 435;              ObjectInfo = &#8220;2&#8221;;     Operation = &#8220;ExecMethod&#8221;;        ParameterInfo = &#8220;SMS\_CM\_UpdatePackages.PackageGuid=\&#8221;0D256560-ED2C-45B5-8D75-4D38AB3F758C\&#8221;&#8221;;           ProviderName = &#8220;WinMgmt&#8221;;          StatusCode = 2147749889;};_

<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0819_Configurati1.png?resize=594%2C387" alt="ConfigMgr Error Object" width="594" height="387" data-recalc-dims="1" />

In order to resolve this issue – I needed to make Changes to the Configuration Manager _(SCCM)_ SQL database. I don&#8217;t take responsibility for any damage this may cause and of course highly recommend doing this in Test first, and of course making sure a SQL backup has been done before hand.

1. Open SQL Management Studio with an account that has sysadmin permissions on your SCCM database – and connect to it.

2. Expand Databases, and locate your SCCM database. Right click your database and select New Query

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0819_Configurati2.png?w=1500" alt="" data-recalc-dims="1" />

3. Type in or Copy the following Query and Execute it:

<span style="font-family: Consolas; font-size: 9pt;"><span style="color: blue;">select </span><span style="color: gray;">*<span style="color: blue;">from </span><span style="color: teal;">RBAC_ADMINS<br /> </span></span></span>4. You should now get all the specified Administrators for SCCM role based Full Administrator group; this includes LogonName, DisplayName and their CreatedBy and Created Date

5. Now we need to set the correct permissions on the Security Scope – find the account you want to make Full Administrator _(best practice would indicate – this should be an Active Directory group, which your account is then a member of to avoid future problems)_ and note down the AdminID of your account

6. Clear the Query box and type in:

<span style="font-family: Consolas; font-size: 9pt;"><span style="color: fuchsia;">Update </span><span style="color: teal;">v_securedScopePermissions </span></span><span style="font-family: Consolas; font-size: 9pt;"><span style="color: blue;">Set </span><span style="color: teal;">categoryid<span style="color: gray;">=<span style="color: red;">&#8216;sms00all&#8217; </span><span style="color: blue;">where </span><span style="color: teal;">adminid<span style="color: gray;">=</span><ADMINID></span><br /> </span></span></span>

7. Replace <ADMINID> with the number of your account, Admin ID without the <>.

8. When you are ready to make the change, click Execute

9. You have now successfully gained Full Administrator permissions over all Scopes and Permissions. Close the SCCM console and relaunch and you should now be able to do the upgrade or enable Automatic client upgrade.
