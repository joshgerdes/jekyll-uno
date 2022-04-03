---
date: 2022-03-29 00:00:00 +1300
title: Azure Network Adapter - Implementation and Testing
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Azure Network Adapter, introduced in Windows Server 2019 _(and available in Windows Server 2022)_, allows standalone servers access to Microsoft Azure by creating a Point-to-Site connection into an Azure Virtual Network.

Although most organizations will implement expressroute or site-to-site connectivity through a physical or NVA _(Network Virtual Appliance)_ firewall or router, there may be times when you want to limit connectivity, stand up a PoC _(Proof of Concept)_ or need access to Azure services on a single server only, which is where the Azure Network Adapter comes into play.

In order to configure the Azure Network Adapter on Windows Server, we need to install [Windows Admin Center](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview "Windows Admin Center"); Windows Admin Center allows us to leverage modern ways of working _(integrates traditional Server Manager functionality with new server and Hybrid/Azure functionality)_ with Windows Server(s) and enables features such as [Storage Migration Services](https://docs.microsoft.com/en-us/windows-server/storage/storage-migration-service/overview "Storage Migration Service overview") and [Azure Network Adapter](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/use-azure-network-adapterhttps://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/use-azure-network-adapter "Use Azure Network Adapter to connect a server to an Azure Virtual Network").

The Windows Server 2022 _(called: UTILITY-P01)_ I am using is running from my home _(on-premises network)_ on a VMWare ESXi host.

My Azure network is sitting in: the 'Australia East' region.

### Install Windows Admin Center

There are a few deployment options when it comes to Windows Admin Center, the most common are:

* Standalone
* Gateway

Standalone deployment is for managing a small number of virtual machines, it is usually installed locally on users' endpoints.

A gateway installation is a more formal deployment, where the gateway has access to the servers it is managing, gateway installs are recommended when multiple users are accessing it.

Both options rely on the following protocols, HTTPS to the user displaying Windows Admin Center and WMI/PowerShell to the servers that it needs to manage, whether an Internet connection for Azure workloads or on-premises.

In this article, I am going to install Windows Admin Center as a Standalone _(on the same Windows Server 2022, that I will set up the Azure Network Adapter on, but this is not required)._

Although you can use a custom SSL cert _(and you should in production scenarios, particularly when using a trusted Gateway)_, for the purposes of this article I am going to generate a self-signed certificate _(this certificate can be changed by rerunning the setup file and changing the certificate thumbprint)_.

I will also install using the Windows Admin Center default TCP port of 6516, although this can be changed to suit your environment _(for example to 443)_, for Gateway servers using 6516 will stop any issues if already using TCP 443 for another service.

1. **Open PowerShell** as Administrator on your server
2. **Run** the following **commands** to download the latest version of Windows Admin Center to your Desktop and install it:

       #Download the msi file
       Invoke-WebRequest -Uri 'https://aka.ms/WACDownload' -OutFile "$env:USERPROFILE\Desktop\WinAdminCenter.msi"
       #install windows admin center
       $msiArgs = @('/i', "$env:USERPROFILE\Desktop\WinAdminCenter.msi", '/qn', '/L*v', 'log.txt', 'SME_PORT=6516', 'SSL_CERTIFICATE_OPTION=generate')
       Start-Process msiexec.exe -Wait -ArgumentList $msiArgs
3. ![](/uploads/install-windowsadmincenter.gif)
4. Once, installed let us start it, type in:

       #Runs WinAdminCenter
       Start-Process 'https://localhost:6516/'
5. 