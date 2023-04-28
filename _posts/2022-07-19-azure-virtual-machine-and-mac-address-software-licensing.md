---
date: '2022-07-19 00:00:00 +1200'
title: Azure Virtual Machine and a custom MAC address
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: images/iazure-marketplace-banner.png
_template: new_post
---

You may need an Azure Virtual Machine to install or license software bound to a media access control address _(MAC address)_.

In Microsoft Azure, you can make changes to the Primary Network interface; these changes include manually setting the IP settings to changing the MAC address - these settings are managed by the underlying Network Interface and Azure host.

> _If you do inadvertently make changes to this, you will lose connection to the Azure Virtual Machine, however, don't panic! Until its rebooted and the configuration is reset by the Azure fabric._

This causes issues when the software is licensed to a specific MAC address; you could reissue the license to the new MAC address OR create a Secondary Interface in Microsoft Azure and update the MAC address on the secondary network interface.

You can easily [create a new Network Interface](https://learn.microsoft.com/en-us/azure/virtual-network/network-overview?WT.mc_id=AZ-MVP-5004796#network-interfaces "Network interfaces"){:target="_blank"} from the Azure Portal and then attach it to the Virtual Machine (_the virtual machine needs to be off to allow the NIC to be attached)_.

##### Change Network Adapter MAC using PowerShell

Once the NIC is created and attached, run the following PowerShell command in the Azure Virtual Virtual machine _(assuming this is a Windows OS, but the same process should work for_ [_Linux_](https://www.linuxshelltips.com/change-mac-address-linux/ "How to Change Network MAC Address in Linux"){:target="_blank"}_)_:

    Get-NetAdapter

You want to make sure you are targeting the right Network Adapter; in my example, it is the Hyper-V Interface #2 _(with #1 being my Primary NIC)_.

Add the new MAC address into the $MACAddress variable, and make sure you update the InterfaceDescription to match the Network Adapter you are targeting _(note the wildcard before the #2, this targets any network adapter with #2 at the end)_.

    $MACAddress = '000000000000'
    $NetAdapter = Get-NetAdapter -InterfaceDescription "*#2"
    Set-NetAdapter $NetAdapter.Name -MacAddress $MACAddress

##### Change Network Adapter MAC using Device Manager

You can also use Device Manager to check and update the MAC address:

1. Open the Device Manager.
2. Expand the Network Adapters section.
3. Right-click on your adapter.
4. Click the Advanced tab.
5. Enter your new MAC address.
6. Reboot your computer to enable the changes.
7. Check that the changes took effect.

> Finally - make sure you document this MAC address somewhere with the reasons WHY the change was made. You can also Tag the secondary MAC address in Azure with notes, such as the reason why it exists, who created it etc.
