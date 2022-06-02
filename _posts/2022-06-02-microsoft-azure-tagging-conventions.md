---
date: 2022-06-02T00:00:00.000+12:00
title: Microsoft Azure Tagging Conventions
author: Luke
categories:
- Azure
toc: false
header: 
  teaser: "images/iazure-marketplace-banner.png"
---
Organizing cloud-based resources is a crucial task for IT unless you only have simple deployments. Use naming and tagging standards to organize your resources for these reasons:

* **Resource management**: Your IT teams will need to quickly locate resources associated with specific workloads, environments, ownership groups, or other important information. Organizing resources is critical to assigning organizational roles and access permissions for resource management.
* **Cost management and optimization**: Making business groups aware of cloud resource consumption requires IT to understand each team's resources and workloads.
* **Operations management**: Visibility for the operations management team regarding business commitments and SLAs is an essential aspect of ongoing operations.
* **Security:** Classification of data and security impact is a vital data point for the team when breaches or other security issues arise.
* **Governance and regulatory compliance:** Maintaining consistency across resources helps identify deviation from agreed-upon policies.
* **Automation:** In addition to making resources easier for IT to manage, a proper organizational scheme allows you to take advantage of automation as part of resource creation, operational monitoring, and the result of DevOps processes.

**Workload optimization:** Tagging can help identify patterns and resolve broad issues. A tag can also help determine the assets required to support a single workload. Tagging all assets associated with each workload enables a more profound analysis of your mission-critical workloads to make sound architectural decisions.

* [Use tags to organize your Azure resources and management hierarchy](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json&WT.mc_id=AZ-MVP-5004796 "Use tags to organize your Azure resources and management hierarchy"){:target="_blank"}

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

Tag at the Resource Group level and then have an Azure policy implemented that tags the resources in that Resource Group with the appropriate tags.

| Tag Name | Value | Tag Type | Description | Example |
| --- | --- | --- | --- | --- |
| Environment | Production Development Sandbox | Functional | Tags the resources with the Environment Tag. This can be used to determine if a resource is Production, Development or Sandbox. | Environment: Production |
| Creator | {CreatorName} | Partnership | Tags the resource with the name of who created the resource. This can be used to determine who created the resource to be able to get more information. | Creator: Luke Murray |
| CreatedDate | {CreatedDate} | Purpose | Tags the resource with the Date/Time when the resource was created. This can be used to determine how old a resource is, which can be used to look at new functionality on created resources or check if resources are still required. | CreatedDate: 10:00 PM 03/06/2022 NZT |
| Criticality | P1 P2 P3 | Purpose | Tags the resources with the criticality of the resources, i.e., if critical, then it is P1. This can be used to determine whether resources need to be highly available, whether changes can be made during or out of business hours. | Criticality:P1 |
| SupportedBy | {TeamName} | Partnership | Tags the resources with the team/person or company who supports the resources, whether it is internally supported by the company or outsourced. | SupportedBy:Company |
| RequesterName | {Requestor}-{CompanyName) | Partnership | Tags the resources with the user that requested the creation of the resources. | RequesterName:Project Manager |
| BillTo | {BillTo} | Accounting | Tags the resources with the cost centre or project codes who will pay for the resources. | BillTo:AppTransformationProject1 |
| AutoShutDown | Yes | Functional | This is an Automation functional tag, i.e., tag the resource (Virtual Machine) with a tagging code which will automatically Shut down and Start-up the Virtual Machine at specified times. | AutoShutDown:Yes |
| ApplicationName | {ProjectName} | Partnership | Tags the resource with the name of the project or what the resources in the resource group are for. | ApplicationName:AzureVirtualDesktopSH |
| Business Unit | {BusinessUnit} | Partnership | Tags the resource with the name of the Business Unit or Company that owns the resources. | BusinessUnit:Finance |
| Snapshot | True | Functional | This is an Automation functional tag, i.e., tag the resource (Disk) with a tagging code which can create daily snapshots of disks. | Snapshot:True |


