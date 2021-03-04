---
title: VMWare Workstation – How to share a folder with a virtual machine
date: 2014-01-02 00:00:00 +13:00
permalink: "/win/vmware-workstation-how-to-share-a-folder-with-a-virtual-machine/"
categories:
- Windows
---

  1. First up – you need to create a folder on the host machine. For this example we are using a folder on the Desktop. 
  2. Right click a blank space on the Desktop and select – New, Folder. 
  3. Name it: vmshared and press Enter 
  4. This will be our base folder – anything we put in here will be shared with the virtual machines. 
  5. Open VMWare Workstation 
  6. Right click the Virtual Machine you are using and select Settings 
  7. Click on the Options tab and navigate to – Shared Folders 
 8. Here you can choose to have it Always Enabled or Enabled until next power off or suspend – I will select Always Enabled. 
 9. Check Map as a network drive in Windows Guests 
 10. Down the bottom select Add 
 11. This Wizard will guide you through to navigating to the hosts path – the location of the folder you created earlier – ie Deskop/vmshared 
 12. You can specify an alternative name if you want or just select Next 
 13. You can specify to have the share Read Only here if you want, make sure Enable this Share is selected and select Finish 
 14. Done – as soon you as press Ok your virtual machine would have mapped a network share to your workstation. You can find this under My Computer or Computer! 

Note: You can map the same network share between multiple Virtual Machines.
Note: The Virtual machine must be on to allow Shared Folder configuration – if it is off the option will simply not be enabled.
