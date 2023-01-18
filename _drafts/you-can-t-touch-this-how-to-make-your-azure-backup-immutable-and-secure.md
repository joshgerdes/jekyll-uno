---
date: 2023-01-18 00:00:00 +1300
title: 'You Can''t Touch This: How to Make Your Azure Backup Immutable and Secure'
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
With [immutable vaults](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-concept?tabs=recovery-services-vault&WT.mc_id=AZ-MVP-5004796 "Immutable vault for Azure Backup"), Azure Backup ensures that recovery points that are once created cannot be deleted before their intended expiry time. Azure Backup does this by preventing any operations which could lead to the loss of backup data.

Hence, this helps you protect your backups against ransomware attacks and malicious actors by disallowing operations such as deleting backups or reducing retention in backup policies.

> [Immutable vaults are now in preview](https://azure.microsoft.com/en-us/updates/azure-backup-immutable-vaults-preview/?WT.mc_id=AZ-MVP-5004796 "Public preview: Immutable vaults for Azure Backup") _(as of this article - Jan 2023)_ in all regions.

An immutable vault can assist in safeguarding your backup data by prohibiting any actions that might result in the loss of recovery points.

By securing the immutable vault setting, it can be made irreversible, which can prevent any unauthorized individuals from disabling the immutability feature and erasing the backups.

The Immutable vault configuration supports both Recovery Services vaults and Backup vaults.

> While Azure Backup stores data in isolation from production workloads, it allows performing management operations to help you manage your backups, including those operations that allow you to delete recovery points. However, in certain scenarios, you may want to make the backup data immutable by preventing any such operations that, if used by malicious actors, could lead to the loss of backups. The Immutable vault setting on your vault enables you to block such operations to ensure that your backup data is protected, even if any malicious actors try to delete them to affect the recoverability of data.

Enabling immutability for the vault is a reversible operation. However, you can make it irreversible to prevent any malicious actors from disabling it _(after disabling it, they can perform destructive operations)_.

The type of operations enabling immutability on the Azure Backup vault can prevent and safeguard from is.

| System | Operation type | Description |
| --- | --- | --- |
| Recovery Services Vault & Backup Vault | Stop protection with delete data | A protected item can't have its recovery points deleted before their respective expiry date. However, you can still stop protection of the instances while retaining data forever or until their expiry. |
| Recovery Services Vault | Modify backup policy to reduce retention | Any actions that reduce the retention period in a backup policy are disallowed on Immutable vault. However, you can make policy changes that result in the increase of retention. You can also make changes to the schedule of a backup policy. |
| Recovery Services Vault | Change backup policy to reduce retention | Any attempt to replace a backup policy associated with a backup item with another policy with retention lower than the existing one is blocked. However, you can replace a policy with the one that has higher retention. |

There are three current states for the immutability of the Backup and Recovery Services Vault:

* Disabled
* Enabled _(soft immutability)_
* Enabled and locked _(hard immutability)_

| State of Immutable vault setting | Description                                                                                                                                                                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disabled                         | The vault doesn't have immutability enabled and no operations are blocked.                                                                                                                                                                                                                      |
| Enabled                          | The vault has immutability enabled and doesn't allow operations that could result in loss of backups. However, the setting can be disabled.                                                                                                                                                     |
| Enabled and locked               | The vault has immutability enabled and doesn't allow operations that could result in loss of backups. As the Immutable vault setting is now locked, it can't be disabled. Note that immutability locking is irreversible, so ensure that you take a well-informed decision when opting to lock. |

sd