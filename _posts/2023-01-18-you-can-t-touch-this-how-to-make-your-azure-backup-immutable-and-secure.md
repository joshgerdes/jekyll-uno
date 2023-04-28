---
date: '2023-01-18 00:00:00 +1300'
title: 'You Can''t Touch This: How to Make Your Azure Backup Immutable and Secure'
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /uploads/can-ttouchthis_immutability.png
_template: new_post
---

With [immutable vaults](https://learn.microsoft.com/en-us/azure/backup/backup-azure-immutable-vault-concept?tabs=recovery-services-vault&WT.mc_id=AZ-MVP-5004796 "Immutable vault for Azure Backup"){:target="_blank"}, Azure Backup ensures that recovery points that are once created cannot be deleted before their intended expiry time. Azure Backup does this by preventing any operations which could lead to the loss of backup data.

Hence, this helps you protect your backups against ransomware attacks and malicious actors by disallowing operations such as deleting backups or reducing retention in backup policies.

> [Immutable vaults are now in preview](https://azure.microsoft.com/en-us/updates/azure-backup-immutable-vaults-preview/?WT.mc_id=AZ-MVP-5004796 "Public preview: Immutable vaults for Azure Backup"){:target="_blank"} _(as of this article - Jan 2023)_ in all regions.

An immutable vault can assist in safeguarding your backup data by prohibiting any actions that might result in the loss of recovery points.

![](/uploads/can-ttouchthis_immutability.png)

By securing the immutable vault setting, it can be made irreversible, which can prevent any unauthorized individuals from disabling the immutability feature and erasing the backups.

The Immutable vault configuration supports both Recovery Services vaults and Backup vaults.

> While Azure Backup stores data in isolation from production workloads, it allows performing management operations to help you manage your backups, including those operations that allow you to delete recovery points. However, in certain scenarios, you may want to make the backup data immutable by preventing any such operations that, if used by malicious actors, could lead to the loss of backups. The Immutable vault setting on your vault enables you to block such operations to ensure that your backup data is protected, even if any malicious actors try to delete them to affect the recoverability of data.

Enabling immutability for the vault is a reversible operation. However, you can make it irreversible to prevent any malicious actors from disabling it _(after disabling it, they can perform destructive functions)_.

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

| State of Immutable vault setting | Description |
| --- | --- |
| Disabled | The vault doesn't have immutability enabled and no operations are blocked. |
| Enabled | The vault has immutability enabled and doesn't allow operations that could result in loss of backups. However, the setting can be disabled. |
| Enabled and locked | The vault has immutability enabled and doesn't allow operations that could result in loss of backups. As the Immutable vault setting is now locked, it can't be disabled. Note that immutability locking is irreversible, so ensure that you take a well-informed decision when opting to lock. |

Immutable vaults and [multi-user authorization](https://learn.microsoft.com/en-us/azure/backup/multi-user-authorization-concept?tabs=recovery-services-vault&WT.mc_id=AZ-MVP-5004796 "Multi-user authorization using Resource Guard"){:target="_blank"} can safeguard your backups from various human and technological accidents or disruptions.

Immutable vaults will not affect live or hot backups, such as snapshots.

Using the Azure Portal, let us configure immutability on your Azure Backup Vault.

 1. Navigate to your [**Recovery Services Vault**](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.RecoveryServices%2Fvaults "Recovery Services vaults"){:target="_blank"}
 2. Navigate to **Properties** _(under Settings)_
 3. ![Recovery Services Vault - Immutability](/uploads/azureportal_rsv_configureimmutable.png "Recovery Services Vault - Immutability")
 4. Under Immutable vault, select **Settings**
 5. Click the **box** to enable vault immutability
 6. ![Enable vault immutability](/uploads/azureportal_rsv_configureimmutablecheck.png "Enable vault immutability")
 7. Click **Apply**
 8. The Recovery Services vault will be adjusted, and the status has changed to **Enabled but not locked**; this means that your vault is now immutable and won't allow operations that will result in the loss of backups; however, you can reverse the change by unticking vault immutability.
 9. ![Immutable vault - soft](/uploads/azureportal_rsv_immutableenabledsoft.png "Immutable vault - soft")
10. To hard lock, your vault, navigate back into the Immutable vault settings, toggle Locked, and Apply. **This cannot be undone, so make this decision thought out, as it will stop the ability to reduce retention policies that will cause the deletion of recovery points, which could lead to increased costs in the longer term.**

The Azure Backup vault immutability can also be adjusted using Azure Bicep, reference below.

    param vaults_name string = 'rsv'
    
    resource vaults_name_resource 'Microsoft.RecoveryServices/vaults@2022-09-10' = {
      name: vaults_rsv_name
      location: 'australiaeast'
      sku: {
        name: 'RS0'
        tier: 'Standard'
      }
      properties: {
        securitySettings: {
          immutabilitySettings: {
            state: 'Unlocked'
          }
        }
      }
    }

The immutabilitySettings states are:

| State | Actions |
| --- | --- |
| Disabled | Immutability is Disabled |
| Locked | Enabled but locked |
| Unlocked | Enabled but unlocked |

_Note: I was able to delete a Recovery Vault, with locked Immutability successfully, that didn't have any Recovery points._
