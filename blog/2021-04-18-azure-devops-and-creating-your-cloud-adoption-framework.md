---
date: '2021-04-17 00:00:00 +1200'
title: Azure DevOps and creating your Cloud Adoption Framework
authors: [Luke]
tags:
  - Azure
toc: false
header:
  teaser: images/iazure-marketplace-banner.png
---

Do you want to make a start on Azure Adoption and Governance, Server Migration or Azure Virtual Desktop and do not know where to start, or whether you are asking the right questions?

If you want to create a framework for your cloud adoption or migration plans, you can look at... using [Azure DevOps Demo Generator](https://azuredevopsdemogenerator.azurewebsites.net/ "Azure DevOps Generator")…

Azure DevOps is not only a continuous integration and deployment tool, along with the Repos, Pipelines, Test plans and Artifacts – there is Azure Boards, with Boards you can plan and track your work items and use the Kanban board functionality to easy update or track your work in progress items and add to the backlog, although Agile squads and sprint planning organizations primarily use Azure Boards – it does not have to be. 

The Azure DevOps Board’s come with your MSDN license or free under the Basic plan for the first 5 users.

The Azure DevOps Demo Generator can create projects in your Azure DevOps organization, already prepopulated with relevant Epics, Features and Tasks that can help you on your cloud journey!

![Azure DevOps Demo Generator](/uploads/AzureDevOpsGeneratorPage.png "Azure DevOps Demo Generator")

There are many prepopulated projects in the Demo Generator, from Security to Learning; you can even import prepopulated templates from other people.

The ones we are going to concentrate on is the: Cloud Adoption Framework projects.

![Azure DevOps Generator - Choose a template](/uploads/AzureDevOpsCloudAdoptionTemplates.png "Azure DevOps Generator - Choose a template")

The following projects are available under the Cloud Adoption Framework heading to help you on your journey *(as of the date this article was published)*:

| Project | Description |
| --- | --- |
| Cloud Adoption Plan | The Cloud Adoption Plan template creates a backlog for managing cloud adoption efforts based on the guidance in the Microsoft Cloud Adoption Framework. |
| CAF Strategy-Plan-Ready-Gov | In this checklist we share all the decision points needed to successfully build a Cloud Adoption Plan as well as the Landing Zone with Governance |
| ServerMigration_CAF_DevOps_ProjectTaskList | Server migration has many different activities. In the Azure DevOps Project we will provide the steps necessary to go from zero to a complete Server migration and management. |
| AKS_CAF_DevOps_Project_TaskList | AKS deployment has many different activities. In the Azure DevOps Project we will provide the steps necessary to go from zero to a complete AKS deployment and management. |
| SQL Migration | SQL migration has many different activities. In the Azure DevOps Project we will provide the steps necessary to go from zero to a complete SQL migration and management. |
| Windows Virtual Desktop | Project work plan templates in Azure DevOps that provide the steps necessary to go from zero to a complete WVD deployment with ongoing management |
| Knowledge Mining | Knowledge project simplifies the process of accessing the latent insights contained within structured and unstructured data. Use this project to help you address all the steps. |
| Azure Governance Readiness | The standalone Azure governance project provides guidance and tools on how to ensure that your Azure environment is governed in the correct way. |
| Modern Data Warehouse | Build your modern data warehouse using this ADO checklist of items, in this checklist we have links to assets, code and learning material. |
| Retail Recommender with Azure Synapse | This Solution Accelerator is an end-to-end example on how to enable personalized customer experiences for retail scenarios by leveraging Azure Synapse Analytics, Azure Machine Learning Services, and other Azure Big Data services. |
| Modern IOT | Connected sensors, devices, and intelligent operations can transform businesses and enable new growth opportunities. In this project you will get the work items needed to plan and implement your IOT solution using the Azure IoT Platform. |

Once the project has been created, you can go into Azure Board and click on: Work Items.

If we take a look at the CAF Strategy-Plan-Ready-Gov Team one, we can see the Epics, Features and Tasks associated with Cloud Adoption:

![Azure DevOps - Cloud Adoption Strategy](/uploads/AzureDevOps_CloudAdoptionWorkItems.png "Azure DevOps - Cloud Adoption Strategy")

If we click Boards, we can see the Kanban board, the state of the Epics, features etc. and where they are.

![Azure DevOps - Kanban](/uploads/AzureDevOps_CloudAdoptionKanban.png "Azure DevOps - Kanban")

Depending on the Tasks, it may have a description of the task with links to the relevant documentation, such as this SQL Deployment and Migration testing:

![Azure DevOps - Kanban](/uploads/AzureDevOps_Task.png)

As you can see, the Azure DevOps Generator offers not only a place to track your progress but relevant data to help you put a framework around your cloud journey, and these projects work well with the Microsoft Cloud Adoption and Azure Well Architected Framework!

These are guidelines, and they do not need to be followed to the letter; however, in my opinion, they offer an excellent base to build your cloud adoption and implementations upon.

I have extracted the following work items from the projects as CSV, in case you prefer to start with excel or want to take a look at the epics, features and tasks that come with these projects:

* [CAF Strategy-Plan-Ready-Gov Team - Epics](https://luke.geek.nz/uploads/files/AzureDevOpsDemoGenerator/CAF Strategy-Plan-Ready-Gov Team - Epics.csv "CAF Strategy-Plan-Ready-Gov Team - Epics")
* [Windows Virtual Desktop Guidance](https://luke.geek.nz/uploads/files/AzureDevOpsDemoGenerator/WVD_Guidance.csv "Windows Virtual Desktop Guidance")
* [Cloud Adoption](https://luke.geek.nz/uploads/files/AzureDevOpsDemoGenerator/CloudAdoption.csv "Cloud Adoption")
* [SQL Migration](https://luke.geek.nz/uploads/files/AzureDevOpsDemoGenerator/SQLMigration.csv "SQL Migration")
