---
title: Using PowerShell to set up Automatic Login on Windows Servers
categories:
  - Windows
date: 2016-04-30 00:00:00 +1300
header:
  teaser: "images/powershell-blog-feature-banner.png"
---
Some server based applications require to be logged into a service account to allow an Application or service to run, These applications usually require manual intervention by systems administrators to login to the account manually after a server restart.

There are many ways to setup Automatic Logon, using _&#8220;control userpasswords2_&#8221; via the Run Prompt, using Third Party utilities like _LogonExpert_ or_ Sysinternals Autologon for Windows  _this simply using RegEdit and setting them manually.

I have created a PowerShell script for editing the registry to set this manually in a standardized way and could be run remotely. It is pretty simple and only requires version 1 of PowerShell.

{% highlight PowerShell %}

#Author: Luke Murray (Luke.Geek.NZ)
#Version: 0.1
#Purpose:

#The purpose of this PowerShell script is to set the AutoLogon and WinLogon registry strings using PowerShell, to setup a Windows Server #or Workstation for Automatic Logon.
#The $UserName and $Password variables need to be configuration for your environment. Please make sure the $UserName variables follows #DOMAINNAME\SAMACCOUNTNAME format.
#This needs to be ran using an Elevated PowerShell ISE or PowerShell window (with Admin access on the computer you are running this on).

$usrname = 'DOMAINNAME\SAMACCOUNTNAME'
$password = 'PASSWORD'
$RegistryLocation = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
Set-ItemProperty $RegistryLocation -Name 'AutoAdminLogon' -Value '1'
Set-ItemProperty $RegistryLocation -Name 'DefaultUsername' -Value "$usrname"
Set-ItemProperty $RegistryLocation -Name 'DefaultPassword' -Value "$password"

{% endhighlight %}

Note: Also note following this method, the username and password are not encrypted and stored as plain text in the registry.
