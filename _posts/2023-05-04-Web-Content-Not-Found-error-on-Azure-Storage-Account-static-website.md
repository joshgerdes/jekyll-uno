---
title: Web Content Not Found error on Azure Storage Account static website
author: Luke
categories: Azure
description: >-
  Web Content Not Found error when hosting a static webpage using an Azure
  Storage account.
date: 2023-05-03T12:00:00.000Z
toc: false
header:
  teaser: /images/posts/AzureStorageAccount_Static_Site_WebContent_Error.png
---

Azure Storage accounts [can host static websites](https://learn.microsoft.com/azure/storage/blobs/storage-blob-static-website?WT.mc_id=AZ-MVP-5004796){:target="blank"} by opening up a public endpoint to an Azure storage
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

If this occurs, make sure:

* There is no whitespace in the index document name.

![Azure storage account - index.html](/images/posts/AzureStorageAccount_Static_Site_WebContent_Filenamespace.png "Azure storage account - index.html")

* The Case matters, make sure if the filename is all lowercase in the container, then it’s all lowercase in the Azure storage account static website configuration.
* Define a 404 page (the page that gets loaded) when attempting to browse paths that don’t match the index - make sure the site exists in a container and is added to the site storage account configuration,
  like the index document name.

![404.html](/images/posts/AzureStorageAccount_Static_Site_WebContent_404filename.png "404.html")

* If you don’t have a 404 page, you can have   index.html as both.

![Azure static web site - filenames](/images/posts/AzureStorageAccount_Static_Site_WebContent_bothfiles.png "Azure static web site - filenames")

* If you have a CDN _(Content Delivery Network)_
  in front of your Azure Storage account _(Azure CDN, Cloudflare)_, you may need to adjust the access level of your Container from Private to: Blob (Anonymous).
  You [shouldn’t have to adjust this usually](https://learn.microsoft.com/azure/storage/blobs/storage-blob-static-website?WT.mc_id=AZ-MVP-5004796#impact-of-setting-the-access-level-on-the-web-container){:target="blank"}, as the Access level controls the container endpoint access – not the static website endpoint.

![Azure storage account - blob access level](/images/posts/AzureStorageAccount_Static_Site_WebContent_containeraccesslevel.png "Azure storage account - blob access level")
