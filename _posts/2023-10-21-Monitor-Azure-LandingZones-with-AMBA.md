---
title: Monitor your Azure Landing Zone with Baseline Alerts
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlogHeading_AMBA.gif
date: 2023-10-21 00:00:00 +1300
keywords:
  - azure
  - monitor
  - landing zones
description: Monitor your Azure Landing Zone with Azure Monitor Baseline Alerts (AMBA).
---

> When deploying Azure resources, it is crucial to configure alerts to ensure your resources' health, performance, and security.

By setting up alerts, you can proactively monitor your resources and take timely actions to address any issues that may arise.
Here are the key reasons why configuring alerts is essential:

* Early detection of issues: Alerts enable you to identify potential problems or anomalies in your Azure resources at an early stage. By monitoring key metrics and logs, you can detect high CPU usage, low memory, network connectivity problems, or security breaches. This allows you to take immediate action and prevent any negative impact on your applications or services.
* Reduced downtime: By configuring alerts, you can minimise downtime by being notified of critical events or failures in real time. This allows you to quickly investigate and resolve issues before they escalate, ensuring the availability and reliability of your applications.
* Optimized resource utilisation: Alerts help you optimise resource utilization by providing insights into resource usage patterns and trends. By monitoring metrics such as CPU utilisation, memory consumption, or storage capacity, you can identify opportunities for optimisation and cost savings.
* Compliance and security: Configuring alerts is essential for maintaining compliance with regulatory requirements and ensuring the security of your Azure resources. By monitoring security logs and detecting suspicious activities or unauthorised access attempts, you can immediately mitigate potential risks and protect your data.
* Proactive capacity planning: Alerts provide valuable information for capacity planning and scaling your resources. By monitoring resource utilisation trends over time, you can identify patterns and forecast future resource requirements. This helps you avoid performance bottlenecks and ensure a smooth user experience."

## Overview

[Azure Monitor Baseline Alerts (AMBA)](https://azure.github.io/azure-monitor-baseline-alerts/welcome/) exists to help you get started with proactive and reactive monitoring straight out of the bat, focused on standard scenarios for your platform and application Landing Zone that are not industry or application-specific.

Previously under the azure/alz-monitor repository, it is now generally available under the [Azure/azure-monitor-baseline-alerts](https://github.com/Azure/azure-monitor-baseline-alerts) GitHub repository.

The objectives of AMBA are to:

* Help simplify onboarding to Azure Monitor through a scalable and consistent approach.
* Reduce time to identify failure within Azure tenants and platforms (i.e., outages).

More documentation can be found on the official Microsoft Learn documentation page: [Monitor Azure platform landing zone components](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/design-area/management-monitor?WT.mc_id=AZ-MVP-5004796).

![Monitor your Azure Landing Zone with Azure Monitor Baseline Alerts](/images/posts/BlogHeading_AMBA.gif)

> "AMBA Provides best practice guidance around creating and configuring Azure Monitor Alerts for Azure services and workload pattern/scenarios)."

One of the ways that makes Azure Monitor Baseline Alerts (AMBA) so useful is the details around the Alerts.

Reference: [Alerts Details](https://azure.github.io/azure-monitor-baseline-alerts/patterns/alz/Alerts-Details/)

Out-of-the-box alerts that are part of the base AMBA solution include (but are not limited to) alerts such as:

| **Resource Type**       | **Name**                           | **Description**                                                                                                                                                                                                                                                                                                                                                                 | **metricName**                     |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| automationAccounts      | TotalJob                           | The total number of jobs                                                                                                                                                                                                                                                                                                                                                        | TotalJob                           |
| storageAccounts         | Availability                       | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Availability                       |
| virtualMachines         | Available Memory Bytes (MBytes)    | Amount of physical memory, in bytes, immediately available for allocation to a process or for system use in the Virtual Machine                                                                                                                                                                                                                                                 | Available Memory Bytes             |
| virtualMachineScaleSets | Percentage CPU                     | The percentage of allocated compute units that are currently in use by the Virtual Machine(s)                                                                                                                                                                                                                                                                                   | Percentage CPU                     |
| virtualMachineScaleSets | OS Disk IOPS Consumed Percentage   | Percentage of operating system disk I/Os consumed per minute                                                                                                                                                                                                                                                                                                                    | OS Disk IOPS Consumed Percentage   |
| virtualMachineScaleSets | Data Disk IOPS Consumed Percentage | Percentage of data disk I/Os consumed per minute                                                                                                                                                                                                                                                                                                                                | Data Disk IOPS Consumed Percentage |
| virtualMachineScaleSets | Outbound Flows                     | Outbound Flows are number of current flows in the outbound direction (traffic going out of the VM)                                                                                                                                                                                                                                                                              | Outbound Flows                     |
| virtualMachineScaleSets | Inbound Flows                      | Inbound Flows are number of current flows in the inbound direction (traffic going into the VM)                                                                                                                                                                                                                                                                                  | Inbound Flows                      |
| virtualMachineScaleSets | Available Memory Bytes             | Amount of physical memory, in bytes, immediately available for allocation to a process or for system use in the Virtual Machine                                                                                                                                                                                                                                                 | Available Memory Bytes             |
| virtualMachineScaleSets | Network In Total                   | The number of bytes received on all network interfaces by the Virtual Machine(s) (Incoming Traffic)                                                                                                                                                                                                                                                                             | Network In Total                   |
| virtualMachineScaleSets | Network Out Total                  | The number of bytes out on all network interfaces by the Virtual Machine(s) (Outgoing Traffic)                                                                                                                                                                                                                                                                                  | Network Out Total                  |
| virtualMachineScaleSets | VmAvailabilityMetric               | Measure of Availability of Virtual machines over time.                                                                                                                                                                                                                                                                                                                          | VmAvailabilityMetric               |
| virtualMachineScaleSets | Disk Read Operations/Sec           | Disk Read IOPS                                                                                                                                                                                                                                                                                                                                                                  | Disk Read Operations/Sec           |
| virtualMachineScaleSets | Disk Write Operations/Sec          | Disk Write IOPS                                                                                                                                                                                                                                                                                                                                                                 | Disk Write Operations/Sec          |
| virtualNetworks         | If Under DDoS Attack               | Metric Alert for VNet DDOS Attack                                                                                                                                                                                                                                                                                                                                               | ifunderddosattack                  |
| publicIPAddresses       | Bytes In DDoS                      | Metric Alert for Public IP Address Bytes IN DDOS                                                                                                                                                                                                                                                                                                                                | bytesinddos                        |
| publicIPAddresses       | If Under DDoS Attack               | Metric Alert for Public IP Address Under Attack                                                                                                                                                                                                                                                                                                                                 | ifunderddosattack                  |
| publicIPAddresses       | Packets In DDoS                    | Inbound packets DDoS                                                                                                                                                                                                                                                                                                                                                            | PacketsInDDoS                      |
| publicIPAddresses       | VIP Availability                   | Average IP Address availability per time duration                                                                                                                                                                                                                                                                                                                               | VipAvailability                    |
| expressRouteCircuits    | ARP Availability                   | ARP Availability from MSEE towards all peers.                                                                                                                                                                                                                                                                                                                                   | ArpAvailability                    |
| expressRouteCircuits    | BGP Availability                   | BGP Availability from MSEE towards all peers.                                                                                                                                                                                                                                                                                                                                   | BgpAvailability                    |

For:

* Metric Alerts
* Log Alerts
* Activity Logs
* Service health alerts

![Graph 1](/images/posts/AMBA_Graph1.png)

![Graph 2](/images/posts/AMBA_Graph1.png)

![Monitoring Management Resource Group](/images/posts/AMBA_MangementRG.png)

## Deployment

The Azure Monitor Baseline Alerts are deployed using Azure Policy *(DINE – Deploy If Not Exist)* and are included in the [Azure Enterprise-Scale landing zone accelerator](https://github.com/Azure/Enterprise-Scale).

Deployment is currently done via an Azure Resource Manager (ARM) template and can be deployed with the following:

* PowerShell
* Azure CLI
* GitHub Actions
DevOps

Because the Azure Monitor Baseline alerts are intended to follow the Azure Landing Zone framework, in accordance with the Ready phase of the Cloud Adoption Framework, the deployment can be scaled across multiple Management groups, such as:

* Connectivity
* Identity
* Management
* Service Health
* Landing Zone (i.e., Application)

Or a single management group/subscription consisting of all features, with Alert processing rules sending relevant subscription alerts to an Action group that will notify by email if an alert is raised.

For my own Azure environment, I only have 2 Subscriptions that sit under the following Management Group hierarchy:

![Management Group structure](/images/posts/AMBA_LukeGeekNZMG.png)

We will deploy these initiatives to the MG Management Group, which allows us to then Assign those initiatives to anything beneath it, in our case, the mg-landingzones and trey-platform management groups.

As part of the deployment, we will adjust the following parameters to match our environment:

* Management groups
* Assignment of PolicySetDefinitions
* Resource Group Name and Tags
* Location
* Action group emails

We can adjust the alert rule parameters, such as the severity, and change their effect, whether they automitigate or adjust the MonitorDisable tag, which can be used to exclude from alert monitoring; we will leave these to the default.

Make sure you review and test these policies first! Before proceeding to Production.

We will deploy the ARM template using the [Azure Cloud Shell](https://learn.microsoft.com/azure/cloud-shell/overview?WT.mc_id=AZ-MVP-5004796).

1. Login to the Azure Portal
2. Click on Cloud Shell *(top right)*
3. Select your subscription and create a Storage account to host your Cloud Shell drives *(if it hasn't already been done)*
4. I'm going to adjust the parameters to match my environment by changing the following (these will need to be tuned to your specific environment):.
5. Type in:

    git clone [https://github.com/Azure/azure-monitor-baseline-alerts](https://github.com/Azure/azure-monitor-baseline-alerts)

Type in:

    cd azure-monitor-baseline-alerts\patterns\alz\

Type in:

    nano alzArm.param.json

I'm going to adjust the parameters to match my environment by changing the following *(these will need to be tuned to your specific environment)*:

| Parameters                      | Values                                          |
| ------------------------------- | ----------------------------------------------- |
| enterpriseScaleCompanyPrefix    | lukegeeknz                                      |
| platformManagementGroup         | trey-platform                                   |
| IdentityManagementGroup         | mg-landingzones                                 |
| managementManagementGroup       | trey-platform                                   |
| connectivityManagementGroup     | trey-platform                                   |
| LandingZoneManagementGroup      | mg-landingzones                                 |
| ALZMonitorResourceGroupName     | rg-management-monitoring-001                    |
| ALZMonitorResourceGroupLocation | australiaeast                                   |
| ALZMonitorActionGroupEmail      | <email@luke.geek.nz> |

> If you want the alerts to go to more than one email address, add them as comma-separated (i.e. "<email1@contos.com>, <email2@contoso.com>, <email3@contoso.com>")

8. Press Ctrl+X
9. Press Y to save buffer
10. Press Enter to overwrite the parameter json file.
11. Before proceeding to the next step, you can cat the file *(cat ./alzArm.param.json)* to view it and make sure the parameters are correct and nothing else needs changing.
12. Now that the parameters are sorted, it is time to deploy:

    $location = 'AustraliaEast'
    $psedudoRootManagementGroup = "mg"
    New-AzManagementGroupDeployment -ManagementGroupId $psedudoRootManagementGroup -Location $location -TemplateUri  '[https://raw.githubusercontent.com/Azure/azure-monitor-baseline/alerts/main/patterns/alz/alzArm.json](https://raw.githubusercontent.com/Azure/azure-monitor-baseline/alerts/main/patterns/alz/alzArm.json)' -TemplateParameterFile  'alzArm.param.json'

> The ARM template location needs to be internet accessible due to links in the ARM template to dependent resources, although the parameter file can be sourced locally.
> Error: Code=InvalidTemplate; Message=Deployment template validation failed: 'The template variable 'deploymentUris' is not valid: The language expression property 'templateLink' doesn't exist, available properties are 'template, templateHash, parameters, mode, provisioningState'.. Please see [https://aka.ms/arm-functions](https://learn.microsoft.com/azure/azure-resource-manager/templates/template-functions?WT.mc_id=AZ-MVP-5004796) for usage details.'

All going well after a few minutes – your initiatives and policies have been deployed.

![Deploy - AMBA](/images/posts/AzureCloudShell_DeployAMBA.gif)

![AMBA - Policy Definition](/images/posts/AMBA_PolicyDefinitions.png)

![AMBA - Policy Assignments](/images/posts/AMBA_PolicyAssignments.png)

If you have already existing Azure resources, you can remediate the policies, forcing them to create the Resource Group, Alerts and action groups by running the following PowerShell commands:

    cd scripts

    $pseudoRootManagementGroup = "mg"
    $identityManagementGroup = "mg-landingzones"
    $managementManagementGroup = "trey-platform"
    $connectivityManagementGroup = "trey-platform"
    $LZManagementGroup= "mg-landingzones"

    #Run the following commands to initiate remediation
    .\\Start-AMBARemediation.ps1 -managementGroupName $managementManagementGroup -policyName Alerting-Management
    .\Start-AMBARemediation.ps1 -managementGroupName $connectivityManagementGroup -policyName Alerting-Connectivity
    .\Start-AMBARemediation.ps1 -managementGroupName $identityManagementGroup -policyName Alerting-Identity
    .\Start-AMBARemediation.ps1 -managementGroupName $LZManagementGroup -policyName Alerting-LandingZone
    .\Start-AMBARemediation.ps1 -managementGroupName $pseudoRootManagementGroup -policyName Alerting-ServiceHealth

You can check the Alert rules in Azure Monitor:

![AMBA - Alert Rules](/images/posts/AMBA_AlertRules.png)

> It won't deploy all alert rules unless you have the resources; an example is the Deploy VNetG Tunnel Bandwidth alert; the policy rule will only deploy if it matches:
> The existence of a Virtual Network Gateway, with a VPN Gateway type, doesn't include the MonitorDisable tag; if I were to deploy a VPN Gateway, it would create the alert rule for me.

Finally, if you want to clean up *(delete the resources)*, you can leverage the Start-AMBACleanup.ps1 script; it will leave the Resource Group, Alert processing rules and action group.
