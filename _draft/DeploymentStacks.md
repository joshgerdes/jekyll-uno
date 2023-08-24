---
title: Azure Bicep - Deployment Stacks
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/Header-AzureBicepDeployPane.gif
date: '2023-08-25 00:00:00 +1300'
---

[Deployment Stacks](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deployment-stacks?tabs=azure-powershell&WT.mc_id=AZ-MVP-5004796)! What is it?

Maybe you have been browsing the Microsoft Azure Portal and noticed a new section in the management blade called: Deployment stacks and wondered what it was, and how you can use it.

Let us take a look!

> Before we get started its worth noting that as of the time of this article, this feature is under Public Preview. Features or ways of working with Deployment Stacks may change, when it becomes generally available.

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
   
_It is always recommended to refer to the official documentation for the most up-to-date and comprehensive information._

It is hard to do a complete comparison, as always 'it depends' on your use cases and requirements, but hopefully this makes it clear where Deployment Stacks come into play, with out-of-the-box benefits such as:

* **Simplified Management**: Azure Deployment Stacks allow you to manage a group of Azure resources as an **atomic unit**. This simplifies the provisioning and management of resources, making it easier to deploy and maintain complex infrastructure configurations.
* Standardization and Compliance: With Azure Deployment Stacks, you can define and deploy a repeatable set of Azure resources that adhere to organizational standards. This ensures consistency across deployments and helps maintain compliance with regulatory requirements.
* Granular Access Control: Access to the deployment stack can be restricted using Azure role-based access control (Azure RBAC). This allows you to control who can manage and modify the stack, ensuring secure and controlled access to your infrastructure.
* Efficient Resource Cleanup: Azure Deployment Stacks provide an efficient way to clean up resources. By deleting the stack, you can easily remove all the associated resources in a single operation, preventing undesired modifications and ensuring a clean environment.
* Integration with Azure Services: Azure Deployment Stacks seamlessly integrate with other Azure services, such as Azure CLI, Azure PowerShell, and Azure portal. This allows you to manage and modify resources both within the stack and outside of the stack using familiar tools and interfaces.

_Note: The Benefits paragraph above, was created with the use of AI (Azure OpenAI and GPT 3.5)._

The key here is that Azure Deployment Stacks, treats your infrastructure components as an atmonic unit or stack, so you manage the lifecycle of the resources as a whole vs every resource separately.