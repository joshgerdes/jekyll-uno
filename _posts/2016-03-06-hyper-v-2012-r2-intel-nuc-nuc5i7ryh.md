---
id: 3672
title: Hyper-V 2012 R2 on an Intel NUC (NUC5i7RYH)
date: 2016-03-06T12:05:00+00:00
author: Luke
layout: post
guid: http://luke.geek.nz/?p=3672
permalink: /misc/hyper-v-2012-r2-intel-nuc-nuc5i7ryh/
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
post_views_count:
  - "1123"
dsq_thread_id:
  - "4791684490"
categories:
  - Misc
  - Windows
---
One of the problems with Hyper-V 2012 R2 on an Intel NUC &#8211; NUC5i7RYH was because of the &#8216;Client&#8217; network card chipset. Windows Server 2012 would not install the Ethernet Adapter for the Server operating system.

Once I made the manual adjustments to the Network drivers to get this going, I then slipstreamed the drivers and Server 2012 R2 updates (as of Feb 2016) into a Hyper-V 2012 R2 ISO which can then be made bootable for future Hyper-V installations.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Changing_the_Intel_Network_Drivers_Manually"><span class="toc_number toc_depth_1">1</span> Changing the Intel Network Drivers Manually</a>
    </li>
    <li>
      <a href="#Downloading_Intel_Network_Drivers_8211_NUC5i7RYH_Compatible"><span class="toc_number toc_depth_1">2</span> Downloading Intel Network Drivers &#8211; NUC5i7RYH Compatible</a>
    </li>
    <li>
      <a href="#Intel_NUC5i7RYH_Hyper-V_2012_R2_ISO"><span class="toc_number toc_depth_1">3</span> Intel NUC5i7RYH Hyper-V 2012 R2 ISO</a>
    </li>
  </ul>
</div>

## <span id="Changing_the_Intel_Network_Drivers_Manually">Changing the Intel Network Drivers Manually</span>

7-Zip or WinRAR will be needed to extract the EXE to a folder location. In these examples, I am using 7-Zip.

  * Download the Intel x64 Network Drivers here: <a href="https://downloadcenter.intel.com/download/23071/Network-Adapter-Driver-for-Windows-8-1-" target="_blank">https://downloadcenter.intel.com/download/23071/Network-Adapter-Driver-for-Windows-8-1-</a>
  
    _(20.7 Date: 2/11/2016)_
  * Once downloaded. Right click the &#8216;PROWinx64.exe&#8217; and select 7-Zip and Extract to &#8220;PROWinx64\&#8221; this will extract the driver executable to a folder

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R1.png?w=1500" alt="" data-recalc-dims="1" />

  * Once extracted navigate to: \PROWinx64\PRO1000\Winx64\NDIS64Find &#8216;e1d64x64.INF&#8217; and right click and select Open to open with Notepad
  * Find the Heading &#8216;[Intel.NTamd64.6.3.1]&#8217; and copy the devices in this section

<!--more-->

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R2.png?w=1500" alt="" data-recalc-dims="1" />

  * Navigate to the Heading &#8216;[Intel.NTamd64.6.3]&#8217; and paste underneath the Devices (for example – underneath: PCI\VEN\8086&DEV\_15B7&SUBSYS\_00011179 – the last line):

&nbsp;

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R3.png?w=1500" alt="" data-recalc-dims="1" />

  * So it looks like the below with the devices from the top copied onto the bottom. You may have some duplicate Device IDs on the bottom section, you can remove these if you want to. I left mine in there. Once confirmed, save the file: e1d64x64.INF.

&nbsp;

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R4.png?w=1500" alt="" data-recalc-dims="1" />

  * Once completed, copy the: NDIS64 folder to a USB flash drive and plug it into one of the Intel NUCs Flash drive slots.
  * Open the command prompt and type the following commands to allow unsigned/driver testing drivers:

<pre class="lang:default decode:true">bcdedit /set LOADOPTIONS DISABLE_INTEGRITY_CHECKS
bcdedit /set TESTSIGNING ON
bcdedit /set nointegritychecks ON</pre>

  * Once ran, restart the NUC.
  * Once restarted and logged in navigate back to the Command Prompt again and navigate to your USB Flash drive – time to install the drivers.
  * Type in the below and press Enter:

<pre class="lang:default decode:true ">pnputil -i -a e1d64x64.inf</pre>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R5.png?w=1500" alt="" data-recalc-dims="1" />

  * Wait a minute while it installs the driver. Once you have the Windows Security Dialog &#8220;Windows can&#8217;t verify the publisher of this driver software&#8221; select &#8220;Install this software anyway&#8221;
  * Once installed. Restart your Hyper-V server the Network Adapter should now be installed.
  * You can then disable the unsigned/driver testing drivers if needed in the Command Prompt window:

<pre class="lang:default decode:true ">bcdedit /set LOADOPTIONS ENABLE_INTEGRITY_CHECKS
bcdedit /set TESTSIGNING OFF
bcdedit /set nointegritychecks OFF</pre>

  * Back at the Server Configuration window _(type sconfig in the Command Prompt if missing it)_ you can now select 8 to configure your Network settings, remember to specify the Computer Name an add it to a Domain if needed.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R6.png?w=1500" alt="" data-recalc-dims="1" />

References: Thanks to an article written by Jay &#8220;<a href="http://jayrbarrios.com/2014/11/19/intel-nuc-d54250wykh-installing-lan-driver-on-windows-hyper-v-server-2012-r2" target="_blank">Intel NUC D54250WYKH: Installing LAN Driver on Windows Hyper-V Server 2012 R2</a>&#8221; for a lot of assistance in getting this going, was able to easily adapt it for the NUC5i7RYH.

## <span id="Downloading_Intel_Network_Drivers_8211_NUC5i7RYH_Compatible">Downloading Intel Network Drivers &#8211; NUC5i7RYH Compatible</span>

I have bundled the tweaked driver packed I used into a ZIP file – You can download it here: <a href="https://mega.nz/#!5ZtQUTqZ!iKWih9idK-jil6dT4Q7C_D16N5MQiCF9vr6qws6CmFc" target="_blank">Intel_NUC_2012R2_NUC5i7RYH_Drivers.zip</a>
  
_(20.7 Date: 2/11/2016_). This will take you to Step 8 of the guide above. This driver pack should also be able to be used in a normal Windows Server 2012 R2 x64 environment.

## <span id="Intel_NUC5i7RYH_Hyper-V_2012_R2_ISO">Intel NUC5i7RYH Hyper-V 2012 R2 ISO</span>

As mentioned earlier. I have created an ISO _(which I then used to create my Hyper-V server on my NUC)_ which I have added the recommended _(excluding .Net)_ Windows Updates _(as of Feb 2016)_ and added the Intel NUC drivers too. This allowed me to easily rebuild my Hyper-V server on the Intel NUC NUC5i7RYH a few times during testing, minimizing the need to do the Network drivers manually and reduced the amount of Windows Updates I had to install.

The ISO I used as a source was Hyper-V Core RTM _(9600.16384.WINBLUE\_RTM.130821-1623\_X64FRE\_SERVERHYPERCORE\_EN-US-IRM\_SHV\_X64FRE\_EN-US\_DV5)_ downloaded directly from Microsoft.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R7.png?w=1500" alt="" data-recalc-dims="1" />

I then used a WSUS server to download the 2012 R2 updates and slipstreamed them into the Retail ISO. Then I added the NUC Intel Drivers.

Other than the above: 2012 R2 Updates, Intel Ethernet Drivers for the Intel NUC and enabling the .Net 3.5 feature this is untouched.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R8.png?w=1500" alt="" data-recalc-dims="1" />

This can be downloaded here: <a href="https://mega.nz/#!wclQwJKB!l6pM0XU5sv63mgSu7rYaPIHvQRYfXaMDvzBBJCVX9Gw" target="_blank">SERVERHYPERVCORE_EN-US-NUC_NUCi57RYH_Feb2016.ISO</a>

_README
  
_ 

_&#8212;&#8212;&#8212;&#8212;
  
_ 

_This Hyper-V Core DVD ISO was created by: Luke Murray (Luke.Geek.NZ) on the: 05/03/16
  
_ 

_The following adjustments have been made (no other adjustments have been made and should be RTM)
  
_ 

_This 2012 R2 server core ISO has the latest Windows Updates slipstreamed (except .net updates) to: Feb 2016.
  
_ 

_This 2012 server core also has the following Intel drivers for the Intel NUC system:
  
_ 

_Note: Please note Intel does not fully support Windows Server 2012 R2 on the NUC5i7RYH due to using a client Network chipset.
  
_ 

_The Network driver&#8217;s configurations had to be tweaked to allow installation.
  
_ 

_Intel(R) Network Drivers 20.7 (January 21, 2016)
  
_ 

_Intel® 82599EB 10 Gigabit Ethernet Controller
  
_ 

_Intel® 82580EB Gigabit Ethernet Controller
  
_ 

_Intel® Ethernet Server Adapter I340-F4
  
_ 

_Intel® Ethernet Converged Network Adapter X520-SR1
  
_ 

_Intel® Ethernet Converged Network Adapter X520-DA2
  
_ 

_Intel® Ethernet Controller I350-BT2
  
_ 

_Intel® Ethernet Controller I350-AM2
  
_ 

_Intel® Ethernet Controller I350-AM4
  
_ 

_Intel® Ethernet Controller I210-IT
  
_ 

_Intel® Ethernet Converged Network Adapter X540-T2
  
_ 

_Intel® Ethernet Server Adapter I350-F2
  
_ 

_Intel® Ethernet Server Adapter I350-F4
  
_ 

_Intel® Ethernet Controller X540-AT2
  
_ 

_Intel® Ethernet Connection I217-V
  
_ 

_Intel® Ethernet Connection I218-V
  
_ 

_Intel® Ethernet Connection I218-LM
  
_ 

_Intel® Ethernet Controller I210-AT
  
_ 

_Intel® Ethernet Controller I210-IS
  
_ 

_Intel® Ethernet Converged Network Adapter X520-DA4
  
_ 

_Intel® Ethernet Converged Network Adapter X520-QDA1
  
_ 

_Intel® Ethernet Converged Network Adapter X520-LR1
  
_ 

_Intel® 82599ES 10 Gigabit Ethernet Controller
  
_ 

_Intel® 82579LM Gigabit Ethernet PHY
  
_ 

_Intel® Ethernet Server Adapter I340-T4
  
_ 

_Intel® Ethernet Server Adapter I350-T2
  
_ 

_Intel® Ethernet Server Adapter I350-T4
  
_ 

_Intel® Ethernet Connection I217-LM
  
_ 

_Intel® Ethernet Converged Network Adapter X520-T2
  
_ 

_Intel® Ethernet Converged Network Adapter X520-SR2
  
_ 

_Intel® 82579V Gigabit Ethernet PHY
  
_ 

_Intel® Ethernet Converged Network Adapter X540-T1
  
_ 

_Intel® Ethernet Controller I211-AT
  
_ 

_Intel® 82599EN 10 Gigabit Ethernet Controller
  
_ 

_Intel® Ethernet Converged Network Adapter X520-DA1
  
_ 

_Intel® Ethernet Controller I210-AS
  
_ 

_Intel® Ethernet Controller I210-CS
  
_ 

_Note: I take no liability for loss or damage following these guides or using my driver pack or ISO. This is merely intended to help people
  
_ 

I recommend using <a href="https://rufus.akeo.ie/" target="_blank">Rufus</a> to load the ISO to a USB flash drive using the settings below:

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/03/030516_2351_HyperV2012R9.jpg?w=1500" alt="" data-recalc-dims="1" />

Once completed, put the USB drive into the NUC and restart. On startup press F10 to navigate to the Boot Menu and select the USB drive.