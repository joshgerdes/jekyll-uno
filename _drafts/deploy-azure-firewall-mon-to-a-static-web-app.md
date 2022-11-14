---
date: 2022-11-14 00:00:00 +1300
title: Deploy Azure-Firewall-mon to a Static Web App
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
[Azure-Firewall-mon](https://github.com/nicolgit/azure-firewall-mon "Azure-Firewall-mon") is a near real-time [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Firewall?") log viewer.

> Azure-Firewall-mon provides an _alternative_and_opinable_ 😊 way to access and inspect Azure Firewall logs. The recommended approach for analysing Azure Firewall logs is to set up a Log Analytics Workspace to collect all the data and use Kusto _(KQL)_ queries to check what's happening.
>
> In Azure-Firewall-mon, the idea is to provide an approach much more like Sysinternals Process Monitor or Check Point's SmartView, where there is no queries or dashboards that you need to implement first to get working. Still, all events are available as a log stream. In addition, a full-text search at the top of the page lets you quickly filter the content displayed on the screen, helping you understand what is happening right now (or close to present).

### Overview

Azure-Firewall-mon _(AFM or Azure Firewall Monitor)_ is a custom solution _(currently in a functional beta)_ created by an Italian Microsoft Cloud Solution Architect called: [Nicola Delfino](https://nicolgit.github.io/ "Nicola Delfino"), its worth mentioning that although a Microsoft CSA makes AFM, **IT IS NOT A SUPPORTED MICROSOFT PRODUCT**.

Monitoring Azure Firewall can be a pain - with trawling through logs - using the [Azure Firewall Workbook](https://learn.microsoft.com/en-us/azure/firewall/firewall-workbook?WT.mc_id=AZ-MVP-5004796 "Monitor logs using Azure Firewall Workbook") - helps fill in the gap - especially around the application and network rule traffic. Still, you may want something more straightforward and designed for real-time traffic to assist with in-the-moment troubleshooting.

**Azure-Firewall-mon is an open-source,** [**Single Page Application**](https://en.wikipedia.org/wiki/Single-page_application) **written in** [**Angular**](https://angular.io/) **and hosted on an** [**Azure WebApp **](https://az-firewall-mon.azurewebsites.net "az-firewall-mon")- so to use this, you don't need to deploy to your environment.. add in an Event Hub connection string, and away you go _(there is also a demo mode - so you can see what the experience will be like)_!

![az-firewall-mon landing page](/uploads/az-firewall-mon.png "az-firewall-mon")

**We can deploy it to an Azure** [**Static Web App**](https://azure.microsoft.com/en-us/products/app-service/static/?WT.mc_id=AZ-MVP-5004796 " Static Web Apps") **for those who would instead host it in our environment.**

> "Azure Static Web Apps is a service that automatically builds and deploys full-stack web apps to Azure from a code repository. When you create an Azure Static Web Apps resource, Azure interacts directly with GitHub or Azure DevOps to monitor a branch of your choice. Every time you push commits or accept pull requests into the watched branch, a build is automatically run and your app and API is deployed to Azure."

![Azure Static WebApps - Overview](/uploads/azure-static-web-apps-overview.png "Azure Static WebApps - Overview")

### Deployment

#### Prerequisites

Today, we are going to deploy Azure-Firewall-mon into an Azure Static Web App - to do this; we will need the following prerequisites:

* A [GitHub](https://github.com/ "GitHub") account
* An [Azure](https://azure.microsoft.com/en-us/?WT.mc_id=AZ-MVP-5004796 "Do more with less. On Azure.") subscription _(with permissions to deploy Event Hub, deploy an Azure Static WebApp, and configure Diagnostics on the Azure Firewall)_
* Azure Firewall _(provisioned)_

_Note: Also, ensure that your Event Hub is in the same region as your Azure Firewall so that you can use Diagnostics settings. Regarding the Azure Static WebApp - it doesn't matter; this is a global service  - and you will be entering the Event Hub listener._

We will use the Azure Portal and a browser to provision the workflow _(however, I will have added Azure Bicep to the bottom of the article for reference)_.

This article - assumes you have basic knowledge of GitHub and Microsoft Azure.

For this demo, I am using a [Hub & Spoke Azure](https://learn.microsoft.com/azure/architecture/reference-architectures/hybrid-networking/hub-spoke?tabs=cli&WT.mc_id=AZ-MVP-5004796 "Hub-spoke network topology in Azure") topology.

#### Fork the GitHub repository

The first thing we need to do is clone the Azure-Firewall-mon repository; this repository holds the source control of Azure-Firewall-mon. However, we need a clone of it - to use in our Static Web App - this will also allow us to pull down and build the latest changes and updates of the Azure-Firewall-mon tool while having the stability of maintaining your version of the tool.

1. In your favourite browser of choice, navigate to: [https://github.com/nicolgit/azure-firewall-mon](https://github.com/nicolgit/azure-firewall-mon "https://github.com/nicolgit/azure-firewall-mon")
2. Click **Fork** _(top right of the repository)_
3. ![GitHub - Create a new fork](/uploads/github_azfirewall_mon_createfork.png "GitHub - Create a new fork")
4. Click **Create fork**
5. You have now created a fork of the 'azure-firewall-mon' repository; when a new update of Azure-Firewall-mon comes out - you can also select 'Sync fork' - to keep your fork up-to-date and trigger a new build.

#### Create Static Web App and deploy azure-firewall-mon

Now that you have created a fork, it's time to create your Azure Static WebApp!

 1. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Click **+ Create a resource**
 3. Type in: **Static Web App**
 4. Select and click **Create**
 5. Create or **select** a **Resource Group**
 6. **Type** in the **name** of your Static Web App
 7. For the plan type, we will go with **Free**
 8. Select your **region** _(this is the staging environment used to create your resource so it can then be replicated geographically)_.
 9. Select **Source**, as **GitHub**
10. Click **Sign in** with **GitHub** _(and sign in with an account with access to the GitHub Repository fork of azure-firewall-mon created earlier)_.
11. **Authorise** the **Azure Static Web Apps** to have access to your repositories
12. **Select** your **organisation** and the azure-firewall-mon **repository** you forked earlier.
13. Select '**main**' for the branch
14. Under Build Presents, select **Angular**
15. For App location, enter "**/firewall-mon-app/**"
16. Leave Api location empty
17. For the Output location, enter: **"dist/firewall-mon-app"**
18. ![Azure Static WebApps - Angular Build](/uploads/github_azfirewall_mon_createbuildangular.png "Azure Static WebApps - Angular Build")
19. If you navigate to your own forked GitHub repository, you should see a new folder created under .github/workflows - and a new GitHub Actions workflow file!
20. ![Create Azure Static WebApp - Angular - Azure Portal](/uploads/create_azstaticwebapp_portal_azfw-mon.gif "Create Azure Static WebApp - Angular - Azure Portal")
21. If you select **Actions** in GitHub, you should see a deployment start.
22. After roughly 5 minutes, your **Azure Static App - will have deployed azure-firewall-mon**!
23. **Navigate** to your newly created [**Azure Static App**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2FStaticSites "Static Web Apps") in the Azure Portal
24. Click **Browse**
25. You should now see **azure-firewall-mon**!
26. ![azure-firewall-mon](/uploads/azure_azfirewall_mon_deployed.png "azure-firewall-mon")

_Note: In GitHub, under Actions and the Build and Deploy Job, you may see a note that about Note.js 12 actions are deprecated; you can set the node version to be higher._

Add the step to set the node version below submodules and above the Build and Deploy step:

          - uses: actions/setup-node@v1
            with:
              node-version: "18.x"

Refer to a copy of my Github Actions file here: [AzureStaticWebAppsCICD.yml](https://gist.github.com/lukemurraynz/3f300a5eb73b2693d3a9378261a023db "Azure Static Web Apps CI/CD") for a comparison of GitHub action - a setup-node step running on the latest version of 18.

#### Create Event Hub namespace and shared access policy

Even if you use the externally hosted version of [Azure Firewall Monitor](), you still need an Event Hub and namespace - which will stream the events from our Azure Firewall - to the Azure Firewall Monitor.

 1. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
 2. Click **+ Create a resource**
 3. Type in: **Event Hubs**
 4. Select and click **Create**
 5. Select your subscription and **Resource Group**;
 6. Type in the **Namespace** of the event hub _(i.e. AzureFirewallMonitor)_
 7. Select your **location** _(make sure this is the same region as your Azure Firewall)_
 8. Select your **Pricing Tier** _(in this example, I am going with Basic)_
 9. Click **Review + create**
10. Once the Namespace has been created, it's time to create our Event Hub; navigate to your newly created AzFirewallMonitor namespace.
11. Under **Entitles**, click **+ Event Hub**
12. Under the name, enter the Event Hub name _(i.e. AzMonitorCapture)_
13. Leave the defaults _(and Message retention to 1 day)_
14. Click **Review + Create**
15. Click **Create**
16. ![Create Azure Event Hub](/uploads/azure_azfirewall_mon_createeventhub.png "Create Azure Event Hub")
17. Now that the Event Hub is created - we now need to create a Shared access policy; in the Event Hub namespace, click on **Shared access policies.**
18. Click **+ Add**
19. Type in a **Policy name **_(i.e. AzMonitorListener)_
20. Select **Listen**
21. Click **Create**
22. ![Azure Event Hub - Create shared access policy](/uploads/azure_azfirewall_mon_sharedaccesspolicy.png "Azure Event Hub - Create shared access policy")

    #### Configure Azure Firewall to stream to Event Hub

    Now that we have an Event Hub configured, and a Shared access policy, set to Listen - its time to configure the Azure Firewall to direct logs to the Namespace.


1. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal")
2. Click **+ Create a resource**