---
date: 2021-03-25 00:00:00 +1300
title: Installing the RSAT (Remote Server Administration Tools for Windows 10) tools
  using PowerShell
author: Luke
categories: []
toc: false

---
Installing the RSAT (Remote Server Administration Tools for Windows 10) tools using PowerShell. This is just a quick article, written purely as an easy reference.

In the age of the cloud and work from anywhere, Windows 10 allows you easily, install the Remote Server Administration Tools using PowerShell, sometimes (like me) you need these tools not to actually use them - but for the PowerShell modules that come with them to work on scripts locally.

Note: This needs to be run from an elevated PowerShell console (ie ran as Administrator). You can check this using the following:

    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

If it returns:

* False - You are not in an elevated PowerShell window and will have to relaunch as Administrator
* True - You are all set to go and can continue...

To get a list of all the Remote Server Administration tools you can install run the following:

    Get-WindowsCapability -Name RSAT.* -Online

The versions as of the time this article was written are:

* Rsat.ActiveDirectory.DS-LDS.Tools\~\~\~\~0.0.1.0
* Rsat.BitLocker.Recovery.Tools\~\~\~\~0.0.1.0
* Rsat.CertificateServices.Tools\~\~\~\~0.0.1.0
* Rsat.DHCP.Tools\~\~\~\~0.0.1.0
* Rsat.Dns.Tools\~\~\~\~0.0.1.0
* Rsat.FailoverCluster.Management.Tools\~\~\~\~0.0.1.0
* Rsat.FileServices.Tools\~\~\~\~0.0.1.0
* Rsat.GroupPolicy.Management.Tools\~\~\~\~0.0.1.0
* Rsat.IPAM.Client.Tools\~\~\~\~0.0.1.0
* Rsat.LLDP.Tools\~\~\~\~0.0.1.0
* Rsat.NetworkController.Tools\~\~\~\~0.0.1.0
* Rsat.NetworkLoadBalancing.Tools\~\~\~\~0.0.1.0
* Rsat.RemoteAccess.Management.Tools\~\~\~\~0.0.1.0
* Rsat.RemoteDesktop.Services.Tools\~\~\~\~0.0.1.0
* Rsat.ServerManager.Tools\~\~\~\~0.0.1.0
* Rsat.Shielded.VM.Tools\~\~\~\~0.0.1.0
* Rsat.StorageMigrationService.Management.Tools\~\~\~\~0.0.1.0
* Rsat.StorageReplica.Tools\~\~\~\~0.0.1.0
* Rsat.SystemInsights.Management.Tools\~\~\~\~0.0.1.0
* Rsat.VolumeActivation.Tools\~\~\~\~0.0.1.0
* Rsat.WSUS.Tools\~\~\~\~0.0.1.0

To install ALL the RSAT Tools run the following:

    Get-WindowsCapability -Name RSAT.* -Online | Add-WindowsCapability -Online

To only install ONLY the Active Directory Users & Computers Remote Administration tool run the following command:

    Get-WindowsCapability -Name RSAT.ActiveDirectory* -Online | Add-WindowsCapability -Online

To only install ONLY the Group Policy Management Remote Administration tool run the following command:

    Get-WindowsCapability -Name RSAT.GroupPolicy* -Online | Add-WindowsCapability -Online