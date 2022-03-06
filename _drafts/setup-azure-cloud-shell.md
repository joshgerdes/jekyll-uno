---
date: 2022-03-07 00:00:00 +1300
title: Setup Azure Cloud Shell
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
The Azure Cloud Shell allows connectivity to Microsoft Azure using an authenticated, browser-based shell experience that’s hosted in the cloud and accessible from virtually anywhere as long as you have access to your favourite browser! 

Azure Cloud Shell is assigned per unique user account and automatically authenticated with each session. 

Get a modern command-line experience from multiple access points, including the [Azure portal](https://portal.azure.com/), [shell.azure.com](https://shell.azure.com/), [Azure mobile app](https://azure.microsoft.com/en-us/features/azure-portal/mobile-app/), Azure docs _(e.g._ [_Azure CLI_](https://docs.microsoft.com/en-us/cli/azure/overview?view=azure-cli-latest)_,_ [_Azure PowerShell_](https://docs.microsoft.com/en-us/powershell/azure/get-started-azureps?view=azurermps-6.8.1&viewFallbackFrom=azurermps-6.1.0)_)_, and [VS Code Azure Account extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account).

Both Bash and PowerShell experiences are available.

> Microsoft routinely maintains and updates Cloud Shell, which comes equipped with commonly used CLI tools including Linux shell interpreters, PowerShell modules, Azure tools, text editors, source control, build tools, container tools, database tools, and more. Cloud Shell also includes language support for several popular programming languages such as Node.js, .NET, and Python.

Along with native tools such as Azure PowerShell, it also contains Azure Bicep and Terraform, allowing you to implement and test functionality, without needing to touch your local machine and is always up-to-date.

It is reasonably easy to set up, but in this article, I will show you the additional configuration options you have available, such as selecting your own storage account, region and resource group to conform to any naming policies and preferences you may have.