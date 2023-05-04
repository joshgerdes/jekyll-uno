---
title: Web Content Not Found error on Azure Storage Account static website
author: Luke
categories: Azure
description: >-
  Web Content Not Found error when hosting a static webpage using an Azure
  Storage account
date: 2023-05-03T12:00:00.000Z
Header: /images/posts/AzureStorageAccount_Static_Site_WebContent_Error.png
---

Azure Storage accounts [can host static websites](https://learn.microsoft.com/azure/storage/blobs/storage-blob-static-website?WT.mc_id=AZ-MVP-5004796) by opening up a public endpoint to an Azure storage
container ($web), so anything inside of $web will be accessible publicly.

This can be enabled easily by toggling the Static website to Enabled.

![Azure Storage Account - Static website](/images/posts/AzureStorageAccount_Static_Site_WebContent_Config.png "Azure Storage Account - Static website")

Once enabled, the Azure storage account will add a NEW endpoint - \<storageaccname>.z\*.web.core.windows.net.

Once you have enabled the static website functionality, a new container named: $web will be created; this is the root of your static website – and where your HTML or static website will go.

After you upload your website files to the $web folder.

![Azure Storage Account - $web container](/images/posts/AzureStorageAccount_Static_Site_WebContent_WebContainer.png "Azure Storage Account - $web container")

Add the index document name (i.e., index.html) and click Save.

![Azure Storage Account - Static Website primary endpoint](/images/posts/AzureStorageAccount_Static_Site_WebContent_PrimaryEndpoint.png "Azure Storage Account - Static Website primary endpoint")

If done correctly, your website should now show your website.![Azure Storage account static websitev](/images/posts/AzureStorageAccount_Static_Site_WebContent_Website.png "Azure Storage account static website")

If done incorrectly, you may get: The requested content does not exist.

![The requested content does not exist](/images/posts/AzureStorageAccount_Static_Site_WebContent_Error.png "The requested content does not exist")
