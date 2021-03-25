---
date: 2021-03-26 00:00:00 +1300
title: Allow Azure DevOps Microsoft Hosted Agent to communicate with Azure KeyVault
author: Luke
categories:
- Azure
toc: false

---
It is best practice to lock down Azure resources to be accessible by location and services that is only to what's required and, the Azure Key vault is no exception.

When using Microsoft Hosted Agents in Azure DevOps, you need to make sure that the AzureCloud IPs for the Azure DevOps regions are opened on the Firewall.

In my case, I was in the: AustraliaEast region and needed to identify and add the following 'AzureCloud' Address Ranges to the KeyVault firewall:

* "name": "**_AzureCloud.australiaeast_**",
* "id": "AzureCloud.australiaeast",
* "properties": {
* "changeNumber": 13,
* "region": "australiaeast",
* "regionId": 3,
* "platform": "Azure",
* "systemService": "",
* "addressPrefixes": \[
* "13.70.64.0/18",
* "13.72.224.0/19",
* "13.73.192.0/20",
* "13.75.128.0/17",
* "13.104.211.128/26",
* "13.105.16.192/26",
* "13.105.20.128/26",
* "13.105.52.192/26",
* "13.105.53.128/26",
* "20.37.192.0/19",
* "20.38.112.0/23",
* "20.40.64.0/20",
* "20.40.80.0/21",
* "20.40.120.0/21",
* "20.40.176.0/20",
* "20.42.192.0/19",
* "20.43.96.0/20",
* "20.47.37.0/24",
* "20.47.122.0/23",
* "20.53.32.0/28",
* "20.53.40.0/21",
* "20.53.64.0/18",
* "20.53.128.0/17",
* "20.58.128.0/18",
* "20.60.72.0/22",
* "20.60.182.0/23",
* "20.70.128.0/17",
* "20.135.120.0/21",
* "20.150.66.0/24",
* "20.150.92.0/24",
* "20.150.117.0/24",
* "20.157.44.0/24",
* "20.188.128.0/17",
* "20.190.142.0/25",
* "20.190.167.0/24",
* "20.191.192.0/18",
* "20.193.0.0/18",
* "20.193.64.0/19",
* "23.101.208.0/20",
* "40.79.160.0/20",
* "40.79.211.0/24",
* "40.82.32.0/22",
* "40.82.192.0/19",
* "40.87.208.0/22",
* "40.90.18.0/28",
* "40.90.30.0/25",
* "40.90.130.80/28",
* "40.90.130.208/28",
* "40.90.140.32/27",
* "40.90.142.160/27",
* "40.90.147.64/27",
* "40.90.150.0/27",
* "40.112.37.128/26",
* "40.126.14.0/25",
* "40.126.39.0/24",
* "40.126.224.0/19",
* "52.108.40.0/23",
* "52.108.83.0/24",
* "52.109.112.0/22",
* "52.111.224.0/24",
* "52.113.88.0/22",
* "52.113.103.0/24",
* "52.114.16.0/22",
* "52.114.58.0/23",
* "52.114.192.0/23",
* "52.115.98.0/24",
* "52.120.158.0/23",
* "52.121.108.0/22",
* "52.143.199.0/24",
* "52.143.200.0/23",
* "52.147.0.0/19",
* "52.156.160.0/19",
* "52.187.192.0/18",
* "52.232.136.0/21",
* "52.232.154.0/24",
* "52.237.192.0/18",
* "52.239.130.0/23",
* "52.239.226.0/24",
* "52.245.16.0/22",
* "104.44.90.64/26",
* "104.44.93.96/27",
* "104.44.95.48/28",
* "104.46.29.0/24",
* "104.46.30.0/23",
* "104.209.80.0/20",
* "104.210.64.0/18",
* "191.238.66.0/23",
* "191.239.64.0/19",
* "2603:1010::/46",
* "2603:1010:5::/48",
* "2603:1010:6::/48",
* "2603:1016:1400:60::/59",
* "2603:1016:2402::/48",
* "2603:1016:2500:c::/64",
* "2603:1017:0:60::/59"

You only need to add the IP ranges of the Region that your Azure DevOps instance sits in.

You can find the region that your Azure DevOps instance sits in by following the article below:

* [Microsoft-hosted agents for Azure Pipelines - Azure Pipelines | Microsoft Docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml#networking)

You can retrieve the list of Azure IP Ranges and Service Tags from the following Microsoft JSON file:

* [Download Azure IP Ranges and Service Tags – Public Cloud from Official Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=56519)

_Note: These IP ranges can change and update, depending on Microsoft removing and adding new datacenter capability, it is always worth rechecking the list if you find you start having problems with intermittent connectivity to check whether new ranges have been added that haven't been whitelisted._