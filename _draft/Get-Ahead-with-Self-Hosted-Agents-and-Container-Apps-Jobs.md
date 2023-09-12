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

| **Criteria** | **Self-Hosted Agent**                                        | **Microsoft-Hosted Agent**                                      |
|--------------|--------------------------------------------------------------|-----------------------------------------------------------------|
| **Pros**     | Customization: Tailored environment.                         | Easy Setup: Pre-configured and no setup required.               |
|              | Resource Control: Full control over resources.               | Scalability: Suitable for most workloads.                       |
|              | Security: Can be deployed within a controlled network.       | Maintenance-Free: No need for updates or patching.              |
|              | Offline Usage: Useful for environments with strict policies. | Cost-Efficiency: Pay for resources used.                        |
|              | Cost Control: Potential cost optimization.                   |                                                                 |
| **Cons**     | Maintenance: Requires ongoing management.                    | Limited Customization: Predefined configurations.               |
|              | Initial Setup: Time-consuming setup.                         | Resource Contention: Possible slowdowns during peak times.      |
|              | Resource Costs: Costs can add up if not managed.             | Internet Dependency: Requires internet access for dependencies. |
|              |                                                              | Less Control: Limited control over underlying infrastructure.   |

As Azure DevOps pipeline jobs, come and go as they complete each task required, you want to be able to scale the agents out as required and pay for only what you use, you could consider [Azure Virtual Machine Scale Set agents](https://learn.microsoft.com/azure/devops/pipelines/agents/scale-set-agents?view=azure-devops&WT.mc_id=AZ-MVP-5004796), but you have to have to maintain virtual machine images and storage, they can be slow to provision and start and they could become inconsistant as manual changes can be easier to do.

| **Criteria**                      | **Container Apps for Azure DevOps Agents**                                            | **Virtual Machine Scalesets for Azure DevOps Agents**                              |
|-----------------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Scalability**                   | Dynamic Scaling: Quick scaling based on demands.                                  | Scalability: Suitable for large workloads and predictable scaling.             |
| **Resource Efficiency**           | Resource Isolation: Efficient resource utilization.                                | Resource Overhead: Each VM has its OS, which can lead to resource inefficiency.  |
| **Speed of Provisioning**         | Fast Startup: Containers start quickly.                                            | VM Boot Time: VMs may take longer to start.                                     |
| **Portability**                   | Consistent Environment: Easier environment management.                             | VM Image Management: VMs may require more image management.                      |
| **Isolation**                     | Isolation Benefits: Containers provide isolation between agents.                    | VM Isolation: VMs offer isolation but are heavier.                              |
| **Cost Optimization**             | Cost Control: Granular pricing, cost-effective for short tasks.                     | Predictable Pricing: VMs have predictable but potentially higher costs.         |
| **Managed Services**              | Azure Integration: AKS and ACI simplify container management.                       | Azure VM Management: VM scalesets are also managed but require more setup.      |
| **Easier Maintenance**            | Updates and Patching: Easier container updates and patching.                         | OS Updates: Managing OS updates can be more complex.                             |

*The choice between Container Apps and VM scalesets for Azure DevOps agents should consider your specific project requirements and constraints. Each option has its own set of advantages and trade-offs.*

For our discussion today, we will provision Azure DevOps Agents using [Azure Container Apps Jobs](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796).

![Get Ahead with Self-Hosted Agents and Container Apps Jobs](/images/posts/BlogHeader-GetAheadwithSelf-HostedAgentsandContainerAppsJobs.gif)

As we want a self-hosted agent to have access to our internal resources, we will deploy a [Consumption based Internal Container Apps Environment](https://learn.microsoft.com/en-us/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796), to host our jobs.

[Azure Container Apps](https://learn.microsoft.com/azure/container-apps/overview?WT.mc_id=AZ-MVP-5004796) is a service that allows you to run containerized applications in the cloud. It provides a platform for running and scaling containerized applications, and it can be used to deploy and manage containerized applications in a variety of environments

There are two types of compute resources in Azure Container Apps: **apps** and **jobs**.

Apps are services that run continuously. If a container in an app fails, it's restarted automatically. Examples of apps include HTTP APIs, web apps, and background services that continuously process input.

Without, [scaled job](https://github.com/microsoft/azure-container-apps/issues/24) support by Azure Container App Jobs, a job could fail, during execution, this has now resolved with Container App Jobs.

> Azure Container Apps jobs enable you to run containerized tasks that execute for a finite duration and exit. You can use jobs to perform tasks such as data processing, machine learning, or any scenario where on-demand processing is required.
> Jobs are tasks that start, run for a finite duration, and exit when finished. Each execution of a job typically performs a single unit of work. Job executions start manually, on a schedule, or in response to events. [Examples of jobs include batch processes that run on demand and scheduled tasks](https://learn.microsoft.com/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796).

Running self-hosted agents as event-driven jobs allows you to take advantage of the serverless nature of Azure Container Apps. Jobs execute automatically when a workflow is triggered and exit when the job completes.

> Container apps and jobs don't support running Docker in containers. Any steps in your workflows that use Docker commands will fail when run on a self-hosted runner or agent in a Container Apps job, other [restrictions also exist](https://learn.microsoft.com/en-us/azure/container-apps/jobs?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#jobs-restrictions).

For the purposes of an Azure DevOps Agent, we want to execute tasks or tasks, then remove, this is where Container Apps Jobs and [KEDA](https://keda.sh/) comes in handy.

> KEDA (Kubernetes-based Event Driven Autoscaling) is an open-source project that provides event-driven autoscaling for Kubernetes workloads. KEDA can be used to scale any container in response to events from various event sources such as Azure Service Bus, Azure Event Hubs, Azure Storage Queues, Azure Storage Blobs, RabbitMQ, Kafka, and more.

One of the supported scalers is: [Azure Pipelines](https://keda.sh/docs/2.11/scalers/azure-pipelines/).

*This specification describes the azure-pipelines trigger for Azure Pipelines. It scales based on the amount of pipeline runs pending in a given agent pool.*

Jobs can be triggered in three ways:

* Manual jobs are triggered on-demand.
* Scheduled jobs are triggered at specific times and can run repeatedly.
* Event-driven jobs are triggered by events such as a message arriving in a queue.

For purposes, we will use both **Manual** and **Event-driven**.

The **Manual** job will be ran once, to create a [placeholder](https://keda.sh/blog/2021-05-27-azure-pipelines-scaler/#placeholder-agent), Azure DevOps agent in the pool.

> "You cannot queue an Azure Pipelines job on an empty agent pool because Azure Pipelines cannot validate if the pool matches the requirements for the job."

As our Container Jobs are ephemeral, a placeholder agent **needs to remain** in the Agent pool *(ie don't delete it)*, to keep it active. This agent will be offline and can be Disabled if required in Azure DevOps. The Azure resource however, then be deleted.

For the actual agents themselves, that will run our code they will be **event-driven**.

To provision our Azure Container App Job build agents, we will use [Azure Bicep](https://learn.microsoft.com/azure/azure-resource-manager/bicep/overview?tabs=bicep&WT.mc_id=AZ-MVP-5004796) to create our resources.

Our resources will consist of:

* [Internal Container Apps Environment](https://learn.microsoft.com/azure/container-apps/networking?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796#accessibility-levels) *(Internal environments have no public endpoints and are deployed with a virtual IP (VIP) mapped to an internal IP address)*
* [Virtual Network](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview?WT.mc_id=AZ-MVP-5004796) with 2 subnets *(One subnet for resources, such as Azure Keyvault, Container Registry, the other subnet dedicated to the Container App environment)*
* [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/container-registry-intro?WT.mc_id=AZ-MVP-5004796) *(this registry will be used to build and contain our container for the DevOps agent. The container registry will have a private endpoint to the internal network)*
* [Log Analytics workspace](https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-workspace-overview?WT.mc_id=AZ-MVP-5004796) *(to hold the Logs from the Container App Environment)*
* [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/overview?WT.mc_id=AZ-MVP-5004796) *(the keyvault will hold our PAT (Personal Access Token), which will be used to join our COntainer App Job agents to the agent pool. The keyvault will also be on the internal network, accessed via a private endpoint)*
* [Azure Private DNS zones](https://learn.microsoft.com/azure/dns/private-dns-privatednszone?WT.mc_id=AZ-MVP-5004796) *(the DNS zones, will allow the Container App Environment, to reach the Keyvault and Container Registry over the internal network)*
* [Deployment scripts](https://learn.microsoft.com/azure/azure-resource-manager/templates/deployment-script-template?WT.mc_id=AZ-MVP-5004796) *(these can be deleted afterwards, but they will run the scripts to build our container image, and placeholder agent within the confines of Bicep)*

We will also need a [User Assigned Managed Identity](https://learn.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview?WT.mc_id=AZ-MVP-5004796), for the purposes of this article *(and the scope only being to the Resource Group)* I have a precreated User Assigned Managed identity named: *usrmi*. This Managed identity has the following role assignments to the Resource Group that the resources will be deployed into.

| **Role**                   | **Assigned To** | **Notes**                                                                                                                          |
|------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| Contributor            | usrmi       | Contributor role on the container registry resource to push the container image, create the Container App Jobs, and resources. |
| Key Vault Secrets User | usrmi       | Secret Reader to access the Key Vault secrets.                                                                                 |

![Container App Jobs - High-level architecture](images/posts/privatecontainerappsjob_architecture.png)
