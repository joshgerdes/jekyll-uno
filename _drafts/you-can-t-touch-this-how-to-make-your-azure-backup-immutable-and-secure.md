---
date: 2023-01-18 00:00:00 +1300
title: 'You Can''t Touch This: How to Make Your Azure Backup Immutable and Secure'
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
With immutable vaults, Azure Backup ensures that recovery points that are once created cannot be deleted before their intended expiry time. Azure Backup does this by preventing any operations which could lead to the loss of backup data.

Hence, this helps you protect your backups against ransomware attacks and malicious actors by disallowing operations such as deleting backups or reducing retention in backup policies.

> [Immutable vaults are now in preview](https://azure.microsoft.com/en-us/updates/azure-backup-immutable-vaults-preview/?WT.mc_id=AZ-MVP-5004796 "Public preview: Immutable vaults for Azure Backup") _(as of this article - Jan 2023)_ in selected regions and will be available in other regions in the coming weeks.

An immutable vault can assist in safeguarding your backup data by prohibiting any actions that might result in the loss of recovery points. 

By securing the immutable vault setting, it can be made irreversible, which can prevent any unauthorized individuals from disabling the immutability feature and erasing the backups.