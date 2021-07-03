---
date: 2021-07-03 00:00:00 +1200
title: Create Custom Roles for Microsoft Azure
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Microsoft Azure uses Role's to define who can access what - Role-Based Access Control (_RBAC)_.

You may be familiar with some of the more common ones such as:

* Owner
* Contributor
* Reader

Behind the scenes, each role is a separate grouping of permissions that determine what level of permissions someone or something has in Azure, these permissions are usually in the form of:

* Read
* Write
* Delete
* Action

Each role can be assigned to a specific Resource, Subscription, Management Group or Resource Group, through what is called an 'Assignment' _(you are assigning a role if you give someone Contributor rights to a Resource Group for example)_.

These permissions can be manipulated and custom roles created.

Why would you use custom roles you ask? As usual - it depends!

Custom Roles can be used to give people or objects JUST the right amount of permissions to do what they need to do, nothing more and nothing less, an example of this is maybe you are onboarding a support partner, but they are only supporting Logic Apps, WebApps and Backups and you don't want them to be able to log support cases for your Azure resources for example, instead of attempting to mash several roles together that may give more or fewer rights than you need, you can create a custom role that specifically gives them what they need, you can then increase or decrease the permissions as needed, however, if a built-in role already exists for what you want, then there is no need to reinvent the wheel so use it!

I am going to run through a few things that will help arm you to understand and build your own Custom Roles, primarily using PowerShell.

### Install the Azure PowerShell Modules

As a pre-requisite for the following, you need to install the Azure (Az) PowerShell Module, you can skip this section if you already have the PowerShell modules installed.

Open Windows PowerShell

Type in:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

If you have issues, with installing the Azure PowerShell module - see the Microsoft documentation directly: Install the [Azure Az PowerShell module](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.1.0 "Install the Azure Az PowerShell module")

Once you have the Azure PowerShell module installed, you can connect to your Azure subscription using the little snippet below:

sd