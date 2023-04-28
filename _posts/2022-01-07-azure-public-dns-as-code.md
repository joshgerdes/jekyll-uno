---
date: '2022-01-07 00:00:00 +1300'
title: Azure Public DNS as Code
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png
_template: new_post
---

The Microsoft Azure ecosystem offers a lot of capabilities that empower individuals and businesses; one of those capabilities that are often overlooked is [DNS](https://en.wikipedia.org/wiki/Domain_Name_System){:target="_blank"}_(Domain Name System)_.

> _Azure DNS allows you to host your DNS domain in Azure, so you can manage your DNS records using the same credentials, billing, and support contract as your other Azure services. Zones can be either public or private, where Private DNS Zones (in Managed Preview) are only visible to VMs that are in your virtual network._
>
> _You can configure Azure DNS to resolve hostnames in your public domain. For example, if you purchased the contoso.xyz domain name from a domain name registrar, you can configure Azure DNS to host the contoso.xyz domain and resolve `www.contoso.xyz` to the IP address of your web server or web app._

In this article, we are going to focus on [Azure Public DNS](https://learn.microsoft.com/en-us/azure/dns/dns-overview?WT.mc_id=AZ-MVP-5004796){:target="_blank"}.

I had my external DNS under source control using Terraform and the Cloudflare provider a few years ago. I wanted to see if I use source control and continuous integration to do the same thing using Azure DNS and Azure Bicep.

My theory was I could make a change to a file and then commit it and have the Azure DNS records created or modified automatically, allowing changes to DNS to be gated, approved, scheduled and audited, allowing changes and rollback a lot easier – without having to give people access to be able to create DNS records with no auditability, turns out you can!

Using an Azure DevOps pipeline and repository and Azure Bicep, we will deploy an Azure Public DNS zone to a resource group automatically on a successful commit and any records.

![Azure Bicep - Pipeline High Level](/uploads/azurebicep_dns_hld.png "Azure Bicep - Pipeline High Level")

### Create Azure Public DNS as Code

#### Prerequisites

* An [Azure DevOps](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/?WT.mc_id=AZ-MVP-5004796){:target="_blank"} account and permissions to create a service endpoint
* An Azure subscription that you have at least contributor rights to
* A git repository _(I am going to use the repository in Azure DevOps, but you could use a nested repository from GitHub)_
* The latest [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-7.5.0&WT.mc_id=AZ-MVP-5004796){:target="_blank"} modules and [Azure Bicep/Azure CLI](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install?WT.mc_id=AZ-MVP-5004796){:target="_blank"} for local editing
* A domain name and rights to change the nameservers to point towards Azure DNS

In this article, I will be using an Azure subscription. I have access to an Azure DevOps _(free)_ subscription and a custom domain I joined named 'badasscloud.com'.

I will assume that you have nothing set up but feel free to skip the sections that aren't relevant.

That that we have the prerequisites sorted let's set it up...

#### Create Azure DevOps Repository

 1. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314){:target="_blank"}
 2. Select **+ New Project**
 3. Give your **project** a **name** _(i.e., I am going with: DNSAsCode)_
 4. ![Azure DevOps - Create New Project](/uploads/azuredevops-creatednsproject.png "Azure DevOps - Create New Project")
 5. Click **Create** _(your project will now be created)_
 6. Click on **Repos**
 7. Click on **Files**
 8. Find the '**Initialize Main branch with a README or gitignore**' section and click **Initialize.**
 9. ![Azure DevOps - Create New Project](/uploads/azuredevops-initializerepo.png "Azure DevOps - Create New Project")
10. You should now have an empty git repository!

    #### Create Azure DevOps Service Connection

    For Azure DevOps to connect to Microsoft Azure, we need to set up a service principal; you can create the service connection in Azure DevOps. However, it usually generates a service principal with a name that could be unrecognizable in the future in Azure, and I prefer to develop them according to naming convention and something that I can look at and instantly recognize its use-case. To do that, we will create it using Azure CLI.
     1. Open **PowerShell**
     2. **Run** the following **commands** to connect to Azure and **create** your **Service Principal** with Contributor **access** to **Azure**:

            #Connects to Microsoft Azure
            az.cmd login
            #Set SPN name
            $AppRegName = 'SPN.AzureSubscription.Contributor'
            #Creates SPN and sets SPN as Contributor to the subscription
            $spn = az.cmd ad sp create-for-rbac --name $AppRegName --role 'contributor'
            #Exports Password, Tenant & App ID for better readability - required for Azure DevOps setup
            $spn | ConvertFrom-Json | Select-Object -Property password, tenant, appId
            az.cmd account show --query id --output tsv
            az.cmd account show --query name --output tsv
     3. Make sure you **record** the **password**, **application ID** and the **subscription ID/name**; you will need this for the next step - you won't be able to view it anywhere else; if you lose it, you can rerun the sp create command to generate a new password. Now that we have the SPN, we need to add the details into Azure DevOps.
     4. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314){:target="_blank"}
     5. Navigate to the DNS As Code **project** you created earlier
     6. Click on **Project Setting**s _(bottom right-hand side of the window)_
     7. Click on **Service connections**
     8. Click on: **Create a service connection**
     9. Select **Azure Resource Manager**
    10. Click **Next**
    11. Click on: **Service Principal (Manual**) and click Next
    12. **Enter** in the following **details** that we exported earlier from the creation of the service principal:
        * Subscription ID
        * Subscription Name
        * Service Principal ID _(the appId)_
        * Service principal key _(password)_
        * Tenant ID
    13. Click **Verify** to verify that Azure DevOps can connect to Azure; you should hopefully see a Verification succeeded.
    14. Give the **Service** connection a **name** _(this is the display name that is visual in Azure DevOps)_
    15. **Add** a **description** _(i.e. created by, created on, created for)_
    16. Click on **Verify and save**
    17. You now have a new Service connection!
    18. ![Azure DevOps - Service Connection](/uploads/new_azure_serviceconnectioncreated.png "Azure DevOps - Service Connection")

_Note: The password for the service principal is valid for one year, so when they expire, you can come into the Azure DevOps service connection and update it here._

#### Add Azure Bicep to Repository

Now that Azure DevOps has the delegated rights to create resources in Microsoft Azure, we need to add the Azure Bicep for Azure DNS Zone.

I have created the below Azure Bicep file named: Deploy-PublicDNS.bicep

**Don't edit the file yet. You can add your DNS records later - after we add some variables into the Azure Pipeline.**

This file will:

* Create a new public Azure DNS zone, if it doesn't exist
* Add/Remove and modify any records

I have added CNAME, A Record and TXT Records as a base.

{% gist ce9c06f3afdb43666409acc3ccd619b6 %}

To add the Azure Bicep file into Azure DevOps, you can commit it into the git repository; see a previous post on '[Git using Github Desktop on Windows for SysAdmins](https://luke.geek.nz/windows/git-using-github-desktop-on-windows-for-sysadmins/ "Git using Github Desktop on Windows for SysAdmins "){:target="_blank"}' to help get started. However, at this stage, I will create it manually in the portal.

 1. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314){:target="_blank"}
 2. Navigate to the DNS As Code **project** you created earlier
 3. Click on **Repos**
 4. Click on **Files**
 5. Click on the **Ellipsis** on the right-hand side
 6. Click **New**
 7. Click **File**
 8. ![Azure DevOps - New File](/uploads/azuredevops-createfile.png "Azure DevOps - New File")
 9. Type in the name of your file _(including the bicep extension)_, i.e. **Deploy-PublicDNS.bicep**
10. Click **Create**
11. **Copy** the **contents** of the Azure **Bicep** file supplied above and **paste** them into the Contents of **Deploy-PublicDNS.bicep in Azure DevOps**
12. ![Azure DevOps - Azure Bicep](/uploads/azuredevops-deploypublicdnsinitialcommit.png "Azure DevOps - Azure Bicep")
13. Click **Commit**
14. Click **Commit** again
15. While we are here, let's **delete** the **README.md** file (as it will cause issues with the pipeline later on), click on the README.md file.
16. Click on the Ellipsis on the right-hand side
17. Click **Delete**
18. Click **Commit**
19. You should now only have your: Deploy-PublicDNS.bicep in the repository.

#### Create Azure DevOps Pipeline

Now that we have the initial Azure Bicep file, it's time to create our pipeline that will do the heavy lifting. I have created the base pipeline that you can download, and we will import it into Azure DevOps.

{% gist 41f615da65884024384dbf13288ff7c2 %}

This pipeline will run through the following steps:

* Spin up an Azure-hosted agent running Ubuntu _(it already has the Azure CLI and PowerShell setup)_
* Create the Azure resource group to place your DNS zone into _(if it doesn't already exist)_
* Finally, do the actual Azure Bicep deployment and create your Primary DNS zone resource, and, if necessary, modify any resources.

Copy the contents of the YAML pipeline above, and let's import it to Azure DevOps.

 1. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314){:target="_blank"}
 2. Navigate to the DNS As Code **project** you created earlier
 3. Click on **Pipelines**
 4. Click on the **Create Pipeline**
 5. Select **Azure Repos Git (YAML)**
 6. **Select** your DNSAsCode **repository**
 7. Select **Starter pipeline**
 8. **Overwrite** the contents of the starter **pipeline** with the YAML file supplied
 9. ![Azure DevOps - YAML](/uploads/azuredevops-newpipeline.png "Azure DevOps - YAML")
10. Click on the arrow next to Save and Run and select **Save**
11. Select **Commit directly to the main branch**
12. Click **Save**
13. You may get an error about the trigger. You can ignore it - we will need to set the variables and trigger now.
14. Click on **Pipelines**, select your newly created pipeline
15. Select **Edit**
16. Click **Variables**
17. Click on **New Variable**
18. We need to **add** four **variables**. To make the deployment more environment-specific, add the following variables into Azure DevOps _(these variables will be accessible by this pipeline only)._

| Variable | Note |
| --- | --- |
| location | Location where you want to deploy the Resource into – i.e. ‘Australia East’ |
| PrimaryDNSZone | The name of your domain you want the public zone to be, i.e. badasscloud.com |
| ResourceGroupName | The name of the Resource Group that the DNS Zone resource will be deployed into, i.e. DNS-PRD-RG |
| SPN | The name of the Service Connection, that we created earlier to connect Azure DevOps to Azure, i.e., SPN.AzureDNSCode |

 1. ![Azure DevOps Variables](/uploads/azuredevops-variables.png "Azure DevOps Variables")
 2. Click **Save**

    #### Test & final approval of Azure DevOps Pipeline

    Now that the Azure Pipeline has been created and variables set, it's time to test, warning **this will run an actual deployment to your Azure subscription**!

    We will deploy a once-off to grant the pipeline access to the service principal created earlier and verify that it works.
 3. [**Sign in to Azure DevOps**](https://go.microsoft.com/fwlink/?LinkId=2014676&githubsi=true&clcid=0x409&WebUserId=e3e298aac5104b0e8e949b3b5bbeb314){:target="_blank"}
 4. Navigate to the DNS As Code **project** you created earlier
 5. Click on **Pipelines**
 6. Click on your **Pipeline**
 7. Select **Run pipeline**
 8. Click **Run**
 9. **Click** on A**gent job 1**
10. You will see a message: **This pipeline needs permission to access a resource before this run can continue**
11. Click **View**
12. ![Azure DevOps - badasscloud.com DNS deployment](/uploads/azuredevops-spn-approval.png "Azure DevOps - badasscloud.com DNS deployment")
13. Click **Permit**
14. Click **Permit** again, to authorise your SPN access to your pipeline for all future runs
15. Your **pipeline** will be added to the **queue** and once an agent becomes available will start to **run**.

As seen below, there were no resources before my deployment and the Azure Pipeline agent kicked off and created the resources in the Azure portal.

_Note: You can expand the Agent Job to see the steps of the job, I hid it as it revealed subscription ID information etc during the deployment._

![Azure DevOps - badasscloud.com DNS deployment](/uploads/azure-devopsdeployment-azurebicep.gif "Azure DevOps - badasscloud.com DNS deployment")

Remember to update your nameserver records for your domain to point towards the nameserver entries in the Azure DNS zone resource, to use Azure DNS!

#### Edit the Bicep file

Now that you have successfully deployed your Azure Bicep file, you can go into the Azure Bicep and update the A, CNAME records to match your own environment - any new change to this repository will automatically trigger Continous Integration and deployment, you can override this behaviour by editing the Pipeline, clicking Edit Trigger and unselect 'Enable; continuous integration

Each variable _(var object) (cnames, arecords)_ is enclosed in brackets, this array allows you to add multiple records, for example, if I wanted to add another name record, it would look like this:

    //Variable array for your CNAME records. Add, remove and amend as needed, any new record needs to be included in {}.
    var cnamerecords = [
     {
     name: 'blog'
     value: 'luke.geek.nz'
     }
      {
     name: 'fancierblog'
     value: 'azure.com'
     }
    ]

Simply add another object under the first, as long as it is included in the brackets, then upon deployment Azure Bicep will parse the variable array and for each record, create/modify the DNS records, you only ever need to edit the content in the variable without touching the actual resource deployment.

As records are added and removed over time, you will develop a commit history and with the power of Azure DevOps, can implement scheduling changes at certain times and approval!

Hopefully, this article helps you achieve Infrastructure as Code for your Azure DNS resource, the same concept can be applied for other resources using Azure Bicep as well.
