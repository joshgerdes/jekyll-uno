---
date: 2021-07-06 00:00:00 +1200
title: Create Custom Roles for Microsoft Azure
permalink: /azure/create-custom-roles-for-microsoft-azure/
author: Luke
categories:
- Azure
- PowerShell
toc: true
header:
  teaser: images/iazure-marketplace-banner.png
---
Microsoft Azure uses Role's to define who can access what - Role-Based Access Control (_RBAC)_.

You may be familiar with some of the more common ones, such as:

* Owner
* Contributor
* Reader

Behind the scenes, each role is a separate grouping of permissions that determine what level of permissions someone or something has in Azure; these permissions are usually in the form of:

* Read
* Write
* Delete
* Action

Each role can be assigned to a specific Resource, Subscription, Management Group or Resource Group through an 'Assignment' _(you assign a role if you give someone Contributor rights to a Resource Group, for example)_.

These permissions can be manipulated and custom roles created.

> Why would you use custom roles you ask? As usual - it depends!

Custom Roles can give people or objects JUST the right amount of permissions to do what they need to do, nothing more and nothing less, an example of this is maybe you are onboarding a support partner, if they are will only be supporting your Logic Apps, WebApps and Backups, you may not want them to be able to log support cases for your Azure resources; instead of attempting to mash several roles together that may give more or fewer rights than you need, you can create a custom role that specifically gives them what they need, you can then increase or decrease the permissions as needed, however, if a built-in role already exists for what you want. There is no need to reinvent the wheel, so use it!

I will run through a few things to help arm you understand and build your own Custom Roles, primarily using PowerShell.

### Install the Azure PowerShell Modules

As a pre-requisite for the following, you need to install the Azure (Az) PowerShell Module. You can skip this section if you already have the PowerShell modules installed.

1. Open **Windows PowerShell**
2. Type **in**:

       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
       Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
3. If you have issues **installing** the **Azure PowerShell module** - see the Microsoft documentation directly: Install the [Azure Az PowerShell module](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.1.0 "Install the Azure Az PowerShell module"){:target="_blank"}.
4. Once you have the Azure PowerShell module installed, you can **connect to** your **Azure** subscription using the little snippet below:

       #Prompts for Azure credentials 
       Connect-AzAccount
       #Prompts Window allowing you to select which  Azure Subscription to connect to 
       $subscriptionName = (Get-AzSubscription) | Out-GridView -Title 'Select Azure Subscription' -PassThru | Set-AzContext -SubscriptionName $subscriptionName

### Export Built-in Azure Roles

One of the best ways to learn about how an Azure Role is put together is to look at the currently existing roles.

1. The following PowerShell command will **list** all **current** Azure **roles**:

       Get-AzRoleDefinition
2. For a more human-readable view that **lists** the B**uilt-in Azure roles and their descriptions,** you can filter it by:

       Get-AzRoleDefinition | Select-Object Name, Description
3. As you can see in the screenshot below, there are many various roles, from EventGrid Contributor to AgFood Platform Service and more! At the time of this article, there were 276 built-in roles.
4. ![Azure Builtin Roles](/uploads/az_roledefinitions.png "Azure Builtin Roles")
5. Now that we have successfully been able to pull a list of the existing roles, we will now **export** them as **JSON** files to take a proper look at them.
6. The PowerShell script below will create a few folders on your computer as a base to work from _(feel free to change the folders to suit your folder structure or access rights)_.
   * c:\\Temp
   * c:\\Temp\\AzureRoles
   * C:\\Temp\\AzureRoles\\BuiltinExports\\
   * C:\\Temp\\AzureRoles\\CustomRoles
7. Once the folders have been created, it will Get the Azure Role definitions and export them into JSON into the **BuiltinExports folder** to be reviewed.

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
8. Once completed, you should now **see** the **JSON files** below:
9. ![Azure Role - JSON files](/uploads/az_exportroles.png "Azure Role - JSON files")

_Although you can use Notepad, I recommend using_ [_Visual Studio Code_](https://code.visualstudio.com/Download){:target="_blank"} _to read these files. This is because Visual Studio Code will help with the syntax as well._

### Review Built-in Azure Roles

If you open one of the roles, I will open the Azure Digital Twins Data Owner role; however, it doesn't matter.

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

These fields make up your Role.

![Azure Role - JSON](/uploads/az_rolereview_azdigitaltwinsdataowner.png "Azure Role - JSON")

* The **Name field** is pretty self-explanatory - this is the name of the Azure Role and what you see in the Azure Portal, under Access control (IAM).
* ![Azure Portal - Role](/uploads/az_rolereview_azdigitaltwinsdataowneriam.png "Azure Portal - Role")
* The same is true for the: **Description** **field**.

  _These are essential fields as they should tell the users what resource or resources the role is for and what type of access is granted._
* The **IsCustom field** is used to determine if the Azure Role is a custom made policy or not; any user-created Role will be set to True, while any In-Built role will be False.
* The **Actions field** is used to determine what management operations can be performed. However, the Azure Digital Twins role doesn't have any (as it is mainly Data Action based) if we look at another Role such as the: Azure Kubernetes Service RBAC Admin role:
  * ""Microsoft.Authorization/*/read",
  * "Microsoft.Insights/alertRules/*",
  * "Microsoft.Resources/deployments/write",

  You can see that it has the rights to Read the permissions, create and delete any Alert rules and update resources.
* The **NotActions field** is used to exclude anything from the Allowed actions
* The **DataActions field** allows you to determine what data operations can be performed. Usually, these are sub-resource tasks, where management or higher-level operations are performed in the Actions field, more specific resource actions are performed in the DataActions field.

  The NotDataActions field is used to exclude anything from the Allowed actions in the DataActions

To help get a feel of the differences with the Actions, here is a list of Actions and DataActions for the Azure Kubernetes Service RBAC Admin role:

* ![Azure Custom Role - JSON](/uploads/az_rolereview_azkuberservicerbacactions.png "Azure Custom Role - JSON")
* And finally, the **AssignableScopes** is used to specify where the role will be available for assignment, whether it can be assigned at a subscription or resource group or management group level. You will notice that most if not all built-in Azure Roles have an Assignable scope of "/" - this means that it can be assigned everywhere _(Subscriptions, Resource Groups, Management Groups etc.)._

### Review Azure Provider Namespaces

You may have noticed that each Action has a provider. In the example of a Virtual Machine, the provider is Microsoft.Compute.

1. To get a **list** of all **current Providers,** run the following command:

       Get-AzProviderOperation | Select-Object ProviderNamespace -Unique

   At the time of writing, there are 198 current Providers! So that's 198 providers or overall buckets of resources that has permissions over.
2. We can **drill** into a **provider** a bit **further** to check out current Operations:

       Get-AzProviderOperation -Name Microsoft.Compute/*
3. This **displays** a **list** of **all providers** within the Microsoft.Compute namespace, such as (but definitely not limited to):
   1. Virtual machines
   2. Virtual Machine Scale Sets
   3. Locations
   4. Disks
   5. Cloud Services
4. If we wanted to drill into the Virtual Machines **providers** a bit more, we could **filter** it like:

       Get-AzProviderOperation -Name Microsoft.Compute/virtualMachines/*
5. Here we can finally see the available actions, and for example, the following Action will allow you to Read the VM sizes available to a Virtual Machine:

* Operation: Microsoft.Compute/virtualMachines/vmSizes/read
* operation name: Lists Available Virtual Machine Sizes
* ProviderNamespace: Microsoft Compute
* ResourceName: Virtual Machine Size
* Description: Lists available sizes the virtual machine can be updated to
* IsDataAction      : False

1. You can use the PowerShell script below to export all the Providers and their Operations to a CSV for review:

       $Providers = Get-AzProviderOperation
       
       $results = @()
       
       ForEach ($Provider in $Providers) {
       
       
       
           $results += [pscustomobject]@{
               'Provider NameSpace' = $Provider.ProviderNamespace
               Description          = $Provider.Description
               'Operation Name'     = $Provider.OperationName
               Operation            = $Provider.Operation
               ResourceName         = $Provider.ResourceName
       
                               
           }
       
       }
         
       $results | Export-csv c:\temp\AzureRBACPermissions.csv -NoTypeInformation

Using the namespace, providers and actions, you should now be able to see the power behind Role-based access control and how granular you can get.

### Add a Custom Role using PowerShell

Now that we understand how to navigate the Namespaces and Built-In Roles available in Microsoft Azure using PowerShell, now we will create one.

I have created a base template to help you start.

This base template has the following fields that the majority of most custom roles will use:

* Name
* IsCustom
* Description
* Actions
* AssignableScopes _(make sure you put in the <SubscriptionID> of your Azure subscription, you are assigning the role to.)_

1. **Edit** these **fields** _(apart from IsCustom, which you should leave as True)_ as you need.

{% gist 2f5f4e0a4cc587d7cd297cee7569f621 %}

This Custom Role - Template allows you to read the name of all Resource Groups in a subscription and open a Microsoft Support case.

In my example, I am going to add a new role called:

* LukeGeek-WebApp Deployment-RW

This role will allow users to Deploy and modify Azure WebApps, among other things!

{% gist c7112d45f01959963c7e919ce06098d0 %}

1. To **add** the **Custom Role** to Azure, I will **run** the following **PowerShell** command:

       New-AzRoleDefinition -InputFile "C:\\temp\\AzureRoles\\CustomRoles\\LukeGeek-WebApp Deployment-RW.json" -Verbose

**Your new Custom Role has now been uploaded to Azure and can be selected for an assignment.**

### Add a Custom Role using the Azure Portal

Now that we have been through and investigated the Azure roles and their providers and actions, instead of using PowerShell to look through and create manually, you can use the Azure Portal!

> _*Gasp!* Why didn't you tell me earlier about this, Luke?_
>
> _Well, fellow Azure administrator, I found it easier to look at PowerShell and JSON to explain how the Custom Roles were made, vs staring at the Azure Portal and to be honest, really just because! Like most things in IT there are multiple ways something can be done!_

 1. Log in to the **Azure Portal**
 2. Navigate to your **Subscription**
 3. Click on **Access Control (IAM)** on the left-hand side blade
 4. Click on **Add**
 5. Click on **Add Custom Role**
 6. Type in the **Role Name**, for example, WebAdmin-RO
 7. Type in a clear **description** so that you can remember what this role is used for in a year!
 8. For Baseline permissions, select: **Start from Scratch**
 9. Click **Next**
10. Click **Add Permissions**
11. If you want, you can select: Download all permissions to review the providers and actions _(very similar to the Get-AzProviderOperation PowerShell command)_.![Azure Portal - Create Custom Role](/uploads/ad_role_addpermissions.png "Azure Portal - Create Custom Role")
12. As you should **see**, all the **Namespace providers** are listed with the Actions/Permissions that you can do.
13. In my example, I am going to search for **Microsoft Web Apps**
14. **Select** all '**Read**' operations _(remember to look at Data Actions as well, there may be resource level actions you might want to allow or exclude)_
15. Click **Add**
16. ![Azure Portal - Create Custom Role](/uploads/ad_role_webpermissions.png "Azure Portal - Create Custom Role")
17. Review the permissions and click **Next**
18. **Select** your assignable **scope** _(where the Role will be allowed so that you can assign it)_
19. Click **Next**
20. You can **review** and download the JSON for backup later _(this is handy if you are going to Automate the creation of roles in the future and want a base to start from)_
21. Click **Next**
22. Click **Create to create your Custom Role!**
23. ![Azure Portal - Create Custom Role](/uploads/ad_role_createcustomroleportal.png "Azure Portal - Create Custom Role")

### Assign a Custom Role using the Azure Portal

Now that you have created your Custom Role - it is time to assign it! So it is actually in use.

1. Log in to the **Azure Portal**
2. Navigate to your **Subscription or Resource Group** you want to delegate this role to
3. Click on **Access Control (IAM)**
4. Click **Add**
5. Click on **Role Assignment**
6. Under the 'Role' dropdown, **select** your Custom **Role.**
7. ![Azure Portal - Add Role Assignments](/uploads/ad_roleassignmentportal.png "Azure Portal - Add Role Assignments")
8. Now you can **select** the **Azure AD Group/User or Service Principal** you want to **assign** the role to and click **Save.**
9. Congratulations, **you have now assigned your Custom role!**

### Assign a Custom Role using PowerShell

You can assign Custom Role's using PowerShell. To do this, you need a few things such as the Object ID, Assignable Scope IDs etc., instead of rehashing it, this Microsoft article does an excellent job of running through the process.

* [Assign Azure roles using Azure PowerShell](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-powershell "Assign Azure roles using Azure PowerShell"){:target="_blank"}