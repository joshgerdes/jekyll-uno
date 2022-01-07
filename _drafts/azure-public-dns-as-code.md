---
date: 2022-01-07 00:00:00 +1300
title: Azure Public DNS as Code
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
The Microsoft Azure ecosystem offers a lot of capabilities that empower individuals and businesses, one of those capabilities that is often overlooked is [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) _(Domain Name System)_.

> _Azure DNS allows you to host your DNS domain in Azure, so you can manage your DNS records using the same credentials, billing, and support contract as your other Azure services. Zones can be either public or private, where Private DNS Zones (in Managed Preview) are only visible to VMs that are in your virtual network._
>
> _You can configure Azure DNS to resolve hostnames in your public domain. For example, if you purchased the contoso.xyz domain name from a domain name registrar, you can configure Azure DNS to host the contoso.xyz domain and resolve `www.contoso.xyz` to the IP address of your web server or web app._

In this article, we are going to focus on [Azure Public DNS](https://docs.microsoft.com/en-us/azure/dns/dns-overview).

A few years ago, I had my personal external DNS under source control using Terraform and the Cloudflare provider, I wanted to see if I use source control and continuous integration to do the same thing using Azure DNS and Azure Bicep.

My theory was I could make a change to a file and then commit it and have the Azure DNS records created or modified automatically, allowing changes to DNS to be gated, approved, scheduled and audited allowing changes and rollback a lot easier – without having to give people access to be able to create DNS records with no auditability, turns out you can!

Using an Azure DevOps pipeline and repository and Azure Bicep, we are going to deploy an Azure Public DNS zone to a resource group automatically on a successful commit, and any records.

![Azure Bicep - Pipeline High Level](/uploads/azurebicep_dns_hld.png "Azure Bicep - Pipeline High Level")

### Create Azure Public DNS as Code

#### Prerequisites

* An [Azure DevOps](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) account and permissions to create a service endpoint
* An Azure subscription that you have at least contributor rights to
* A git repository _(I am going to use the repository in Azure DevOps, but you could use a nested repository from GitHub)_
* The latest [Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-7.1.0) modules and [Azure Bicep/Azure CLI](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) for local editing
* A domain name and rights to change the nameservers to point towards Azure DNS

In this article, I will be using an Azure subscription I have access to an Azure DevOps _(free)_ subscription, and a custom domain I join named ‘badasscloud.com’.

I am going to assume that you have nothing set up, but feel free to skip the sections that aren’t relevant.

That that we have the prerequisites sorted, let’s set it up...

#### Create Azure DevOps Repository

 1. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314)
 2. Select **+ New Project**
 3. Give your **project** a **name** _(i.e., I am going with: DNSAsCode)_
 4. ![](/uploads/azuredevops-creatednsproject.png)
 5. Click **Create** _(your project will now be created)_
 6. Click on **Repos**
 7. Click on **Files**
 8. Find the ‘**Initialize Main branch with a README or gitignore**’ section and click **Initialize**
 9. ![](/uploads/azuredevops-initializerepo.png)
10. You should now have an empty git repository!

    #### Create Azure DevOps Service Connection

    For Azure DevOps to connect to Microsoft Azure, we need to set up a service principal,  you can create the service connection in Azure DevOps, however, it usually generates a service principal with a name that could be unrecognisable in the future, I prefer to generate them according to naming convention and something that I can look at and instantly recognised its use-case, to do that we will create it using Azure CLI.
    1. Open PowerShell
    2. Run the following to connect to Azure and create your Service Principal with Contributor access to Azure:

           #Connects to Microsoft Azure
           az.cmd login
           #Set SPN name
           $AppRegName = 'SPN.AzureSubscription.Contributor'
           #Creates SPN and sets SPN as Contributor to the subscription
           $spn = az.cmd ad sp create-for-rbac --name $AppRegName --role 'contributor'
           #Exports Password, Tenant & App ID for better readability - required for Azure DevOps setup
           $spn | ConvertFrom-Json | Select-Object -Property password, tenant, appId
    3. Make sure you record the password and application ID, you will need this for the next step - you won't be able to view anywhere else, if you lose it you can rerun the sp create command to generate a new password.