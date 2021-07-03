---
date: 2021-06-27T00:00:00.000+12:00
title: How to create a Azure Virtual Desktop farm
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
Previously known as Windows Virtual Desktop, [Azure Virtual Desktop](https://docs.microsoft.com/en-us/azure/virtual-desktop/overview "What is Azure Virtual Desktop?"){:target="_blank"} is the successor of Microsoft Remote Desktop; although compatible with Server OS (Operating System), it is the first to support Windows 10 _(and soon Windows 11)_ multisession, reducing application compatibility issues and giving consistent user experience.

In this guide, I will run you through creating Azure Virtual Desktop from scratch, along with some prerequisites that will help you manage AVD after you create it.

Before I begin, I recommend reading the Azure Virtual Desktop Azure product page "[here](https://azure.microsoft.com/en-us/services/virtual-desktop/ " Azure Virtual Desktop -   Enable a secure remote desktop experience from virtually anywhere."){:target="_blank"}" to understand the pricing model, features and additional resources that could help you in your journey.

When selecting a region for your Session Hosts _(Virtual Machines)_, I recommend you have a look at the: [Azure Virtual Desktop Experience Estimator](https://azure.microsoft.com/en-us/services/virtual-desktop/assessment/ " Azure Virtual Desktop Experience Estimator") to help validate the proper region for your Session Hosts and the round trip time _(I am in New Zealand, so my recommended region is: Australia East, which is what I will be using for this guide)_.

_If you don't already have a Microsoft Azure subscription, you can sign up for a Free subscription "_[_here_](https://azure.microsoft.com/en-us/free/ "Create your Azure free account today"){:target="_blank"}_"._

Assuming you already have an Azure subscription and the appropriate access to create resources in that subscription, gets begin!

## Create Azure Active Directory Domain Services

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource**
 3. Search for: **Azure AD Domain Services**. You can change the Publisher Type to Microsoft, so it doesn't display any other marketplace offerings.
    ![Azure AD Domain - Marketplace](/uploads/azureaddssearch.png "Azure AD Domain - Marketplace")
    ![Azure AD Domain - Marketplace](/uploads/azureaddsmarketplace.png "Azure AD Domain - Marketplace")
 4. Click **Create**
 5. If you already have a **Resource Group**, select it - in this Demo, we are going to create one: aad_prod
 6. Type in the **DNS** domain **name** - this is the **FQDN** of your **domain**; in my demo, I will choose internal.luke.geek.nz.
 7. Because I am in New Zealand, the closest region to me is Australia East, so that’s the region I will select. Make sure you **select** the **appropriate region** for where your Azure Virtual Desktop workloads are.
 8. **Select** the **SKU** and **Resource Type**; you can see the Pricing Calculator and the "Help Me choose.." links to verify your SKU and Forest type _(however, in most cases, such as Azure Virtual Desktop, your Forest Type will be 'User')_.
    ![Azure AD Domain Services - Basic Config](/uploads/adds_basics.png "Azure AD Domain Services - Basic Config")
 9. Click **Next**
10. We will set up the **Networking**; if you have an already existing Virtual Network, select it.
    _Azure AD Domain Services uses a dedicated subnet within a virtual network to hold all of its resources. If using an existing network, ensure that the network configuration does not block the ports required for Azure AD Domain Services to run._ [_Learn more_](https://docs.microsoft.com/azure/active-directory-domain-services/create-instance?WT.mc_id=Portal-Microsoft_AAD_DomainServices){:target="_blank"}
11. I will let it create a **Virtual Network** and its Subnet (/24); click **Next**.
    ![Azure AD Domain Services - Networking Config](/uploads/adds_networking.png "Azure AD Domain Services - Networking Config")
12. **Azure AD Domain Services** will **create** a new Azure AD **Group** called: **AAD DC Administrators** - this group will be used for Administrator level permissions on the Azure AD Domain Services domain _(it automatically adds the account you are using to create Azure AD Domain Services into this group)_.
13. You can **configure Membership** of this **group** now and configure who gets alerted if there are issues with Azure AD Domain Services.
14. When you are ready, select **Next**.
    ![Azure AD Domain Services - Administration Config](/uploads/adds_admin.png "Azure AD Domain Services - Administration Config")
15. Depending on the amount of Azure Active Directory users you have in your organisation, and whether they will need Azure AD Domain Services, you can choose to synchronise **ALL Azure AD Groups and Users**, or specific groups of users _(this can be changed later)_, because my Azure AD Organisation is fairly low, I am going to Sync everything, click **Next**.
16. One thing to note here is the recommendation on the number of Objects _(Users, Groups)_ that will get synced to Azure AD Domain Services; for the Standard SKU, the suggested Object Count is 0 to 25,000 - for the Enterprise SKU, it is 25,000 to 100,000. So although there is no hard limit, it might be worth upgrading the SKU you are running for the additional backups and authentication if fit in the Enterprise space.
    ![Azure AD Domain Services - Syncronisation Config](/uploads/adds_sync.png "Azure AD Domain Services - Syncronisation Config")
17. We can now **configure** the **Security Setting**s, the only setting I am going to change here is **TLS 1.2 Only Mode** to **Enable**
    ![Azure AD Domain Services - Security Config](/uploads/adds_securitysettings.png "Azure AD Domain Services - Security Config")
18. Enter any applicable Tags and click **Review & Create** to **validate** your **configuration**.
19. Review your configuration, and if you are happy with it: Select **Create**.
20. Confirm that you are happy with the following and click **Ok**
    ![Azure AD Domain Services](/uploads/adds_youshouldknow.png "Azure AD Domain Services")
    **Note: Azure AD Domain Services can take up to an hour to provision.**
21. Once your Azure AD Domain Services has been configured, we must make some final configuration changes to point the Virtual Network DNS to use the Azure AD Domain Services. So first, **open** your newly created **Azure AD Domain Services**.
22. Click on **Overview** and: **Configuration** issues for your managed domain were detected. **Run configuration Diagnostics**
    ![Azure AD Domain Services](/uploads/adds_configissues.png "Azure AD Domain Services")
23. Click on **Run**
24. It should find a DNS record issue; click **Fix** to **set** the **DNS settings** of the Virtual Network to use the Azure AD Domain Services.
    Please **be careful here**, especially if you have already existing DNS settings; you might have to add it manually.

## Create a Utility server to help Administer Azure Virtual Desktop

We need to create a Virtual Machine to help manage the AAD Domain and deploy Group Policies to help manage and configure the Azure Virtual Desktop farm.

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource.**
 3. Search for: **Windows Server 2019 Datacenter** and select **Create**
 4. If you already have a **Resource Group**, select it - in this Demo, we are going to create one: aad_infra
 5. **Specify** a **name** for the **Virtual Machine** _(I am going to use: UTILITY-P01)_
 6. **Select** a **Region** _(use the same Region as the Azure AD Domain Services and Azure Virtual Desktop resources)_
 7. For the **Image**, you can select either Windows Server 2019 Datacenter -Gen 1 or **Gen 2**; in my case, I am going with Gen2 _(although it doesn't matter)_.
 8. I am a firm believer in **selecting** the **smallest size** possible for the size, then scaling up when/where needed; I am going to go with a Standard_B2ms.
    ![Azure - Create VM](/uploads/createvm1.png "Azure - Create VM")
 9. Now we need to enter in the **Administrator** (local account) **Username** and **Password**.
10. Select '**None**' for **Public** inbound **ports**
11. If you have existing Windows Server licenses, you can select Hybrid Use Benefit; if not, select **Next: Disks**.
    ![Azure - Create VM](/uploads/createvm2.png "Azure - Create VM")
12. For the disks, I only need the OS disk, so I don't need to add a Data Disk _(although you could use this to store your Application install files etc.)_; however, to reduce cost, I am going to change the **Disk type** to **Standard SSD** _(locally-redundant storage)_ and select **Next: Networking**.
    ![Azure - Create VM](/uploads/createvmdisks.png "Azure - Create VM")
13. For the Virtual Network, make sure you **select** the **same** Virtual **Network** that the **Azure AD Domain Services** has been **installed to**; I will select the: aadds-subnet created earlier for my Utility server.
14. Set '**None**' for the **Public IP** and select **Next: Management**
    ![Azure - Create VM](/uploads/createvmnetworkinterface.png "Azure - Create VM")
15. Feel free to **leave** this all **as Default**
16. Just **be wary** of the **Auto-shutdown** settings, which will automatically shut down the VM daily _(I will keep mine selected as this is just a demo, and I only need the UTILITY server for initial configuration, it doesn't need to be running 24.7)_.
17. If you have a **Recovery Services Vault**, now is a good time to **add** the Utility **server** to **Backups**, so you don't forget it later, select Review & Create
18. **Verify** the **configuration** is correct and select **Create**

## Create Azure Bastion to connect to the Utility server

Once the VM has been created, we now need to connect to it securely, so we will create a Bastion instance, which will allow us to connect to it without publishing the RDP (Remote Desktop Protocol) over the internet.

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource**
 3. Search for: **Bastion**
    ![Azure - Bastion](/uploads/bastionmarketplace.png "Azure - Bastion")
 4. Click **Create**
 5. This is a Networking resource to place it in the same Resource Group as my Virtual Network.
 6. Please type in a **Name** for the **Bastion** instance; I will call mine: Bastion
 7. **Select** the **Region** that **matches** the Virtual **Network** region
 8. Select the **Virtual Network**
 9. It now warns you about creating an: AzureBastionSubnet with a prefix of at least /27, so we need to create one; click on **Manage Subnet Configuration**.
10. Click **+ Subnet**
11. For the Name type in: **AzureBastionSubnet**
12. For the **Subnet** address range: **10.0.1.0/27**
    _If you get an error that indicates the address is overlapping with the aadds-subnet, it may be because the Address space is only a /24; click Cancel and click on Address Space in the Virtual Network and change the /24 to/16 to increase the address range._
13. Click **Save** to create the subnet
    ![Azure - Bastion](/uploads/az_subnet.png "Azure - Bastion")
14. Up the Top, click **Create a Bastion**. To go back to the Bastion setup, your Subnet should be selected automatically.
15. You do need a **Public IP** for Bastion, so **confirm** the **name** is appropriate, then click **Review + Create**
    ![Azure - Bastion](/uploads/bastionsetup.png "Azure - Bastion")
16. Click on **Create** to create your Bastion instance!

**Note: Bastion may take 10-20 minutes to provision.**

## Configure the Utility server

Now that we have a Bastion instance, it is time to connect and configure the Utility server and create a new Azure AD user for Azure Virtual Desktop configuration.

 1. First thing I am going to create a separate Azure AD account to manage the Utility server and join the Azure Virtual Desktop session hosts to the domain; this is to separate my own account. Azure AD Domain Services relies on password hash. So you won't be able to log in using Azure AD Domain Services unless you and the people using it have reset their passwords AFTER Azure AD Domain Services has been created.
 2. Navigate to the Azure Portal and open **Azure Active Directory**
 3. Click on **Users**
 4. Click on **+ New User**
 5. **Type** in the **username** of a **user**, I am going to use: 'avdjoin'
 6. Type in an **easily identifiable name**
 7. Generate or put in a secure **password**
 8. **Add** to the **AAD DC Administrators** group
 9. Click **Ok** to create the user
    ![Azure AD - Users](/uploads/avdjoin.png "Azure AD - Users")
10. Once the account has been created, make sure to **login** with it **to** the **Azure Portal** or Office portal to **force** a final **password reset**, or you won't be able to use it in the next steps as it will be waiting for a password reset.
11. Once that account has been created, it's time to **join** your utility **server** to the Azure Active Directory **Domain**, navigate to your Utility **server** and click **Connect**.
12. Select **Bastion**
13. Select **Use Bastion**
14. **Type** in the **username** and **password** of the **LOCAL account** created when the Virtual Machine was created and click **Connect**
    _Note: If you are running a popup blocker, you need to allow it to open, as Bastion opens up the connection in a new window._
    ![Azure Bastion](/uploads/azurebastionconnect.png "Azure Bastion")
15. You should now be logged in to the server successfully.
16. Now it's time to join the server to the domain _(make sure that DNS is configured for AD Domain Services on the Virtual Network, see the last step in the AD Domain Services section, or you won't be able to domain join anything)_.
17. In **Server Management**, click on **Local Server**
18. Select **WORKGROUP**
19. Click **Change…**
20. Select **Domain**
21. Please **type** in the DNS name of your **domain**; in my demo, it is: luke.geek.nz
22. **Type** in the **username** and **password** of the account we created earlier and clicked **Ok**
    ![Azure - Domain Join](/uploads/jointodomain.png "Azure - Domain Join")
23. Once you see, Welcome to the domain, click **Ok** a few times to **restart** the **server**.
24. Once the server has been restarted, you can now close your **bastion** window and **reconnect** using your **Azure AD** credentials (in my case, avdjoin), a **member** of the **ADDC Administrators group**.
    ![Azure - Connect to Bastion](/uploads/azurebastionconnect2.png "Azure - Connect to Bastion")
25. You have now successfully connected using an Azure AD account to the AD Services domain.
26. Now it's time to install some base Active Directory tools
27. Open Windows **PowerShell** as **Administrator**
28. **Type** in the following PowerShell **commands**:

        Add-WindowsFeature RSAT-Role-Tools
        
        Install-WindowsFeature –Name GPMC

_Note: You can use the little arrows on the left-hand side of your Remote Desktop window to copy and paste text to and from your Bastion connection._

1. This will now install the base Active Directory remote management tools, including Group Policy Management, so you can now create and manage the Group Policy objects for your Azure Virtual Desktop hosts.
   ![](/uploads/utility_servertools.png)
2. We will now set up some base configurations to **create** a custom **OU** for the Azure Virtual Desktops **hosts** to go into:

* Open **Active Directory Users & Computers**
* **Expand** out the **Domain** and right-click (at the Top Level)
* Select **New, Organisational Unit**

![](/uploads/utility_newou.png)

* Type in: AVD
* In the AVD OU, **create** a new **OU** called: Hosts
* Now that we have an OU for the hosts, we will need to tell Azure what OU the hosts go into, so while we have Active Directory Users and Computers open, click on View.
* Select **Advanced Features**
* **Right-click** the Hosts **OU**
* Select **Properties**
* Click on **Attribute Editor**
* Find the **distinguishedName attribute**

![](/uploads/utility_serverdn.png)

* Open and **Copy** the **Value** for future _(in my case: OU=Hosts,OU=AVD,DC=luke,DC=geek,DC=nz)_ for future reference.
* Now that we have the AVD Hosts OU, you can also open Group Policy Management and create your Computer policies.

## Deploy Azure Virtual Desktop

Now we are ready to deploy Azure Virtual Desktop finally!

 1. Log in to the **Azure Portal**
 2. Click on **Create a resource**
 3. Find and select **Host pool**
    ![Azure Virtual Desktop - Host Pool](/uploads/avdhostpoolmarketplace.png "Azure Virtual Desktop - Host Pool")
 4. Click **Create**
 5. Please **create** a new **Resource Group** to help resources separately, and I am going to name mine: avd_prod
 6. **Type** in a **Host Pool Name**, I will call mine: avd-pooled
 7. Please select the **location** of the **Metadata** _(this is NOT the location of your session hosts, it’s the gateway, select the Region closet to you as possible)_
 8. For **Host Pool Type**, if you want everyone to have a Virtual Machine each, you can select Personal; however, I want people to be shared across my servers, so I will select **Pooled**.
 9. For the Load balancing algorithm, we can choose to spread people over available hosts or fill up one host before moving connections to the next; we are going with **Breadth-first**.
10. Click **Next: Virtual Machines**
    ![Azure Virtual Desktop - Host Pool](/uploads/avdhostpoolsetup1.png "Azure Virtual Desktop - Host Pool")
11. Now we can **add** your Session **hosts** to the **Pool**.
12. By default, it has defaulted the Resource Group to the same Resource Group as the Host pool; however, you can separate them.
13. Please **select** a **Name prefix** for your session hosts, and it must be unique. Azure will automatically add a number to it as you build out more sessions hosts. I will put avdhost.
14. As I am based in New Zealand, I will be using the Australia East region.
15. We are going to use a **Gallery Image** of **Windows 10 Enterprise multi-session, Version 20H2 + M365 Apps** _(select the newest image at the time of your deployment)_
16. Select your **Virtual machine size**
17. **Select** the **number** of Virtual **Machines** you need
18. Select the **OS disk type**
    ![Azure Virtual Desktop - Host Pool](/uploads/avdhostpoolsetup2.png "Azure Virtual Desktop - Host Pool")
19. Select your **Virtual Machine** and **subnet**
20. Select **Yes** to specify your **domain** or unit
21. Type in your A**D Domain Services domain name**
22. If you don't **specify** an **OU**, it will create it in the: AADDC Computers OU. I had previously created a separate OU for my hosts so that I will enter the OU information.
23. For the **Domain Administrator** account, I will use the AVDJoin account I created earlier.
24. When the Virtual Machines get created, a **local Administrator** account will be created for each machine, and you can **specify** the **username** and **password** of what you want this account to be.
    ![Azure Virtual Desktop - Host Pool](/uploads/avdhostpoolsetup3.png "Azure Virtual Desktop - Host Pool")
25. Click **Next: WorkSpace**
26. Select **Yes** to **Register Desktop App Group**
27. We haven’t created an Azure Virtual Desktop Workspace yet, so select **Create New**.
28. **Create** a **name** for your **Workspace**; my example is: avd_workspace
29. Click **Ok**
    ![Azure Virtual Desktop - Workspace](/uploads/avdworkspacesetup.png "Azure Virtual Desktop - Workspace")
30. Click on **Review + Create**
31. Confirm everything looks ok and click Create
    **Note: This may take 10-20 minutes to create your Azure Virtual Desktop resources:**

* Host Pool
* Workspace
* Session hosts

1. Once the resources have been created, you should now have an **Application group** for the Session Desktop.
2. **Open** the Application **Group** and click **Applications**; you should confirm the SessionDesktop application is listed. ![Azure Virtual Desktop - Application Group](/uploads/avdapplications.png "Azure Virtual Desktop - Application Group")
3. Click on the **SessionDesktop** to **change** the **Display name** _(this is the resource people will see when they go to your Azure Virtual Desktop_), and I changed mine to AVD Desktop. ![Azure Virtual Desktop - Application Group](/uploads/avddesktop.png "Azure Virtual Desktop - Application Group")
4. Click on **Assignments**
5. These are the Users & Groups that are allowed to access your Azure Virtual Desktop.
6. My recommendation would be to **add** a **Group** that contains your users, but in my demo, I will add in my: 'avdjoin' account. ![Azure Virtual Desktop - Application Group](/uploads/avddesktopassignment.png "Azure Virtual Desktop - Application Group")
7. Using an assigned account, you can now **navigate** to**:** [https://rdweb.wvd.microsoft.com/arm/webclient/index.html](https://rdweb.wvd.microsoft.com/arm/webclient/index.html "https://rdweb.wvd.microsoft.com/arm/webclient/index.html") ![Azure Virtual Desktop - RD Web](/uploads/avdremotewebapp.png "Azure Virtual Desktop - RD Web")
8. You can now **launch** your **Desktop**.
9. **Congratulations**, you have now created and connected to Azure Virtual Desktop! ![Azure Virtual Desktop](/uploads/avddesktopfull.png "Azure Virtual Desktop")

## Additional Configuration

* You can Navigate to your Host Pool; under Settings, you can restrict or allow RDP settings, Device redirections and configure Display sessions.
* Configure [Start VM On Connect](https://luke.geek.nz/azure/start-vm-on-connect-for-azure-virtual-desktop/ "Start VM on Connect for Azure Virtual Desktop"){:target="_blank"} to help reduce your spend.
* If you click on Session hosts, you can add additional hosts to your pool or Drain them to prevent logins.
* If you click Application Groups, you can add RemoteApp groups to allow users to connect directly to an Application versus a Full Desktop.
* Configure [FSLogix](https://luke.geek.nz/azure/how-to-setup-fslogix-profiles-for-azure-virtual-desktop/ "How to setup FSLogix profiles for Azure Virtual Desktop"){:target="_blank"} profiles for user persistance.
* Set Disconnected Session Time limits in Group Policy, to automatically log off Disconnected sessions after 'x' period of time.

