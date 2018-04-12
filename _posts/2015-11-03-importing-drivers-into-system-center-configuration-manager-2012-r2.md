---
id: 3639
title: Importing drivers into System Center Configuration Manager 2012 R2
date: 2015-11-03T16:04:17+00:00
author: Luke
layout: post
guid: http://luke.geek.nz/?p=3639
permalink: /win/importing-drivers-into-system-center-configuration-manager-2012-r2/
post_views_count:
  - "1667"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4790528426"
categories:
  - Windows
---
Importing drivers into System Center Configuration Manager R2 _(SCCM)_ is a task I do at least once a month as new models are introduced into my work environment.

In this guide I am going to guide you through a step by step method of exporting drivers from an already existing build _(ie vendor supplied, OEM)_ or from a driver package supplied for operating system deployment purposes from a vendor, such as Hewlett Packard.

<!--more-->

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#How_can_I_extract_the_drivers_from_an_already_existing_Operating_System"><span class="toc_number toc_depth_1">1</span> How can I extract the drivers from an already existing Operating System?</a>
    </li>
    <li>
      <a href="#Where_can_I_find_driver_packages_for_new_builds_for_System_Center_Configuration_Manager"><span class="toc_number toc_depth_1">2</span> Where can I find driver packages for new builds for System Center Configuration Manager?</a><ul>
        <li>
          <a href="#Hewlett_Packard"><span class="toc_number toc_depth_2">2.1</span> Hewlett Packard</a>
        </li>
        <li>
          <a href="#Lenovo"><span class="toc_number toc_depth_2">2.2</span> Lenovo</a>
        </li>
        <li>
          <a href="#Microsoft"><span class="toc_number toc_depth_2">2.3</span> Microsoft</a>
        </li>
        <li>
          <a href="#Dell"><span class="toc_number toc_depth_2">2.4</span> Dell</a>
        </li>
      </ul>
    </li>
    
    <li>
      <a href="#How_can_I_import_drivers_into_System_Center_Configuration_Manager"><span class="toc_number toc_depth_1">3</span> How can I import drivers into System Center Configuration Manager?</a>
    </li>
    <li>
      <a href="#How_can_I_add_a_driver_pack_into_the_task_sequence_for_Operating_System_Deployment"><span class="toc_number toc_depth_1">4</span> How can I add a driver pack into the task sequence for Operating System Deployment?</a>
    </li>
  </ul>
</div>

# <span id="How_can_I_extract_the_drivers_from_an_already_existing_Operating_System">How can I extract the drivers from an already existing Operating System?</span>

  1. Download and install <a href="http://www.majorgeeks.com/files/details/double_driver.html" target="_blank">Double Driver</a>
  
    _(this is freeware)_on the workstation you would like to extract the drivers from
  2. Run Double Driver

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr2.png?w=1500" alt="" data-recalc-dims="1" />

  1. Select Backup
  2. Select Scan Current System

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr3.png?w=1500" alt="" data-recalc-dims="1" />

  1. Double Driver will then go through and scan the OS for drivers. It will automatically de-select all Microsoft drivers and only select those drivers that are not Microsoft signed. This is useful to avoid differences in MS supplied drivers compared to those that will install that are on the WIM and to avoid bloat on your driverstore.
  2. Select Backup Now

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr5.png?w=1500" alt="" data-recalc-dims="1" />

  1. Select the destination you would like to back up the folder too. In my case I usually extract to a USB device (ie e:\drivers\) as long as Structured Folder is selected _(as is Default)_ Double Driver will export the drivers into suitability labelled folders – ie a folder for Bluetooth for the Bluetooth drivers.
  2. This will then start the driver back-up which depending on your configuration _(amount and size of drivers)_ may take 5-10 minutes to complete.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr6.png?w=1500" alt="" data-recalc-dims="1" />

  1. Once completed. You have now extracted the drivers from your Windows workstation which can now be imported into a driver package in System Center Configuration Manager.

# <span id="Where_can_I_find_driver_packages_for_new_builds_for_System_Center_Configuration_Manager">Where can I find driver packages for new builds for System Center Configuration Manager?</span>

There are times when you won&#8217;t be using an already existing workstation as a base for drivers. Depending on the hardware manufacturers you are able to download a driver package directly from the vendor which can then be imported into configuration manager. Below is a list of manufacturer supplied MDT/SCCM driver packages:

## <span id="Hewlett_Packard">Hewlett Packard</span>

  * Windows 64 bit Driver Packs &#8211; [http://ftp.hp.com/pub/caps-softpaq/cmit/HP\_Driverpack\_Matrix_x64.html](http://ftp.hp.com/pub/caps-softpaq/cmit/HP_Driverpack_Matrix_x64.html)
  * Windows 32 bit Driver Packs &#8211; [http://ftp.hp.com/pub/caps-softpaq/cmit/HP\_Driverpack\_Matrix_x86.html](http://ftp.hp.com/pub/caps-softpaq/cmit/HP_Driverpack_Matrix_x86.html)
  * HP WinPE Driver Packs &#8211; [http://ftp.hp.com/pub/caps-softpaq/cmit/HP\_WinPE\_DriverPack.html](http://ftp.hp.com/pub/caps-softpaq/cmit/HP_WinPE_DriverPack.html)

## <span id="Lenovo">Lenovo</span>

  * Windows 64 & 32bit drivers _(inc WinPE)_ &#8211; <https://support.lenovo.com/us/en/documents/sccm-index>

## <span id="Microsoft">Microsoft</span>

  * Surface Pro 3 Driver Packs &#8211; <https://www.microsoft.com/en-nz/download/details.aspx?id=38826>
  * Surface 3 Driver Packs &#8211; <https://www.microsoft.com/en-us/download/details.aspx?id=49040>
  * Surface Pro 4 Win 10 Driver Packs &#8211; <https://www.microsoft.com/en-us/download/details.aspx?id=49498>
  * Surface Book Win 10 Driver Packs &#8211; <https://www.microsoft.com/en-us/download/details.aspx?id=49497>

## <span id="Dell">Dell</span>

  * Windows Driver Packs &#8211; <http://en.community.dell.com/techcenter/enterprise-client/w/wiki/2065.dell-command-deploy-driver-packs-for-enterprise-client-os-deployment>

# <span id="How_can_I_import_drivers_into_System_Center_Configuration_Manager">How can I import drivers into System Center Configuration Manager?</span>

Before opening the SCCM console – I would recommend copying the drivers you have either downloaded from the vendor or extracted from the workstation into the drivers source folder on your configuration manager server. You can then use the UNC path to quickly add the drivers in.

For example – my driver folder structure is as follows:

\\SERVERNAME\sources$\Drivers\Microsoft

Underneath that folder structure I have the following folders & underneath that is another folder for the specific Model:

  * _DriverPackages
  
_ 
  * _Drivers
  
_ 
  * _Sources
  
_ 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr7.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    Open SCCM <em>(Configuration Manager 2012 R2)</em>
  </li>
</ol>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr8.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    Navigate to Software Library
  </li>
  <li>
    Expand Operating Systems
  </li>
  <li>
    Right click Driver Packages
  </li>
  <li>
    Select Create Driver Package
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr9.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    The Driver Package creation Wizard will open. Give the Driver Package a name – for example &#8220;Microsoft Surface Pro 3 x64&#8221; and add the UNC path for the driver package folder <em>(this has to be empty)</em> and click Ok
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr10.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    Once completed – you have created the driver package but now you need to import the drivers to add into the driver package. Navigate to: Software Library, Operating Systems, Drivers
  </li>
  <li>
    Right click Drivers and select Import Driver
  </li>
</ol>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr11.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    You now point the Import New Driver wizard to the location you previously uploaded your drivers to – drivers source folder using a UNC path and click Next.
  </li>
</ol>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr12.png?w=1500" alt="" data-recalc-dims="1" />

<ol style="margin-left: 39pt;">
  <li>
    SCCM will then verify the path and list the drivers you would like to import. Verify the information is correct and if needed specific a Category and click Next
  </li>
  <li>
    Select the Driver package you created to add the drivers into and select Next
  </li>
  <li>
    In the terms of this example – we are skipping adding the drivers to the boot image but if you do have a Network or Storage driver to add to your boot image you can add it here (make sure you tick <em>Update distrubution points when finished </em>option), click Next
  </li>
  <li>
    Verify the summary is correct and click Next to start the import process. This will then import the drivers into the Configuration Manager Driver database and assign them to the specified driver package.
  </li>
  <li>
    Once completed – navigate to: Software Library, Operating Systems, Driver Packages and find your package. Right click and Distribute Content – select your Distribution points to deploy the package too and you are done!
  </li>
</ol>

# <span id="How_can_I_add_a_driver_pack_into_the_task_sequence_for_Operating_System_Deployment">How can I add a driver pack into the task sequence for Operating System Deployment?</span>

Once you have your driver pack added and distributed you want to add it to your operating system task sequence for use.

  1. Navigate to: Software Library, Operating Systems, Task Sequences and find your OS task sequence right click it and select Edit
  2. Find the section in the Task Sequence you want to add the drivers to. Select Add and Apply Driver Package

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr14.png?w=1500" alt="" data-recalc-dims="1" />

  1. Select Browse… next to Driver Package and find and locate your driver package and Add.
  2. Once Added specify an appropriate name and comment.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr15.png?w=1500" alt="" data-recalc-dims="1" />

  1. Click the Options tab up the top
  2. Click Add Condition and select Any Condition and click Ok
  3. WQL _(WMI queries)_ allow you separate models allows you to specify differnet driver packages to different models in Configuration Manager (SCCM). Even if it is a task sequence for only one device I usually do a WMI query to avoid any mishap in the future and easily allows for additional growth of devices. Once the &#8220;Any Condition&#8221; has been specified as per the last step.. Click Add Condition again and select: Query WMI.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr17.png?w=1500" alt="" data-recalc-dims="1" />

  1. Add the follow WMI query in – Be aware of any syntax which may be incorrect from copying from the internet (such as &#8220;) and in the %% instead of – Surface Pro 3 replace with your model:

SELECT * FROM Win32_ComputerSystem WHERE Model Like &#8220;%**Surface Pro 3**%&#8221;

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr18.png?w=1500" alt="" data-recalc-dims="1" />

Note: In order to find the model, you can run: &#8220;**wmic csproduct get name**&#8221; from a command prompt on a machine that you are about to build and use that output to put in the query.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/11/110315_0403_Importingdr19.png?w=1500" alt="" data-recalc-dims="1" />

Or you may have to do some googling or binging to get the correct WMI queries. You can also do it by manufacturer such as:

SELECT * FROM Win32_ComputerSystem WHERE Manufacturer LIKE &#8220;%**Dell**%&#8221;

  1. Once you have done that click Apply and save your TS changes. You have now imported the driver package into your SCCM task sequence ready for deployment!