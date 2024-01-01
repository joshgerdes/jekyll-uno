---
title: Empowering Resilience with Azure backup services
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: /images/posts/Header-Blog-AzureBackup_Services_Innovations.gif
date: 2023-09-23 00:00:00 +1300
slug: azure/Empowering-Resilience-with-Azure-backup-services
---

This article is part of [Azure Back to School](https://azurebacktoschool.github.io/) - 2023 event! Make sure to check out the fantastic content created by the community!

![Empowering Resilience with Azure backup services](/images/posts/Header-Blog-AzureBackup_Services_Innovations.gif)

Along with the basics of the Azure Backup solutions, particularly on Virtual Machines running on Microsoft Azure, there have been a lot of changes in the last year, including Immutable vaults, enhanced policies, intelligence tiering, and cross-region restore.

## Introduction

Let us start with the basics with a user story; what do we need to achieve:

> "As a Cloud Infrastructure Administrator at Contoso, I want to implement an automated backup solution for virtual machines (Windows and Linux) hosted in Microsoft Azure,
So that I can ensure data reliability, disaster recovery, and compliance with minimal manual intervention."

With some assumptions around further requirements, we can jump into solutions using native Microsoft Azure services to fulfil the Cloud Administrator's need.
It is worth mentioning, especially around disaster recovery, that there is much more you can (and should do) do around [mission-critical](https://learn.microsoft.com/azure/well-architected/mission-critical/mission-critical-overview?WT.mc_id=AZ-MVP-5004796) Azure architecture. This article will focus primarily on the data loss portion of disaster recovery with Azure Backup services.

| **Requirement**                                                     | **Azure Service(s) Used**                       |
| ------------------------------------------------------------------- | ----------------------------------------------- |
| Specific (S): Backup virtual machines in Azure                      | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796), [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)
| Measurable (M):                                                     |                                                 |
| \- Achieve 99% backup success rate                                  | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796), [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796)                     |
| \- Define and meet RTO _(recovery time objective)_ for critical VMs | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796), [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)         |
| \- Monitor and optimise storage consumption                         | [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796), [Microsoft Cost Management](https://learn.microsoft.com/azure/cost-management-billing/costs/reporting-get-started?WT.mc_id=AZ-MVP-5004796)            |
| Achievable (A):                                                     |                                                 |
| \- Select and configure Azure-native backup solution                | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796)                                    |
| \- Configure Azure permissions and access controls                  | [Azure Role-Based Access Control (RBAC)](https://learn.microsoft.com/azure/role-based-access-control/rbac-and-directory-admin-roles?WT.mc_id=AZ-MVP-5004796)          |
| \- Define backup schedules and retention policies                   | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796), [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796)                      |
| Relevant (R):                                                       |                                                 |
| \- Align with Azure best practices                                  | [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/?WT.mc_id=AZ-MVP-5004796), [Azure Advisor](https://learn.microsoft.com/azure/advisor/advisor-overview?WT.mc_id=AZ-MVP-5004796) |
| \- Comply with data protection regulations                          | [Azure Compliance Center](https://learn.microsoft.com/azure/compliance/?WT.mc_id=AZ-MVP-5004796), [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796)           |
| \- Support disaster recovery and business continuity                | [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)                       |
| Time-bound (T):                                                     |                                                 |
| \- Implement within the next two Azure sprint cycles                | [Azure DevOps - Boards](https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards?view=azure-devops&WT.mc_id=AZ-MVP-5004796)                             |
| \- Regular progress reviews during sprint planning                  | [Azure DevOps - Boards](https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards?view=azure-devops&WT.mc_id=AZ-MVP-5004796)                             |

| **Definition of Done (DoD):**                              |                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------- |
| 1\. Select a cost-effective Azure-native backup solution   | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796)                                           |
| 2\. Configure Azure permissions and access controls        | [Azure Role-Based Access Control (RBAC)](https://learn.microsoft.com/azure/role-based-access-control/rbac-and-directory-admin-roles?WT.mc_id=AZ-MVP-5004796)                   |
| 3\. Define backup policies and RTOs                        | [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796), [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796)                               |
| 4\. Monitor and meet 99% backup success rate               | [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796)                                            |
| 5\. Optimize backup storage utilisation                    | [Microsoft Cost Management](https://learn.microsoft.com/azure/cost-management-billing/costs/reporting-get-started?WT.mc_id=AZ-MVP-5004796)                                    |
| 6\. Create backup and recovery documentation               | [Microsoft Learn documentation](https://learn.microsoft.com/azure/backup/backup-azure-restore-files-from-vm?WT.mc_id=AZ-MVP-5004796)                             |
| 7\. Train the team to manage and monitor the backup system | [Azure Training](https://learn.microsoft.com/training/modules/intro-to-azure-backup/?WT.mc_id=AZ-MVP-5004796)                        |
| 8\. Integrate with Azure monitoring and alerting           | [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796)                                            |
| 9\. Conduct disaster recovery tests                        | [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)                                |

*Note: [Azure DevOps - Boards](https://learn.microsoft.com/azure/devops/boards/get-started/what-is-azure-boards?view=azure-devops&WT.mc_id=AZ-MVP-5004796) are outside of the scope of this article; the main reflection here is to make sure that your decisions and designs are documented in line with business requirements.*
*There are also some further assumptions we will make, particularly around security and RTO requirements for the organisation of Contoso.*

We know to fulfil the requirements, we need to implement the following:

* [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796)
* [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)
* [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796)
* [Microsoft Cost Management](https://learn.microsoft.com/azure/cost-management-billing/costs/reporting-get-started?WT.mc_id=AZ-MVP-5004796)
* [Azure Role-Based Access Control (RBAC)](https://learn.microsoft.com/azure/role-based-access-control/rbac-and-directory-admin-roles?WT.mc_id=AZ-MVP-5004796)
* [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796)

So, let us take our notebooks and look at the Backup sections.

## Backup Center

When needing a single control plane for your Backups across multiple tenancies _(using [Azure Lighthouse](https://learn.microsoft.com/azure/lighthouse/overview?WT.mc_id=AZ-MVP-5004796)_), Subscriptions and regions, then Backup Center is the place to start with.

> "Backup center provides a single unified management experience in Azure for enterprises to govern, monitor, operate, and analyze backups at scale. It also provides at-scale monitoring and management capabilities for Azure Site Recovery. So, it's consistent with Azure's native management experiences. Backup center is designed to function well across a large and distributed Azure environment. You can use Backup center to efficiently manage backups spanning multiple workload types, vaults, subscriptions, regions, and Azure Lighthouse tenants."

![Backup center](/images/posts/AzureBackupCenter_Portal_Overview.png)

As you can see, Backup center can be used to see manage:

* Backup instances
* Backup policies
* Vaults
* Monitor and report on backup jobs
* Compliance *(ie Azure Virtual Machines that are not configured for backup)*

You can find the [Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted) directly in the Azure Portal.

![Backup center](/images/posts/AzurePortal-SearchBackupCenter.png)

We can create and manage these resources by ourselves, but throughout this article, we will refer back to the Backup Center, to take advantage of the single pane of glass and integrate these resources.

### Create Vault

In Microsoft Azure, there are two types of Vaults that the Backup center works with. These vaults are:

* [Recovery Services vault](https://learn.microsoft.com/azure/backup/backup-azure-recovery-services-vault-overview?WT.mc_id=AZ-MVP-5004796)
* [Backup vault](https://learn.microsoft.com/azure/backup/backup-vault-overview?WT.mc_id=AZ-MVP-5004796)

![Backup center](/images/posts/AzurePortal_CreateVault_VaultTypes.png)

Depending on your requirements depends on which Vault you will need to create _(for our purposes, we will need the Recovery Services vault)_; Backup Center makes it remarkably easy to configure a new vault and select the right vault type by using the wizard.

*Please refer to: [Support matrix for Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-support-matrix?WT.mc_id=AZ-MVP-5004796) for further information.*

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Vaults**
1. Click **+ Vault**
1. Select **Recovery Services vault**
1. Select **Continue**
1. Specify a **location** and **Resource Group** to house your Recovery Services vault
1. Specify your **vault name** *[(abbreviation examples for Azure resources)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations?WT.mc_id=AZ-MVP-5004796)*
1. Click **Next: Vault properties**

> Immutability:
I talked a bit about immutability in another blog article: [You Can't Touch This: How to Make Your Azure Backup Immutable and Secure](https://luke.geek.nz/azure/you-can-t-touch-this-how-to-make-your-azure-backup-immutable-and-secure/). Essentially an immutable vault, prevents unauthorised changes and restore point deletions, for this article, we will enable it to prevent unintended or malicious data loss (keep in mind with immutable vaults, reducing retention of recovery points is not allowed).

1. Check **enabled immutability**, and click **Next: Networking**.
1. We can join our Recovery Services vault to our [private network using private endpoints](https://learn.microsoft.com/azure/backup/private-endpoints?WT.mc_id=AZ-MVP-5004796), forcing Azure Backup and Site Recovery to traverse a private network, for the purposes of this article, we will skip it. **Click Next: Tags**
1. **Enter in Tags** *(tags useful for a Recovery Service vault, could be: Application, Support Team, Environment, Cost Center, Criticality)*
1. Click **Review + Create**

![Create Azure Recovery Services Vault](/images/posts/Create_RSV_BackupCenter_AzurePortal.gif)

If we navigate back to the [Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted) and then Vaults (under Manage), we will be able to see the newly created vault.

We now have our Backup solution provisioned for the Cloud Administrator to use, but we next need to define the policies for the backup.

### Create Backup Policies

Now that we have our Recovery Services vault, we need to create backup policies; these backup policies will help define the frequency of backups, the retention (Daily, weekly, monthly, yearly) and [vault tiering](https://learn.microsoft.com/azure/backup/use-archive-tier-support?pivots=client-portaltier&WT.mc_id=AZ-MVP-5004796#enable-smart-tiering-to-vault-archive-using-a-backup-policy-preview), which enables the Recovery Services Vault to move recovery vaults to an [archive tier](https://learn.microsoft.com/en-us/azure/backup/archive-tier-support?WT.mc_id=AZ-MVP-5004796#archive-recommendations-only-for-azure-virtual-machines) _(slower to restore, but can be cheaper overall, for those long retention policies)_.

> Backup policies are very organisation-specific and can depend a lot on operational and industry requirements; some industries have a legal obligation to store their backups for a certain number of years, the [Azure compliance center documentation](https://learn.microsoft.com/en-us/azure/compliance/?WT.mc_id=AZ-MVP-5004796) may help, around security and data requirements, make sure your backup policies are understood by the business you are working with.

For Contoso, we have the following requirements:

| Resource                   | Daily     | Weekly    | Monthly   | Yearly    | Snapshot Retention (Hot) |
|----------------------------|-----------|-----------|-----------|-----------|--------------------------|
| **Critical Application DB - Prod**| 7 days - Every 4 Hours   | 4 weeks   | 6 months  | 7 years   | 5 days                   |
| **File Server- Prod**            | 7 days   - Every 4 Hours | 6 weeks   | 6 months  | 7 years   | 5 days                   |
| **Web Application VM - Dev**     | 20 days   | 8 weeks   | 12 months | 2 years   |  2 days             |
| **Database Server - Dev**        | 30 days   | 8 weeks   | 12 months | 2 years   |  2 days            |

There are a few things to call out here:

* We can see that for Development, items need to be retained for 2 years
* For Production, its 7 years
* Snapshots need to be stored for 5 days and 2 days to allow fast restore
* Production requires a backup to be taken every 4 hours to reduce RTO *(Recovery point objective)*

![Create Azure Recovery Services Vault](/images/posts/rpo-rto-infographic.jpg)

If we take a look at the Snapshot retention, we can leverage [Instant restore](https://learn.microsoft.com/en-us/azure/backup/backup-instant-restore-capability?WT.mc_id=AZ-MVP-5004796) snapshots, to restore the workloads, quickly from the previous 5 days, reducing our time RTO (recovery time objective), and overall impact of an outage or restore, by storing the snapshots locally (as close to the original disk) without putting it (waiting for it) into archive (slower disk), this will incurr more cost, but dramatically reduces restores time. I recommend always keeping a few Instant restore snapshots available for all production systems.

![Snapshot](/images/posts/instant-rp-flow.png)

Let us create the policies _(we will only create one policy, but the same process can be used to create the others)_.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Backup policies**
1. Click **+ Add**
1 .Select **Azure Virtual Machines**
1. **Select** the **Vault** created earlier
1. Click **Continue**
1. As this will be the policy for the Critical Application DB, we will specify: **Enhanced** *(due to the multiple backups, [Zone-redundant storage (ZRS)](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy?WT.mc_id=AZ-MVP-5004796) snapshots)*
1. Specify a **Policy name**, ie Tier-1-Prod-AppDB
1. Specify **Frequency** to: Hourly, Schedule to Every 4 Hours, and Duration: 24 Hours
1. Specify **Retain instance recovery snapshots** for '5' days
1. Update **Daily Backup point** to: 7 days
1. **Configure the Weekly backup point** to occur every Sunday and retain for 4 weeks
1. **Configure the Monthly backup point** to occur on the first Sunday of the month and retain for 6 months
1. **Configure the yearly backup point** to occur on the first Sunday of the year and retain for 7 years
1. Select **enable Tiering**, and specify Recommended recovery points
1. You can also update the Resource Group name used to store the Snapshots.
1. Click **Create**

![Snapshot](/images/posts/Create_RSV_AzurePolicyEnhanced.gif)

Note: If you want, you can repeat the same process to create any others you need. Remember, with immutable vaults, you cannot reduce the retention (but you can add), so if starting for the first time, keep the retention low until you have a clear direction of what is required. A workload can use the same policy. A Standard _(not Enhanced)_ policy may be all you need for Development workloads.

### Add Virtual Machines

Now that we have our Recovery Services Vault and custom backup policies, it's time to add our Virtual Machines to the backup! To do this, we can use the Backup center to view Virtual Machines that are not getting backed up, and then configure the backup.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Protectable data sources**
1. Click on the **ellipsis** of a  Virtual Machine you want to backup
1. Click on **Backup**
1. **Select** the appropriate **Backup vault** and **policy**
1. Click **Enable backup**

> Although cross-region restore is now supported on a Recovery Services vault, the second region is read-only (RA-GRS), so make sure you have a backup recovery vault created in the region (and subscription) of the virtual machines you are trying to protect. Backup center, can see all Recovery services vaults across multiple regions and subscriptions that you have access to.

![Add Virtual Machines](/images/posts/BackupItem_BackupCenter_RSV_AzurePolicyEnhanced.gif)

Once added, the Virtual Machine will now get backed up according to the specified policy.

> Its worth noting that you can backup a Virtual Machine if it is deallocated, but it will Crash-consistent _(Only the data that already exists on the disk at the time of backup is captured and backed up, and it triggers a disk check during recovery)_ compared to Application consistent, which is more application and OS aware, so can prepare to the OS and applications for the backups to make sure that everything is written successfully to the disk ahead of the backup. You can read more about [Snapshot consistency](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction?WT.mc_id=AZ-MVP-5004796#snapshot-consistency).

## Monitor Backups

Now that we have our Recovery Services Vault, policies and protected items _(backed up Virtual Machines)_, we need to monitor to make sure that the backups are working. Backup center gives us a complete view of Failed, In Progress, and Completed jobs in the overview pane, which is excellent for a quick view of the status across subscriptions and regions.

![Azure BackupCenter](/images/posts/Azure_BackupCenter_Overview.png)

But you may want something a bit more detailed; let us look into some of the options for monitoring your backups.

### Alerts

As part of operational checks, you may want assurance or a ticket raised if there's an issue with a backup; one of the ways to achieve this is to set up an email alert that will send an email if a backup fails.

By default, these types of alerts are enabled out-of-the-box on a recovery services vault; examples of alerts can be found here: [Azure Monitor alerts for Azure Backup](https://learn.microsoft.com/azure/backup/backup-azure-monitoring-built-in-monitor?tabs=recovery-services-vaults&WT.mc_id=AZ-MVP-5004796#azure-monitor-alerts-for-azure-backup), these can be displayed in the Recovery Services Vault or Backup Center blade, immediately.

> If a destructive operation, such as stop protection with deleted data is performed, an alert is raised, and an email is sent to subscription owners, admins, and co-admins even if notifications aren't configured for the Recovery Services vault.

| Type                                       | Description                                                                                                                                                                | Example alert scenarios                                                                                          | Benefits                                                                                                                                                                                                     |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Built-in Azure Monitor alerts (AMP alerts) | These are alerts that will be available out-of-the-box for customers without needing additional configuration by the customer.                                            | Security scenarios like deleting backup data, soft-delete disabled, vault deleted, etc.                            | Useful for critical scenarios where the customer needs to receive alerts without the possibility of alerts being subverted by a malicious admin. Alerts for destructive operations fall under this category |
| Metric alerts                              | Here, Azure Backup will surface backup health-related metrics for customers' Recovery Services vaults and Backup vaults. Customers can write alert rules on these metrics. | Backup health-related scenarios such as backup success alerts, restore success, schedule missed, RPO missed, etc. | Useful for scenarios where customers would like some control over the creation of alert rules but without the overhead of setting up LA or any other custom data store.                                     |
| Custom Log Alerts                          | Customers configure their vaults to send data to the Log Analytics workspace and write alert rules on logs.                                                                    | 'N' consecutive failed backup jobs, Spike in storage consumed, etc.                                               | Useful for scenarios where there is a relatively complex, customer-specific logic needed to generate an alert.                                                                                               |

Backup alerts are supported by Azure Monitor, so under [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796), and Alerts pane you can see all your other alerts, including Azure Backup alerts from a single pane.

![Azure BackupCenter](/images/posts/AzureMonitor_BackupAlert_AzurePortal.png)

If you want to configure notifications via emails for other types of alerts, such as Backup failures, we can use [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796) Action Groups and Alert processing rules, to let us know, without having to login to the Azure Portal directly, so let us create an email alert.

To do this, we will create an Action Group and Alert Processing rule.

| Component              | Description                                                                                          |
|------------------------|------------------------------------------------------------------------------------------------------|
| Action Group           | An Action Group is a collection of actions or tasks that are executed automatically when an alert that matches specific criteria is triggered. Actions can include sending notifications, running scripts, triggering automation, or escalating the alert. Action Groups help streamline incident response and automate actions based on the nature and severity of an alert. |
| Alert Processing Rule  | An Alert Processing Rule is a set of conditions and criteria used to filter, categorize, or route incoming alerts within a monitoring or alerting system. These rules enable organizations to define how alerts are processed, prioritize them, and determine the appropriate actions to take when specific conditions are met. Alert Processing Rules are crucial for managing and efficiently responding to alerts. |

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Alerts**
1. Click on **Alert Processing rule**
1. Click **+ Select Scope**
1. Click **All Resource Types**, and Filter by: **Recovery Services Vault**
1. **Select** your **Recovery Services vault**, you would like to alert on
1. Click **Apply**
1. Click on **Filter, and change: Alert condition = Fired**.
1. Click Next: **Rule Settings**
1. Click **Apply action group**
1. Click **+ Create action group**
1. **Select** the Subscription, **Resource Group** to store your action group (i.e. monitor resource group)
1. Give the **Action Group** a **name**, and give it a Display name
1. Specify **Notification** type _(ie Email/SMS message/push/voice)_
1. For this article, we will add an Email _(but you can have it ring a number, push a notification to the [Azure Mobile App](https://azure.microsoft.com/en-us/get-started/azure-portal/mobile-app?WT.mc_id=AZ-MVP-5004796))_
1. Enter in **your details**, then click **Next: Actions**
1. In the Actions pane, is where you can trigger automation, such as Azure Logic Apps, Runbooks, ITSM connections, Webhooks etc., to help self-remediate the issues, or better notifications, such as a Logic App that posts in a Teams channel when an alert is fired, or a wehbook that triggers a webpage to update. In this example, we will leave it empty and rely on email notifications and click Next: Tags
1. Enter any Tags and click **Review + create**
1. Make note of Suppress Notifications; this could be handy during scheduled maintenance windows where backups may fail due to approved work.
1. Once the Action Group has been created, click **Next: Scheduling**
1. Select **Always**
1. Click **Next: Details**
1. Enter in a **Resource Group**, for the Alert processing rule to be placed
1. Enter in **Rule name**, **description** and click **Review + Create**

![Azure BackupCenter](/images/posts/BackupItem_BackupCenter_RSV_BackupAlertRuleCreation.gif)

As you can see Azure Monitor integration into backups, gives you some great options to keep on top of your backups, and integrate with other systems, like your IT Service Management toolsets.

## Azure Site Recovery

[Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796) can be used to migrate workloads, across [Availability Zones and regions](https://learn.microsoft.com/azure/reliability/availability-zones-overview?WT.mc_id=AZ-MVP-5004796), by replicating the disks of a Virtual Machine to another region (GRS) or zone (ZRS), in fact [Azure Resource Mover](https://learn.microsoft.com/azure/resource-mover/overview?WT.mc_id=AZ-MVP-5004796) uses Azure Site Recovery when moving virtual machines between regions. Azure Site Recovery can also help with migrating workloads outside of Azure, to Azure, for disaster recovery.

When looking at migrating workloads, to Azure from the VMWare stack, consider the [Azure Site Recovery Deployment Planner for VMware](https://learn.microsoft.com/azure/site-recovery/site-recovery-deployment-planner?WT.mc_id=AZ-MVP-5004796) to Azure to assist.

For the purposes of this guide, we will achieve disaster recovery of our virtual machine, by replicating it to another region _(i.e. from Australia East to Central India)_.

> Azure Recovery Services contributes to your BCDR strategy:
Site Recovery service: Site Recovery helps ensure business continuity by keeping business apps and workloads running during outages. Site Recovery replicates workloads running on physical and virtual machines (VMs) from a primary site to a secondary location. When an outage occurs at your primary site, you fail over to a secondary location, and access apps from there. After the primary location is running again, you can fail back to it.
Backup service: The Azure Backup service keeps your data safe and recoverable.

![Azure BackupCenter](/images/posts/CausesITDisasters.png)

> Just as important (if not more) than the technology to enable this, clear business requirements and preparation is paramount for a successful disaster recovery solution, I highly recommend the [Azure Business Continuity Guide](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/introducing-the-azure-business-continuity-guide/ba-p/3905424?WT.mc_id=AZ-MVP-5004796). Supplied by the Microsoft Fastrack team, this guide includes resources to prepare for thorough disaster recovery plan.

The key to successful disaster recovery is not only the workloads themselves but supporting services, such as DNS, Firewall rules, connectivity etc., that need to be considered, These are out of the scope of this article but the following Microsoft Azure architecture references are worth a read:

* [Enterprise-scale disaster recovery](https://learn.microsoft.com/azure/architecture/solution-ideas/articles/disaster-recovery-enterprise-scale-dr?WT.mc_id=AZ-MVP-5004796)
* [SMB disaster recovery with Azure Site Recovery](https://learn.microsoft.com/azure/architecture/solution-ideas/articles/disaster-recovery-smb-azure-site-recovery?WT.mc_id=AZ-MVP-5004796)
* [Azure to Azure disaster recovery architecture](https://learn.microsoft.com/azure/site-recovery/azure-to-azure-architecture?WT.mc_id=AZ-MVP-5004796)
* [Multi-region N-tier application](https://learn.microsoft.com/azure/architecture/reference-architectures/n-tier/multi-region-sql-server?WT.mc_id=AZ-MVP-5004796)
* [Build high availability into your BCDR strategy](https://learn.microsoft.com/azure/architecture/solution-ideas/articles/build-high-availability-into-your-bcdr-strategy?WT.mc_id=AZ-MVP-5004796)
* [Retain IP addresses during failover](https://learn.microsoft.com/azure/site-recovery/site-recovery-retain-ip-azure-vm-failover?WT.mc_id=AZ-MVP-5004796)
* [Empowering Disaster Recovery for Azure VMs with Azure Site Recovery and Terraform](https://techcommunity.microsoft.com/t5/azure-architecture-blog/empowering-disaster-recovery-for-azure-vms-with-azure-site/ba-p/3885378?WT.mc_id=AZ-MVP-5004796)

For Azure Site Recovery to work, it relies on a mobility service running within the Virtual Machine to replicate changes, the source virtual machine needs to be on to replicate the changes.

> When you enable replication for a VM to set up disaster recovery, the Site Recovery Mobility service extension installs on the VM and registers it with Azure Site Recovery. During replication, VM disk writes are sent to a cache storage account in the source region. Data is sent from there to the target region, and recovery points are generated from the data.

Azure Site Recovery, does not currently support virtual machines protected with [Trusted Launch](https://learn.microsoft.com/azure/virtual-machines/trusted-launch?WT.mc_id=AZ-MVP-5004796).

### Enable Azure Site Recovery

For now, we have 'VM1' a Ubuntu workload, running in Australia East, with a Public IP, that we will failover to Central India. The source Virtual Machine can be backed up normally by a vault in the source region, and replicated to another vault in the destination region.

> Azure Site Recovery has a specific Operating System and Linux kernel [support](https://learn.microsoft.com/azure/site-recovery/azure-to-azure-support-matrix?WT.mc_id=AZ-MVP-5004796#replicated-machine-operating-systems). Make sure you confirm that your workloads are supported.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Vaults**
1. **Create** a new Recovery Services **vault** in your **DR** _(Disaster Recovery **region** - ie Central India)_
1. Click on **Site Recovery**
1. Under Azure Virtual Machines, click on: **Enable replication**
1. Specify the **source Virtual Machine**, you wish to migrate
1. Click **Next**
1. Select your **source Virtual Machine**
1. Click **Next**
1. Select the **target location (i.e. Central India)**
1. Select the **target Resource Group**
1. Select the **Target Virtual Network** _(create one if it doesn't exist)_
1. Select the **target subnet**
1. Under the Storage, you can consider changing the replica disk to Standard, to reduce cost (this can be [changed](https://learn.microsoft.com/azure/virtual-machines/disks-convert-types?tabs=azure-portal&WT.mc_id=AZ-MVP-5004796#change-the-type-of-an-individual-managed-disk) later).
1. Select a cache storage account _(The cache storage account is a storage account used for transferring the replication data before its written to the destination disk)_
1. You can then adjust the availability zone of the destination virtual machine
1. Click **Next**
1. Here we can **define a Replication Policy** _(a replication policy in Azure Site Recovery is a set of rules and configurations that determine how data is replicated from the source environment to the target environment (Azure) in case of a disaster or planned failover, such as retention, ie you can restore a point within the retention period)_ we will leave the default 24-hour retention policy.
1. We can specify a Replication Group, An example of a replication group is application servers that need to be consistent with each other, in terms of data _( replication policy in Azure Site Recovery is a set of rules and configurations that determine how data is replicated from the source environment to the target environment (Azure) in case of a disaster or planned failover.)_.
1. Specify an automation account to manage the mobility service, and we will leave the update extension to be ASR (Azure Site Recovery) managed.
1. Click **Next**
1. Click **Enable replication**
1. At the Recovery Services Vault, under Site Recovery Jobs you can monitor the registration, registration and initial replication can take 30-60 minutes to install the agent and start the replication.

![Azure BackupCenter](/images/posts/BackupCenter_RSV_EnableAzureSiteRecovery.gif)

### Failover to the secondary region using Azure Site Recovery

Once your virtual machine has been replicated in the secondary region. you can do a Failover, or Test failover. A Test failover is recommended, in your DR testing, and application testing.

![Azure BackupCenter](/images/posts/ASR_AUE_to_CentralIndia.png)

| Aspect               | Failover                                      | Test Failover                               |
|----------------------|----------------------------------------------|---------------------------------------------|
| Purpose              | To switch to a secondary site during a disaster or planned maintenance event. | To validate your disaster recovery plan without impacting production. |
| Impact on Production | Disrupts production services as the primary site becomes unavailable during the failover process. | No impact on production services; the primary site remains operational. |
| Data Replication     | Replicates data from primary to secondary site, making it the active site during the failover. | Uses the same replicated data but doesn't make the secondary site the active site; it's for testing purposes only. |
| Recovery Time        | Longer recovery time, as it involves setting up and activating the secondary site. | Faster recovery time, as it doesn't require making the secondary site the active site. |
| Data Consistency     | Ensures data consistency and integrity during the failover process. | Ensures data consistency for testing but doesn't make the secondary site the primary site. |
| Cost                 | May incur additional costs due to the resources activated at the secondary site. | Typically incurs minimal additional costs as it's for testing purposes. |
| Use Cases            | Actual disaster recovery scenarios or planned maintenance events. | Testing and validating disaster recovery procedures, training, and compliance. |
| Post-Operation       | The secondary site becomes the new primary site until failback is initiated. | No change to the primary site; the secondary site remains inactive. |
| Rollback Option      | Failback operation is required to return to the primary site once it's available. | No need for a rollback; the primary site remains unaffected. |

1. Navigate to your destination Recovery Services Vault
1. Click on REplicated Items
1. Select the Virtual Machine you wish to recover in your second region
1. Select Test Failover (or Failover, depending on your requirements)
1. Select your Recovery point and destination Virtual network
1. Select Failover
1. If it is a test failover, you can then Clean up your Test failover _(deleted replicated item)_ after you have tested

![Azure BackupCenter](/images/posts/BackupCenter_RSV_TestFailoverAzureSiteRecovery.gif)

## Azure Policies

Automatically, mapping of Virtual Machines, to backup policies can be done using [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796).

Azure policies such as:

* Azure Backup should be enabled for Virtual Machines
* Configure backup on virtual machines without a given tag to an existing recovery services vault in the same location
* Disable Cross Subscription Restore for Backup Vaults
* Soft delete should be enabled for Backup Vaults

More, are built-in to the Azure policy engine and can be easily assigned, across subscriptions and management groups, found in the Backup Center.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Azure policies for backup**
1. Click on a policy and click **Assign**

> You can find a list of custom and built-in policies at the [AzPolicyAdvertizerPro](https://www.azadvertizer.net/azpolicyadvertizer_all.html) website.

![Azure AutoManage](/images/posts/azure-automanage-intelligently-onboard-services.png)

[Azure Automanage](https://learn.microsoft.com/azure/automanage/overview-about?WT.mc_id=AZ-MVP-5004796) can be used alongside Azure policy, to onboard Virtual Machines, into backup, patching etc automatically, with reduced manual intervention, and although not directly part of this article, what you have learned can be used to develop your automanage profiles.
