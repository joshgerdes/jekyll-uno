---
date: 2021-04-23T00:00:00.000+12:00
title: How to mount an Azure Blob Container on your Windows Server
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/AzureBlobBanner.png"

---
As of January 2021, Blob storage now supports the Network File System (NFS) 3.0 protocol. This support provides Linux file system compatibility at object storage scale and prices and enables Linux clients to mount a container in Blob storage from an Azure Virtual Machine (VM) or a computer on-premises.

With the NFS client feature, these can be mapped on Windows as well, but there are some pre-requisites you need to do first.

Note: The storage account must be a member of an Azure Virtual Network and so does your Virtual Machine, either directly or via a connected expressroute or site to site VPN.

# Register AllowNFSV3 Provider

Connect to Azure using PowerShell and register the `AllowNFSV3 provider by running the following:`

    Register-AzProviderFeature -FeatureName AllowNFSV3 -ProviderNamespace Microsoft.Storage 

    Register-AzResourceProvider -ProviderNamespace Microsoft.Storage
    Get-AzProviderFeature -ProviderNamespace Microsoft.Storage -FeatureName AllowNFSV3

To mount a container by using NFS 3.0, You must create a storage account after you register the feature with your subscription. You can't enable accounts that existed before you registered the feature.

## Disable Secure Transfer on your Storage Account

1. Sign in to the [Azure portal](https://portal.azure.com/#home) and access the storage account containing the NFS share you created.
2. Select **Configuration**.
3. Select **Disabled** for **Secure transfer required**.
4. Select **Save**.

## Create a Container on your Storage Account

1. Sign in to the [Azure portal](https://portal.azure.com/#home) and access the storage account containing the NFS share you created.
2. Under Blob Service, select **Containers**
3. Click **+Container**
4. Name the container, something that is relevant to the share, in my example I am going with: Mount _- all lowercase._

![](/uploads/azstorageaccountnewcontainer.png)

1. Select **Create**.

#
## Install NFS Client Tools

1. Open PowerShell as Administrator on your Windows 10 endpoint and run the following command to install the NFS Client features:

       Enable-WindowsOptionalFeature -FeatureName ServicesForNFS-ClientOnly, ClientForNFS-Infrastructure -Online -NoRestart

## Enable write permissions for the anonymous user when mounting a UNIX share using the anonymous user.