---
date: 2021-07-03 00:00:00 +1200
title: Start VM on Connect for Azure Virtual Desktop
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/avddesktopfull.png"

---
One of the models of Cloud governance and cost in Microsoft Azure is _'Pay As You Go', ie. Pay for what you need, when you need it._

The Azure Resource Manager fabrics allow you to scale up down resources when you need it, whether it is built-in to the Azure portal or through various other automation mechanisms.

For Azure Virtual Desktop, this means making sure that session hosts _(Virtual Machines)_ are available for users to connect to consume their services, when they need it the most, whether it’s the first thing in the morning or late hours of the evening.

One of the technologies, that can help with this is: [Start VM on Connect ](https://docs.microsoft.com/en-us/azure/virtual-desktop/start-virtual-machine-connect "Start VM On Connect")_(Start VM on Connect allows users to start the virtual machine from a deallocated state)_.

* Imagine a 9 - 5 PM Monday to Friday business, during the business period, Azure Virtual Desktop is available, anything out of these hours the session hosts are shut down to reduce operational costs.
* A business user, get some urgent work on Saturday morning then tries to connect to Azure Virtual Desktop resources to complete the work, because they were turned off outside of business hours, they can't and have to ring IT support to get resources started (the alternative would be to leave Virtual Machines running, which may or may not be needed).
* Using 'Start Virtual Machine on Connect', the moment that the user attempts to connect a Virtual Machine is started, and then it allows the users to log in and do their work, without a call to IT overall saving money, as the hosts are only started when they are first needed. The feature will also only turn on additional VMs (if available) when the first VM reaches the session limit.

This is a host-level setting, so setting 'Start VM on Connect' will affect all session hosts in the host pool, you cannot target specific Virtual Machines in a session host at this stage.

> _As of 03/07/21 (NZ date format - DD/MM/YY): The Start VM on Connect feature is currently in public preview. This preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see_ [_Supplemental Terms of Use for Microsoft Azure Previews_](https://azure.microsoft.com/support/legal/preview-supplemental-terms/)_._

Follow the guide below to implement, the Microsoft documentation is pretty good, but hoping this might fill in a few gaps for people.

### Create a Custom Role for "Windows Virtual Desktop"

In order for the "Windows Virtual Desktop" service principal (this should already exist, it is an inbuilt SPN created by the Azure infrastructure, it currently called Windows Virtual Desktop but expect this name to be updated in the future) to have the ability to Start a Virtual Machine, we first need to give it rights. You could simply give it Contributor, or Virtual Machine Contributor rights, but want to go with the least privileged, so we will create a custom role.

 1. Log in to the **Azure Portal**
 2. Navigate to the **Subscription** _(you can only currently create custom roles at a subscription level)_ that your session hosts exist in
 3. Look for the **Subscription ID** _(**copy** this, we will need it later on, usually found on the Overview window of the Subscription)_
 4. **Download** the AVD-StartVMOnConnect **JSON** file **below** and **save** it to a location, you can edit.
 5. [https://gist.github.com/lukemurraynz/398a8b15257c65d94b8f1993dee22365](https://gist.github.com/lukemurraynz/398a8b15257c65d94b8f1993dee22365 "https://gist.github.com/lukemurraynz/398a8b15257c65d94b8f1993dee22365")
 6. **Open** up the **JSON** file _(this is the Custom Role we are creating, as you can see we are only allowing the ability to Read a Virtual Machine and Start it)_
 7. **Replace** the: **<SubscriptionID>** with **your subscription ID**, created earlier and **save** the JSON file.
 8. ![](/uploads/customrolejson_subscriptionid.png).
 9. Click on **Access Control (IAM)** in the left-hand side blade
10. Click **Add**
11. Click **Add Custom Role**
12. ![](/uploads/azureportal_iam_customrole.png)
13. **Name** your Custom Role **Name** something meaningful, for example, _AVD-StartVMOnConnect_
14. **Add** a meaningful **Description**, for example, mine is:

    _Created: 03/07/21_

    _Created by: Luke Murray_

    _Created for: Custom role, designed to allow 'Windows/Azure Virtual Desktop' rights to Start session hosts._
15. For: Baseline permissions, select **Start from JSON**

    **Select** the **JSON file** you downloaded and edited earlier
16. ![](/uploads/azureportal_iam_customrole_create.png)
17. Click on **Next**
18. **Verify** the **permissions** are as below _(if they aren't, you may need the redownload or check the JSON file for syntax issues - I recommend downloading_ [_Visual Studio Code_](https://code.visualstudio.com/ "Visual Studio Code")_)_:
19. ![](/uploads/azureportal_iam_customrole_permissions.png)
20. Click **Next**
21. We used the subscription property, to **select** the **assignable scope** _(ie the scope is where this role will be available for you to assign access to)_, but now using the Azure Portal, we can select a specific Resource Group to limit the roles access, please be careful with doing this, especially if you are planning on expanding out your Azure Virtual Desktop infrastructure in the future as you may forget that this role may not be available in other resource groups. I am going to leave mine at the Subscription level and click **Next**
22. Here we can **verify** and **save** the changed JSON file _(if you want for future reference)_ and click Next to review your configuration
23. Click Create to create your Custom Role!
24. ![](/uploads/azureportal_iam_customrole_reviewcreate.png)

### Assign your Custom Role

Now that you have created your custom role, for Azure Virtual Desktop, it is now time to assign it, this is where you can assign and lock down the role, in my case I only have one Resource Group where my session hosts sit in, so going to assign it a Resource Group level, but feel free to assign this at a subscription level.

 1. Log in to the **Azure Portal**
 2. **Navigate** to the **Resource Group** _(or Subscription)_, that has your Azure Virtual Desktop session hosts
 3. Click on **Access Control (IAM)** in the left-hand side blade
 4. Click on **+ Add**
 5. Click on **Add role assignment**
 6. **Select** the **Role** you created earlier _(ie AVD-StartVMOnConnect)_
 7. **Specify** the '**Windows Virtual Desktop**' service principal and select **Save**
 8. ![](/uploads/azureportal_addroleassignment.png)
 9. If you want you can click on Role Assignments, to verify your role has been assigned:
10. ![](/uploads/azureportal_assignedrolecheck.png)

### Configure Start VM on Connect

 1. Log in to the **Azure Portal**
 2. Navigate to your **Host Pool**
 3. Click on **Properties**
 4. Select '**Yes**' to **Start VM on Connect**
 5. Click **Save**
 6. ![](/uploads/azureportal_startvmonconnect.png)
 7. **Congratulations you have now set up Azure Virtual Desktop - Start VM on Connect**, next time someone connects to a turned-off Azure Virtual Desktop session host, the Virtual Machines will now automatically start the users will get a prompt like below:
 8. ![](/uploads/avd_startvmconnectprogress1.png)
 9. ![](/uploads/avd_startvmconnectprogress2.png)
10. Before finally, prompting for their login credentials!