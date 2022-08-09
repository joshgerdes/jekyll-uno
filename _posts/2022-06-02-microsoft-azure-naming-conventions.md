---
date: 2022-06-02 00:00:00 +1200
title: Microsoft Azure Naming Conventions
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/azurenaming.png"

---
Accurately representing and naming your resources is essential for security purposes.

In a security incident, it is critical to identify affected systems quickly, what functions those systems support, and the potential business impact.

A useful naming convention composes resource names from important information about each resource. A well-chosen name helps you quickly identify the resource's type, its associated workload, its deployment environment, and the Azure region hosting it.

Some resource names, such as PaaS services with public endpoints or virtual machine DNS labels, have global scopes, so they must be unique across the Azure platform.

There's no one size fits all to Azure naming conventions, it needs to suit your organisation, however, it is worth noting that there are limitations to naming rules to Azure resources.

* [Naming rules and restrictions for Azure resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules?WT.mc_id=AZ-MVP-5004796 "Naming rules and restrictions for Azure resources"){:target="_blank"}
* [Define your naming convention](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming?WT.mc_id=AZ-MVP-5004796 "Define your naming convention"){:target="_blank"}
* [Deploy Azure Naming Tool into an Azure WebApp as a container](https://luke.geek.nz/azure/deploy-azure-naming-tool-into-an-azure-webapp-as-a-container/) "Deploy Azure Naming Tool into an Azure WebApp as a container"){:target="_blank"}

The use of these limitations and scopes have been used to determine the following naming conventions across associated resources.

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

### Resource Group

| Environment | Application Name | Azure Region | Azure Service | Example Name |
| --- | --- | --- | --- | --- |
| Production | application1 | Australia East | Resource Group | company-application1-rg-au-e-prod |

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
