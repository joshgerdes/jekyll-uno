---
date: 
title: Implement WebJEA for self-service Azure Resource creation with PowerShell
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
WebJEA allows you to dynamically build web forms for any PowerShell script. WebJEA automatically **parses the script at page load for description, parameters and validation**, **then dynamically builds a form to take input and display formatted output! No webpage knowledge is needed!**

The main goals for WebJEA:

* Reduce delegation of privileged access to users
* Quickly automate on-demand tasks and grant access to less-privileged users
* Leverage your existing knowledge in PowerShell to build web forms and automate on-demand processes
* Encourage proper script creation by parsing and honouring advanced function parameters and comments

Because WebJEA is simply a Self-Service Portal for PowerShell scripts, anything that you can script with PowerShell can be run through the Portal! Opening a lot of opportunities for automation, without having to learn third party automation toolsets! Anyone who knows PowerShell can use it! Each script can be locked down to specific users and AD groups!

You can read more about WebJEA, directly on the GitHub page: [https://github.com/markdomansky/WebJEA](https://github.com/markdomansky/WebJEA "https://github.com/markdomansky/WebJEA")

This guide will concentrate on setting up WebJEA for self-service Azure Resource creation, however, can be used to enable much more self-service automation.

We will use a Windows Server 2019, running in Microsoft Azure, to run WebJEA from, and an Azure Key Vault to retrieve the secrets.

### Prerequisites

* Domain Joined server running Windows 2016+ Core/Full with PowerShell 5.1 
* The server must have permission to go out over the internet to Azure and be able to download PowerShell modules.
* CPU/RAM Requirements will depend significantly on your usage, start off low _(2-vCPU/4GB RAM)_ and grow as needed. 
* A service account to run WebJEA under.

I've created a Standard_B2ms _(2vCPU, 8GB RAM)_ virtual machine, called: WEBJEA-P01 in an Azure Resource Group called: webjea_prod

This server is running: Windows Server 2019 Datacenter and is part of my Active Directory domain, I've also created a service account called: webjea_services.

### Setup WebJEA

Once we have a Windows Server, now it's time to set up WebJEA!

#### Setup Self-Signed Certificate

If you already have a certificate you can use, skip this step, in the case of this guide, we are going to use a self-signed certificate.

1. Log into the WebJEA Windows server using your service account _(in my case it is: luke\\webjea_services)_.
2. Open PowerShell ISE as Administrator and after replacing the DNS name to suite your own environment run the following:

    $todaydt = Get-Date

    $3years = $todaydt.AddYears(3)

    New-SelfSignedCertificate -dnsname WEBJEA-P01.luke.geek.nz, WEBJEA.luke.geek.nz -notafter $3years -CertStoreLocation cert:\LocalMachine\My

Copy the Thumbprint, we will need that later.

3. Run the following to add the certificate to the 'Trusted Root Authorities' of the server

#### Setup WebJEA

1. Download the latest [release package](https://github.com/markdomansky/WebJEA/releases "WebJEA - Releases") _(zip file)_ onto the WebJEA Windows server
2. Extract it, you should have 2 files and 2 folders:

* Site\\
* StarterFiles\\
* DSCConfig.inc.ps1
* DSCDeploy.ps1

3. Open PowerShell ISE as Administrator and open DSCDeploy.ps1

WebJEA uses PowerShell DSC _(Desired State Configuration)_ to set up a lot of the setup for us. 

DSC will do the following for us:

* Install IIS
* Create the App Pool and set the identity
* Create and migrate the Site files to the IIS website folder
* Configure SSL (if we were using it)
* Update the WebJEA config files to point towards the script and log locations

Even though most of the work will be automated for us, we do have to do some configurations to make it work in our environment

I am not using a Group Managed Service Account, I am just going to use a normal AD account as a service account _(ie webjea_services)_, but you can and the commands to create them are in the DSCDeploy.ps1 script.

Change the following variables to suit your setup, in my case, I have moved WebJEA resources to their own folder, so it's not sitting directly on the OS drive, but until its own Folder.

* AppPoolUserName =  'your service account name'
* AppPoolPassword = 'the password for your service account' #make sure you don't save the DSC file so the password is stored in plain text.
* WEB

![](/uploads/webjea_dsc.png)

One thing to note is that the DSCDeploy.ps1 is calling _(dot sourcing)_ the DSCConfig deploy script, by default, it is looking for it in the same folder as the DSCDeploy.ps1 folder, however, if you just opened up PowerShell ISE, you may notice that you are actually in C:\\Windows\\System32, so it won't be able to find the script to run, you can either change the script to point directly to the file location or you can change the directory you are into to match the files, in my case in the Script pane I run the following: 

    cd 'C:\Users\webjea_services\Downloads\webjea-1.1.157.7589'

Now run the script and wait.

If you get an error, saying that the script is not digitally signed run the following in the script pane:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

This is because the PowerShell execution policy hasn't been set, depending on the scripts you are running you may have to update the execution policy for the entire system, but for now, we will set it to Bypass for this process only, now re-run the script again, you should see DSC kick-off and start your configuration and setup of IIS and the WebJEA site.

![](/uploads/webjea_startingdsc.png)

You should also see the files/folders starting to be created!

Note: If you need to make a configuration change, feel free to change it in the DSCDeploy.ps1, DSC will make sure that the configuration is applied as per your configuration.