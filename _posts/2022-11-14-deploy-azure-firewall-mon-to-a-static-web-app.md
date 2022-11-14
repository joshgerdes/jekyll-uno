---
date: 2022-11-14 00:00:00 +1300
title: Deploy Azure-Firewall-mon to a Static Web App
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azfirewallmon.png"

---
[Azure-Firewall-mon](https://github.com/nicolgit/azure-firewall-mon "Azure-Firewall-mon") is a near real-time [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Firewall?"){:target="_blank"} log viewer.

> Azure-Firewall-mon provides an _alternative_and_opinable_ 😊 way to access and inspect Azure Firewall logs. The recommended approach for analysing Azure Firewall logs is to set up a Log Analytics Workspace to collect all the data and use Kusto _(KQL)_ queries to check what's happening.
>
> In Azure-Firewall-mon, the idea is to provide an approach much more like Sysinternals Process Monitor or Check Point's SmartView, where there is no queries or dashboards that you need to implement first to get working. Still, all events are available as a log stream. In addition, a full-text search at the top of the page lets you quickly filter the content displayed on the screen, helping you understand what is happening right now (or close to present).

### Overview

Azure-Firewall-mon _(AFM or Azure Firewall Monitor)_ is a custom solution _(currently in a functional beta)_ created by an Italian Microsoft Cloud Solution Architect called: [Nicola Delfino](https://nicolgit.github.io/ "Nicola Delfino"), its worth mentioning that although a Microsoft CSA makes AFM, **IT IS NOT A SUPPORTED MICROSOFT PRODUCT**.

Monitoring Azure Firewall can be a pain - with trawling through logs - using the [Azure Firewall Workbook](https://learn.microsoft.com/en-us/azure/firewall/firewall-workbook?WT.mc_id=AZ-MVP-5004796 "Monitor logs using Azure Firewall Workbook"){:target="_blank"} - helps fill in the gap - especially around the application and network rule traffic. Still, you may want something more straightforward and designed for real-time traffic to assist with in-the-moment troubleshooting.

**Azure-Firewall-mon is an open-source,** [**Single Page Application**](https://en.wikipedia.org/wiki/Single-page_application){:target="_blank"} **written in** [**Angular**](https://angular.io/){:target="_blank"} **and hosted on an [**Azure WebApp **](https://az-firewall-mon.azurewebsites.net "az-firewall-mon")- so to use this, you don't need to deploy to your environment.. add in an Event Hub connection string, and away you go _(there is also a demo mode - so you can see what the experience will be like)_!

![az-firewall-mon landing page](/uploads/az-firewall-mon.png "az-firewall-mon")

**We can deploy it to an Azure** [**Static Web App**](https://azure.microsoft.com/en-us/products/app-service/static/?WT.mc_id=AZ-MVP-5004796 " Static Web Apps"){:target="_blank"} **for those who would instead host it in our environment.**

> "Azure Static Web Apps is a service that automatically builds and deploys full-stack web apps to Azure from a code repository. When you create an Azure Static Web Apps resource, Azure interacts directly with GitHub or Azure DevOps to monitor a branch of your choice. Every time you push commits or accept pull requests into the watched branch, a build is automatically run and your app and API is deployed to Azure."

![Azure Static WebApps - Overview](/uploads/azure-static-web-apps-overview.png "Azure Static WebApps - Overview")

### Deployment

#### Prerequisites

Today, we are going to deploy Azure-Firewall-mon into an Azure Static Web App - to do this; we will need the following prerequisites:

* A [GitHub](https://github.com/ "GitHub"){:target="_blank"} account
* An [Azure](https://azure.microsoft.com/en-us/?WT.mc_id=AZ-MVP-5004796 "Do more with less. On Azure."){:target="_blank"} subscription_(with permissions to deploy Event Hub, deploy an Azure Static WebApp, and configure Diagnostics on the Azure Firewall)_
* Azure Firewall _(provisioned)_

_Note: Also, ensure that your Event Hub is in the same region as your Azure Firewall so that you can use Diagnostics settings. Regarding the Azure Static WebApp - it doesn't matter; this is a global service  - and you will be entering the Event Hub listener._

We will use the Azure Portal and a browser to provision the workflow _(however, I will have added Azure Bicep to the bottom of the article for reference)_.

This article - assumes you have basic knowledge of GitHub and Microsoft Azure.

For this demo, I am using a [Hub & Spoke Azure](https://learn.microsoft.com/azure/architecture/reference-architectures/hybrid-networking/hub-spoke?tabs=cli&WT.mc_id=AZ-MVP-5004796 "Hub-spoke network topology in Azure"){:target="_blank"} topology.

![Azure Firewall Monitor - High Level Architecture](/uploads/AzMonArchitecture.png "Azure Firewall Monitor - High Level Architecture")

#### Fork the GitHub repository

The first thing we need to do is clone the Azure-Firewall-mon repository; this repository holds the source control of Azure-Firewall-mon. First, however, we need a clone of it - to use in our Static Web App - this will also allow us to pull down and build the latest changes and updates of the Azure-Firewall-mon tool while having the stability of maintaining your version of the device.

1. In your favourite browser of choice, navigate to: [https://github.com/nicolgit/azure-firewall-mon](https://github.com/nicolgit/azure-firewall-mon "https://github.com/nicolgit/azure-firewall-mon"){:target="_blank"}.
2. Click **Fork** _(top right of the repository)_
3. ![GitHub - Create a new fork](/uploads/github_azfirewall_mon_createfork.png "GitHub - Create a new fork")
4. Click **Create fork**
5. You have now created a fork of the 'azure-firewall-mon' repository; when a new update of Azure-Firewall-mon comes out - you can also select 'Sync fork' - to keep your fork up-to-date and trigger a new build.

#### Create Static Web App and deploy azure-firewall-mon

Now that you have created a fork, it's time to make your Azure Static WebApp!

 1. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
 2. Click **+ Create a resource**
 3. Type in: **Static Web App**
 4. Select and click **Create**
 5. Create or **select** a **Resource Group**
 6. **Type** in the **name** of your Static Web App
 7. For the plan type, we will go with **Free**
 8. Please select your **region** _(this is the staging environment used to create your resource so the Azure Static Web App can then be replicated geographically)_.
 9. Select **Source**, as **GitHub**
10. Click **Sign in** with **GitHub** _(and sign in with an account with access to the GitHub Repository fork of azure-firewall-mon created earlier)_.
11. **Authorise** the **Azure Static Web Apps** to have access to your repositories
12. **Select** your **organisation** and the azure-firewall-mon **repository** you forked earlier.
13. Select '**main**' for the branch
14. Under Build Presents, select **Angular**
15. For App location, enter "**/firewall-mon-app/**"
16. Leave the API location empty
17. For the Output location, enter: **"dist/firewall-mon-app"**
18. ![Azure Static WebApps - Angular Build](/uploads/github_azfirewall_mon_createbuildangular.png "Azure Static WebApps - Angular Build")
19. If you navigate to your own forked GitHub repository, you should see a new folder created under .github/workflows - and a new GitHub Actions workflow file!
20. ![Create Azure Static WebApp - Angular - Azure Portal](/uploads/create_azstaticwebapp_portal_azfw-mon.gif "Create Azure Static WebApp - Angular - Azure Portal")
21. If you select **Actions** in GitHub, you should see a deployment start.
22. After roughly 5 minutes, your **Azure Static App - will have deployed azure-firewall-mon**!
23. **Navigate** to your newly created [**Azure Static App**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2FStaticSites "Static Web Apps"){:target="_blank"} in the Azure Portal
24. Click **Browse**
25. You should now see **azure-firewall-mon**!
26. ![azure-firewall-mon](/uploads/azure_azfirewall_mon_deployed.png "azure-firewall-mon")

_Note: In GitHub, under Actions and the Build and Deploy Job, you may see a message about Note.js 12 actions being deprecated; you can set the node version to be higher._

Add the step to set the node version below submodules and above the Build and Deploy step:

          - uses: actions/setup-node@v1
            with:
              node-version: "18.x"

Refer to a copy of my Github Actions file here: [AzureStaticWebAppsCICD.yml](https://gist.github.com/lukemurraynz/3f300a5eb73b2693d3a9378261a023db "Azure Static Web Apps CI/CD"){:target="_blank"} for a comparison of GitHub action - a setup-node step running on the latest version of 18.

#### Create Event Hub namespace and shared access policy

Even if you use the externally hosted version of [Azure Firewall Monitor](https://az-firewall-mon.azurewebsites.net/){:target="_blank"}, you still need an Event Hub and Namespace to stream the events from our Azure Firewall to the Azure Firewall Monitor.

 1. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
 2. Click **+ Create a resource**
 3. Type in: **Event Hubs**
 4. Select and click **Create**
 5. Select your subscription and **Resource Group**;
 6. Type in the **Namespace** of the event hub _(i.e. AzureFirewallMonitor)_
 7. Select your **location** _(make sure this is the same region as your Azure Firewall)_
 8. Select your **Pricing Tier** _(in this example, I am going with Basic)_
 9. Click **Review + create**
10. Once the Namespace has been created, it's time to make our Event Hub; navigate to your newly created AzFirewallMonitor namespace.
11. Under **Entitles**, click **+ Event Hub**
12. Under the name, enter the Event Hub name _(i.e. AzMonitorCapture)_
13. Leave the defaults _(and Message retention to 1 day)_
14. Click **Review + Create**
15. Click **Create**
16. ![Create Azure Event Hub](/uploads/azure_azfirewall_mon_createeventhub.png "Create Azure Event Hub")
17. Now that the Event Hub is created, we need to create a Shared access policy; in the Event Hub namespace, click on **Shared access policies.**
18. Click **+ Add**
19. Type in a **Policy name**_(i.e. AzMonitorListener)_
20. Select **Send**
21. Click **Create**
22. ![Azure Event Hub - Create shared access policy](/uploads/azure_azfirewall_mon_sharedaccesspolicy.png "Azure Event Hub - Create shared access policy")

    #### Configure Azure Firewall to stream to Event Hub and run Azure Firewall monitor

    Now that we have an Event Hub configured and a Shared access policy set to Listen - it's time to configure the Azure Firewall to direct logs to the Namespace.
23. Navigate to the [**Azure Portal**](https://portal.azure.com/#home "Azure Portal"){:target="_blank"}
24. Navigate to your [**Azure Firewall**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FazureFirewalls "Firewalls"){:target="_blank"}
25. Select **Diagnostic Settings**
26. Click **+ Add diagnostic setting**
27. ![Azure Firewall - Diagnostic Settings](/uploads/azure_azfirewall_create_diagsettings.png "Azure Firewall - Diagnostic Settings")
28. Type in a Diagnostic setting name _(i.e. AzureFirewallMonitor)_
29. Select **All Logs**
30. Select **Stream to an event hub**
31. Select your subscription, event hub namespace, event hub and policy created earlier.
32. ![Azure Firewall - Diagnostic setting](/uploads/azure_azfirewall_configure_diagsettings.png "Azure Firewall - Configure Diagnostic setting")
33. Click **Save**
34. Please navigate back to your **Event Hub** namespace and select your **Event Hub entity**; now, we need to create a Shared access policy to **Listen** _(for the entity, not the Namespace)_
35. Click Shared access policies, and create a new Shared access policy with **Listen.**
36. Copy the **Connection string-primary key**
37. **Navigate** to your newly created [**Azure Static App**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2FStaticSites "Static Web Apps"){:target="_blank"} in the Azure Portal
38. Click **Browse**
39. You should now see **azure-firewall-mon**, and enter in the **Connection string-primary key copied** earlier!
40. **Congratulations you have now set up Azure Firewall Monitor on an Azure Static Web App and can troubleshoot your Azure Firewall quickly in real-time!**
41. ![Run Azure Firewall Monitor](/uploads/run_azstaticwebapp_portal_azfw-mon.gif "Run Azure Firewall Monitor")

#### **References: GitHub Action**

    name: Azure Static Web Apps CI/CD
    
    on:
      push:
        branches:
          - main
      pull_request:
        types: [opened, synchronize, reopened, closed]
        branches:
          - main
    
    jobs:
      build_and_deploy_job:
        if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.action != 'closed')
        runs-on: ubuntu-latest
        name: Build and Deploy Job
        steps:
          - uses: actions/checkout@v2
            with:
              submodules: true
    
          - uses: actions/setup-node@v1
            with:
              node-version: "18.x"
          - name: Build And Deploy
            id: builddeploy
            uses: Azure/static-web-apps-deploy@v1
            with:
              azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_POLITE_CLIFF_06D4C2810 }}
              repo_token: ${{ secrets.GITHUB_TOKEN }} # Used for Github integrations (i.e. PR comments)
              action: "upload"
              ###### Repository/Build Configurations - These values can be configured to match your app requirements. ######
              # For more information regarding Static Web App workflow configurations, please visit: https://aka.ms/swaworkflowconfig
              app_location: "/firewall-mon-app/" # App source code path
              api_location: "" # Api source code path - optional
              output_location: "dist/firewall-mon-app" # Built app content directory - optional
    
              ###### End of Repository/Build Configurations ######
    
      close_pull_request_job:
        if: github.event_name == 'pull_request' && github.event.action == 'closed'
        runs-on: ubuntu-latest
        name: Close Pull Request Job
        steps:
          - name: Close Pull Request
            id: closepullrequest
            uses: Azure/static-web-apps-deploy@v1
            with:
              azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_POLITE_CLIFF_06D4C2810 }}
              action: "close"

#### **References: Azure Bicep**

Below are some Azure Bicep references:

##### Azure Static Web App

    param staticSites_AzFw_Mon_name string = 'AzFw-Mon'
    
    resource staticSites_AzFw_Mon_name_resource 'Microsoft.Web/staticSites@2022-03-01' = {
      name: staticSites_AzFw_Mon_name
      location: 'Central US'
      sku: {
        name: 'Free'
        tier: 'Free'
      }
      properties: {
        repositoryUrl: 'https://github.com/lukemurraynz/azure-firewall-mon'
        branch: 'main'
        stagingEnvironmentPolicy: 'Enabled'
        allowConfigFileUpdates: true
        provider: 'GitHub'
        enterpriseGradeCdnStatus: 'Disabled'
      }
    }

##### Event Hub

    param namespaces_AzFirewallMonitor_name string = 'AzFirewallMonitor'
    param location string = resourceGroup().location
    
    
    resource namespaces_AzFirewallMonitor_name_resource 'Microsoft.EventHub/namespaces@2022-01-01-preview' = {
      name: namespaces_AzFirewallMonitor_name
      location: 'Australia East'
      sku: {
        name: 'Basic'
        tier: 'Basic'
        capacity: 1
      }
      properties: {
        minimumTlsVersion: '1.2'
        publicNetworkAccess: 'Enabled'
        disableLocalAuth: false
        zoneRedundant: true
        isAutoInflateEnabled: false
        maximumThroughputUnits: 0
        kafkaEnabled: false
      }
    }
    
    resource namespaces_AzFirewallMonitor_name_AzMonitorListner 'Microsoft.EventHub/namespaces/authorizationrules@2022-01-01-preview' = {
      parent: namespaces_AzFirewallMonitor_name_resource
      name: 'AzMonitorListner'
      location: location
      properties: {
        rights: [
          'Listen'
          'Send'
        ]
      }
    }
    
    
    resource namespaces_AzFirewallMonitor_name_azmonitorcapture 'Microsoft.EventHub/namespaces/eventhubs@2022-01-01-preview' = {
      parent: namespaces_AzFirewallMonitor_name_resource
      name: 'azmonitorcapture'
      location: location
      properties: {
        messageRetentionInDays: 1
        partitionCount: 2
        status: 'Active'
      }
    }
    
    resource namespaces_AzFirewallMonitor_name_default 'Microsoft.EventHub/namespaces/networkRuleSets@2022-01-01-preview' = {
      parent: namespaces_AzFirewallMonitor_name_resource
      name: 'default'
      location: location
      properties: {
        publicNetworkAccess: 'Enabled'
        defaultAction: 'Allow'
        virtualNetworkRules: []
        ipRules: []
      }
    }
    
    resource namespaces_AzFirewallMonitor_name_azmonitorcapture_AzMonitor 'Microsoft.EventHub/namespaces/eventhubs/authorizationrules@2022-01-01-preview' = {
      parent: namespaces_AzFirewallMonitor_name_azmonitorcapture
      name: 'AzMonitor'
      location: location
      properties: {
        rights: [
          'Listen'
        ]
      }
      dependsOn: [
    
        namespaces_AzFirewallMonitor_name_resource
      ]
    }
    
    resource namespaces_AzFirewallMonitor_name_azmonitorcapture_Default 'Microsoft.EventHub/namespaces/eventhubs/consumergroups@2022-01-01-preview' = {
      parent: namespaces_AzFirewallMonitor_name_azmonitorcapture
      name: '$Default'
      location: location
      properties: {
      }
      dependsOn: [
    
        namespaces_AzFirewallMonitor_name_resource
      ]
    }