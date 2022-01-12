---
date: 2022-01-11 00:00:00 +1300
title: Create Azure Point to Site VPN using Azure Active Directory authentication
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
You may be working remotely or only have a few devices needing access to your resources in Azure; a solution that can be deployed is a point to site connection straight into your Microsoft Azure network.

This functionality allows your computer to connect privately to resources over a secure tunnel using your internet connection, using an Azure Virtual Network gateway, you can seamlessly connect to resources without the need of opening up your resources to the internet or having to whitelist your _(or third party vendor)_ IP address, which may change daily.

Using Azure Active Directory, you know only your specified users access your Azure resources.

You can have a site to site and point to site VPN running on the same Gateway today. We will set up a Point to Site VPN using Windows 11.

![](/uploads/hl_azurep2s.png)

Depending on the SKU of your Virtual Network Gateway, depends on the number of concurrent connections and throughput you are allowed; because we are using Azure Active Directory and the OpenVPN protocol, I will be selecting Generation 1, VpnGw1, supporting a max of 250 connections _(you can double the number of throughput and connections if you are running in Active/Active and have a second gateway, or select a higher SKU)_.

> Azure AD authentication is supported for OpenVPN® protocol connections only and requires the Azure VPN client.

A note about Gateway SKUs _(apart from Basic)_ you can resize in the same generation _(i.e. Generation 1 VpnGw1 to VpnGw3, but you can't go from Generation 1 VpnGw1 to Generation 2 VpnGw5, in order to upgrade, you have to delete and recreate the Gateway, just keep this in mind when deciding on the SKU of your resources_).

You can read more about the Virtual Network Gateways and VPN SKUs at the official Microsoft documentation '[here'](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways "What is VPN Gateway?"); your Gateway SKU may differ depending on your requirements.

### Create Azure Point to Site VPN using Azure Active Directory authentication

#### Prerequisites

* An Azure subscription _(that you have at least contributor rights to and the ability to create Users and Groups)_
* An endpoint device running Windows 10 or 11 that you can install the [Azure VPN client](https://www.microsoft.com/en-us/p/azure-vpn-client-preview/9np355qt2sqb?rtc=2&activetab=pivot:overviewtab " Azure VPN Client") onto

#### Create Virtual Network

First things first, let's create a Virtual Network.

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Click on **+ Create a resource**
 3. Search for: **Virtual Network** and click on it
 4. Click **Create**
 5. **Select** or create your **Resource Group** that you want your network resource to sit in _(I recommend Virtual Network and the gateway resources sit in its own Resource Group away from other resources so that they can be protected by resource locks, RBAC and they are usually classified as a shared resource)_.
 6. ![](/uploads/azureportal-createvirtualnetwork.png)
 7. Click **Next: IP Addresses**
 8. Now we need to **define** the **Address space** and subnets; I will leave the Address space as 10.0.0.0/16 but remove the Default subnet _(select the checkbox next to the Subnet and select Delete)_
 9. Click +**Add Subnet**, and add a new subnet with the name of GatewaySubnet with an IP range of: 10.0.1.0/27 _(this Subnet will be used by our Virtual Network Gateway, and the name needs to be exactly GatewaySubnet)_.
10. Now I will add a subnet named: app servers, for the Virtual Machines I will need to connect to will be placed.
11. ![](/uploads/azureportal-createvirtualnetworksubnets.png)
12. Click **Next: Security**
13. Leave everything _(BastionHost, DDoS Protection Standard, Firewall)_ as Disabled.
14. Click **Next: Tags**
15. Enter in any tags and click **Review + Create**
16. Review your configuration and click **Create**

#### Create Virtual Network Gateway

Now that we have the foundation of our setup - an Azure Virtual Network, it is time to provision the Gateway itself; just a note before we continue, the Gateway can take 30-60 minutes to provision.

 1. Log in to the [Azure Portal](https://portal.azure.com/#home "Azure Portal")
 2. Click on **+ Create a resource**
 3. Type in and search for: **Virtual Network Gateway**
 4. Click **Create**
 5. Type in the **name** of your Azure Virtual Network **Gateway**
 6. Select the **region** _(it must be the same region as your virtual network)_
 7. Select the Gateway Type: **VPN**
 8. The VPN type is: **Route-based**
 9. **Select** the **SKU**, in this example - I will be going with VpnGw1
10. **Select** the **Generation** of the Virtual Network Gateway; I am going with: Generation 1
11. **Select** the **Virtual Network** that you created earlier, and it will automatically find and assign the Gateway to the Subnet named: GatewaySubnet
12. **Select** Standard **public IP** address **SKU**
13. **Select Public IP** address and select: **Create new**
14. **Type** in your public IP **name**
15. **Leave** 'Enable active-active mode' and 'Configure BGP' as **Disabled**.
16. Click **Review + Create**
17. ![](/uploads/azureportal-createvnetfgw.png)
18. **Verify configuration** is correct and clicks **Create**
19. It can take up to 30-60 minutes for the Virtual Network Gateway to be created.

#### Setup Azure Active Directory authentication on the Virtual Network Gateway

Now that the Virtual Network has been created, we can now set up Azure Active Directory authentication.

##### Collect Azure Active Directory Tenant ID

First, we need to collect the Azure AD Tenancy ID

1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
2. Click on **Azure Active Directory**
3. In the Overview pane, **copy** the **Tenant ID** and save this for the next step.

##### Grant Azure VPN Client permisisons

Now we need to grant the Azure VPN application permissions.

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Open a new window and type in and press Enter:

        https://login.microsoftonline.com/common/oauth2/authorize?client_id=41b23e61-6c1e-4545-b367-cd054e0ed4b4&response_type=code&redirect_uri=https://portal.azure.com&nonce=1234&prompt=admin_consent
 3. If you get an error about external identity, then replace /**common**/ with your tenant ID.
 4. ![](/uploads/azureportal_azurevpnpermissions.png)
 5. Click **Accept**
 6. Navigate back to **Azure Active Directory**
 7. Select **Enterprise Applications**
 8. Select **Azure VPN**
 9. **Copy** the **Application ID** of the Azure VPN enterprise application _(you will need both Application ID and tenant ID for the next steps)_
10. ![](/uploads/azurevpn_enterpriseappvpn.png)

##### Configure Point to Site Connection

Now its time to configure the Virtual Network Gateway

 1. Log in to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. **Navigate** to the Virtual Network **Gateway** you created earlier
 3. Click on **Point-to-site configuration**
 4. Click **Configure now**
 5. Enter in your **address pool** _(this is the address pool of the VPN clients, make sure this doesn't overlap with any other IP range you use, I will go with: 172.0.0.0/16)_
 6. Make sure the Tunnel type is: **OpenVPN (SSL)**
 7. Select **Azure Active Directory** for the **Authentication** type
 8. For **Tenant, ID enter** in: https://login.microsoftonline.com/**TENANTID**/ and enter in your own Tenant ID.
 9. For the Audience (this is the users and groups that are assigned to the Enterprise Azure VPN application), put in the Application ID of the Azure VPN.
10. For the Issuer, enter in: https://sts.windows.net/**TENANTID**/
11. ![](/uploads/azure-point-to-site-configuration.png)
12. Click **Save**
13. It may take 1-5 minutes to save the configuration

##### Install and connect using the Azure VPN client

Now that the Point to Site VPN has been configured it's time to connect!

 1. Click on **Download VPN client** _(if it is greyed out, then navigate to the Overview pane, then back to the Point-to-site configuration)_.
 2. Extract the zip file, you will need these files
 3. **Download** the [**Azure VPN Client **](https://go.microsoft.com/fwlink/?linkid=2117554)to your computer.
 4. ![](/uploads/windowsstore-azurevpn.png)
 5. Once, downloaded click **Open.**
 6. Click the **+** sign (lower left)
 7. Click **Import**
 8. **Navigate** to the: **azurevpnconfig.xml** file that you downloaded earlier and click **Open**
 9. You can change the Connection Name to something more user friendly _(you can also edit the file directly for when you look at pushing out this to multiple users, but make sure you have a backup of the file)_
10. Click **Save**
11. ![](/uploads/azurevpnclient-beforeconnection.png)
12. Click **Connect**
13. Enter in your Azure Active Directory credentials _(you may be prompted for MFA, depending on the rules - you can use Azure VPN application under conditional access)_
14. ![](/uploads/azurevpnclient-afterconnection.png)
15. **You should now be connected to the Azure network through a point to site VPN!**
16. If I run 'ipconfig /all' on my device, I can see a PPP adapter that is connected and on the VPN address range created earlier: 172.0.0.2
17. ![](/uploads/azurevpn-ipconfig.png)
18. If I navigate back to the Point-to-site connection in the Azure Portal, I can see, my connection has been allocated:
19. ![](/uploads/azurevpn-p2sconnections.png)
20. I can now use Remote Desktop to connect to a Virtual Machine, running in my AppServers Subnet, which I am running without the need of a Public IP or bastion/jump host:
21. ![](/uploads/azurevpn-rdp.png)

Note: I don't have a DNS service running in Azure, but the Azure VPN agent will take DNS from the Virtual Network _(Azure Private DNS zone or your DNS server)_; you can set Custom DNS servers by modifying modifying your DNS the configuration.

You can set your Custom DNS settings (remember to add the DNS suffix if needed) and configure the VPN to automatically connect by following the details on the [OpenVPN Azure AD](https://docs.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-client#faq "Azure Active Directory authentication: Configure a VPN client for P2S OpenVPN protocol connections") Client page.