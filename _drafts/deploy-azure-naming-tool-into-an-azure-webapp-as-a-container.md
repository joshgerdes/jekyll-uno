---
date: 2022-07-10T00:00:00.000+12:00
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

### Deployment

#### Prerequisites

Today, we are going to deploy the Azure Naming Tool, into an Azure WebApp, running as a Container.![Azure Naming Tool - High-Level Architecture](/uploads/azurenamingtool_architecture.png "Azure Naming Tool - High-Level Architecture")

The Azure resources we will create are:

* [Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/?WT.mc_id=AZ-MVP-5004796 " Azure Container Registry")
* [Azure Storage Account](https://azure.microsoft.com/en-us/products/category/storage/?WT.mc_id=AZ-MVP-5004796 "Storage") _(with File Share - to store our persistent data and configuration)_
* [Azure App Service Plan and App Service for Containers](https://azure.microsoft.com/en-us/services/app-service/containers/?WT.mc_id=AZ-MVP-5004796 " Web App for Containers") _(to run our Azure Naming Tool)_

To deploy these Azure resources, you need Contributor rights in at least a Resource Group.

We will be using a mix of services such as:

* [Docker](https://www.docker.com/ "Docker")
* [PowerShell](https://docs.microsoft.com/en-us/powershell/?WT.mc_id=AZ-MVP-5004796 "PowerShell") & [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/?WT.mc_id=AZ-MVP-5004796 "Azure Command-Line Interface (CLI) documentation")
* [Azure Bicep](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/?WT.mc_id=AZ-MVP-5004796 "Bicep documentation")

To reduce the need to set up these dependencies on individual workstations, we will be using a mix of the Azure Cloud Shell and Azure Portal, if you haven't set up your Azure Cloud Shell you can refer to an article I wrote previously "[here](https://luke.geek.nz/azure/setup-azure-cloud-shell/ "Setup Azure Cloud Shell ")", for this remainder of this article I am going to assume you have it set up already.

Note: I am going to connect to the Cloud Shell using the [Windows Terminal](https://docs.microsoft.com/en-us/shows/it-ops-talk/azure-cloud-shell-in-the-windows-terminal?WT.mc_id=AZ-MVP-5004796 "Azure Cloud Shell in the Windows Terminal"), so any screenshots will be of the Terminal, but it's the same behaviour if I was using the browser experience.

#### Clone the Git Repository

Not is time to clone the git repository into our Cloud Shell, so we can build the docker image definition.

1. Log in to the [Microsoft Azure Portal](https://portal.azure.com/#home "Microsoft Azure - Portal") and open up the Azure Cloud Shell _(make sure you are in PowerShell (not Bash))._
2. Run the following commands and wait for the repository to be cloned directly into the CloudShell virtual instance:

       git clone https://github.com/microsoft/CloudAdoptionFramework
       cd ./CloudAdoptionFramework/ready/AzNamingTool/

![AzNaming Tool - CloudAdoptionFramework Repo Cloning](/uploads/aznamingtool_repoclone.gif "AzNaming Tool - CloudAdoptionFramework Repo Cloning")

#### Create Resource Group & Azure Container Registry

Now that we have our Repository, it's time to create our Resource Group and Container Registry _(Public)_, we will use a few PowerShell cmdlets to create the resources, make sure you change the name of your Container Registry and Resource Group to match your environment.

1. Log in to the [Microsoft Azure Portal](https://portal.azure.com/#home "Microsoft Azure - Portal") and open up the Azure Cloud Shell _(make sure you are in PowerShell (not Bash))._
2. Run the following commands to create the Resource Group and the Azure Container Registry:

       $ResourceGroup = New-AzResourceGroup -Name 'AzNamingTool-PROD-RG' -Location 'Australia East'
       $registry = New-AzContainerRegistry -ResourceGroupName 'AzNamingTool-PROD-RG' -Name "ContainerRegistryAzNamingTool" -EnableAdminUser -Sku Basic
       Connect-AzContainerRegistry -Name $registry.Name

![AzureNaming Tool - Create Resource Group & Azure Container Registry](/uploads/AzNamingTool_ContainerRegistryImageBuild.gif "AzureNaming Tool - Create Resource Group & Azure Container Registry")

#### Build your image to the Azure Container Registry

The Azure Container Registry will be stored to host and build your image definition, as Docker support is not native to the Azure Cloud Shell, now that we have created it is time to build the image and push it to the registry. Make sure you are in the AzNamingTool folder _(CloudAdoptionFramework/ready/AzNamingTool/)_.

1. Run the following Azure CLI command:

       az acr build --image azurenamingtool:v1 --registry $registry.Name --file Dockerfile .

![AzureNaming Tool - Azure Container Registry](/uploads/AzNamingTool_ContainerRegistryImageBuild.gif "AzureNaming Tool - Azure Container Registry")

#### Deploy Azure App Service and WebApp

For the following, we will use a mix of Azure Bicep and the Azure Portal _(I ran into an Access Key error and PowerShell_ [_issue_](https://github.com/Azure/azure-powershell/issues/10645 "webapp: New-AzWebApp does not set LinuxFxVersion from ContainerImageName") _when attempting to map the share using Bicep and PowerShell - if you managed to complete the setup feel free to add a comment in the comments below)_.

Azure Bicep will be used to create the App Service and Storage account + file share, then we will use the Azure Portal to complete the setup _(Azure WebApp as a Container and mapping the persistent file share)_.

First, we need to install Azure Bicep and import the Bicep file into Cloud Shell, we could Upload the file straight from the Portal, or clone a [repo](https://github.com/lukemurraynz/Azure-Bicep "Azure-Bicep") with the file - but because I am using Azure Cloud Shell from the Terminal because Azure Cloud Shell runs on Linux - I am going to use 'nano' to create the Bicep file manually - feel free to do any of the above options to get the Azure Bicep into Cloud Shell.

##### Install Azure Bicep

1. To install Azure Bicep run:

    az bicep install

![Azure Cloud Shell - Install Azure Bicep](/uploads/install_azbicep.gif "Azure Cloud Shell - Install Azure Bicep")

##### Create Azure Bicep File

We are going to use Nano, and simply copy the Azure Bicep file and Paste it into nano, make sure you adjust the parameters to suit your environment before deploying.

1. In the Azure Cloud Shell, lets create the file by typing

    nano AzNamingTool_main.bicep

1. Paste the Azure Bicep file and do any final edits
2. Now we need to save the file, press **Ctrl+X** on your keyboard
3. Press **Y** to save the file
4. Verify the file name and press **Enter** to accept the filename.

   ![Azure Cloud Shell - Create Bicep file](/uploads/createazbicepfile.gif "Azure Cloud Shell - Create Bicep file")

##### Deploy Azure Bicep

Now it's time to create the Azure App Service Plan and Storage account _(remove the -whatif flag at the end, when you confirmed there are no errors)_.

We are going to use Nano, and