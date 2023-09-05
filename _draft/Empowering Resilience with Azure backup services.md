---
title: Empowering Resilience with Azure backup services
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/Header-Blog-AzureBackup_Services_Innovations.gif
date: '2023-08-28 00:00:00 +1300'
---

This article is part of [Azure Back to School](https://azurebacktoschool.github.io/) - 2023 event! Make sure to check out the amazing content, created from the community!

![Empowering Resilience with Azure backup services](/images/posts/Header-Blog-AzureBackup_Services_Innovations.gif)

Along with the basics of the Azure Backup solutions, particularly on Virtual Machines running on Microsoft Azure, there have been a lot of changes in the last year, including Immutable vaults, enhanced policies, intelligence tiering, and cross-region restore.

## Introduction

Let us start with the basics with a user story; what do we need to achieve:

> "As a Cloud Infrastructure Administrator at Contoso, I want to implement an automated backup solution for virtual machines (Windows and Linux) hosted in Microsoft Azure,
So that I can ensure data reliability, disaster recovery, and compliance with minimal manual intervention."

With some assumptions around further requirements, we can jump into solutions using native Microsoft Azure services to fulfil the Cloud Administrator's need.
It is worth mentioning, especially around disaster recovery, that there is a lot more you can (and should do) do around mission-critical Azure architecture, but for this article, we will focus primarily on the data loss portion of disaster recovery, in relation to Azure Backup services.

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

We know to fulfil the requirements; we need to implement the following:

* [Azure Backup](https://learn.microsoft.com/azure/backup/?WT.mc_id=AZ-MVP-5004796)
* [Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796)
* [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796)
* [Microsoft Cost Management](https://learn.microsoft.com/azure/cost-management-billing/costs/reporting-get-started?WT.mc_id=AZ-MVP-5004796)
* [Azure Role-Based Access Control (RBAC)](https://learn.microsoft.com/azure/role-based-access-control/rbac-and-directory-admin-roles?WT.mc_id=AZ-MVP-5004796)
* [Azure Policy](https://learn.microsoft.com/azure/governance/policy/overview?WT.mc_id=AZ-MVP-5004796)

So lets take our notebooks and take a look at the Backup sections.

## Backup Center

When needing a single control plane for your Backups, across multiple tenancies _(using [Azure Lighthouse](https://learn.microsoft.com/azure/lighthouse/overview?WT.mc_id=AZ-MVP-5004796)_), Subscriptions and regions, then Backup Center is the place to start with.

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

We can create the manage these resources by themselves, but throughout this article, we will refer back to the Backup Center, to take avantage of the single pane of glass, and integration to these resources.

### Create Vault

In Microsoft Azure, there are 2 types of Vaults, that Backup center works with: these vaults are:

* [Recovery Services vault](https://learn.microsoft.com/azure/backup/backup-azure-recovery-services-vault-overview?WT.mc_id=AZ-MVP-5004796)
* [Backup vault](https://learn.microsoft.com/azure/backup/backup-vault-overview?WT.mc_id=AZ-MVP-5004796)

![Backup center](/images/posts/AzurePortal_CreateVault_VaultTypes.png)

Depending on your requirements, depends on which Vault you will need to create _(for our purposes, we will need the Recovery Services vault)_, Backup Center makes it remarkably easy to configure a new vault and select the right vault type, by using the wizard.

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
I talked a bit about immutability, in another blog article: [You Can't Touch This: How to Make Your Azure Backup Immutable and Secure](https://luke.geek.nz/azure/you-can-t-touch-this-how-to-make-your-azure-backup-immutable-and-secure/). Essentially an immutable vault, prevents unauthorised changes and restore point deletions, for the purposes of this article, we will enable it to prevent unintended or malicious data loss (keep in mind with immutable vaults, reducing retention of recovery points is not allowed).

1. Check **enabled immutability**, and click **Next: Networking**.
1. We can join our Recovery Services vault, to our [private network using private endpoints](https://learn.microsoft.com/azure/backup/private-endpoints?WT.mc_id=AZ-MVP-5004796), forcing Azure Backup and Site Recovery to traverse a private network, for the purposes of this article, we will skip it. **Click Next: Tags**
1. **Enter in Tags** *(tags useful for a Recovery Service vault, could be: Application, Support Team, Environment, Cost Center, Criticality)*
1. Click **Review + Create**

![Create Azure Recovery Services Vault](/images/posts/Create_RSV_BackupCenter_AzurePortal.gif)

If we navigate back to the [Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted), and then Vaults (under Manage), we will be able to see the newly created vault.

We now have our Backup solution provisioned for the Cloud Administrator to use, but we next need to define the policies for the backup.

### Create Backup policies

Now that we have our Recovery Services vault, we need to create backup policies, these backup policies will help define the frequency of backups, the retention (Daily, weekly, monthly, yearly) and [vault tiering](https://learn.microsoft.com/azure/backup/use-archive-tier-support?pivots=client-portaltier&WT.mc_id=AZ-MVP-5004796#enable-smart-tiering-to-vault-archive-using-a-backup-policy-preview), which enables the Recovery Services Vault to move recovery vaults to an [archive tier](https://learn.microsoft.com/en-us/azure/backup/archive-tier-support?WT.mc_id=AZ-MVP-5004796#archive-recommendations-only-for-azure-virtual-machines) _(slower to restore, but can be cheaper overall, for those long retention policies)_.

> Backup policies are very organisation specific, it can depend alot on operational and industry requirements, some industries have a legal obligation to store their backups for a certain number of years, the [Azure compliance center documentation](https://learn.microsoft.com/en-us/azure/compliance/?WT.mc_id=AZ-MVP-5004796) may help, around security and data requirements, make sure your backup policies are understood by the business you are working with.

For Contoso, we have the following requirements:

| Resource                   | Daily     | Weekly    | Monthly   | Yearly    | Snapshot Retention (Hot) |
|----------------------------|-----------|-----------|-----------|-----------|--------------------------|
| **Critical Application DB - Prod**| 7 days - Every 4 Hours   | 4 weeks   | 6 months  | 7 years   | 5 days                   |
| **File Server- Prod**            | 7 days   - Every 4 Hours | 6 weeks   | 6 months  | 7 years   | 5 days                   |
| **Web Application VM - Dev**     | 20 days   | 8 weeks   | 12 months | 2 years   |  2 days             |
| **Database Server - Dev**        | 30 days   | 8 weeks   | 12 months | 2 years   |  2 days            |

There are a few things, to call out here:

* We can see that for Development, items need to be retained for: 2 years
* For Production, its 7 years
* Snapshots need to be stored for 5 days and 2 days to allow fast restore
* Production requires a backup to be taken every 4 hours to reduce RTO *(Recovery point objective)*

![Create Azure Recovery Services Vault](/images/posts/rpo-rto-infographic.jpg)

If we take a look at the Snapshot retention, we can leverage [Instant restore](https://learn.microsoft.com/en-us/azure/backup/backup-instant-restore-capability?WT.mc_id=AZ-MVP-5004796) snapshots, to restore the workloads, quickly from the previous 5 days, reducing our time RTO (recovery time objective), and overall impact of an outage or restore, by storing the snapshots locally (as close to the original disk) without putting it (waiting for it) into archive (slower disk), this will incurr more cost, but dramatically reduces restores time. I recommend always keeping a few Instant restore snapshots avaliable for all production systems.

![Snapshot](/images/posts/instant-rp-flow.png)

Let us create the policies _(we will only create one policy, but the same process can be used to create the others)_.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Backup policies**
1. Click **+ Add**
1 .Select **Azure Virtual Machines**
1. **Select** the **Vault** created earlier
1. Click **Continue**
1. As this will be the policy for the Critical Application DB, wwe will specify: **Enchanced** *(due to the multiple, backups, [Zone-redundant storage (ZRS)](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy?WT.mc_id=AZ-MVP-5004796) snapshots)*
1. Specify a **Policy name**, ie Tier-1-Prod-AppDB
1. Specify **Frequency**, to: Hourly, Schedule to Every 4 Hours, and Duration: 24 Hours
1. Specify **Retain instance recovery snapshots** for '5' days
1. Update **Daily Backup point** to: 7 days
1. **Configure the Weekly backup point** to occur every Sunday and retain for 4 weeks
1. **Configure the Monthly backup point** to occur on the first Sunday of the month and retain for 6 months
1. **Configure the yearly backup point** to occur on the first sunday of the year, and retain for 7 years
1. Select **enable Tiering**, and specify Recommended recovery points
1. You can also update the Resource Group name that is being used to store the Snapshots.
1. Click **Create**

![Snapshot](/images/posts/Create_RSV_AzurePolicyEnhanced.gif)

Note: If you want, you can repeat the same process, to create any others that you need. Remember with immutable vaults, you cannot reduce the retention (but you can add), so if starting for the first time, keep the retention low until you have clear direction of whats required. A workload, can use the same Policy. A Standard _(not Enchanced)_ policy, may be all you need for Development workloads.

### Add Virtual Machines

Now that we have our Recovery Services Vault, and custom backup policies, its time to add our Virtual Machines to the backup! To do this, we can use the Backup center to view Virtual Machines, that are not getting backed up, then configure the backup.

1. Navigate to **[Backup Center](https://portal.azure.com/#view/Microsoft_Azure_DataProtection/BackupCenterMenuBlade/~/gettingstarted)**
1. Click on **Protectable datasources**
1. Click on the **elipsis** of a  Virtual Machine, you want to backup
1. Click on **Backup**
1. **Select** the appropiate **Backup vault** and **policy**
1. Click **Enable backup**

> Although cross region restore is now supported on a Recovery Services vault, the second region is read only (RA-GRS), so make sure you have a backup recovery vault created in the region (and subscription) of the virtual machines you are trying to protect. Backup center, can see all Recovery services vaults across multiple regions and subscriptions that you have access to.

![Add Virtual Machines](/images/posts/BackupItem_BackupCenter_RSV_AzurePolicyEnhanced.gif)

Once added, the Virtual Machine will now get backed up according to the specified policy.

> Its worth noting, that you can backup a Virtual Machine, if its deallocated but it will Crash-consistant _(Only the data that already exists on the disk at the time of backup is captured and backed up, and it triggers a disk check during recovery)_ compared to Application consistant, which is more application and OS aware, so can prepare to the OS and applications for the backups to make sure that everything is writen successfully to the disk ahead of the backup. You can read more about [Snapshot consistency](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction?WT.mc_id=AZ-MVP-5004796#snapshot-consistency).

## Monitor Backups

Now that we have our Recovery Services Vault, policies and protected items _(backed up Virtual Machines)_, we need to monitor to make sure that the backups are working. Backup center gives us that complete view of Failed, In Progress, Completed jobs in the overview pane, which is great for a quick view of the status across subscriptions and regions.

![Azure BackupCenter](/images/posts/Azure_BackupCenter_Overview.png)

But you may want something a bit more detailed, lets look into some of the options for monitoring your backups.

### Alerts

As part of operational checks, you may want assurance, or a ticket raised if theres an issue with a backup, one of the ways to achive this is to setup an email alert, that will send an email if a backup failed.

By default these type of alerts, are enabled out-of-the-box, on a recovery services vault, examples of alerts can be found here: [Azure Monitor alerts for Azure Backup](https://learn.microsoft.com/azure/backup/backup-azure-monitoring-built-in-monitor?tabs=recovery-services-vaults&WT.mc_id=AZ-MVP-5004796#azure-monitor-alerts-for-azure-backup), these can be displayed in the Recovery Services Vault or Backup Center blade, immediately.

> If a destructive operation, such as stop protection with delete data is performed, an alert is raised and an email is sent to subscription owners, admins, and co-admins even if notifications aren't configured for the Recovery Services vault.

| Type                                       | Description                                                                                                                                                                | Example alert scenarios                                                                                          | Benefits                                                                                                                                                                                                     |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Built-in Azure Monitor alerts (AMP alerts) | These are alerts that will be available out-of-the-box for customers, without needing additional configuration by the customer.                                            | Security scenarios like delete backup data, soft-delete disabled, vault deleted, etc.                            | Useful for critical scenarios where the customer needs to receive alerts, without the possibility of alerts being subverted by a malicious admin. Alerts for destructive operations fall under this category |
| Metric alerts                              | Here, Azure Backup will surface backup health related metrics for customers' Recovery Services vaults and Backup vaults. Customers can write alert rules on these metrics. | Backup health related scenarios such as backup success alerts, restore success, schedule missed, RPO missed etc. | Useful for scenarios where customers would like some control over the creation of alert rules, but without the overhead of setting up LA or any other custom data store.                                     |
| Custom Log Alerts                          | Customers configure their vaults to send data to Log Analytics workspace and write alert rules on logs.                                                                    | 'N' consecutive failed backup jobs, Spike in storage consumed etc.                                               | Useful for scenarios where there is a relatively complex, customer-specific logic needed to generate an alert.                                                                                               |

Backup alerts are suppoorted by Azure Monitor, so under [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796), and Alerts pane you can see all your other alerts, including Azure Backup alerts from a single pane.

![Azure BackupCenter](/images/posts/AzureMonitor_BackupAlert_AzurePortal.png)

If you want to configure notifications via emails, for other types of alerts, such as Backup failures, we can use [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview?WT.mc_id=AZ-MVP-5004796) Action Groups and Alert processing rules, to let us know, without having to login to the Azure Portal directly, so lets create an email alert.

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
1. **Select** the Subscription, **Resource Group** to store your action group (ie monitor resource group)
1. Give the **Action Group** a **name**, and give it a Display name
1. Specify **Notification** type _(ie Email/SMS message/push/voice)_
1. For this article, we will add in an Email _(but you can have it ring a number, push a notification to the [Azure Mobile App](https://azure.microsoft.com/en-us/get-started/azure-portal/mobile-app?WT.mc_id=AZ-MVP-5004796))_
1. Enter in **your details**, then click **Next: Actions**
1. In the Actions pane, is where you can trigger automation, such as Azure Logic Apps, Runbooks, ITSM connections, Webhooks etc, to help self-remediate the issues, or better notifications, such as a Logic App that posts in a Teams channel when an alert is fired, or a wehbook that triggers a webpage to update. In this example, we will leave it empty and just rely on email notifications and click Next: Tags
1. Enter in any Tags and click **Review + create**
1. Make note of: Suppress Notifications, this could be handy during scheduled maintenance windows where's backups may fail due to approved work.
1. Once the Action Group has been created, click **Next: Scheduling**
1. Select **Always**
1. Click **Next: Details**
1. Enter in a **Resource Group**, for the Alert processing rule to be placed
1. Enter in **Rule name**, **description** and click **Review + Create**

![Azure BackupCenter](/images/posts/BackupItem_BackupCenter_RSV_BackupAlertRuleCreation.gif)

As you can see Azure Monitor integration into backups, gives you some great options to keep ontop of your backups, and integrate with other systems, like your IT Service Management toolsets.

## Azure Site Recovery

[Azure Site Recovery (ASR)](https://learn.microsoft.com/azure/site-recovery/site-recovery-overview?WT.mc_id=AZ-MVP-5004796) can be used to migrate workloads, across [Availability Zones and regions](https://learn.microsoft.com/azure/reliability/availability-zones-overview?WT.mc_id=AZ-MVP-5004796).
