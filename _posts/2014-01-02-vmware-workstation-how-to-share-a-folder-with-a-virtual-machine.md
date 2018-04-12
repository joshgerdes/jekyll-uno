---
id: 2936
title: VMWare Workstation – How to share a folder with a virtual machine
date: 2014-01-02T10:00:43+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2936
permalink: /win/vmware-workstation-how-to-share-a-folder-with-a-virtual-machine/
dsq_thread_id:
  - "4987904447"
mfn-post-love:
  - "0"
post_views_count:
  - "14"
categories:
  - Windows
---
  1. First up – you need to create a folder on the host machine. For this example we are using a folder on the Desktop. 
  2. Right click a blank space on the Desktop and select – New, Folder. 
  3. Name it: vmshared and press Enter 
  4. 
  5. This will be our base folder – anything we put in here will be shared with the virtual machines. 
  6. Open VMWare Workstation 
  7. Right click the Virtual Machine you are using and select Settings 
  8. 
  9. Click on the Options tab and navigate to – Shared Folders 
 10. Here you can choose to have it Always Enabled or Enabled until next power off or suspend – I will select Always Enabled. 
 11. Check Map as a network drive in Windows Guests 
 12. Down the bottom select Add 
 13. This Wizard will guide you through to navigating to the hosts path – the location of the folder you created earlier – ie Deskop/vmshared 
 14. You can specify an alternative name if you want or just select Next 
 15. You can specify to have the share Read Only here if you want, make sure Enable this Share is selected and select Finish 
 16. 
 17. Done – as soon you as press Ok your virtual machine would have mapped a network share to your workstation. You can find this under My Computer or Computer! 

 

_Note: You can map the same network share between multiple Virtual Machines.
  
_ 

_Note: The Virtual machine must be on to allow Shared Folder configuration – if it is off the option will simply not be enabled._