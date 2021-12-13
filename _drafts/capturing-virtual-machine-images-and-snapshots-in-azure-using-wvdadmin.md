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

Although, possible to do using the Azure Portal, quickly taking an OS disk snapshot and then reverting the change can be a bit tedious, especially if you want to quickly make a backup of the operating system disk before patching or application upgrade, Snapshots are a lot quicker to take and work really well for quick and temporary recovery, especially when you want to quickly try something out - without having to wait for an Azure Backup. Please note this tool does not snapshot any data drives present, if needed you will need to do this manually through the Azure Portal or PowerShell.

#### Capture a Snapshot

 1. Open **WVDAdmin**
 2. On the "Welcome" tab, **enter** in your Azure **Tenant id**
 3. **Enter** in your **Service principal (application) ID** and **key**
 4. Click on **Reload all** - to connect to Azure
 5. **Expand Azure**
 6. **Expand Virtual Machines**
 7. **Expand** your **Resource group**, in my example, it is: SERVERS-RG
 8. **Right-click** your **server**, in my example it is: Server2019
 9. Select **SnapShot-Create**
10. ![](/uploads/snapshot-create.png)
11. WVDAdmin will then prompt you to verify that you want to create your snapshot
12. 

#### Restore a Snapshot

A few things to note:

* WVDAdmin gave me errors, stating that the "Recovering snapshot was not successful", however, this occurred after the Swapping disk process when the old disk was attempting to be deleted. The recovery did in fact reoccur, I then successfully deleted the disks in the Azure Portal manually.
* I also had the: _"Virtual machine agent status is not ready."_ error occur, this self-resolved after the Virtual Machine had enough time to start the Azure agent.

### 