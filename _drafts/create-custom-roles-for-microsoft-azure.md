---
date: 2021-07-03T00:00:00.000+12:00
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

      #Prompts for Azure credentials
      Connect-AzAccount
      
      #Prompts Window allowing you to select which  Azure Subscription to connect to
      $subscriptionName = (Get-AzSubscription) | Out-GridView -Title 'Select Azure Subscription' -PassThru
      Set-AzContext -SubscriptionName $subscriptionName

### Export Built-in Azure Roles

One of the best ways I found to learn about how an Azure Role is put together, is to take a look at the currently existing roles.

The following PowerShell command will list all current Azure roles:

    Get-AzRoleDefinition

For a more human-readable view, that lists the Built-in Azure roles and their descriptions you can filter it by:

    Get-AzRoleDefinition | Select-Object Name, Description

As you can see in the screenshot below, there are a lot of various roles, from EventGrid Contributor to AgFood Platform Service and more! At the time of this article, there were 276 built-in roles.

![](/uploads/az_roledefinitions.png)

Now that we have successfully been able to pull a list of the existing roles, we will now export them as JSON files, so we can take a proper look at them.

The PowerShell script below will create a few folders on your computer, as a base to work from _(feel free to change the folders to suit your folder structure or access rights)_.

* c:\\Temp
* c:\\Temp\\AzureRoles
* C:\\Temp\\AzureRoles\\BuiltinExports\\
* C:\\Temp\\AzureRoles\\CustomRoles

Once the folders have been created, it will Get the Azure Role definitions and export them into JSON into the BuiltinExports folder, so they can be reviewed.

    New-Item -ItemType Directory -Path c:\Temp -Force
    New-Item -ItemType Directory -Path c:\Temp\AzureRoles -Force
    New-Item -ItemType Directory -Path c:\Temp\AzureRoles\BuiltInExports -Force
    New-Item -ItemType Directory -Path c:\Temp\AzureRoles\CustomRoles -Force
    
    $a = Get-AzRoleDefinition
    
    Foreach ($role in $a)
    {
        $name = $role.Name
        Get-AzRoleDefinition -Name ($role).Name | ConvertTo-Json | Out-File c:\Temp\AzureRoles\BuiltInExports\$name.json
    }

Once completed, you should now see the JSON files below:

![](/uploads/az_exportroles.png)

_Although you can use Notepad, I recommend using_ [_Visual Studio Code_]() _to read these files, Visual Studio Code will help with the syntax as well._

### Review Built-in Azure Roles

If you open one of the roles, for example, I will open the Azure Digital Twins Data Owner role, however, it doesn't matter.

You should see the following fields:

* Name
* Id
* IsCustom
* Description
* Actions
* NotActions
* DataActions
* NotDataActions
* AssignableScopes

These fields, make up your Role.

![](/uploads/az_rolereview_azdigitaltwinsdataowner.png)

The Name field is pretty, self-explanatory - this is the name of the Azure Role and what you see in the Azure Portal, under Access control (IAM).

![](/uploads/az_rolereview_azdigitaltwinsdataowneriam.png)

The same is true for the: Description field.

These are highly important fields as they should tell the users, what resource or resources the role is for and what type of access is granted.

The IsCustom field is used to determine if the Azure Role is a custom made policy or not, any user-created Role will be set to True, while any In-Built role will be False.

The Actions field, is used to determine what management operations can be performed, although the Azure Digital Twins role, doesn't have any (as it is mainly Data Action based) if we look at another Role such as the: Azure Kubernetes Service RBAC Admin role:

* ""Microsoft.Authorization/*/read",
* "Microsoft.Insights/alertRules/*",
* "Microsoft.Resources/deployments/write",

You can see that it has the rights to Read the permissions, create and delete any Alert rules and update resources.

The NotActions field is used to exclude anything from the Allowed actions

The DataActions field allows you to determine what data operations can be performed, usually, these are sub-resource tasks, where management or higher-level operations are performed in the Actions field, more specific resource actions are performed in the DataActions field.

The NotDataActions field is used to exclude anything from the Allowed actions in the DataActions

To help get a feel of the differences with the Actions, here is a list of Actions and DataActions for the Azure Kubernetes Service RBAC Admin role:

![](/uploads/az_rolereview_azkuberservicerbacactions.png)And finally, the AssignableScopes is used to specify where the role will be available for assignment, whether it can be assigned at a subscription level or resource group or management group level, you will notice that most if not all built-in Azure Roles have an Assignable scope of "/" - this means that it can be assigned everywhere _(Subscriptions, Resource Groups, Management Groups etc)._

### Review Azure Provider Namespaces

You may have noticed that each Action has a provider, in the example of a Virtual Machine the provider is: Microsoft.Compute.

To get a list of all current Providers run the following command:

    Get-AzProviderOperation | Select-Object ProviderNamespace -Unique

At the time of writing, there are 198 current Providers! That's 198 providers or overall buckets of resources that has permissions over.

We can drill into a provider a bit further to check out current Operations:

    Get-AzProviderOperation -Name Microsoft.Compute/*

This displays a list of all providers within the Microsoft.Compute namespace, such as (but definitely not limited to):

1. Virtual machines
2. Virtual Machine Scale Sets
3. Locations
4. Disks
5. Cloud Services

If we wanted to drill into the Virtual Machines providers a bit more we can filter it like:

    Get-AzProviderOperation -Name Microsoft.Compute/virtualMachines/*

Here we can finally see the available actions, for example, the following Action will allow you to Read the VM sizes available to a Virtual Machine:

* Operation: Microsoft.Compute/virtualMachines/vmSizes/read
* operation name: Lists Available Virtual Machine Sizes
* ProviderNamespace: Microsoft Compute
* ResourceName: Virtual Machine Size
* Description: Lists available sizes the virtual machine can be updated to
* IsDataAction      : False

Using the namespace, providers and actions you should now be able to see the power behind Role-based access control and how granular you can get.

### Add a Custom Role using PowerShell

Now that we understand, how to navigate the Namespaces and Built-In Roles available in Microsoft Azure using PowerShell, now we will create one.

I have created a base template, to help you start.

This base template has the following fields, that will be used by the majority of most custom roles:

* Name
* IsCustom
* Description
* Actions
* AssignableScopes _(make sure you put in the <SubscriptionID> of your Azure subscription, you are assigning the role to.)_

Edit these fields _(apart from IsCustom, which you should leave as True)_ as you need.

[https://gist.github.com/lukemurraynz/2f5f4e0a4cc587d7cd297cee7569f621](https://gist.github.com/lukemurraynz/2f5f4e0a4cc587d7cd297cee7569f621 "https://gist.github.com/lukemurraynz/2f5f4e0a4cc587d7cd297cee7569f621")

This Custom Role - Template, simply allows you to read the name of all Resource Groups in a subscription and open a Microsoft Support case.

In my example, I am going to add a new role called:

* LukeGeek-WebApp Deployment-RW

This role will allow users to Deploy and modify Azure WebApps, among other things!

[https://gist.github.com/lukemurraynz/c7112d45f01959963c7e919ce06098d0](https://gist.github.com/lukemurraynz/c7112d45f01959963c7e919ce06098d0 "https://gist.github.com/lukemurraynz/c7112d45f01959963c7e919ce06098d0")

To add the Custom Role to Azure, I will run the following PowerShell command:

    New-AzRoleDefinition -InputFile "C:\temp\AzureRoles\CustomRoles\LukeGeek-WebApp Deployment-RW.json" -Verbose

Your new Custom Role has now been uploaded to Azure and can be selected for an assignment.

### Add a Custom Role using the Azure Portal

Now that we have been through and investigated the Azure roles and their providers and actions, instead of using PowerShell to look through and create manually, you can use the Azure Portal!