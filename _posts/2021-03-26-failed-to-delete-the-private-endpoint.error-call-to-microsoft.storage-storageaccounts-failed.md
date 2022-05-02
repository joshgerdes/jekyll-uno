---
date: 2021-03-26 00:00:00 +1300
title: 'Failed to delete the private endpoint. Error: Call to Microsoft.Storage/storageAccounts
  failed'
author: Luke
categories:
- Azure
toc: false

---
## Issue Description

Failed to delete the private endpoint. Error: Call to Microsoft.Storage/storageAccounts failed

## Root Cause

Azure Backup locks the storage account when you configure protection for any file share in the corresponding account. This provides protection against accidental deletion of a storage account with backed-up file shares.

## Resolution

In my case, the Storage account I was attempting to remove the Private Endpoint from was an Azure File Sync storage account, that had Azure File Shares that were getting Backuped Up.

* Found and removed the lock on the storage account
* Then successfully delete the private endpoint

## More info

Generally, it is recommended that keep the lock taken on the storage account by Azure Backup. If you delete the lock, your storage account will be prone to accidental deletion and if it's deleted, you'll lose your snapshots or backups.

[https://docs.microsoft.com/en-us/azure/backup/backup-afs#best-practices](https://docs.microsoft.com/en-us/azure/backup/backup-afs?WT.mc_id=AZ-MVP-5004796#best-practices "https://docs.microsoft.com/en-us/azure/backup/backup-afs?WT.mc_id=AZ-MVP-5004796#best-practices")

[https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources "https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json&WT.mc_id=AZ-MVP-5004796")