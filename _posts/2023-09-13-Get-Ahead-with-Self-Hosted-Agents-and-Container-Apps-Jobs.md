---
title: Get Ahead with Self-Hosted Agents and Container Apps Jobs
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlogHeader-GetAheadwithSelf-HostedAgentsandContainerAppsJobs.gif
date: '2023-09-13 00:00:00 +1300'
---

When considering [build agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796){:target="*blank"} to use in [Azure DevOps](https://azure.microsoft.com/products/devops?WT.mc_id=AZ-MVP-5004796){:target="*blank"} *(or [GitHub](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners){:target="*blank"})*, there are 2 main options to consider:

| Agent type              | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| [Microsoft-hosted agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796#microsoft-hosted-agents){:target="*blank"} | Agents hosted and managed by Microsoft                   |
| [Self-hosted agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796#install){:target="*blank"}      | Agents that you configure and manage, hosted on your VMs |

[Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml&WT.mc_id=AZ-MVP-5004796){:target="*blank"}, can be used for most things, but there are times where you may need to talk to internal company resources, or security is a concern, which is when you would consider self-hosting the agent yourself.

Here is a table that summarizes the pros and cons of self-hosted Azure DevOps agents and Microsoft-hosted agents:

| **Agent Type** | **Pros** | **Cons** |
|----------------|----------|----------|
| Self-hosted    | More control over the environment, ability to install dependent software needed for builds and deployments, machine-level caches and configuration persist from run to run, which can boost speed. | Maintenance and upgrades are not taken care of for you; you must manage the agent yourself. |
| Microsoft-hosted | Maintenance and upgrades are taken care of for you; each time you run a pipeline, you get a fresh virtual machine discarded after one use. Microsoft-hosted agents can run jobs directly on the VM or in a container. The pre-defined Azure Pipelines agent pool offers several virtual machine images, each including various tools and software. You can see the installed software for each hosted agent by choosing the Included Software link in the table. Microsoft-hosted agents run on a secure Azure platform. | You have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run. |

## Overview

Self-hosted agents give you more control over your environment, allowing you to install dependent software needed for your builds and deployments.

As Azure DevOps pipeline jobs come and go as they complete each task required, you want to be able to scale the agents out as required and pay for only what you use, you could consider [Azure Virtual Machine Scale Set agents](https://learn.microsoft.com/azure/devops/pipelines/agents/scale-set-agents?view=azure-devops&WT.mc_id=AZ-MVP-5004796){:target="*blank"}. Still, you have to have to maintain virtual machine images and storage, they can be slow to provision and start, and they could become inconsistent as manual changes can be easier to do.

Here is a table that summarizes the comparison between Container Apps Jobs for an Azure DevOps Agent and using an Azure Virtual Machine scale set:

| **Agent Type** | **Pros** | **Cons** |
|----------------|----------|----------|
| Container Apps Jobs | Can run containerized tasks that execute for a finite duration and exit, allowing you to perform tasks such as data processing, machine learning, or any scenario requiring on-demand processing. Container apps and jobs run in the same environment, allowing them to share capabilities such as networking and logging. | You have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run. |
| Azure Virtual Machine scale set | You have more control over the environment, allowing you to install dependent software needed for your builds and deployments. Machine-level caches and configuration persist from run to run, which can boost speed. | Maintenance and upgrades are not taken care of for you; you need to manage the agent yourself. |

Container Apps Jobs allows you to run containerized tasks that execute for a finite duration and exit, performing tasks such as data processing, machine learning, or any scenario requiring on-demand processing. Container apps and jobs run in the same environment, allowing them to share capabilities such as networking and logging. However, you have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run.

*The choice between Container Apps and VM scale sets for Azure DevOps agents should consider your specific project requirements and constraints. Each option has its own set of advantages and trade-offs.*

For our discussion today, we will provision Azure DevOps Agents using [Azure Container Apps Jobs](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796){:target="*blank"}.

![Get Ahead with Self-Hosted Agents and Container Apps Jobs](/images/posts/BlogHeader-GetAheadwithSelf-HostedAgentsandContainerAppsJobs.gif)

As we want a self-hosted agent to have access to our internal resources, we will deploy a [Consumption based Internal Container Apps Environment](https://learn.microsoft.com/en-us/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796){:target="*blank"}, to host our jobs.

[Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"} is a service that allows you to run containerized applications in the cloud. It provides a platform for running and scaling containerized applications, and it can be used to deploy and manage containerized applications in a variety of environments.

There are two types of compute resources in Azure Container Apps: **apps** and **jobs**.

Apps are services that run continuously. If a container in an app fails, it's restarted automatically. Examples of apps include HTTP APIs, web apps, and background services that continuously process input.

Without [scaled job](https://github.com/microsoft/azure-container-apps/issues/24) support by Azure Container App Jobs, a job could fail during execution; this has now been resolved with Container App Jobs.

> Azure Container Apps jobs enable you to run containerized tasks that execute for a finite duration and exit. You can use jobs to perform tasks such as data processing, machine learning, or any scenario where on-demand processing is required.
> Jobs are tasks that start, run for a finite duration, and exit when finished. Each execution of a job typically performs a single unit of work. Job executions start manually, on a schedule, or in response to events. [Examples of jobs include batch processes that run on demand and scheduled tasks](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796){:target="*blank"}.

Running self-hosted agents as event-driven jobs allows you to take advantage of the serverless nature of Azure Container Apps. Jobs execute automatically when a workflow is triggered and exit when the job completes.

> Container apps and jobs don't support running Docker in containers. Any steps in your workflows that use Docker commands will fail when run on a self-hosted runner or agent in a Container Apps job; other [restrictions also exist](https://learn.microsoft.com/en-us/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#jobs-restrictions).

For an Azure DevOps Agent, we want to execute tasks or remove them. This is where Container Apps Jobs and [KEDA](https://keda.sh/) come in handy.

> KEDA (Kubernetes-based Event Driven Autoscaling) is an open-source project that provides event-driven autoscaling for Kubernetes workloads. KEDA can scale any container in response to events from various sources such as Azure Service Bus, Azure Event Hubs, Azure Storage Queues, Azure Storage Blobs, RabbitMQ, Kafka, and more.

One of the supported scalers is [Azure Pipelines](https://keda.sh/docs/2.11/scalers/azure-pipelines/){:target="*blank"}.

*This specification describes the azure-pipelines trigger for Azure Pipelines. It scales based on the number of pipeline runs pending in a given agent pool.*

Jobs can be triggered in three ways:

* Manual jobs are triggered on demand.
* Scheduled jobs are triggered at specific times and can run repeatedly.
* Event-driven jobs are triggered by a message arriving in a queue.

We will use both **Manual** and **Event-driven**.

The **Manual** job will be run once to create a [placeholder](https://keda.sh/blog/2021-05-27-azure-pipelines-scaler/#placeholder-agent){:target="*blank"}, Azure DevOps agent in the pool.

> "You cannot queue an Azure Pipelines job on an empty agent pool because Azure Pipelines cannot validate if the pool matches the requirements for the job."

As our Container Jobs are temporary, a placeholder agent **needs to remain** in the Agent pool *(i.e. don't delete it)* to keep it active. This agent will be offline and can be Disabled if required in Azure DevOps. The Azure resource, however, can then be deleted.

For the actual agents themselves that will run our code, they will be **event-driven**.

To provision our Azure Container App Job build agents, we will use [Azure Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview?tabs=bicep&WT.mc_id=AZ-MVP-5004796){:target="*blank"} to create our resources.

Our resources will consist of:

* [Internal Container Apps Environment](https://learn.microsoft.com/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#accessibility-levels) *(Internal environments have no public endpoints and are deployed with a virtual IP (VIP) mapped to an internal IP address)*
* [Virtual Network](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"} with 2 subnets*(One subnet for resources, such as Azure Key vault, Container Registry, the other subnet dedicated to the Container App environment)*
* [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/container-registry-intro?WT.mc_id=AZ-MVP-5004796){:target="*blank"}* (this registry will be used to build and contain our container for the DevOps agent. The container registry will have a private endpoint to the internal network)*
* [Log Analytics workspace](https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-workspace-overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"}* (to hold the Logs from the Container App Environment)*
* [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"}* (the key vault will hold our PAT (Personal Access Token), which will be used to join our COntainer App Job agents to the agent pool. The key vault will also be on the internal network, accessed via a private endpoint)*
* [Azure Private DNS zones](https://learn.microsoft.com/azure/dns/private-dns-privatednszone?WT.mc_id=AZ-MVP-5004796){:target="*blank"}* (the DNS zones, will allow the Container App Environment, to reach the Key vault and Container Registry over the internal network)*
* [Deployment scripts](https://learn.microsoft.com/azure/azure-resource-manager/templates/deployment-script-template?WT.mc_id=AZ-MVP-5004796){:target="*blank"}* (these can be deleted afterwards, but they will run the scripts to build our container image, and placeholder agent within the confines of Bicep)*

We will also need a [User Assigned Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"} for this article*(and the scope only being to the Resource Group)*I have a pre-created User Assigned Managed identity named:*usrmi*. This Managed identity has the following role assignments to the Resource Group to which the resources will be deployed.

| **Role**                   | **Assigned To** | **Notes**                                                                                                                          |
|------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| Contributor            | usrmi       | Contributor role on the container registry resource to push the container image and create the Container App Jobs and resources. |
| Key Vault Secrets User | usrmi       | Secret Reader to access the Key Vault secrets.                                                                                 |

The cost of the overall solution 'depends' on how active it is and how it is used.

* Resources such as [Azure Container Apps](https://azure.microsoft.com/pricing/details/container-apps/?WT.mc_id=AZ-MVP-5004796), under Consumption, are pay-per-use and dependent on the number of requests and the length of those requests. The idea here is that they only cost something if in use.
* [Container Registry](https://azure.microsoft.com/en-us/pricing/details/container-registry/?WT.mc_id=AZ-MVP-5004796) requires the Premium SKU for Private Endpoint support, but for demo environments, you could get away with a Basic.
* [Key Vault](https://azure.microsoft.com/pricing/details/key-vault/?WT.mc_id=AZ-MVP-5004796){:target="*blank"} also depends on the number of transactions and functionality.

It is recommended to do an estimate using the [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/?WT.mc_id=AZ-MVP-5004796){:target="*blank"} in your currency and region to work out the costs, but the true reflection will be once your Azure DevOps pipelines start consuming the infrastructure.

## Let us get building

To deploy our environment:

![Container App Jobs - High-level architecture](/images/posts/privatecontainerappsjob_architecture.png)

We will Azure Bicep, a User Managed Identity and Resource Group.

The [Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview?tabs=bicep&WT.mc_id=AZ-MVP-5004796){:target="*blank"} file I have written is scoped to a single Resource Group, but to do this in production and work with your existing resources, it may be better to move it to [modules](https://learn.microsoft.com/azure/azure-resource-manager/bicep/modules?WT.mc_id=AZ-MVP-5004796){:target="*blank"}.

All the code required to get this to work can be found in the following GitHub repository: [lukemurraynz/containerapps-selfhosted-agent](https://github.com/lukemurraynz/containerapps-selfhosted-agent), including the [GitHub Codespace](https://luke.geek.nz/azure/Getting-Started-with-GitHub-Codespaces/), configuration I am using to deploy.

We will start with a Resource Group consisting of our Managed Identity.

![Azure Container Apps - Resource Group](/images/posts/AzureContainerApps_AzurePortal_ado-containerapp-rg.png)

### Prepare - Azure DevOps Agent Pool

Before deploying anything into Azure, we must prepare our Azure DevOps environment.

1. Login to your **[Azure DevOps](https://aex.dev.azure.com/)** organisation
2. Click on **Organization Settings**
3. Click on **Agent Pools**
4. Click **Add Pool**
5. Select **Self-hosted**
6. Give the Agent pool a **name** *(ie containerapp-adoagent - we will need the name later in our Bicep code)*
7. Enter a description and click **Create**

![Create Azure DevOps - Agent Pool](/images/posts/AzureDevOps_CreateAgentPool_CAPPS.gif)

Once the agent pool has been created, we need our token to allow the Agents to register to the Agent Pool we have just created.

*This token is a secret and will be stored in an Azure Key Vault as part of our deployment, allowing the secret to be protected from unauthorised people and allowing you to regenerate the secret when required by updating the key vault secret without having to redeploy any of the infrastructure.*

1. Login to your **[Azure DevOps](https://aex.dev.azure.com/)** organisation.
2. Click on the little User icon at the top right *(next to your initials)*
3. Click on **Personal Access Tokens**
4. Click **+ New Token**
5. Type in a **name** *(ie JoinADOPool)*
6. Specify a valid **expiration date** *(for our demo purposes, we will go with 30 days)*.
7. Click **Show all scopes**
8. Find **Agent Pools**
9. Click **Read & manage**
10. Click **Create**
11. Copy the Token for later; if you lose this token before it can be uploaded to Key Vault, you will have to generate a new Token.

![Create Azure DevOps - Agent Pool](/images/posts/AzureDevOps_CreatePATToken_CAPPS.gif)

### Deploy - Azure Container Apps Environment

Now that we have our Azure DevOps Agent Pool and PAT token - it is time to deploy our Container Apps infrastructure.

> The [deployment scripts](https://learn.microsoft.com/azure/azure-resource-manager/templates/deployment-script-template?WT.mc_id=AZ-MVP-5004796){:target="*blank"} used by this solution do not currently support Private Endpoints*(this is coming)*, so during the build process the Container Registry has Public endpoint enabled. This can be disabled after your initial build has been completed if required. If needed, you could add another deployment script to the Container Registry back to private at the end.
> If this is the first time you have deployed Container Apps or Container Registry, you may need to register the [providers](https://learn.microsoft.com/azure/azure-resource-manager/management/resource-providers-and-types?WT.mc_id=AZ-MVP-5004796){:target="*blank"}. This can be done with the following PowerShell commands, against your target subscription, else the deployment will fail:

    Register-AzResourceProvider -ProviderNamespace Microsoft.ContainerRegistry
    Register-AzResourceProvider -ProviderNamespace Microsoft.KeyVault

To proceed, I will use my GitHub Codespace to deploy the Bicep; you could either run your own Codespace if you need it or fork the code [lukemurraynz/containerapps-selfhosted](https://github.com/lukemurraynz/containerapps-selfhosted-agent) and run it locally or from the [Azure CloudShell](https://learn.microsoft.com/azure/cloud-shell/overview?WT.mc_id=AZ-MVP-5004796){:target="*blank"}. The repository will have any updated code.

The Bicep code will be deployed as follows:

{% gist f2f2242ab8580a69db76f01b537d477c %}

We will need our Azure DevOps token created earlier, the name of the Agent Pool and the Azure DevOps URL.

We can adjust the parameters to suit our environment and deploy.

*The token is classified as a secure value, so although it is visible in plain text here, it will not be parsed through in the deployment logs.*

Verify that the Resource Group and the User-Assigned managed identity exist with appropriate permissions.

1. Open the **Codespace**
2. Navigate to the **IaC** folder and select main.bicep
3. Select the **[Deployment Pane](https://luke.geek.nz/azure/Azure-Bicep-Deploy-Pane/)** *(top right)*
4. Select your **Scope** - i.e. the Resource Group you will want to deploy to; you will need to log in with your Azure credentials
5. **Update the parameters**, such as your ADO URL *(make sure it doesn't include an end '/')*, token and Agent Pool
6. Click **Validate** to validate that Bicep code syntax is correct, then click **Deploy**

The bicep code will now do the following:

* Create Azure Virtual Network
* Create Azure Key Vault and private link to the virtual network
* Create DNS zone for Key Vault
* Create a Container Registry and a private link to the virtual network
* Create DNS zone for container registry
* Places the token into a Key Vault secret
* Run a deployment script, which will build the Azure DevOps Agent Container image from the following docker file: [containerapps-selfhosted-agent/Dockerfile.azure-pipelines](https://github.com/lukemurraynz/containerapps-selfhosted-agent/blob/main/Dockerfile.azure-pipelines)
* Create the Consumption Container Apps environment
* Create a Log Analytics workspace and attach it to the Container Apps environment as a diagnostic setting
* Run a deployment script that runs the acrbuild command to deploy the placeholder Azure DevOps agent
* Creates the Azure Container Apps job, used for DevOps agents, with the azure-pipelines KEDA scaler configuration.

![Create Azure DevOps - Agent Pool](/images/posts/Create_AzureContainerApps_BicepCodeSpace.gif)

*In my testing, end-to-end deployment seemed to range between 12 to 15 minutes.*

To validate it worked, you can go into the Azure DevOps and Agent Pools, and you should now have a placeholder agent. This agent needs to stay to keep the Agent pool active but can be toggled to Disabled.

![Create Azure DevOps - Agent Pool](/images/posts/AzureDevOps_ContainerApp_AgentPlaceholder.png)

Once deployed, you can go into the Container Registry, Networking blade and change Public network access to Disabled. You can also delete the DeploymentScript resources, as these are no longer required.

![Public Access disabled - Container Registry](/images/posts/AzureContainerRegistry_PublicAccess_Disabled.png)

## Testing

To test that it is working - I have deployed a Virtual Machine into the sharedservices subnet with RDP open internally.

Let's import a test Azure pipeline to test that the event scaling is working and that the Container App job can communicate with internal resources.

{% gist 128e5d6ace94909436f94535d612f955 %}

1. Login to your **[Azure DevOps](https://aex.dev.azure.com/)** organisation.
2. Navigate to a **repository** that you can test *(create one if it doesn't exist and initialize it)*.
3. Create a new file called **azure-pipelines.yml**, and copy the pipeline into it.
4. Note: I am not talking from experience or anything, but make sure you **update the RDP IP** to make sure it's a valid destination IP in the YML.
5. You can then navigate to **Pipelines**
6. **Import Pipeline**
7. **Run**

![Run Azure DevOps - Agent Pool](/images/posts/Run_AzureContainerApps_Agent.gif)

As the Container App agent runs, the Container App Job will execute (in some cases, multiple job instances will be spawned to fulfil your pipeline needs across multiple parallel jobs and tasks), and the resources get spawned in Azure.

## Logging

The Container App Environment logs are stored in the Log Analytics workspace.

1. Login to the **Azure Portal**
2. Navigate to the **Log Analytics workspace** created *(i.e. law-jcdbxrheta7ug)*
3. Navigate to **Logs**
4. The default logs rules look for an incorrect table *(ContainerAppConsoleLogs_CL*.
5. To retrieve the Logs, click on **Category** and uncollapse **Azure Resources**

Table names are called:

* ContainerAppSystemLogs
* ContainerAppConsoleLogs

![Run Azure DevOps - Agent Pool](/images/posts/Run_AzureContainerApps_LogAnalytics.gif)

## Additional Reading

* A great tutorial exists to use Azure CLI to build the self-hosted Azure DevOps and GitHub Runners: [Tutorial: Deploy self-hosted CI/CD runners and agents with Azure Container Apps jobs](https://learn.microsoft.com/azure/container-apps/tutorial-ci-cd-runners-jobs?tabs=bash&pivots=container-apps-jobs-self-hosted-ci-cd-azure-pipelines&WT.mc_id=AZ-MVP-5004796){:target="*blank"}
* [Jobs in Azure Container Apps](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#event-driven-jobs)
* [KEDA - Kubernetes Event-driven Autoscaling](https://keda.sh/)
