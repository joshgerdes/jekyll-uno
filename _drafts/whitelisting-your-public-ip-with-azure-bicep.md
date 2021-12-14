---
date: 2021-12-14 00:00:00 +1300
title: Whitelisting your Public IP with Azure Bicep
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Being able to whitelist and restrict Azure resources by being accessible by specific Public IP _(Internet Protocol)_ addresses has been around for years, most Azure resources support it, a Storage account is no different.

In this article, I will be using PowerShell to obtain my current public IP, then parse that variable into my Azure Bicep deployment to create a storage account, with the firewall rule allowing ONLY my public IP address.