---
date: 2021-12-13 00:00:00 +1300
title: Capturing Virtual Machine images and Snapshots in Azure using WVDAdmin
author: Luke
categories:
- Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png
---
[WVDAdmin](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/ "WVDAdmin"){:target="_blank"} - is a native administration GUI (graphical user interface) for Azure Virtual Desktop (AVD). WVDAdmin is a free custom-built tool designed to make managing and standing up Azure Virtual Desktop infrastructure easy. Not only can you use it to roll out your Azure Virtual Desktop infrastructure and manage existing workspaces and host pools - you can use it to create Virtual Machine images that can be used for Virtual Scale Sets, but Base also builds or Azure Virtual Desktop session hosts! In addition, WVDAdmin automates creating and using snapshots and virtual machine images in a simple point and click interface - that works!

### Prerequisites

* Azure subscription
* Resource Group
* Virtual Machine _(to be used as your master image)_
* Of course - WVDAdmin

You can download WVDAdmin from the following page:  [Azure Windows Virtual Desktop administration with WVDAdmin](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/ " Azure Windows Virtual Desktop administration with WVDAdmin"){:target="_blank"}.

Also, make sure you have set up a [service principal ](https://blog.itprocloud.de/Windows-Virtual-Desktop-Admin/#service-principal-functional-account "Service principal (functional account) Link"){:target="_blank"} with the appropriate rights to the Resource Groups that holds your Virtual Machine.

Before proceeding ahead, **_make sure you have a virtual machine backup!_**

### Capturing a Snapshot

Although, possible to do using the Azure Portal, quickly taking an OS disk snapshot and then reverting the change can be a bit tedious, especially if you want to make a backup quickly of the operating system disk before patching or application upgrade, Snapshots are a lot quicker to take and work well for immediate and temporary recovery, especially when you want to quickly try something out - without having to wait for an Azure Backup. Please note this tool does not snapshot any data drives present.

#### Capture a Snapshot

 1. Open **WVDAdmin**
 2. On the "Welcome" tab, **enter** in your Azure **Tenant id**
 3. **Enter** in your **Service principal (application) ID** and **key**
 4. Click on **Reload all** - to connect to Azure
 5. **Expand Azure**
 6. **Expand Virtual Machines**
 7. **Expand** your **Resource group**; in my example; it is: SERVERS-RG
 8. **Right-click** your **server**; in my example, it is: Server2019
 9. Select **SnapShot-Create**
10. ![WVDAdmin - Create Snapshot](/uploads/snapshot-create.png "WVDAdmin - Create Snapshot")
11. WVDAdmin will then prompt you to verify that you want to create your Snapshot.
12. ![WVD - Verify Snapshot](/uploads/snapshot-create_verify.png "WVD - Verify Snapshot")
13. Confirm the server is correct and click **Ok**
14. Depending on the size of your disk, this process may only take a few seconds; the virtual Machine may experience a slight performance hit. Still, I did not lose RDP connectivity during the snapshot process in my testing.
15. Review the logs to make sure that the Snapshot has been created successfully:
16. ![](/uploads/snapshot-create_verify_log.png)
17. You should now see the Snapshot in the Azure Portal, in the same Resource Group as the server.
18. ![Azure Portal - Snapshot](/uploads/snapshot-azureportal.png "Azure Portal - Snapshot")

#### Restore a Snapshot

Before you proceed, just a warning that restoring the Snapshot will discard any changes made after the Snapshot. The virtual machine will also be deallocated, so it will stop any connections to it.

 1. Open **WVDAdmin**
 2. On the "Welcome" tab, **enter** in your Azure **Tenant id**
 3. **Enter** in your **Service principal (application) ID** and **key**
 4. Click on **Reload all** - to connect to Azure
 5. **Expand Azure**
 6. **Expand Virtual Machines**
 7. **Expand** your **Resource group**; in my example; it is: SERVERS-RG
 8. **Right-click** your **server**; in my example, it is: Server2019
 9. Select **SnapShot-Restore**
10. ![Azure Disk Snapshot](/uploads/snapshot-restore.png "Azure Disk Snapshot")
11. **Select** the **Snapshot** you would like to **restore** to, and when you are ready, click **Ok**. This will force the Virtual Machine to be shut down and deallocated and the Snapshot to be restored.
12. ![Azure Disk Snapshot](/uploads/snapshot-restore_verify.png "Azure Disk Snapshot")
13. You may also start the VM from WVDAdmin, by right-clicking on the Virtual Server after the Snapshot restores and click: Start.
14. ![Azure Disk Snapshot](/uploads/wvdadmin-startvm.png "Azure Disk Snapshot")
15. Verify that your Virtual Machine is back up and running and remove any unneeded snapshots and disks from the Azure Portal, to reduce additional costs. If you intend to keep any around, make sure you add appropriate Tags and a review date so you know what and why they existed in the first place.

A few things to note:

* WVDAdmin gave me errors, stating that the "Recovering snapshot was not successful", however, this occurred after the Swapping disk process when the old disk was attempting to be deleted. The recovery did, in fact, reoccur; I then successfully deleted the disks in the Azure Portal manually.
* I also had the: _"Virtual machine agent status is not ready."_ error occur. After the Virtual Machine had enough time to start the Azure agent, this self-resolved.

### Capturing a Virtual Machine Image

Virtual Machine images work well for Azure Virtual Desktop and Virtual Machines scale sets, where you want consistency between your various virtual machines. The same process I will run through works with Windows 10/11 along with Windows Server 2022 and below _(and I would also imagine Linux workloads)_. 

I will be using the Windows Server 2019 Virtual Machine I had created before, however with various applications that I want to be standard across new builds; in my demo I used chocolatey to install:

* Adobe Reader
* Microsoft Visual C++ runtimes
* 7Zip
* VLC

Then added a custom user policy to set the wallpaper. WVDAdmin will automatically generalise _(sysprep)_ the Machine for you by creating a 'Temp' machine without touching your original Virtual Machine!

#### Capture a Virtual Machine Image

 1. Open **WVDAdmin**
 2. On the "Welcome" tab, **enter** in your Azure **Tenant id**
 3. **Enter** in your **Service principal (application) ID** and **key**
 4. Click on **Reload all** - to connect to Azure
 5. **Expand Azure**
 6. **Expand Virtual Machines**
 7. **Expand** your **Resource group**; in my example, it is: SERVERS-RG
 8. **Right-click** your **server**; in my example, it is: Server2019
 9. Select **Create a template image**
10. ![WVDAdmin - Create a template image](/uploads/vmimage-create.png "WVDAdmin - Create a template image")
11. WVDAdmin will then display the: **Capture Image tab.**
12. Type in an appropriate image name (make sure you understand it, add specific versioning etc.)
13. **Verify** that your Template **VM** is **correct**
14. Select your **Target Resource Group** for your **Image**
15. If you have a custom PowerShell script, you may add additional customisations. Add the script path here (_make sure it's publically accessible by Azure, i.e. Azure storage account, Github repository etc.)_.
16. Before proceeding to the next step, **your VM will be deallocated**
17. When you are ready, select **Capture**
18. WVDAdmin will then deallocate your VM and run through the following process:
19. Deallocate VM -> Create a snapshot of VM ->Create a temporary VM from the snapshot -> Generalise the VM -> deallocate temporary VM -> create the image -> delete temp VM resources
20. ![WVDAdmin - Capture Image](/uploads/vmimage-log.png "WVDAdmin - Capture Image")
21. You should now see your Image in your Azure Portal.
22. ![Azure - Custom Image](/uploads/inkedvmimage-azureportal.jpg "Azure - Custom Image")
23. You can now create additional Virtual Machines from your Custom image using the Azure Portal.
24. WVDAdmin can also copy your Custom Image into a Shared Image Gallery, or you can use it to create an Azure Virtual Desktop session host!
25. ![WVDAdmin - New Session Host](/uploads/wvdadmin_newsessionhost.png "WVDAdmin - New Session Host")

Hopefully, this article has been of some use - even if you don't use Azure Virtual Desktop - WVDAdmin is a great tool to help with day-to-day Azure Virtual Machine operations.