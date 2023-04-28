---
date: 2021-06-28T12:00:00.000Z
title: >-
  No Available Resources Error when attempting to connect to Azure Virtual
  Desktop
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: images/iazure-marketplace-banner.png
_template: new_post
---

When connecting to Azure Virtual Desktop, you may get a _"We couldn't connect because there are currently no available resources. Try again later or contact tech support for help if this keeps happening."_

![We couldn't connect because there are currently no available resources.](/uploads/noresourcesavd.png "We couldn't connect because there are currently no available resources.")

### Check your Max Session Count

On your Azure Virtual Desktop Host Pool, check your Max Session Count, which hasn't been exceeded. 

In my screenshot below, even 1 connection to my Azure Virtual Desktop farm couldn't connect, this was fixed when I raised this.

![Host Pool - Max Session Count](/uploads/maxsessionlimitavd.png "Host Pool - Max Session Count")

### Check your Host Pool sessions are available

Check your Azure Virtual Desktop Host pool, Session Hosts are: 

* Available
* Not in Drain Mode

![Host Pool - Host Pool Status](/uploads/avd_sessionhots.png "Host Pool - Host Pool Status")
