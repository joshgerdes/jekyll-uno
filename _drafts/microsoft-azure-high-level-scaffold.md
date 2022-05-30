---
date: 2022-05-31 00:00:00 +1200
title: Microsoft Azure - High Level Scaffold
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/microsoft_azure.jpg"

---
The term ‘_Scaffolding_’ for Cloud essentially refers to creating a base design to establish an architecture foundation that supports a scalable, reliable, flexible, dynamic, and redundant architecture.

Although the Azure Scaffold methodology itself has been integrated into the [Microsoft Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/?WT.mc_id=AZ-MVP-5004796 "Microsoft Cloud Adoption Framework for Azure"), I do like the use of the word scaffold for building your core foundation, we are going to take a look at some key resources to develop your scaffold.

We are going to take a look at a theoretical company, and what the beginning of its governance may look like.

## Accounts

[Azure ](https://docs.microsoft.com/en-us/azure/?product=popular&WT.mc_id=AZ-MVP-5004796 "Azure documentation")subscriptions are bound to Accounts.

These accounts will be subscription and Billing owners and need to have MFA _(Multi-factor authentication)_ enabled.

## Subscriptions

The Azure account is a globally unique entity that gets you access to Azure services and your Azure subscriptions. You can create multiple subscriptions in your Azure account to create separation e.g., for billing or management purposes. In your subscription(s) you can manage resources in resources groups. Azure subscription can have a trust relationship with an Azure Active Directory _(Azure AD)_ instance.

![Management Groups](/uploads/managementgroupsandsubscriptions.png "Management Groups")

Depending on the size of the environment, you may have one or many subscriptions, you may have a Subscription to separate resources for:

* Production
* Development
* Sandbox _(testing)_

| Environment | Azure Region | Azure Service | Example Name |
| --- | --- | --- | --- |
| Production | Australia East | Subscription | company-application1-sub-prod |

Depending on the size of the environment, it is best to start with one subscription for Production resources _(most resources can be moved across subscriptions)_ and add additional subscriptions where/as needed.

Each subscription is also managed by resource quotas, for example, if you were setting up a reasonably large Azure Virtual Desktop farm, you may have the session hosts in another subscription to prevent any issues creating Virtual Machines on another subscription.

## Resource Groups

A [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal?WT.mc_id=AZ-MVP-5004796#what-is-a-resource-group "What is a resource group") is a container that holds related resources for an Azure solution.

The resource group can include all the resources for the solution, or only those resources that you want to manage as a group. You decide how you want to allocate resources to resource groups based on what makes the most sense for your organization.

Generally, add resources that share the same lifecycle to the same resource group so you can easily deploy, update, and delete them as a group.

A Resource Group should be created for each application separately, it is also recommended to separate Production and Development resources into separate resource groups.

Resource Groups also allow you to enable Locks, to prevent anyone from deleting or modifying the resources, this is extremely useful when working with infrastructure resources, such as Networks.

| Environment | Application Name | Azure Region | Azure Service | Example Name |
| --- | --- | --- | --- | --- |
| Production | application1 | Australia East | Resource Group | company-application1-rg-au-e-prod |

## Management Groups

[Azure management groups](https://docs.microsoft.com/en-us/azure/governance/management-groups/overview?WT.mc_id=AZ-MVP-5004796 "What are Azure management groups?") provide a level of scope above subscriptions.

You organize subscriptions into containers called "management groups" and apply your governance conditions to the management groups. All subscriptions within a management group automatically inherit the conditions applied to the management group. You can build a flexible structure of management groups and subscriptions to organize your resources into a hierarchy for unified policy and access management.

It is recommended to use management groups to deploy _(but not limited to)_:

* Access rights
* Policies

![](/uploads/managementgroup.png)

## Azure Policies

Resource [policies ](https://docs.microsoft.com/en-us/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Policy?")will be used to assign resource tags to resources, control costs by limiting the types of resources that can be created and restrict resources to preferred Azure locations. The azure policy is a default allow and explicit deny system.

Azure Policies can be deployed to Subscriptions/Resource Groups and Management Groups, example policies to deploy as a base could be:

### **Built-in policies**

* **Allowed locations**

Resources should be created only in the Australian regions below. Attempts to create resources in other regions will be denied and audited.

* Australia East
* Australia Southeast
* **Allowed virtual machine SKUs**
* Production Environments - Virtual Machines should be configured to use managed disks
* Non-Production Environments - Virtual Machines should be configured to use managed disks
* Virtual Machines must be provisioned based on the least number of resources required.
* **Allowed storage account SKUs**
* Production Environments – Storage accounts created for production subscriptions should use one of the following storage account SKUs:
* Standard_GRS. Geo-redundant storage
* Standard_RAGRS. Read access geo-redundant storage
* Non-Production Environments – Storage accounts created for non-production subscriptions should use one of the following storage account SKUs:
* Standard_LRS. Locally redundant storage
* Standard_ZRS. Zone-redundant storage
* Premium_LRS. Premium locally redundant storage
* **CIS Level 1 Benchmark**
* CIS Level 1 Auditing policies will be deployed across all Clients against the Client Management Group.
* **Apply tag and default value**

Tags should be applied to all Azure resources using policies. When a resource tag is not provided, the resource creation should be denied and audited _(changed from audit and create to deny)_

Tags should be applied using policy sets that can be reused.

* **Require storage account encryption**

Encryption should be enabled for all storage accounts. Since only newly created data will be encrypted, all existing data must be encrypted by moving between storage accounts that are configured for encryption or between containers after enabling encryption on the relevant storage account.

* **New Zealand Information Security Manual**

This initiative includes policies that address a subset of New Zealand Information Security Manual controls.

## Resource Locks

[Resource Locks](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Lock your resources to protect your infrastructure") must be used to protect production resources _(such as Virtual Networks, or Domain Controllers)_ from being accidentally deleted.

* Who can create or delete locks in your organization?

To create or delete management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions. Access should be controlled using RBAC.

* **CanNotDelete** means authorized users can still read and modify a resource, but they can't delete the Resource.
* **ReadOnly** means authorized users can read a resource, but they can't delete or update the Resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the **Reader** role.

  **Exceptions**
* For example, placing a ReadOnly lock on a storage account prevents all users from listing the keys. The list keys operation is handled through a POST request because the returned keys are available for write operations. For another example, placing a ReadOnly lock on an App Service resource prevents Visual Studio Server Explorer from displaying files for the Resource because that interaction requires to write access.

## Azure Naming Conventions

Accurately representing and naming your resources is essential for security purposes.

In a security incident, it is critical to identify affected systems quickly, what functions those systems support, and the potential business impact.

A useful naming convention composes resource names from important information about each resource. A well-chosen name helps you quickly identify the resource's type, its associated workload, its deployment environment, and the Azure region hosting it.

Some resource names, such as PaaS services with public endpoints or virtual machine DNS labels, have global scopes, so they must be unique across the Azure platform.

The use of these limitations and scopes have been used to determine the following naming conventions, across associated client resources.

| Casing | Name Format |
| --- | --- |
| Lowercase | {organizationName}-{component}-{resourceTypeshortCode}-{regionShortCode}-{environmentlongcode} |

### Naming Convention Examples

| Environment | Application Name | Azure Region | Azure Service | Example Name |
| --- | --- | --- | --- | --- |
| Production | application1 | Australia East | App Service | company-application1-asvc-au-e-prod |
| Production | application1 | Australia East | App Service Environment | company-application1-ase-au-e-prod |
| Production | application1 | Australia East | App Service Plan | company-application1-asp-au-e-prod |
| Production | application1 | Australia East | Application Gateway | company-application1-agw-au-e-prod |
| Production | application1 | Australia East | Automation Account | company-application1-aum-au-e-prod |
| Production | application1 | Australia East | Availability Set | company-application1-avs-au-e-prod |
| Production | application1 | Australia East | Azure Arc enabled Kubernetes cluster | company-application1-arck-au-e-prod |
| Production | application1 | Australia East | Azure Arc enabled server | company-application1-arcs-au-e-prod |
| Production | application1 | Australia East | Azure Cosmos DB database | company-application1-cosmos-au-e-prod |
| Production | application1 | Australia East | Azure Data Factory | company-application1-adf-au-e-prod |
| Production | application1 | Australia East | Azure Search | company-application1-srch-au-e-prod |
| Production | application1 | Australia East | Azure SQL Database | company-application1-sqldb-au-e-prod |
| Production | application1 | Australia East | Azure SQL Elastic Pool | company-application1-sqlep-au-e-prod |
| Production | application1 | Australia East | Azure SQL Server | company-application1-sql-au-e-prod |
| Production | application1 | Australia East | Container registry | company-application1-cr-au-e-prod |
| Production | application1 | Australia East | Cosmos DB | company-application1-cdb-au-e-prod |
| Production | application1 | Australia East | Function App | company-application1-func-au-e-prod |
| Production | application1 | Australia East | Gateway connection | company-application1-cn-au-e-prod |
| Test | application1 | Australia East | IoT Central | company-application1-iotc-au-e-test |
| Test | application1 | Australia East | Key Vault | company-application1-kv-au-e-test |
| Test | application1 | Australia East | Load Balancer | company-application1-lb-au-e-test |
| Test | application1 | Australia East | Local Network Gateway | company-application1-lgw-au-e-test |
| Test | application1 | Australia East | Log Analytics workspace | company-application1-la-au-e-test |
| Production | application1 | Australia East | MySQL database | company-application1-mysql-au-e-prod |
| Production | application1 | Australia East | Network Interface | company-application1-nic-au-e-prod |
| Production | application1 | Australia East | Network Security Group | company-application1-nsg-au-e-prod |
| Production | application1 | Australia East | Network Security Group Rule | company-application1-nsg-au-e-prod |
| Production | application1 | Australia East | Public IP Address | company-application1-pip-au-e-prod |
| Production |  | Australia East | Recovery Services vault | company-rsv-au-e-prod |
| Production | application1 | Australia East | Recovery Services Vault - Backup policies | company-application1-rsvp-au-e-prod |
| Production | application1 | Australia East | Resource Group | company-application1-rg-au-e-prod |
| Production | application1 | Australia East | Route table | company-application1-route-au-e-prod |
| Production | application1 | Australia East | Runbooks | company-application1-run-au-e-prod |
| Production | application1 | Australia East | Service Bus - Namespace | company-application1-sbns-au-e-prod |
| Production | application1 | Australia East | SQL Data Warehouse | company-application1-sqldw-au-e-prod |
| Production | application1 | Australia East | SQL Managed Instance | company-application1-sqlmi-au-e-prod |
| Production | App1 | Australia East | Storage Account | company-pp1-stg-au-e-prod |
| Production | application1 | Australia East | Subnet | company-application1-snet-au-e-prod |
| Production | application1 | Australia East | Subscription | company-application1-sub-prod |
| Production | application1 | Australia East | Traffic Manager Profile | company-application1-tmp-au-e-prod |
| Production | application1 | Australia East | User defined route (UDR) | company-application1-udr-au-e-prod |
| Production | application1 | Australia East | Virtual machine scale set | company-application1-vmss-au-e-prod |
| Production | application1 | Australia East | Virtual Network | company-application1-vn-au-e-prod |
| Production | application1 | Australia East | Virtual Network Gateway | company-application1-vngw-au-e-prod |

![Azure Naming - Global](/uploads/azurenaming.png "Azure Naming - Global")

### Resource Type Codes

| Resource Type | Short Code | Scope | Character Limit |
| --- | --- | --- | --- |
| App Service | asvc | Global | 40 |
| App Service Environment | ase | Resource Group | 38 |
| App Service Plan | asp | Resource Group | 40 |
| Application Gateway | agw | Resource Group | 80 |
| Automation Account | aum | Resource Group | 50 |
| Availability Set | avs | Resource Group | 80 |
| Azure Arc enabled Kubernetes cluster | arck | Resource Group | 63 |
| Azure Arc enabled server | arcs | Resource Group | 15 |
| Azure Cosmos DB database | cosmos | Global | 63 |
| Azure Data Factory | adf | Global | 63 |
| Azure Search | srch | Global | 60 |
| Azure SQL Database | sqldb | Server | 128 |
| Azure SQL Elastic Pool | sqlep | Server | 128 |
| Azure SQL Server | sql | Global | 63 |
| Container registry | cr | Global | 50 |
| Cosmos DB | cdb | Global | 50 |
| Function App | func | Global | 40 |
| Gateway connection | cn | Resource Group | 80 |
| IoT Central | iotc | Global | 63 |
| Key Vault | kv | Global | 24 |
| Load Balancer | lb | Resource Group | 80 |
| Local Network Gateway | lgw | Resource Group | 80 |
| Log Analytics workspace | la | Global | 24 |
| MySQL database | mysql | Global | 63 |
| Network Interface | nic | Resource Group | 80 |
| Network Security Group | nsg | Resource Group | 80 |
| Network Security Group Rule | nsg | Resource Group | 80 |
| Public IP Address | pip | Resource Group | 80 |
| Recovery Services vault | rsv | Resource Group | 50 |
| Recovery Services Vault - Backup policies | rsvp | vault | 50 |
| Resource Group | rg | Global | 64 |
| Route table | route | Resource Group | 80 |
| Runbooks | run | Automation Account | 63 |
| Service Bus - Namespace | sbns | Global | 50 |
| SQL Data Warehouse | sqldw | Global | 63 |
| SQL Managed Instance | sqlmi | Global | 63 |
| Storage Account | stg | Global | 24 |
| Subnet | snet | Virtual Network | 80 |
| Subscription | sub | Account | 64 |
| Traffic Manager Profile | tmp | Resource Group | 63 |
| User defined route (UDR) | udr | Resource Group | 80 |
| Virtual Machine | vm | Resource Group | 15 |
| Virtual machine scale set | vmss | Resource Group | 15 |
| Virtual Network | vn | Resource Group | 63 |
| Virtual Network Gateway | vngw | Resource Group | 80 |

### Environment Names

| Environment Name | Long Code |
| --- | --- |
| Development | dev |
| Test | test |
| Staging | stg |
| Production | prod |

### Azure Regions

| Azure Region | Geo Short Code | Datacentre Short Code | Short Code |
| --- | --- | --- | --- |
| East US | us | e | us-e |
| East US 2 | us | e2 | us-e2 |
| Central US | us | c | us-c |
| North Central US | us | cn | us-cn |
| West Central US | us | cw | us-cw |
| West US | us | w | us-w |
| West US 2 | us | w2 | us-w2 |
| Australia East | au | e | au-e |
| Australia Southeast | au | se | au-se |
| Australia Central | au | c | au-c |
| New Zealand North | nz | n | nz-n |

## Tagging Conventions

Organizing cloud-based resources is a crucial task for IT unless you only have simple deployments. Use naming and tagging standards to organize your resources for these reasons:

* **Resource management**: Your IT teams will need to quickly locate resources associated with specific workloads, environments, ownership groups, or other important information. Organizing resources is critical to assigning organizational roles and access permissions for resource management.
* **Cost management and optimization**: Making business groups aware of cloud resource consumption requires IT to understand the resources and workloads each team is using.
* **Operations management**: Visibility for the operations management team regarding business commitments and SLAs is an important aspect of ongoing operations.
* **Security:** Classification of data and security impact is a vital data point for the team when breaches or other security issues arise.
* **Governance and regulatory compliance:** Maintaining consistency across resources helps identify deviation from agreed-upon policies.
* **Automation:** In addition to making resources easier for IT to manage, a proper organizational scheme allows you to take advantage of automation as part of resource creation, operational monitoring, and the creation of DevOps processes.

**Workload optimization:** Tagging can help identify patterns and resolve broad issues. Tag can also help identify the assets required to support a single workload. Tagging all assets associated with each workload enables deeper analysis of your mission-critical workloads to make sound architectural decisions.

### Tagging Types

The common tagging patterns listed below provide examples of how tagging can be used to organize cloud assets. These patterns are not meant to be exclusive and can be used in parallel, providing multiple ways of organizing assets based on your company's needs.

| Tag type | Examples | Description |
| --- | --- | --- |
| Functional | app = catalogsearch1 tier = web webserver = apache env = prod env = staging env = dev | Categorize resources in relation to their purpose within a workload, what environment they have been deployed to, or other functionality and operational details. |
| Classification | confidentiality = private SLA = 24hours | Classifies a resource by how it is used and what policies apply to it. |
| Accounting | department = finance program = business-initiative region = northamerica | Allows a resource to be associated with specific groups within an organization for billing purposes. |
| Partnership | owner = jsmith contactalias = catsearchowners stakeholders = user1; user2; user3 | Provides information about what people (outside of IT) are related or otherwise affected by the resource. |
| Purpose | businessprocess = support businessimpact = moderate revenueimpact = high | Aligns resources to business functions to better support investment decisions. |

### Tagging Baselines

Tag at the Resource Group level and then have an Azure policy implemented which tags the resources in that Resource Group with the appropriate tags.

| Tag Name | Value | Tag Type | Description | Example |
| --- | --- | --- | --- | --- |
| Environment | Production Development Sandbox | Functional | Tags the resources with the Environment Tag. This can be used to determine if a resource is Production, Development or Sandbox. | Environment: Production |
| Creator | {CreatorName} | Partnership | Tags the resource with the name of who created the resource. This can be used to determine who created the resource to be able to get more information. | Creator: Luke Murray |
| CreatedDate | {CreatedDate} | Purpose | Tags the resource with the Date/Time when the resource was created. This can be used to determine how old a resource is, which can be used to look at new functionality on created resources or check if resources are still required. | CreatedDate: 07:52 AM 02/01/2021 NZT |
| Criticality | P1 P2 P3 | Purpose | Tags the resources with the criticality of the resources, i.e., if critical, then it is P1. This can be used to determine whether resources need to be highly available, whether changes can be made during or out of business hours. | Criticality:P1 |
| SupportedBy | {TeamName} | Partnership | Tags the resources with the team/person or company who supports the resources, whether it is internally supported by the company or outsourced. | SupportedBy:Company |
| RequesterName | {Requestor}-{CompanyName) | Partnership | Tags the resources with the user that requested the creation of the resources. | RequesterName:Project Manager |
| BillTo | {BillTo} | Accounting | Tags the resources with the cost centre or project codes who will pay for the resources. | BillTo:AppTransformationProject1 |
| AutoShutDown | Yes | Functional | This is an Automation functional tag, i.e., tag the resource (Virtual Machine) with a tagging code which will automatically Shut down and Start-up the Virtual Machine at specified times. | AutoShutDown:Yes |
| ApplicationName | {ProjectName} | Partnership | Tags the resource with the name of the project or what the resources in the resource group are for. | ApplicationName:AzureVirtualDesktopSH |
| Business Unit | {BusinessUnit} | Partnership | Tags the resource with the name of the Business Unit or Company that owns the resources. | BusinessUnit:Finance |
| Snapshot | True | Functional | This is an Automation functional tag, i.e., tag the resource (Disk) with a tagging code which can create daily snapshots of disks. | Snapshot:True |

## Security

### Azure PaaS to on-premises connectivity

Azure Private Endpoint will be configured for PaaS resources which only need to be accessed on an internal network.

Azure Private Link enables you to access Azure PaaS Services (for example, Azure Storage and SQL Database) and Azure hosted customer-owned/partner services over a [private endpoint](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview?WT.mc_id=AZ-MVP-5004796 "What is a private endpoint?") in your virtual network. Traffic between your virtual network and the service travels the Microsoft backbone network. Exposing your service to the public internet is no longer necessary.

### RBAC

Role Based Access Control will be used across Azure resources and resource groups.

Each Azure Resource Group will have an Azure Active Directory group created for it with Contributor access. This allows any user a member of the group to only have access to the Resource Group resources only.

Users are to be added to groups ONLY – not directly to the resources or resource groups, so simplify management and increase visibility.

### Microsoft Defender for Cloud

Microsoft Defender for Cloud has two main goals:

* to help you understand your current security situation
* to help you efficiently and effectively improve your security

The central feature in Defender for Cloud that enables you to achieve those goals is a secure score. Defender for Cloud continually assesses your resources, subscriptions, and organization for security issues. It then aggregates all the findings into a single score so that you can tell, at a glance, your current security situation: the higher the score, the lower the identified risk level.

Defender for Cloud and Security contacts will be enabled on all subscriptions, Basic is Free.

## Cost Management

### Budgets

Implement Budget alerts. These Alerts will be configured to email the Business Owners or other Stakeholders once a Resource Group reaches a specific threshold.

It is recommended to set 3 Budget alerts, to help with awareness.

For Resource Group budgets the following naming standard has been created for Resource Groups:

| Budget Name | Alert Threshold (Percent) |
| --- | --- |
| {RESOURCEGROUPNAME}-MonthlyBudget-{Number} | 50% |
| {RESOURCEGROUPNAME}-MonthlyBudget-{Number} | 60% |
| {RESOURCEGROUPNAME}-MonthlyBudget-{Number} | 70% |

For Subscription budgets the following naming standard is created:

| Budget Name | Alert Threshold (Percent) |
| --- | --- |
| {SUBSCRIPTIONNAME}-MonthlyBudget-{Number} | 50% |
| {SUBSCRIPTIONNAME}-MonthlyBudget-{Number} | 60% |
| {SUBSCRIPTIONNAME}-MonthlyBudget-{Number} | 70% |

### Processes

Proactive Cost Management activities to be performed and defined as part of BAU/Cloud Operations on a continuous basis.

* Monitor and forecast
* Cost controls – Forecast and tune
* Azure Hybrid Benefit
* Reserve Instances
* Shutdown
* Resize
* Move to PaaS