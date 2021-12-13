---
date: 2021-12-13 00:00:00 +1300
title: Capturing Virtual Machine images and Snapshots in Azure using WVDAdmin
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
[WVDAdmin](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/ "WVDAdmin") - is a native administration GUI (graphical user interface) for Azure Virtual Desktop (AVD). WVDAdmin is a free custom-built tool, designed to make managing and standing up Azure Virtual Desktop infrastructure really easy, not only can you use it to roll out your Azure Virtual Desktop infrastructure and manage existing workspaces and host pools - you can use it to create Virtual Machine images, that can be used for Virtual Scale Sets, Base builds or Azure Virtual Desktop session hosts! WVDAdmin automates the creation and use of snapshots and virtual machine images, in a simple point and click interface - that just works!

### Prerequisites

* Azure subscription
* Resource Group
* Virtual Machine _(to be used as your master image)_
* Of course - WVDAdmin

You can download WVDAdmin from the following page:  [Azure Windows Virtual Desktop administration with WVDAdmin](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/ " Azure Windows Virtual Desktop administration with WVDAdmin").

Also, make sure you have set up a [service principal ](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/#service-principal-functional-account "Service principal (functional account) Link")with the appropriate rights to the Resource Groups that holds your virtual machine.

Before proceeding ahead - **_make sure you have a backup of your Virtual Machine!_**

### Capturing a Snapshot

### 