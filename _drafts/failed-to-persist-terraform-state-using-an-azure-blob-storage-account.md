---
date: 2023-04-07 00:00:00 +1200
title: Failed to persist Terraform state using an Azure Blob Storage account
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
When attempting to make changes with Terraform, and the state changes are in an Azure storage account, you may come across: Failed to save state.

> Error: Failed to save state
>
> Error saving state: blobs:Clien#GetProperties: Failure responding to request: StatusCode=403 -- Original Error: autorest/azure: error response cannot be parsed: {"" '\\x00' '\\x00'} error: EOF

And: Error: Failed to persist state to backend.

or Error: Error releasing the state lock.

![Terraform - Failed to save state](/uploads/terraform_savestate.PNG "Terraform - Failed to save state")

s