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

Azure-Firewall-mon _(AFM)_ is a custom solution _(currently in a functional beta)_ created by an Italian Microsoft Cloud Solution Architect called: [Nicola Delfino](https://nicolgit.github.io/ "Nicola Delfino"), its worth mentioning that although a Microsoft CSA creates AFM, IT IS NOT A SUPPORTED MICROSOFT PRODUCT.

Monitoring Azure Firewall, can be a pain - with trawling through logs - using the [Azure Firewall Workbook](https://learn.microsoft.com/en-us/azure/firewall/firewall-workbook?WT.mc_id=AZ-MVP-5004796 "Monitor logs using Azure Firewall Workbook") - helps fill in the gap - especially around application and network rule traffic , but you may want something more simple and designed for real-time traffic to assist with troubleshooting.

Azure-Firewall-mon is an open-source, [Single Page Application](https://en.wikipedia.org/wiki/Single-page_application) written in [Angular](https://angular.io/) and hosted on an [Azure WebApp](https://az-firewall-mon.azurewebsites.net "az-firewall-mon") - so to use this, you don't need to deploy to your environment.. add in an Event Hub connection string, and away you go _(there is also a demo mode - so you can see what the experience will be like)_!

![az-firewall-mon landing page](/uploads/az-firewall-mon.png "az-firewall-mon")

For those of us - who would rather host it in our environment, we can deploy it to an Azure Static Web App.