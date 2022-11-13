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

> Azure-Firewall-mon provides an _alternative_and_opinable_ 😊 way to access and inspect Azure Firewall logs. The recommended approach for analysing Azure Firewall logs is to set up a Log Analytics Workspace to collect all the data and use Kusto (KQL) queries to check what's happening.
>
> In Azure-Firewall-mon, the idea is to provide an approach much more like Sysinternals Process Monitor or Check Point's SmartView, where there is no queries or dashboards that you need to implement first to get working. Still, all events are available as a log stream. In addition, a full-text search at the top of the page lets you quickly filter the content displayed on the screen, helping you understand what is happening right now (or close to present).

### Overview

Azure-Firewall-mon _(AFM)_ is a custom solution _(currently in a functional beta)_ created by an Italian Microsoft Cloud Solution Architect called: [Nicola Delfino](https://nicolgit.github.io/ "Nicola Delfino"), its worth mentioning that although a Microsoft CSA creates AFM, IT IS NOT A SUPPORTED MICROSOFT PRODUCT.

Monitoring Azure Firewall can be a pain - with trawling through logs - using the [Azure Firewall Workbook](https://learn.microsoft.com/en-us/azure/firewall/firewall-workbook?WT.mc_id=AZ-MVP-5004796 "Monitor logs using Azure Firewall Workbook") - helps fill in the gap - especially around the application and network rule traffic. Still, you may want something simpler and designed for real-time traffic to assist with in-the-moment troubleshooting.

Azure-Firewall-mon is an open-source, [Single Page Application](https://en.wikipedia.org/wiki/Single-page_application) written in [Angular](https://angular.io/) and hosted on an [Azure WebApp](https://az-firewall-mon.azurewebsites.net "az-firewall-mon") - so to use this, you don't need to deploy to your environment.. add in an Event Hub connection string, and away you go _(there is also a demo mode - so you can see what the experience will be like)_!

![az-firewall-mon landing page](/uploads/az-firewall-mon.png "az-firewall-mon")

We can deploy it to an Azure [Static Web App](https://azure.microsoft.com/en-us/products/app-service/static/?WT.mc_id=AZ-MVP-5004796 " Static Web Apps") for those of us who would rather host it in our environment.

> "Azure Static Web Apps is a service that automatically builds and deploys full-stack web apps to Azure from a code repository. When you create an Azure Static Web Apps resource, Azure interacts directly with GitHub or Azure DevOps to monitor a branch of your choice. Every time you push commits or accept pull requests into the watched branch, a build is automatically run and your app and API is deployed to Azure."

![Azure Static WebApps - Overview](/uploads/azure-static-web-apps-overview.png "Azure Static WebApps - Overview")

### Deployment

#### Pre-requisites

Today, we are going to deploy Azure-Firewall-mon into an Azure Static Web App - to do this, we will need the following prerequisites:

* A [GitHub](https://github.com/ "GitHub") account
* An [Azure](https://azure.microsoft.com/en-us/?WT.mc_id=AZ-MVP-5004796 "Do more with less. On Azure.") subscription _(with permissions to deploy Event Hub, deploy an Azure Static WebApp, and configure Diagnostics on the Azure Firewall)_

_Note: Also, ensure that your Event Hub is in the same region as your Azure Firewall so that you can use Diagnostics settings. Regarding the Azure Static WebApp - it doesn't matter; this is a global service  - and you will be entering the Event Hub listener._