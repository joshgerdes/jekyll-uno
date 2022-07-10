---
date: 2022-07-10 00:00:00 +1200
title: Deploy Azure Naming Tool into an Azure WebApp as a container
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azurenamingtool_referencepage.png"

---
Organising your cloud workloads to support governance, operational management, and accounting requirements, can take a lot of effort before the first resource is first created.

Well-defined naming and metadata tagging conventions help to quickly locate and manage resources. These conventions also help associate cloud usage costs with business teams via chargeback and show-back accounting mechanisms, along with quickly identifying what services are used across services.

A useful naming convention composes resource names from important information about each resource. A well-chosen name helps you quickly identify the resource’s type, its associated workload, its deployment environment, and the Azure region hosting it. Some resource names, such as PaaS services with public endpoints or virtual machine DNS labels, have global scopes, so they must be unique across the Azure platform.

There’s no one size fits all to Azure naming conventions, it needs to suit your organisation, however, it is worth noting that there are limitations to naming rules to Azure resources.

* [Naming rules and restrictions for Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules?WT.mc_id=AZ-MVP-5004796 "Naming rules and restrictions for Azure resources")
* [Define your naming convention](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming?WT.mc_id=AZ-MVP-5004796 "Define your naming convention")

With rules around naming resources that are Global, specific to Resource Groups or that have maximum character limits that can't contain specific characters - it can become a project on its own, the world of Cloud where resources are treated as [cattle and not pets](http://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/ "The History of Pets vs Cattle and How to Use the Analogy Properly") - the effort to develop a proper naming convention, used across teams or even companies can be quiet complex.

This is where the Azure Naming Tool, as part of the Microsoft Cloud Adoption framework comes into play.

### Overview

The Naming Tool _(v2 as of June 2022)_ was developed using a naming pattern based on [Microsoft's best practices](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging). Once the organizational components have been defined by an administrator, users can use the tool to generate a name for the desired Azure resource.

![Azure \[naming-tool\]](/uploads/azurenamingtoollogo.png "Azure [naming-tool]")

This tool sitting in the [Microsoft/CloudAdoptionFramework](https://github.com/microsoft/CloudAdoptionFramework "Microsoft Cloud Adoption Framework for Azure") GitHub repository runs as a standalone Web _(.NET 6 Blazor application)_ application using stateless JSON files for its configuration and offers users the ability to generate and customize their own [Microsoft Azure Naming convention](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming?WT.mc_id=AZ-MVP-5004796 "Define your naming convention") taking all the restrictions into account. Azure Naming Tool - also offers a Swagger API that can be used in your Infrastructure as Code deployments to generate the names of resources on the fly.

![Azure Naming Tool - Reference](/uploads/azurenamingtool_referencepage.png "Azure Naming Tool - Reference")

This information is straight from the project [README.md](https://github.com/microsoft/CloudAdoptionFramework/blob/master/ready/AzNamingTool/README.md "Azure Naming Tool v2"):

> **Project Components**
>
> * UI/Admin
> * API
> * JSON configuration files
> * Dockerfile
>
> **Important Notes**
>
> The following are important notes/aspects of the Azure Naming Tool:
>
> * The application is designed to run as a stand-alone solution, with no internet/Azure connection.
> * The application can be run as a .NET 6 site, or as a Docker container.
> * The site can be hosted in any environment, including internal or in a public/private cloud.
> * The application uses local JSON files to store the configuration of the components.
> * The application requires persistent storage. If running as a container, a volume is required to store configuration files.
> * The application contains a _repository_ folder, which contains the default component configuration JSON files. When deployed, these files are copied to the _settings_ folder.
> * The Admin interface allows configurations to be "reset", if needed. This process copies the configuration from the _repository_ folder to the _settings_ folder.
> * The API requires an API Key for all executions. A default API Key (guid) will be generated on first launch. This value can be updated in the Admin section.
> * On first launch, the application will prompt for the Admin password to be set.