---
date: 2022-01-03T00:00:00.000+13:00
title: Azure Active Directory Application Proxy Implementation
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Are you running internal web-based applications that you want to securely give
access to users working remotely? Do you want to enforce or use Azure
Conditional Access policies to protect and manage access?

Let me introduce the [Azure Active Directory Application Proxy](https://docs.microsoft.com/en-us/azure/active-directory/app-proxy/what-is-application-proxy)…

> Application Proxy is a feature of Azure AD that enables users to access on-premises web applications from a remote client. Application Proxy includes both the Application Proxy service which runs in the cloud, and the Application Proxy connector which runs on an on-premises server. Azure AD, the Application Proxy service, and the Application Proxy connector work together to securely pass the user sign-on token from Azure AD to the web application.
>
> Application Proxy supports single sign-on. For more information on supported methods, see [Choosing a single sign-on method](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/sso-options#choosing-a-single-sign-on-method).
>
> Application Proxy is recommended for giving remote users access to internal resources. Application Proxy replaces the need for a VPN or reverse proxy.

## Overview

Azure Application Proxy has been around for a few years and allows users _(by Azure Active Directory and an Application Proxy Connector)_ to connect to internally hosted web applications.

![Azure Application Proxy - Network Diagram](/uploads/aadproxynetworkdiagram.png "Azure Application Proxy - Network Diagram")

Application Proxy supports the following types of applications:

* Web applications
* Web APIs that you want to expose to rich applications on different devices
* Applications hosted behind a Remote Desktop Gateway
* Rich client apps that are integrated with the [Microsoft Authentication Library (MSAL)](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview)

Azure Application Proxy can often be overlooked to solve your business requirements, without the need to implement costly third-party firewalls _(it also doesn’t have to be an on-premises workload, for example, if the web application is running on a VM in Azure, it will also work)_.

The Azure Application proxy connector is a lightweight agent that is installed on a Windows Server machine, that is logically close to the backend services it is giving access to and relays the information to the Application proxy service in Microsoft Azure via HTTP/HTTPS as long as it has access to the following:

| URL | Port | How it's used |
| --- | --- | --- |
| *.msappproxy.net  *.servicebus.windows.net | 443/HTTPS | Communication between the connector and the Application Proxy cloud service |
| crl3.digicert.com  crl4.digicert.com  ocsp.digicert.com  crl.microsoft.com  oneocsp.microsoft.com  ocsp.msocsp.com | 80/HTTP | The connector uses these URLs to verify certificates. |
| login.windows.net  secure.aadcdn.microsoftonline-p.com  *.microsoftonline.com  *.microsoftonline-p.com  *.msauth.net  *.msauthimages.net  *.msecnd.net  *.msftauth.net  *.msftauthimages.net  *.phonefactor.net  enterpriseregistration.windows.net  management.azure.com  policykeyservice.dc.ad.msft.net  ctldl.windowsupdate.com  www.microsoft.com/pkiops | 443/HTTPS | The connector uses these URLs during the registration process. |
| ctldl.windowsupdate.com | 80/HTTP | The connector uses this URL during the registration process. |

## Pre-requisites for Azure Application Proxy setup

The following resources and rights will be needed to set up Azure Application Proxy:

* An Azure Active Directory tenant
* A minimum of Application Administrator rights is required to set up the Application and user and group assignments
* A server running 2012 R2 or above to install the Application Proxy connector on (and the permissions to install)
* If you are using a third-party domain (you will need a public SSL certificate) and of course the ability to edit external DNS records.
* [Azure Active Directory Premium P1](https://www.microsoft.com/en-nz/security/business/identity-access-management/azure-ad-pricing?rtc=1) license or M365 Business Premium or E3 license for each user using Azure Active Directory Application Proxy.

![Azure Active Directory Application Proxy Licensing](/uploads/aadproxylicensing.png "Azure Active Directory Application Proxy Licensing")

Note: Normal [Azure AD service limits and](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/directory-service-limits-restrictions) restrictions, apply.

## Setup Azure Application Proxy

In this guide, I am going to set up Azure Application Proxy to grant access to my Synology NAS _(Network Attached Storage)_ device webpage, although it can be any webpage _(Unifi Controller etc)._

I will be configuring the Azure Application Proxy on a domain controller running Windows Server 2022.

### Disable IE Enhanced Security Configuration

The Azure Application Proxy connector requires you to log in to Microsoft Azure, I will be installing this on a Windows Server 2022 domain controller, if this Enhanced Security Configuration is enabled (as it should be) you will have problems authenticating to Microsoft Azure, so the easiest thing is to turn it off temporarily.

1. Open Server Manager
2. Click on Local Server
3. Click on: IE Enhanced Security Configuration
4. Select Off for: Administrators
5. ![Graphical user interface, text, application Description automatically](media/e53e53d41b8069043fb03da19ef29d6f.png)
6. Close Microsoft Edge (if you have it opened)

### Install Azure Application Proxy Connector

 1. Login to Azure Portal (on the server that you want to install the connector on)
 2. Navigate to: [Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
 3. Select Application Proxy
 4. ![Graphical user interface, text, application, email Description](media/c3d59ee0dd543f1f2c46ee6755d33e05.png)
 5. Click on: Download connector service
 6. Accept the system requirements and click Accept Terms & Download
 7. A file named: ‘AADApplicationProxyConnectorInstaller.exe’ should have been downloaded. Run it.
 8. Select: I agree to the license terms and conditions and select Install
 9. ![Graphical user interface, text, application Description automatically](media/67d490658590b49827b612c32fb8f89e.png)
10. Wait for the Microsoft Azure Active Directory Application to display and login
11. The Microsoft Azure Active Directory Application Connector will now be registered in your Azure Active Directory tenancy
12. ![Graphical user interface, text, application Description automatically](media/14fe5895fd079dac1c906544e4ea8037.png)
13. Click Close
14. Now re-enable IE enhanced security configuration.

You should now see 2 new services appear in services as Automatic (Delayed Start):

* WAPCsvc - Microsoft AAD Application Proxy Connector
* WAPCUpdaterSvc - Microsoft AAD Application Proxy Connector Updater

And 2 new processes running:

* ApplicationProxyConnectorService
* ApplicationProxyConnectorUpdateService

![Graphical user interface, text Description automatically](media/79d5ca2e9942db9b94c4cd0b24ba2b63.png)

If you are running Server Core, Microsoft Azure Active Directory Application Proxy can be installed via [PowerShell](https://docs.microsoft.com/en-us/azure/active-directory/app-proxy/application-proxy-register-connector-powershell).

The Azure Application Proxy Connector agent gets [updated](https://docs.microsoft.com/en-us/azure/active-directory/app-proxy/application-proxy-faq#why-is-my-connector-still-using-an-older-version-and-not-auto-upgraded-to-latest-version-) automatically when a new major version is released by Microsoft.

### Configure Connector Group

Now that you have created the connector, the Application Proxy has put our Connector in a group, that has defaulted to: Asia, because you can have more than one Application Proxy Connector for redundancy and different applications, we will create a new Connector Group that is set to use the Australia region, if Asia works for you – feel free to skip this step.

 1. Login to Azure Portal (on any PC/server)
 2. Navigate to: [Azure Active
    Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
 3. Select Application Proxy
 4. You should now see: Default and your Region
 5. ![Graphical user interface, text, application, email Description](media/ed39566a7692c5d2b7cc83a4b66a2cae.png)
 6. If you expand the Default Group, will you see your connector:
 7. ![Graphical user interface, text, application Description automatically](media/27bb798f4476d4ab1d550405a609acd6.png)
 8. Click on + New Connector Group
 9. Give it a name _(i.e., On-premises_)
10. Select the Connector you had earlier and select the region closest to you
    (currently the following can be selected: Asia, Australia, Europe, North
    America)
11. ![Graphical user interface, text, application, email Description](media/9e2da9fc515b594c11a7ac4dc097b275.png)
12. Click + Create
13. This will now create your new On-premises connector group and add the
    connector to it.

### Configure your Azure Application Proxy Application

Now that you have your Connector setup, its time to setup your application

1. Login to Azure Portal (on any PC/server)
2. Navigate to: [Azure Active
   Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
3. Select Application Proxy
4. Click on: + Configure an app
5. Fill in the details, that match your application:

* Name: This is the application that users will see _(i.e. I am going with
  Pizza, which is the name of my NAS)_
* Internal URL: This is the internal URL used to access your application inside the network _(in my example it is:_ [_http://pizza.corp.contoso.com/_](http://pizza.corp.contoso.com/)_)_
* External Url: This is the external URL that will be created, that users can access the application form _(this is not where you set your custom domain)_, _I am going to go with: pizza._ Note this URL down.
* Pre-Authentication: You don’t have to authenticate with Azure AD, you can just use passthrough, but it is not something I would recommend without delving into requirements, testing _– I am going to select: Azure Active Directory._
* Connector Group: Select the connector group you created earlier or that your Connector is signed to.
* Leave all Additional Settings as default – they can be changed later if you
  need to.

1. ![Graphical user interface, text, application, email Description](media/3c0a7e531ec5f57207bcd06ff55b2480.png)
2. Verify that everything is filled out correctly and, click + Add
3. Azure Application Proxy has now created a new Enterprise Application for
   you, based on the name mentioned earlier, if you navigate to the external
   URL mentioned earlier, you should get a prompt similar to below:
4. ![Graphical user interface, text, application Description automatically](media/d05773fc034271dc8512e8b1b02c12f4.png)
5. Its time to assign the rights!

### Assign rights to your Azure Application Proxy Application

 1. Login to Azure Portal (on any PC/server)
 2. Navigate to: [Azure Active
    Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
 3. Select [Enterprise
    Applications](https://portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AllApps/menuId/)
 4. Find the Application that was created earlier by the Azure Application Proxy
    service
 5. ![Graphical user interface, text, application, email Description](media/69931be4533d60671e73ffde60fa4e83.png)
 6. Click on the Application
 7. Click on: Users and Groups
 8. Click Add Assignment
 9. Add a user or group _(preferred)_ you want to have access to this
    Application
10. Click Assigned
11. ![Graphical user interface, text, application, email Description](media/1f870a8f049b221113c7756b5185b7cd.png)
12. Click on Application Proxy
13. Here you can see and edit the information you created earlier when you
    created the application, copy the External URL
14. Open Microsoft Edge (or another browser of your choice)
15. Paste in the External URL
16. Login with the account that was assigned to the Enterprise application
17. You should now have access to your on-premises web application from anywhere
    in the world:
18. ![Graphical user interface, website Description automatically](media/664b00f8d9f19123dc0461929c210728.png)

Note: Because the Synology web interface ran on port: 5000, I had to go back and
add in the port to the internal URL, as Application Proxy was attempting to
route to port: 5001.

### Setup Password-based Single-Sign on

Azure Application Proxy supports various [single
sign](https://docs.microsoft.com/en-us/azure/active-directory/app-proxy/application-proxy-config-sso-how-to)
on methods, including Kerbeos SPN integration, but the Synology NAS, uses
standalone accounts, so I am going to set Password-based single sign on,
allowing Azure AD to store the credentials for me.

 1. Download and install the [MyApps Secure Sign-in
    extension](https://microsoftedge.microsoft.com/addons/detail/my-apps-secure-signin-ex/gaaceiggkkiffbfdpmfapegoiohkiipl#:\~:text=My%20Apps%20Secure%20Sign-in%20Extension.%20This%20extension%20is,to%20cloud%20applications%20within%20your%20organization%20or%20school.)
 2. Login using your Microsoft account to: the MyApps extension
 3. ![](media/6dca6f46484862247c171bc97cd5a2b0.png)
 4. Login to Azure Portal (on any PC/server)
 5. Navigate to: [Azure Active
    Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview)
 6. Select [Enterprise
    Applications](https://portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AllApps/menuId/)
 7. Find the Application that was created earlier by the Azure Application Proxy
    service
 8. Click on Single signon
 9. Select Password-based
10. ![Graphical user interface, application Description automatically](media/a6a93ed8a81dfd9915bc57c4f3c21ea4.png)
11. Type in the URL of the authentication webpage and click Save
12. ![Graphical user interface, text, application, email Description](media/b086c4853f6cc08a54f70d1f76c2b16c.png)
13. The Azure AD Application Proxy didn’t find my sign-in login and password
    fields, so I have to manually configure them, select: Configure Pizza
    Password Single Sign-on Settings
14. Select: Manually detect sign-in fields
15. Select Capture sign-in fields
16. ![Graphical user interface, text, application Description automatically](media/b057fb46250bd76d972b18ac23905483.png)
17. Your MS Edge Extension should show:
18. ![Graphical user interface, website Description automatically](media/a5f480353055db212b43946c2645c989.png)
19. Enter in your username
20. Press Enter
21. Enter in your password
22. Select the MS Apps extension and select Save
23. Navigate back to the Azure Portal
24. Select ‘I was able to sign in
25. If successful, Azure AD should now have mapped the fields:
26. ![Graphical user interface, text, application, email Description](media/96dff89a4a6a5706d0266034343e727d.png)
27. Click Save
28. Next time you log in to the Application, the My Apps Secure Sign-in Extension will have cached the credentials and should log you into the application automatically, meaning you should only need to login once with your Azure AD credentials.

### Access your Azure Application Proxy published application

1. You can now go to [My Apps (microsoft.com)](https://myapps.microsoft.com/)
   and you will see your application
2. ![Graphical user interface, application Description automatically](media/713f13c298df2a63bcf844a39e5bea38.png)

Your application will also appear in the Microsoft 365 Waffle (it may take up to
an hour to appear):

![Graphical user interface, application Description automatically](media/e84bf867076476601ca4d6027724c3d7.png)

I recommend, you go into the Enterprise Application and upload a better
image/logo of your Application so your users can easily tell it apart.