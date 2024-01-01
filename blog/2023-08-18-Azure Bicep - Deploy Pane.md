---
title: Azure Bicep - Deploy Pane
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: /images/posts/Header-AzureBicepDeployPane.gif
date: '2023-08-18 00:00:00 +1300'
slug: azure/Azure-Bicep-Deploy-Pane
---

Working with [Azure Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep&WT.mc_id=AZ-MVP-5004796) using Visual Studio Code, is as native as an experience as you can get, made even better by the [Bicep Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep).

The Bicep Visual Studio Code extension keeps evolving, with a recent (Experimental) feature being added called the **Deploy Pane**.

> The Deployment Pane is a UI panel in VSCode that allows you to connect to your Azure subscription and execute validate, deploy & whatif operations and get instant feedback without leaving the editor.

![Azure Bicep - Deploy Pane](/images/posts/VisualStudioCode_DeployPane.png)

The Deploy Pane, brings together some key actions:

* Deploy
* Validate
* What-If

The Deploy step, will deploy the Bicep file using the Subscription Scope and ID specified in the pane.
The validate step, will validate that the Bicep syntax is correct for the Azure Resource Manager to process the template.
The What-If step, will let you know what it will deploy and what changes will be made, without having to deploy or touch any resources.

To enable the new Experimental Feature, make sure you are running the latest version of both Bicep, and the Bicep Visual Studio Code extension.

1. Click on **Settings**
2. Expand **Extensions**
3. Navigate to: **Bicep**
4. Check the box labelled: **Experimental: Deploy Pane**

![Azure Bicep - Deploy Pane](/images/posts/Bicep-DeploymentPreviewPane.gif)

Once enabled, you will see the new Deploy Pane, appear in the top right of your Visual Studio code interface, next to Bicep Visualizer, once you have a Bicep file loaded.

![Azure Bicep - Deploy Pane](/images/posts/VisualStudioCode_DeployPaneIcon.png)

If you have any feedback regarding this extension, make sure to add your feedback to the [azure/bicep issues](https://github.com/Azure/bicep/issues)
