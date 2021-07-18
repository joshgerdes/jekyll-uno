---
date: 
title: Implement WebJEA for self-service Start/Stop of Azure Virtual Machines
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
WebJEA allows you to build web forms for any PowerShell script dynamically. WebJEA automatically **parses the script at page load for description, parameters and validation**, **then dynamically builds a form to take input and display formatted output! No webpage knowledge is needed!**

The main goals for WebJEA:

* Reduce delegation of privileged access to users
* Quickly automate on-demand tasks and grant access to less-privileged users
* Leverage your existing knowledge in PowerShell to build web forms and automate on-demand processes
* Encourage proper script creation by parsing and honouring advanced function parameters and comments

Because WebJEA is simply a Self-Service Portal for PowerShell scripts, anything you can script with PowerShell you can run through the Portal! Opening a lot of opportunities for automation without having to learn third party automation toolsets! Anyone who knows PowerShell can use it! Each script can be locked down to specific users and AD groups!

You can read more about WebJEA directly on the GitHub page: [https://github.com/markdomansky/WebJEA](https://github.com/markdomansky/WebJEA "https://github.com/markdomansky/WebJEA").

This guide will concentrate on setting up WebJEA for self-service Azure Resource management. However, WebJEA can be used to enable much more self-service automation.

We will use a Windows Server 2019, running in Microsoft Azure, to run WebJEA from.

### Prerequisites

* Domain Joined server running Windows 2016+ Core/Full with PowerShell 5.1
* The server must have permission to go out over the internet to Azure and download PowerShell modules.
* CPU/RAM Requirements will depend significantly on your usage, start low _(2-vCPU/4GB RAM)_ and grow as needed.

I've created a Standard_B2ms _(2vCPU, 8GB RAM)_ virtual machine, called: WEBJEA-P01 in an Azure Resource Group called: webjea_prod

This server is running: Windows Server 2019 Datacenter and is part of my Active Directory domain; I've also created a service account called: webjea_services.

### Setup WebJEA

Once we have a Windows Server, now it's time to set up WebJEA!

#### Setup Self-Signed Certificate

If you already have a certificate you can use, skip this step. In the case of this guide, we are going to use a self-signed certificate.

Log into the WebJEA Windows server using your service account _(in my case, it is: luke\\webjea_services)_.

Open PowerShell ISE as Administrator, and after replacing the DNS name to suit your own environment, run the following to create the Root CA certificate:

Now that the Root CA is created and trusted, we want to create the actual self-signed certificate:

    #Create RootCA
    $rootCA = New-SelfSignedCertificate -Subject "CN=MyRootCA"  `
    -KeyExportPolicy Exportable  `
    -KeyUsage CertSign,CRLSign,DigitalSignature  `
    -KeyLength 2048  `
    -KeyUsageProperty All  `
    -KeyAlgorithm 'RSA'  `
    -HashAlgorithm 'SHA256'  `
    -Provider "Microsoft Enhanced RSA and AES Cryptographic Provider"  `
    -NotAfter (Get-Date).AddYears(10)
    
    #Create Self-Signed Certificate
    $cert = New-SelfSignedCertificate -Subject "CN=WEBJEA-P01.luke.geek.nz"  `
    -Signer $rootCA  `
    -KeyLength 2048  `
    -KeyExportPolicy Exportable  `
    -DnsName WEBJEA-P01.luke.geek.nz, WEBJEA, WEBJEA-P01  `
    -KeyAlgorithm 'RSA'  `
    -HashAlgorithm 'SHA256'  `
    -Provider "Microsoft Enhanced RSA and AES Cryptographic Provider"  `
    -NotAfter (Get-Date).AddYears(10)
    $certhumbprint = $cert.Thumbprint
    
    #Add Root CA to Trusted Root Authorities
    New-Item -ItemType Directory 'c:\WebJea\certs' -Force
    Export-Certificate -Cert $rootCA -FilePath "C:\WebJEA\certs\rootCA.crt" -Force
    Import-Certificate -CertStoreLocation 'Cert:\LocalMachine\Root' -FilePath "C:\WebJEA\certs\rootCA.crt"
    
    Write-Host -ForegroundColor Green -Object "Copy this: $certhumbprint - The Thumbprint is needed for the DSCDeploy.ps1 script"

Copy the Thumbprint _(if you do this manually, make sure it is the Thumbprint of the certificate, not the Trusted Root CA certificate)_; we will need that later.

Run the following to add the certificate to the 'Trusted Root Authorities' of the server.

#### Setup a Group Managed Service Account

This is the account we will use to run WebJEA under; it can be a normal Active Directory user account if you feel more comfortable or want to assign permissions to.

I am using a Normal AD service account in this guide because I am using Azure Active Directory Domain Services as my Domain Controller, and GMSA is not currently supported. I have also seen some scripts require the ability to create and read user-specific files. However, it's always good to follow best practices where possible.

_Note: Group Managed Services accounts automatically renew and update the passwords for the accounts; they allow for additional security. You can read more about them here:_ [_Group Managed Service Accounts Overview_](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview "Group Managed Service Accounts Overview")_._

    #Create A group MSA account
    Add-kdsrootkey -effectivetime ((get-date).addhours(-10))
    New-ADServiceAccount -name webjeagmsa1 -dnshostname (get-addomaincontroller).hostname -principalsallowedtoretrievemanagedpassword WEBJEA-P01.luke.geek.nz
    
    #Create AD Group
    New-ADGroup -Name "WebJEAAdmins" -SamAccountName WebJEAAdmins -GroupCategory Security -GroupScope Global -DisplayName "WebJEA - Admins" -Description "Members of this group are WebJEA Admins"
    
    Install-adserviceaccount webjeagmsa1
    Add-ADGroupmember -identity "luke.geek.nz\WebJEAAdmins" -members (get-adserviceaccount webjeagmsa1).distinguishedname

Add the WebJEAAdmins group to the Administrators group of your WebJEA server.

#### Install WebJEA

Download the latest [release package](https://github.com/markdomansky/WebJEA/releases "WebJEA - Releases") _(zip file)_ onto the WebJEA Windows server

Extract it, and you should have 2 files and 2 folders:

* Site\\
* StarterFiles\\
* DSCConfig.inc.ps1
* DSCDeploy.ps1

  Open PowerShell ISE as Administrator and open DSCDeploy.ps1

WebJEA uses PowerShell DSC _(Desired State Configuration)_ to set up a lot of the setup.

DSC will do the following for us:

* Install IIS
* Create the App Pool and set the identity
* Create and migrate the Site files to the IIS website folder
* Configure SSL (if we were using it)
* Update the WebJEA config files to point towards the script and log locations

Even though most of the work will be automated for us by Desired State Configuration, we have to do some configurations to work in our environment.

I am not using a Group Managed Service Account. Instead, I will use a normal AD account as a service account _(i.e. webjea_services)_, but if you use a GMSA, you need to put the username in the AppPoolUserName; no credentials are needed _(make sure the GMSA has access to the server)_.

Change the following variables to suit your setup; in my case, I have moved WebJEA resources to their own folder, so it's not sitting directly on the OS drive, but until its own Folder.

* AppPoolUserName =  'your service account name'
* AppPoolPassword = 'the password for your service account' #make sure you don't save the DSC file, so the password is stored in plain text.
* WEB

![](/uploads/webjea_dsc.png)

One thing to note is that the DSCDeploy.ps1 is calling _(dot sourcing)_ the DSCConfig deploy script; by default, it is looking for it in the same folder as the DSCDeploy.ps1 folder.

If you just opened up PowerShell ISE, you may notice that you are actually in C:\\Windows\\System32, so it won't be able to find the script to run; you can either change the script to point directly to the file location, or you can change the directory you are into to match the files, in my case in the Script pane I run the following:

    cd 'C:\Users\webjea_services\Downloads\webjea-1.1.157.7589'

Now run the script and wait.

If you get an error saying that the script is not digitally signed, run the following in the script pane:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

This is because the PowerShell execution policy hasn't been set; depending on the scripts you are running, you may have to update the execution policy for the entire system, but for now, we will set it to Bypass for this process only, now re-run the script again, you should see DSC kick-off and start your configuration and setup of IIS and the WebJEA site.

![](/uploads/webjea_startingdsc.png)

You should also see the files/folders starting to be created!

_Note: If you need to make a configuration change, please change it in the DSCDeploy.ps1, DSC will ensure that the configuration is applied as per your configuration and rerun the script, i.e. if you need to replace the certificate from a self-signed certificate to a managed PKI certificate._

Once DSC has completed, your server should now be running IIS and the IIS server!

To add the IIS Management Tool, this is not required but will help you manage IIS, run the following PowerShell cmdlet:

    Enable-WindowsOptionalFeature -Online -FeatureName IIS-ManagementConsole

Open an Internet Browser and navigate to _(your equivalent of)_: [https://webjea-p01.luke.geek.nz/WebJEA](https://webjea-p01.luke.geek.nz/WebJEA "https://webjea-p01.luke.geek.nz/WebJEA").

If you need assistance finding the Website path, open the Internet Information (IIS) Manager, installed and uncollapse Sites, Default WebSite, right-click WebJEA, Manage Application and select Browse.

![](/uploads/webjea_iis_authentication.png)

If successful, you should get a username and password prompt:

![](/uploads/webjea_authentication.png)

That's normal - it means you haven't been given access and now need to configure it.

### Configure WebJEA

Now that WebJEA has been set up, it is time to configure it; the first thing we need to do is create a Group for WebJEA admins _(see all scripts)_.

Create an Active Directory group for:

* WebJEA-Admins
* WebJEA-Users

Add your account to the: WebJEA-Admins group.

Navigate to your WebJEA scripts folder; in my case, I set it up under c:\\WebJEA\\Scripts:

![](/uploads/webjea_scripts.png)

Before we go any further, take a Backup of the config.json file, rename it to "config.bak".

I recommend using Visual Studio Code to edit the config.json to help avoid any syntax issues.

Now right click config.json and open it to edit

This file is the glue that holds WebJEA together.

We are going to make a few edits:

* Feel free to update the Title to match your company or Teams
* Add in the WebJEA-Admins group earlier _(include the Domain Name)_ into the permitted group's session - this controls access for ALL scripts.

Note the: \\\\ for each path that is required. If you get a syntax error when attempting to load the WebJEA webpage, this is most likely missing.

![](/uploads/webjea_democonfig.png)

Save the config file and relaunch the WebJEA webpage. It should now load without prompting for a username and password.

Set the PowerShell execution policy on the machine to Unrestricted so that you can run any PowerShell scripts on it:

    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine

![](/uploads/webjea_initialoverview.png)

If you get an: AuthorizationManager check failed error, it is because the PowerShell scripts are still in a blocked state from being downloaded from the internet, run the following command to unblock them, then refresh the WebJEA webpage:

    Get-ChildItem -Path 'C:\WebJEA\scripts\' -Recurse | Unblock-File

You now have a base WebJEA install! By default, WebJEA comes with 2 PowerShell files:

* overview.ps1
* validate.ps1

You may have noticed these in the config.json file; WebJEA has actually run the overview.ps1 file as soon as the page loads, so you can have scripts run before running another one, which is handy when you need to know the current state of something before taking action.

The validate.ps1 script is a really good resource to use to check out the parameter types that could be used to generate the forms.

### Setup Azure Virtual Machine Start/Stop

Now that we have a working WebJEA install, it's time to set up the Azure VM Start/Stop script we will use for this demo.

On the WebJEA server, we need to install the Azure PowerShell modules, run the following in Powershell as Administrator:

    Install-Module Az -Scope AllUsers

#### Create Service Principal

Once, the Az PowerShell modules are installed, we need to set a Service Principal for the PowerShell script to use to connect to Azure to manage our Virtual Machines.

Run the following PowerShell cmdlet to connect to Azure:

    Connect-AzAccount

Now that we are connected to Azure, we now need to create the SPN, run the following:

    $sp = New-AzADServicePrincipal -DisplayName WebJEA-AzureResourceCreator -Role Contributor
    $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($sp.Secret)
    $UnsecureSecret = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

Now you have created an SPN called: WebJEA-AzureResourceCreator, we now need to grab the Tenant ID, run the following:

    Get-AzContext | Select-Object Tenant

Now that we have the SPN and Tenant ID, it's time to test connectivity.

    # Login using service principal 
    $TenantId = 'TENANTIDHERE' 
    $ApplicationId = 'APPLICATIONIDHERE'  
    $Secret = ConvertTo-SecureString -String 'SECRETSTRINGHERE' -AsPlainText -Force 
    $Credential = [System.Management.Automation.PSCredential]::New($ApplicationId, $Secret) 
    Connect-AzAccount -ServicePrincipal -Credential $Credential -TenantId $TenantId

Copy the TenantID into the TenantID section

Type:

    $sp.ApplicationID

To retrieve the ApplicationID created from the SPN in the previous step and add it into the ApplicationID part.

Type in:

    $UnsecureSecret

To retrieve the Secret, created in the SPN and add it to the String.

Now run the snippet, and you should be successfully connected to Azure.

#### Create Get-VM script

One of the features of WebJEA is the ability to run scripts on page load, we are going to get the current Power State of our Azure VMs, in the WebJEA scripts directory create a new PS1 file called: Get-VM.ps1

Add the following script to it:

    # Login using service principal 

    $TenantId = 'TENANTIDHERE' 

    $ApplicationId = 'APPLICATIONIDHERE'  

    $Secret = ConvertTo-SecureString -String 'SECRETSTRINGHERE' -AsPlainText -Force 

    $Credential = [System.Management.Automation.PSCredential]::New($ApplicationId, $Secret) 

    Connect-AzAccount -ServicePrincipal -Credential $Credential -TenantId $TenantId

    Get-AzVM -Status | Select-Object Name, PowerState, ResourceGroupName