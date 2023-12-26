---
title: Guide to using Hyper-V
image: /wp-content/uploads/2014/02/Hyper-V-logo.png
categories:
  - Windows
date: 2014-02-23 00:00:00 +1300
---

### Introduction to Hyper-V

Hyper-V is an emulation/hyper-visor Microsoft developed technology – similar to VMWare Workstation or ESXI that allows you to run Virtual Machines and different workloads simultaneously. Hyper-V is currently available in Windows 8, Windows Server 2008, Windows Server 2008 R2, Windows 8.1 & Windows Server 2012, Windows Server 2012 R2. The Hyper-V hypervisor allows multiple workloads to run on the same physical hardware that in the past would have otherwise only been suitable for one workload – allowing for power and resource efficiency.

### Hyper-V Specifications

**Host operating system:**

To install the Hyper-V role, Windows Server 2008, Windows Server 2008 R2 Standard, Enterprise or Datacentre edition, Windows Server 2012 Standard or Datacentre edition, or Windows 8 (or 8.1) Pro or Enterprise edition is required. Hyper-V is only supported on x86-64 variants of Windows. It can be installed regardless of whether the installation is a full or core installation. **Processor: **An x86-64 processor

Hardware-assisted virtualization support: This is available in processors that include a virtualization option; specifically, Intel VT or AMD Virtualization (AMD-V, formerly code-named &#8220;Pacifica&#8221;).

A NX bit-compatible CPU must be available and Hardware Data Execution Prevention (DEP) must be enabled.

Although this is not an official requirement, Windows Server 2008 R2 and a CPU with second-level address translation support are recommended for workstations.

Second-level address translation is a mandatory requirement for Hyper-V in Windows 8

**Memory**

Minimum 2 GB. (Each virtual machine requires its own memory, and so realistically much more.)

Windows Server 2008 Standard (x64) Hyper-V full GUI or Core supports up to 31 GB of memory for running VMs, plus 1 GB for the Hyper-V parent OS.]

Maximum total memory per system for Windows Server 2008 R2 hosts: 32 GB (Standard) or 2 TB (Enterprise, Datacentre)

Maximum total memory per system for Windows Server 2012 hosts: 4 TB

### Guest operating systems

Hyper-V in Windows Server 2008 and 2008 R2 supports virtual machines with up to 4 processors each (1, 2, or 4 processors depending on guest OS-see below)

Hyper-V in Windows Server 2012 supports virtual machines with up to 64 processors each.

Hyper-V in Windows Server 2008 and 2008 R2 supports up to 384 VMs per system.

Hyper-V in Windows Server 2012 supports up to 1024 active virtual machines per system.

Hyper-V supports both 32-bit (x86) and 64-bit (x64) guest VMs.

#### Improvements of Hyper-V in Windows Server 2012

Hyper-V Extensible Virtual Switch

Network virtualization

Multi-tenancy

Storage Resource Pools

.vhdx disk format supporting virtual hard disks as large as 64 TB with power failure resiliency

Virtual Fibre Channel

Offloaded data transfer

Hyper-V replica

Cross-premise connectivity

Cloud backup

#### Installing Hyper-V in Windows 8 & Windows 8.1

  1. Navigate to **Control Panel** & select **Uninstall a Program** underneath programs
  2. Select **Turn Windows Features On or Off**
  3. Check **Hyper-V & Hyper-V Platform** and select additional relevant features – I would HIGHLY recommend Hyper-V GUI Management Tools.
  4. Windows will go through and install the Hyper-V modules onto the Windows 8 workstation. Once completed the workstation will need a restart and you will be able to now fully utilise Hyper-V!

#### Installing Hyper-V for Windows Server 2012

  1. Open **Server Manager**
  2. Click **Add Roles and Features** and click **Next**
  3. Select **Hyper-V Role** and click **Next**
  4. Select the appropriate NIC (network interface card) for live migration and select **Next**
  5. Select the default locations for your VHD (virtual hard disks) and VM (virtual machine) configuration files to be held and select **Next**
  6. Once the Hyper-V role has been fully installed – restart the Windows Server 2012 machine. You should now have access to the Hyper-V Manager.

### Hyper-V Tips and Tricks

#### How to stop and restart the Hyper-V service

  1. Open **Hyper-V Manager**
  2. Select the relevant Hyper-V server
  3. Select Stop Service

#### How to create a new Virtual Machine in Hyper-V

  1. Open **Hyper-V Manager**
  2. Select **New** and **Virtual Machine**
  3. The before you Begin Wizard will now appear – click **Next**
  4. Choose a name for your Virtual Machine and verify the storage location is for the virtual machine is appropriate and click **Next**
  5. Here you can select the &#8220;generation&#8221; of the Virtual Machine.
  6. **Generation 1** – These are for 32bit legacy based systems usually used for Windows 7 and Windows XP/Linux virtual machines.
  7. **Generation 2** – These are for Windows Server 2012 or 64bit versions of Windows 8
  8. <em style="font-family: sans-serif; font-size: medium;">NOTE: Once Virtual Machine generation has been selected – YOU CANNOT change it.</em>
  9. <em style="font-family: sans-serif; font-size: medium;">NOTE: Using </em>Convert-VMGeneration <em style="font-family: sans-serif; font-size: medium;">script you can convert a Generation 1 VM to Generation 2.</em>
 10. You can now **select** the **RAM** amount you would like to delegate to your Virtual Machine and select **Next**
 11. If you have VLAN setup you can set your Virtual Machine to use the connection – I don&#8217;t so I am just going to click **Next**
 12. Now you can specify the appropriate VHD (Virtual Hard Disk) for the Virtual Machine to use – you can either create a new one or use an existing VHD.
 13. This is where you **specify** the **path** to your installation media for your virtual machine – such as an OS (operating system) ISO.
 14. You have finally setup your new Virtual Machine! Verify all the settings are correct and click **Finish** to configure and generate your new Virtual Machines.
 15. You can now **right click** on your **Virtual Machine** under the Hyper-V Manager and **select Connect…** to **start** it.
