---
date: 2023-01-17T00:00:00.000+13:00
title: Azure Deployment history cleanup with Azure DevOps
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Microsoft Azure has a limit of [800 deployments per resource group](https://learn.microsoft.com/azure/azure-resource-manager/management/azure-subscription-service-limits?WT.mc_id=AZ-MVP-5004796#resource-group-limits "Resource group limits"). This means that a single resource group can only contain 800 historical deployments at most.

> A deployment in Azure refers to the process of creating or updating resources in a resource group.

When deploying resources in Azure, it is essential to keep track of the number of [historic deployments](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history?tabs=azure-portal&WT.mc_id=AZ-MVP-5004796 "View deployment history with Azure Resource Manager") in a resource group to ensure that the limit is not exceeded. This is because new deployments will fail if the limit is exceeded, and creating or updating resources in that resource group will not be possible.

If you have CI/CD _(Continuous Integration and Continuous Deployment)_ set up to deploy or change your infrastructure or services with code, it can be easy to reach this limit. [Azure will attempt to do this automatically](https://learn.microsoft.com/azure/azure-resource-manager/troubleshooting/deployment-quota-exceeded?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796 "Resolve error when deployment count exceeds 800") when reaching your limit, but you may want to pre-empt any problems if you make a lot of deployments and the system hasn't had time to prune automatically.

To avoid exceeding the deployment limit, it may be necessary to clean up old deployments.

This can be done by using a script to remove deployments that are no longer needed.

So let's build an Azure DevOps pipeline that runs weekly to connect to our Microsoft Azure environment and clean up historical deployments.

For this article, I will assume you have an Azure DevOps repository setup and the permissions _(Owner)_ to make the necessary privileged actions to the Microsoft Azure environment to do the setup.

#### Deploy and Configure

##### Create Service Prinicipal

 1. Navigate to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure")
 2. Click on [**Azure Active Directory**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/\~/Overview "Azure Active Directory")
 3. Click on [**App Registrations**](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/\~/RegisteredApps "Azure App Registrations")
 4. Click on: **+ New Registration**
 5. Enter the following information:
    * **Name** (i.e. SPN.AzDeploymentCleanup)
 6. Click **Register**
 7. Copy the following for later when we add the SPN to Azure DevOps.
    * Application (client) ID
    * Directory (tenant ID)
 8. Click on **Certificates & Secrets**
 9. Press **+ New Client Secret**
10. Enter a relevant description and expiry date and click Add
11. **Copy** the **value** of the new secret (this is essentially your password), and you won't be able to see the value again.

##### Create Custom Role & Assign permissions

Now that your service principal has been created, it is time to assign permissions because this script targets all subscriptions under a management group; we are going to set the permissions to that management group so that it flows to all subscriptions underneath it - and in the view of least privileged we will create a Custom Role to apply to our Service Principal.

##### Create Custom Role

In order for the deployment history to be completed, we will need the following permissions:

* "Microsoft.Resources/deployments/delete",
* "Microsoft.Resources/subscriptions/resourceGroups/read",
* "Microsoft.Management/managementGroups/read",
* "Microsoft.Resources/subscriptions/read",
* "Microsoft.Management/managementGroups/descendants/read",
* "Microsoft.Management/managementGroups/subscriptions/read",
* "Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read",
* "Microsoft.Resources/subscriptions/resourcegroups/deployments/read",
* "Microsoft.Resources/subscriptions/resourcegroups/deployments/write",
* "Microsoft.Resources/deployments/read"

 1. Navigate to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure")
 2. In the search bar above, type in and navigate to [**Management Groups**](https://portal.azure.com/#view/Microsoft_Azure_ManagementGroups/ManagementGroupBrowseBlade/\~/MGBrowse_overview "Management Groups")
 3. Click a management group, click on **Access Control (IAM)**
 4. Click **+ Add**
 5. Click **Add Custom Role**
 6. Type in a role name _(an example is: AzDeploymentHistoryCleanup)_
 7. Check Start from **Scratch** and next click
 8. Click **+ Add permissions** and the permissions above _(you can search for them)_. Feel free to import the role from a JSON file "[here](https://github.com/lukemurraynz/AzDeploymeantCleanup "AzDeploymeantCleanup")".
 9. Click **Next**
10. Add **Assignable Scopes** _(this is the scope you can use to assign a role to - this won't assign it to the Service Principal; it will only open it up so we can assign it)_. Make sure you assign it at the management group level you are targetting.
11. Click **Review + Create**
12. Click **Create**

##### Assign Permissions

Now that the custom role has been created, it is time to assign the role to the service principal we created earlier.

 1. Navigate to the [**Microsoft Azure Portal**](https://portal.azure.com/#home "Microsoft Azure")
 2. In the search bar above, type in and navigate to [**Management Groups**](https://portal.azure.com/#view/Microsoft_Azure_ManagementGroups/ManagementGroupBrowseBlade/\~/MGBrowse_overview "Management Groups")
 3. Click on the management group you want to manage and click on **Access Control (IAM)**
 4. Click **Add**
 5. Click **Add Role Assignment**
 6. Select your custom role _(you can toggle the type column, so CustomRoles are first in the list)_
 7. Click **Members**
 8. Make sure '_User, group or service principal_' is selected and click **+ Select Members**
 9. Select your Service Principal created earlier _(i.e. SPN.AzDeploymentCleanup)_
10. Click **Select**
11. Click **Review + assign** to assign the role.

Note: Copy the Management Group ID and name, as we will need the information, along with the Service Principal and tenant IDs from earlier, in the next step of setting up Azure DevOps.

##### Configure Azure DevOps Service Endpoint

Now that the Service Principal and permissions have been assigned in Azure, it's time to create the service connection endpoint that will allow Azure DevOps to connect to Azure.

 1. Navigate to your [**Azure DevOps**](http://dev.azure.com/ "Azure DevOps") organisation
 2. Create a **Project**, if you haven't already
 3. Click on **Project Settings**
 4. Navigate to **Service Connection**
 5. Click on **New service connection**
 6. Select **Azure Resource Manager**
 7. Click **Next**
 8. Select **Service principal (manual)**
 9. Click **Next**
10. For the scope, select **Management Group**
11. Enter the **Management Group ID**, the **Management Group Name**
12. Time to enter in the Service Principal details copied earlier, for the Service Principal Id paste in the Application ID.
13. The Service Principal key, enter the secret client value and select the Tenant ID
14. Click **Verify** - to verify the connectivity to the azure platform from Azure DevOps
15. Select **Grant access permission to all pipelines** and click **Verify and save**

##### Configure script and pipeline

Now that we have our:

* Azure Service Principal
* Custom role and assignment
* Service connection

We now need to import the script and pipeline.

If you haven't already done - [create a Repo](https://learn.microsoft.com/azure/devops/repos/git/create-new-repo?view=azure-devops&WT.mc_id=AZ-MVP-5004796 "Create a new Git repo in your project") for the AzHistoryCleanup script.

You can clone _(or copy)_ the files in the [**AzDeploymentCleanup**](https://github.com/lukemurraynz/AzDeploymeantCleanup "AzDeploymeantCleanup") repo to your own.

First, we need to copy the name of the Service Principal.

 1. Click **Project settings**
 2. Click **Service Connections**
 3. Click on your **Service Connection** and copy the **name** _(ie SC.AzDeploymentCleanup)_
 4. Navigate back to your Repo, and click on **AzDeploymentCleanup.yml** (this will become your pipeline)
 5. Click **Edit**
 6. Update the variable for **ConnectedServiceNameARM** to the name of your service connection
 7. Here you can also edit the **Script Arguments** - for example, in my demo, I am targeting the **ManagementGroup** named: mg-landing zones and keeping the latest five **deployments**.
 8. By default, I also have a [cron job](https://learn.microsoft.com/azure/devops/pipelines/process/scheduled-triggers?view=azure-devops&tabs=yaml&WT.mc_id=AZ-MVP-5004796 "Configure schedules for pipelines") to schedule this pipeline at 6 AM UTC every Sunday, and you can remove or edit this.
 9. Once your changes are made, click **Commit**
10. Now that your pipeline has been updated, its time to create it - click on **Pipelines**
11. 