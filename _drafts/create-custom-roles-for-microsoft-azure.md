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

###  Review Built-in Azure Roles

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

The Actions field, is used to determine what management operations can be performed, although the Azure Digital Twins role, doesn't have any (as it is mainly Data Action based), if we look at another Role such as the: Azure Kubernetes Service RBAC Admin role:

* ""Microsoft.Authorization/*/read",
* "Microsoft.Insights/alertRules/*",
* "Microsoft.Resources/deployments/write",

You can see that it has the rights to Read the permissions, create and delete any Alert rules and update resources.

* 