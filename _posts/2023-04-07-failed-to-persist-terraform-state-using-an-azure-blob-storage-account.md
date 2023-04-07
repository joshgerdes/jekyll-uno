---
date: 2023-04-07 00:00:00 +1200
title: Failed to persist Terraform state using an Azure Blob Storage account
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/terraform_savestate.PNG"

---
When attempting to make changes with Terraform, and the [state changes are in an Azure storage account](https://learn.microsoft.com/azure/developer/terraform/store-state-in-azure-storage?tabs=azure-cli&WT.mc_id=AZ-MVP-5004796 "Store Terraform state in Azure Storage"), you may come across: Failed to save state.

> Error: Failed to save state
>
> Error saving state: blobs:Clien#GetProperties: Failure responding to request: StatusCode=403 -- Original Error: autorest/azure: error response cannot be parsed: {"" '\\x00' '\\x00'} error: EOF

And: Error: Failed to persist state to backend.

Or Error: Error releasing the state lock.

![Terraform - Failed to save state](/uploads/terraform_savestate.PNG "Terraform - Failed to save state")

Recently, encountered this issue when attempting a Terraform deployment; the state file kept locking midway through a deployment, this was traced to the Terraform storage account being in the Terraform code itself - with Public access set to Deny.

So the flow was looking like this: Script ran to allow Azure DevOps IP to the Storage account Firewall, then Terraform would start deploying and Deny access - preventing the state file from saving.

The first thing you need to do is break the lease on the state file.

1. Navigate to your **Azure Storage** account that contains the state file
2. Navigate to the **Container** that contains the state file
3. Click on your state file and select **Break lease**
4. ![Azure Storage account - break lease](/uploads/azure_storageaccount_breaklease.png "Azure Storage account - break lease")
5. Once the lease is broken - make sure that your state file is 'Available' and not 'Leased'
6. Then check your Terraform to make sure that it wasn't changing your Storage account that contained the Terraform state file in any way, then re-run your deployment.

Note: It may be wise, to make sure that the Azure storage account containing your state file is not managed by Terraform, to avoid unintentional mishaps.