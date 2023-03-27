---
date: 2023-03-27T00:00:00.000+13:00
title: Azure Quick Review
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/azurequickreview_excel_overview.png"

---
There are a lot of workbooks that help with Microsoft Azure cost optimization, but when having discussions and looking into SLA/[SLO](https://learn.microsoft.com/azure/cloud-adoption-framework/manage/monitor/service-level-objectives?WT.mc_id=AZ-MVP-5004796 "Cloud monitoring guide: Service Level Objectives"){:target="_blank"} and availability scenarios, there are fewer options to select from - today, we are going to look at the deployment and output of Azure Quick Review.

> Azure Quick Review (azqr) goal is to produce a high level assessment of an Azure Subscription or Resource Group providing the following information for each Azure Service:

[Azure Quick Review](https://github.com/cmendible/azqr "Azure Quick Review"){:target="_blank"}_(created by Microsoft Senior Cloud Solution Architect_[Carlos Mendible](https://www.linkedin.com/in/carlosmendible/){:target="_blank"}_),_ can supplement other tools - to give you visibility into your Azure services and answer questions such as:

* What is my expected SLA?
* Are my resources protected against zone failures?
* Am I collecting diagnostic logs for my resources?
* Is Defender for Cloud-enabled for all my resource types?

Using this tool is pretty simple _(and, as the name suggests, Quick)_, and today we will look at running it from a windows endpoint, but first, we need some prerequisites.

* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796 "How to install the Azure CLI"){:target="_blank"}
* [azqr - windows release](https://github.com/cmendible/azqr/releases "cmendible/azqr/releases"){:target="_blank"}

Install the Azure CLI and make sure you have Reader rights across the subscriptions you want to review; in this demo, we will scan all subscriptions I have access to.

The Azure Quick Review (azqr) windows binary is intended to be run from the command line, so let's run it.

 1. Open your Windows Terminal
 2. Navigate to the location of the azqr binary
 3. ![Azure Quick Review](/uploads/windowsterminal_azqr_binary.png "Azure Quick Review")
 4. Login to Azure using the Azure CLI by typing:

        az login
 5. Once you have authenticated, run the executable.
 6. ![Run azqr-windows-latest](/uploads/run_azurequickreview.gif "Run azqr-windows-latest")
 7. Once it has been completed, there will be an excel spreadsheet in the same folder as the Azure Quick Review executable, with an output that contains something similar to the below:
 8. ![Azure Quick Review - Overview](/uploads/azurequickreview_excel_overview.png "Azure Quick Review - Overview")
 9. ![Azure Quick Review - Recommedations](/uploads/azurequickreview_excel_recommdations.png "Azure Quick Review - Recommedations")
10. ![Azure Quick Review - Defender for Cloud](/uploads/azurequickreview_excel_defenderoverview.png "Azure Quick Review - Defender for Cloud")