---
title: Automate your Azure Bicep deployment with ease using Deployment Stacks
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/Blog-Header-AzureDeploymentStacks.gif
date: '2023-08-25 00:00:00 +1300'
---

[Deployment Stacks](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deployment-stacks?tabs=azure-powershell&WT.mc_id=AZ-MVP-5004796)! What is it? *insert confused look*

Maybe you have been browsing the Microsoft Azure Portal and noticed a new section in the management blade called: Deployment stacks and wondered what it was, and how you can use it.

Let us take a look!

> Before we get started its worth noting that as of the time of this article, this feature is under Public Preview. Features or ways of working with Deployment Stacks may change, when it becomes generally available. If you run into issues, make sure you have a look at the current [known issues](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks?tabs=azure-powershell&WT.mc_id=AZ-MVP-5004796#known-issues).


![Automate your Azure Bicep deployment with ease using Deployment Stacks](/images/posts/Blog-Header-AzureDeploymentStacks.gif)

##### Overview

[Azure Deployment Stacks](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deployment-stacks?tabs=azure-powershell&WT.mc_id=AZ-MVP-5004796) are a type of Azure resource that allows you to manage a group of Azure resources as an atomic unit.

When you submit a Bicep file or an ARM template to a deployment stack, it defines the resources that are managed by the stack.

You can create and update deployment stacks using Azure CLI, Azure PowerShell, or the Azure portal along with Bicep files. These Bicep files are transpiled into ARM JSON templates, which are then deployed as a deployment object by the stack.

Deployment stacks offer additional capabilities beyond regular deployment resources, such as simplified provisioning and management of resources, preventing undesired modifications to managed resources, efficient environment cleanup, and the ability to utilize standard templates like Bicep, ARM templates, or Template specs.

> When planning your deployment and determining which resource groups should be part of the same stack, it's important to consider the management lifecycle of those resources, which includes creation, updating, and deletion. For instance, suppose you need to provision some test VMs for various application teams across different resource group scopes.

###### Comparisons

Before we dig into it further, it may help to give you a comparison between the different products and where Deployment Stacks, could be used, lets us take a look at a comparison, between similar products, that may come to mind, such as:

* Azure Blueprints
* Bicep _(on its own)_
* Template Specs
* Terraform

   
| Feature                 | Deployment Stacks | Azure Blueprints | Using Bicep | Template Specs | Terraform |  
|-------------------------|------------------------|------------------|-------------|----------------|-----------|  
| Management of Resources | Manages a group of Azure resources as an atomic unit. | Defines and deploys a repeatable set of Azure resources that adhere to organizational standards. | Defines and deploys Azure resources using a declarative language. | Defines and deploys reusable infrastructure code using template specs. | Defines and provisions infrastructure resources across various cloud providers using a declarative language. |  
| Resource Definition     | Bicep files or ARM JSON templates are used to define the resources managed by the stack. | Blueprint artifacts, including ARM templates, policy assignments, role assignments, and resource groups, are used to define the blueprint. | Bicep files are used to define the Azure resources. | Template specs are used to define reusable infrastructure code. | Terraform configuration files are used to define the infrastructure resources. |  
| Access Control          | Access to the deployment stack can be restricted using Azure role-based access control (Azure RBAC). | Access to blueprints is managed through Azure role-based access control (Azure RBAC). | Access to Azure resources is managed through Azure role-based access control (Azure RBAC). | Access to template specs is managed through Azure role-based access control (Azure RBAC). | Access to cloud resources is managed through provider-specific authentication mechanisms. |  
| Benefits                | *  Simplified provisioning and management of resources as a cohesive entity. *  Preventing undesired modifications to managed resources. *  Efficient environment cleanup. *  Utilizing standard templates such as Bicep, ARM templates, or Template specs for your deployment stacks. | *  Rapidly build and start up new environments with organizational compliance. *  Built-in components for speeding up development and delivery. | *  Easier management and deployment of Azure resources. *  Improved readability and understanding of resource configurations. | *  Publish libraries of reusable infrastructure code. | *  Infrastructure-as-Code approach for provisioning resources across multiple cloud providers. |  
| Deprecation              | N/A | Azure Blueprints (Preview) will be deprecated. | N/A | N/A | N/A |  
   
_It is always recommended to refer to the [official documentation](https://learn.microsoft.com/?WT.mc_id=AZ-MVP-5004796) for the most up-to-date and comprehensive information. The comparison table above, was created with the help of AI._

It is hard to do a complete comparison, as always 'it depends' on your use cases and requirements, but hopefully this makes it clear where Deployment Stacks come into play, with out-of-the-box benefits such as:

Deployment stacks provide the following benefits:

* Simplified provisioning and management of resources across different scopes as a cohesive entity.
* Preventing undesired modifications to managed resources through deny settings.
* Efficient environment cleanup by employing delete flags during deployment stack updates.
* Utilizing standard templates such as Bicep, ARM templates, or Template specs for your deployment stacks.

> The key here is that Azure Deployment Stacks, is a native way to treat your infrastructure components as an atmonic unit or stack, so you manage the lifecycle of the resources as a whole vs every resource separately.

##### Using Deployment Stacks

Deployment stacks requires [Azure PowerShell](https://learn.microsoft.com/powershell/azure/install-azure-powershell?WT.mc_id=AZ-MVP-5004796) _(version 10.1.0 or later)_ or [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5004796) _(version 2.50.0 or later)_.

For the purposes of this article, I will be using PowerShell.

###### PowerShell

Once you have the latest Azure PowerShell modules, its time to take a look at the cmdlets, that are offered to us for Deployment Stacks.
