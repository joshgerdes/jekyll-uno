---
date: 2022-04-03 00:00:00 +1300
title: Azure Network Adapter - Implementation and Testing
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
Azure Network Adapter, introduced in Windows Server 2019 _(and available in Windows Server 2022)_, allows standalone servers access to Microsoft Azure by creating a Point-to-Site connection into an Azure Virtual Network.

Although most organizations will implement expressroute or site-to-site connectivity through a physical or NVA _(Network Virtual Appliance)_ firewall or router, there may be times when you want to limit connectivity, stand up a PoC _(Proof of Concept)_ or need access to Azure services on a single server only, which is where the Azure Network Adapter comes into play.

In order to configure the Azure Network Adapter on Windows Server, we need to install [Windows Admin Center](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview "Windows Admin Center"){:target="_blank"}; Windows Admin Center allows us to leverage modern ways of working _(integrates traditional Server Manager functionality with new server and Hybrid/Azure functionality)_ with Windows Server(s) and enables features such as [Storage Migration Services](https://docs.microsoft.com/en-us/windows-server/storage/storage-migration-service/overview "Storage Migration Service overview"){:target="_blank"} and [Azure Network Adapter](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/use-azure-network-adapter "Use Azure Network Adapter to connect a server to an Azure Virtual Network"){:target="_blank"}.

The Windows Server 2022 _(called: UTILITY-P01)_ I am using is running from my home _(on-premises network)_ on a VMWare ESXi host.

My Azure network is sitting in: the 'Australia East' region.

> This feature is still in Preview, and compatibility between the API versions and other errors or issues may still be worked on by Microsoft. Keep this in mind, functionality may change, so be wary of using this in a production scenario.

### Install Windows Admin Center

There are a few deployment options when it comes to Windows Admin Center. The most common are:

* Standalone
* Gateway

Standalone deployment is for managing a small number of virtual machines, and it is usually installed locally on users' endpoints.

A gateway installation is a more formal deployment, where the gateway has access to the servers it is managing; gateway installs are recommended when multiple users are accessing it.

Both options rely on the following protocols, HTTPS to the user displaying Windows Admin Center and WMI/PowerShell to the servers that it needs to manage, whether an Internet connection for Azure workloads or on-premises.

In this article, I am going to install Windows Admin Center as a Standalone _(on the same Windows Server 2022, that I will set up the Azure Network Adapter on, but this is not required)._

Although you can use a custom SSL cert _(and you should use in production scenarios, mainly when using a trusted Gateway)_, for this article I am going to generate a self-signed certificate _(this certificate can be changed by rerunning the setup file and changing the certificate thumbprint)_.

I will also install using the Windows Admin Center default TCP port of 6516; although this can be changed to suit your environment _(for example, to 443)_, for Gateway servers using 6516 will stop any issues if you are already using TCP 443 for another service.

1. **Open PowerShell** as Administrator on your server
2. **Run** the following **commands** to download the latest version of Windows Admin Center to your Desktop and install it:

       #Download the msi file
       Invoke-WebRequest -Uri 'https://aka.ms/WACDownload' -OutFile "$env:USERPROFILE\Desktop\WinAdminCenter.msi"
       #install windows admin center
       $msiArgs = @('/i', "$env:USERPROFILE\Desktop\WinAdminCenter.msi", '/qn', '/L*v', 'log.txt', 'SME_PORT=6516', 'SSL_CERTIFICATE_OPTION=generate')
       Start-Process msiexec.exe -Wait -ArgumentList $msiArgs
3. ![Windows Admin Center -Installation](/uploads/install-windowsadmincenter.gif)
4. Once installed, let us start it. Type in:

       Start-Process 'https://localhost:6516' -WindowStyle Maximized
5. ![Windows Admin Center -Run](/uploads/start-windowsadmincenter.gif)
6. Finally, after you have confirmed Windows Admin Center is installed, you can run the following to delete the setup file.

       ## Remove the msi file
       Remove-Item -Path "$env:USERPROFILE\Desktop\WinAdminCenter.msi"

### Setup Azure Network Adapter

#### Register Windows Admin Center with Microsoft Azure

 1. **Open Windows Admin Center** _(ie https://localhost:6516/)_ in your favourite browser.
 2. **Select** the **server** you want to install Azure Network Adapter on, and select **Connect**
 3. **Enter** in any applicable **credentials**
 4. ![Windows Admin Center - Azure Network Adapter Setup](/uploads/select-wac_server.png)
 5. On the upper right-hand side _(not the bottom)_, click on the **Cog** 
 6. ![Windows Admin Center - Azure Network Adapter Setup](/uploads/select-wac_settings.png)
 7. Navigate down to **Register**, under the Gateway heading.
 8. Click **Register** _(the account you use to Register with Azure, needs rights to be able to create an Azure Service Principal)_
 9. ![Windows Admin Center - Azure Registration](/uploads/select-wac_serverregister.png)
10. Make sure that **Azure Global** is **selected** _(this is applicable for most scenarios, but if not select the Cloud that you need to connect to)_
11. Click **Copy**
12. **Click** on the **link** under '3' **Enter** the **Code**
13. **Enter** in the **Code** and press **Enter**
14. **Enter** your **Azure Credentials** to verify connectivity
15. Finally, **make sure** that your **Azure Active Directory** Tenant **ID matches** the correct **tenancy**. You can reuse an existing Azure Application/Service Principal, but in my case, I am, going to let Windows Admin Center create it for me and select **Connect**.
16. ![Windows Admin Center - Azure Application/Service Principal Setup](/uploads/select-wac_serverregisterazapp.png)
17. Then select **Sign In**
18. **Select Accept**.

#### Configure Azure Network Adapter

 1. **Open Windows Admin Center** _(ie https://localhost:6516/)_ in your favourite browser.
 2. **Select** the **server** you want to install Azure Network Adapter on, and select **Connect**
 3. **Enter** in any applicable **credentials**
 4. Select **Azure hybrid center**
 5. Select Setup, under **Azure Network Adapter**
 6. ![Windows Admin Center - Azure Network Adapter Setup](/uploads/select-wac_aznetworkadaptersetup.png)
 7. Select your **Subscription**, **Region** and **Virtual Network**
 8. If you don't already have a [GatewaySubnet](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings#gwsub "VPN Gateway configuration "){:target="_blank"} configured, Windows Admin Center will do that for you, as well as a [Gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings#gwsku "VPN Gateway configuration "){:target="_blank"}.
 9. For: **Client Address Space**, this is where you need to **create** a new **subnet** that doesn't match your existing on-premises and Azure subnets, that the server will connect using when connected via the Point to Site VPN. Make sure the subnet is large enough for all point to site clients. Because my on-premises is: '192.168.1.0/24' and my Azure network is '10.100.0.0/16' - my Client Address space will be: 172.0.0.0/24.
10. ![Windows Admin Center - Azure Network Adapter Setup](/uploads/select-wac_aznetworkadaptersetupgwnetwork.png)
11. The Azure Network Adapter uses certificates to authenticate the VPN connection to Azure, if you have your own PKI _(Public Key Infrastructure)_ [certificate authority](https://docs.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/server-certificate-deployment "Server Certificate Deployment"){:target="_blank"}, I recommend you use this. In this guide, I am going to leave it to auto-generate a self-signed root and client certificate_(these are Computer certificates, not used based)_.
12. Click **Create**
13. Windows Admin Center will now leverage the Azure Application created earlier to **create** the **GatewaySubnet** _(if missing)_ and create the Virtual Network **Gateway**, this creation **process** could take **up to 35 minutes**, so we now need to wait.
14. ![Windows Admin Center - Notification](/uploads/select-wac_aznetworkadapternotification.png)
15. You should be able to see the Gateway being created in the Azure Portal _(ie a new Virtual Network Gateway named: WAC-Created-vpngw-79)_ was created.
16. After a while, you should get a notification that the point to site connection, was successful (if not click on **+ Add Azure Network Adapter**, and rerun the deployment)
17. ![Windows Admin Center - Connected](/uploads/select-wac_aznetworkadapterconnected.png)

#### Testing Azure Network Adapter

* The VPN was established automatically, after a server restart.

* If I do a '_route print_', I can see my Azure App Servers subnet: 10.100.2.0, is available through the VPN interface.

  ![Route Print](/uploads/wac-networkadapter-routeprint.gif)
* I was able to successfully RDP to an Azure VM using the private IP

  ![Windows Network Adapter - RDP](/uploads/wac-networkadapter-vmrdp.gif)

#### Additional Notes

* Do not add Custom Routes _(ie for Service Endpoints)_ to the Virtual Network Gateway, the API used to create the Custom Routes, isn't compatible with the Azure Network Adapter yet. I added some custom routes into the Azure Virtual Network Gateway using the 'Set-AzVirtualNetworkGateway' cmdlet and was unable to add the Azure Network Adapter until the custom routes were removed. 
* Deleting the Azure Network Adapter connection from Windows Admin Center, will not delete the Virtual Network Gateway, this needs to be deleted manually to avoid any additional cost - if not required.
* If you have a naming convention, make sure that the Virtual Network Gateway has been created ahead of time, there is no current way to specify a custom name for the Gateway within the Windows Admin Center experience.