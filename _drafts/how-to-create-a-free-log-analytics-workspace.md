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

You use to be able to create a 'Free' tier using the Azure Portal roughly about a year ago, however they removed it with a change in plans.

However, using PowerShell you can still create a Log Analytics Free SKU!

The Free pricing tier is a [legacy pricing tier](https://go.microsoft.com/fwlink/?linkid=2093511) that is available for trying Azure Log Analytics. It has a data cap of 500 MB/day and only 7 days of data retention, so it is intended only for testing and is not to be used for production deployments. 

You can change a Free Tier Log Analytics workspace to a Pay-as-you-go or commitment tier later.

![](/uploads/log_analytics_free.png)

## Create a 'Free Tier' Log Analytics using PowerShell

Change the variables of the script below, to suit your environment, connect to Azure and run the script to create your Log Analytics workspace.

    #Connect to Azure
    Connect-AzAccount
    
    #Set Variables
    $ResourceGroup = 'aad_mgmt'
    $Location = 'australiaeast'
    $LogAnalyticsName = 'la-free'
    $SKU = 'Free'
    
    #Creates Log Analytics Workspace
    New-AzOperationalInsightsWorkspace -Location $Location -Name $LogAnalyticsName -Sku $SKU -ResourceGroupName $ResourceGroup