---
date: 2021-07-10 00:00:00 +1200
title: How to create a Free Log Analytics workspace
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
When you create a Log Analytics workspace using the Azure Portal, you only get the Pricing or 'Pay-as-you-go' tiers to select.

However, using PowerShell you can create a Log Analytics Free SKU!

The Free pricing tier is a [legacy pricing tier](https://go.microsoft.com/fwlink/?linkid=2093511) that is available for trying Azure Log Analytics. It has a data cap of 500 MB/day and only 7 days of data retention, so it is intended only for testing and is not to be used for production deployments. Note that moving to the Free tier from any other tier with longer retention will result in data older than 7 days is deleted.

![](/uploads/log_analytics_free.png)