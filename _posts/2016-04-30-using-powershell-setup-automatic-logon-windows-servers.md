---
id: 3690
title: Using PowerShell to setup Automatic Logon on Windows Servers
date: 2016-04-30T15:17:36+00:00
author: Luke
layout: post
guid: http://luke.geek.nz/?p=3690
permalink: /win/using-powershell-setup-automatic-logon-windows-servers/
post_views_count:
  - "107"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4790377508"
categories:
  - Windows
---
Some &#8216;server based&#8217; applications require to be logged into into a service account to allow an Application or service to run, These applications usually require manual intervention by systems administrators to login to the account manually after a server restart.

There are many ways to setup Automatic Logon, using _&#8220;control userpasswords2_&#8221; via the Run Prompt, using Third Party utilities like _LogonExpert_ or_ SysInternals Autologon for Windows  _this simply using RegEdit and setting them manually.

I have created a PowerShell script for editing the registry to set this manually in a standardized way and could be ran remotely. It is pretty simple and only requires version 1 of PowerShell.

&nbsp;

<!--more-->

<pre class="lang:ps decode:true ">&lt;#

Author: Luke Murray (Luke.Geek.NZ)
Version: 0.1
Purpose:

The purpose of this PowerShell script is to set the AutoLogon and WinLogon registry strings using PowerShell, to setup a Windows Server or Workstation for Automatic Logon.
The $UserName and $Password variables need to be configuration for your environment. Please make sure the $UserName variables follows DOMAINNAME\SAMACCOUNTNAME format.

This needs to be ran using an Elevated PowerShell ISE or PowerShell window (with Admin access on the computer you are running this on).

#&gt;

$usrname = 'DOMAINNAME\SAMACCOUNTNAME'
$password = 'PASSWORD'
$RegistryLocation = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
Set-ItemProperty $RegistryLocation -Name 'AutoAdminLogon' -Value '1'
Set-ItemProperty $RegistryLocation -Name 'DefaultUsername' -Value "$usrname"
Set-ItemProperty $RegistryLocation -Name 'DefaultPassword' -Value "$password"</pre>

<p style="background: white">
  Feel free to let me know your thoughts in the comments below, this could easily be modified to run in a PowerShell window and prompt for username/password without editing the file manually using Read-Host.
</p>

<p style="background: white">
  Note: Also note following this method, the username and password are not encrypted and stored as plain text in the registry.
</p>