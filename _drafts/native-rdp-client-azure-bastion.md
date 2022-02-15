---
date: 2022-02-16 00:00:00 +1300
title: Native RDP Client & Azure Bastion
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
In early February 2022, Azure Bastion Preview support for the [native Windows SSH and RDP](https://docs.microsoft.com/en-us/azure/bastion/connect-native-client-windows "Connect to a VM using the native client (Preview)") client came out, this meant that we didn't have to rely on the Azure Portal and the limitations of a web browser.

### Prerequisites

* This configuration requires the Standard SKU tier for Azure Bastion.
* A Virtual Machine to connect to 

### Create Azure Bastion