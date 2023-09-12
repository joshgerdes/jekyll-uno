---
title: Get Ahead with Self-Hosted Agents and Container Apps Jobs
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlogHeader-GetAheadwithSelf-HostedAgentsandContainerAppsJobs.gif
date: '2023-09-12 00:00:00 +1300'
---

When considering [build agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796) to use in [Azure DevOps](https://azure.microsoft.com/products/devops?WT.mc_id=AZ-MVP-5004796) *(or [GitHub](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners))*, there are 2 main options to consider:

| Agent type              | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| [Microsoft-hosted agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796#microsoft-hosted-agents) | Agents hosted and managed by Microsoft                   |
| [Self-hosted agents](https://learn.microsoft.com/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser&WT.mc_id=AZ-MVP-5004796#install)      | Agents that you configure and manage, hosted on your VMs |

[Microsoft-hosted agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml&WT.mc_id=AZ-MVP-5004796), can be used for most things, but there are times where you may need to talk to internal company resources, or security is a concern, which is when you would consider self-hosting the agent yourself.

Here is a table that summarizes the pros and cons of self-hosted Azure DevOps agents and Microsoft-hosted agents:

| **Agent Type** | **Pros** | **Cons** |
|----------------|----------|----------|
| Self-hosted    | More control over the environment, ability to install dependent software needed for builds and deployments, machine-level caches and configuration persist from run to run, which can boost speed. | Maintenance and upgrades are not taken care of for you; you must manage the agent yourself. |
| Microsoft-hosted | Maintenance and upgrades are taken care of for you; each time you run a pipeline, you get a fresh virtual machine discarded after one use. Microsoft-hosted agents can run jobs directly on the VM or in a container. The pre-defined Azure Pipelines agent pool offers several virtual machine images, each including various tools and software. You can see the installed software for each hosted agent by choosing the Included Software link in the table. Microsoft-hosted agents run on a secure Azure platform. | You have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run. |
 
Self-hosted agents give you more control over your environment, allowing you to install dependent software needed for your builds and deployments.

As Azure DevOps pipeline jobs come and go as they complete each task required, you want to be able to scale the agents out as required and pay for only what you use, you could consider [Azure Virtual Machine Scale Set agents](https://learn.microsoft.com/azure/devops/pipelines/agents/scale-set-agents?view=azure-devops&WT.mc_id=AZ-MVP-5004796). Still, you have to have to maintain virtual machine images and storage, they can be slow to provision and start, and they could become inconsistent as manual changes can be easier to do.

Here is a table that summarizes the comparison between Container Apps Jobs for an Azure DevOps Agent and using an Azure Virtual Machine scale set:

| **Agent Type** | **Pros** | **Cons** |
|----------------|----------|----------|
| Container Apps Jobs | Can run containerized tasks that execute for a finite duration and exit, allowing you to perform tasks such as data processing, machine learning, or any scenario requiring on-demand processing. Container apps and jobs run in the same environment, allowing them to share capabilities such as networking and logging. | You have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run. |
| Azure Virtual Machine scale set | You have more control over the environment, allowing you to install dependent software needed for your builds and deployments. Machine-level caches and configuration persist from run to run, which can boost speed. | Maintenance and upgrades are not taken care of for you; you need to manage the agent yourself. |

Container Apps Jobs allow you to run containerized tasks that execute for a finite duration and exit, performing tasks such as data processing, machine learning, or any scenario where on-demand processing is required. Container apps and jobs run in the same environment, allowing them to share capabilities such as networking and logging. However, you have less control over the environment, you cannot install dependent software needed for builds and deployments, and machine-level caches and configurations do not persist from run to run.

*The choice between Container Apps and VM scale sets for Azure DevOps agents should consider your specific project requirements and constraints. Each option has its own set of advantages and trade-offs.*

For our discussion today, we will provision Azure DevOps Agents using [Azure Container Apps Jobs](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796).

![Get Ahead with Self-Hosted Agents and Container Apps Jobs](/images/posts/BlogHeader-GetAheadwithSelf-HostedAgentsandContainerAppsJobs.gif)

As we want a self-hosted agent to have access to our internal resources, we will deploy a [Consumption based Internal Container Apps Environment](https://learn.microsoft.com/en-us/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796), to host our jobs.

[Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview?WT.mc_id=AZ-MVP-5004796) is a service that allows you to run containerized applications in the cloud. It provides a platform for running and scaling containerized applications, and it can be used to deploy and manage containerized applications in a variety of environments.

There are two types of compute resources in Azure Container Apps: **apps** and **jobs**.

Apps are services that run continuously. If a container in an app fails, it's restarted automatically. Examples of apps include HTTP APIs, web apps, and background services that continuously process input.

Without [scaled job](https://github.com/microsoft/azure-container-apps/issues/24) support by Azure Container App Jobs, a job could fail during execution; this has now been resolved with Container App Jobs.

> Azure Container Apps jobs enable you to run containerized tasks that execute for a finite duration and exit. You can use jobs to perform tasks such as data processing, machine learning, or any scenario where on-demand processing is required.
> Jobs are tasks that start, run for a finite duration, and exit when finished. Each execution of a job typically performs a single unit of work. Job executions start manually, on a schedule, or in response to events. [Examples of jobs include batch processes that run on demand and scheduled tasks](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796).

Running self-hosted agents as event-driven jobs allows you to take advantage of the serverless nature of Azure Container Apps. Jobs execute automatically when a workflow is triggered and exit when the job completes.

> Container apps and jobs don't support running Docker in containers. Any steps in your workflows that use Docker commands will fail when run on a self-hosted runner or agent in a Container Apps job; other [restrictions also exist](https://learn.microsoft.com/en-us/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#jobs-restrictions).

For an Azure DevOps Agent, we want to execute tasks or remove them. This is where Container Apps Jobs and [KEDA](https://keda.sh/) come in handy.

> KEDA (Kubernetes-based Event Driven Autoscaling) is an open-source project that provides event-driven autoscaling for Kubernetes workloads. KEDA can scale any container in response to events from various sources such as Azure Service Bus, Azure Event Hubs, Azure Storage Queues, Azure Storage Blobs, RabbitMQ, Kafka, and more.

One of the supported scalers is [Azure Pipelines](https://keda.sh/docs/2.11/scalers/azure-pipelines/).

*This specification describes the azure-pipelines trigger for Azure Pipelines. It scales based on the number of pipeline runs pending in a given agent pool.*

Jobs can be triggered in three ways:

* Manual jobs are triggered on demand.
* Scheduled jobs are triggered at specific times and can run repeatedly.
* Event-driven jobs are triggered by a message arriving in a queue.

We will use both **Manual** and **Event-driven**.

The **Manual** job will be run once to create a [placeholder](https://keda.sh/blog/2021-05-27-azure-pipelines-scaler/#placeholder-agent), Azure DevOps agent in the pool.

> "You cannot queue an Azure Pipelines job on an empty agent pool because Azure Pipelines cannot validate if the pool matches the requirements for the job."

As our Container Jobs are temporary, a placeholder agent **needs to remain** in the Agent pool *(ie don't delete it)*, to keep it active. This agent will be offline and can be Disabled if required in Azure DevOps. The Azure resource however, then be deleted.

For the actual agents themselves that will run our code, they will be **event-driven**.

To provision our Azure Container App Job build agents, we will use [Azure Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview?tabs=bicep&WT.mc_id=AZ-MVP-5004796) to create our resources.

Our resources will consist of:

* [Internal Container Apps Environment](https://learn.microsoft.com/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#accessibility-levels) *(Internal environments have no public endpoints and are deployed with a virtual IP (VIP) mapped to an internal IP address)*
* [Virtual Network](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview?WT.mc_id=AZ-MVP-5004796) with 2 subnets *(One subnet for resources, such as Azure Key vault, Container Registry, the other subnet dedicated to the Container App environment)*
* [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/container-registry-intro?WT.mc_id=AZ-MVP-5004796) *(this registry will be used to build and contain our container for the DevOps agent. The container registry will have a private endpoint to the internal network)*
* [Log Analytics workspace](https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-workspace-overview?WT.mc_id=AZ-MVP-5004796) *(to hold the Logs from the Container App Environment)*
* [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/overview?WT.mc_id=AZ-MVP-5004796) *(the key vault will hold our PAT (Personal Access Token), which will be used to join our COntainer App Job agents to the agent pool. The key vault will also be on the internal network, accessed via a private endpoint)*
* [Azure Private DNS zones](https://learn.microsoft.com/azure/dns/private-dns-privatednszone?WT.mc_id=AZ-MVP-5004796) *(the DNS zones, will allow the Container App Environment, to reach the Key vault and Container Registry over the internal network)*
* [Deployment scripts](https://learn.microsoft.com/azure/azure-resource-manager/templates/deployment-script-template?WT.mc_id=AZ-MVP-5004796) *(these can be deleted afterwards, but they will run the scripts to build our container image, and placeholder agent within the confines of Bicep)*

We will also need a [User Assigned Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview?WT.mc_id=AZ-MVP-5004796), for the purposes of this article *(and the scope only being to the Resource Group)* I have a pre-created User Assigned Managed identity named: *usrmi*. This Managed identity has the following role assignments to the Resource Group to which the resources will be deployed.

| **Role**                   | **Assigned To** | **Notes**                                                                                                                          |
|------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| Contributor            | usrmi       | Contributor role on the container registry resource to push the container image and create the Container App Jobs and resources. |
| Key Vault Secrets User | usrmi       | Secret Reader to access the Key Vault secrets.                                                                                 |

![Container App Jobs - High-level architecture](/images/posts/privatecontainerappsjob_architecture.png)
