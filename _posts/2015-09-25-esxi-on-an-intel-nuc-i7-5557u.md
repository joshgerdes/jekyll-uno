---
id: 3518
title: ESXi on an Intel NUC NUC5i7RYH
date: 2015-09-25T10:14:17+00:00
author: Luke
layout: post
guid: http://luke.geek.nz/?p=3518
permalink: /misc/esxi-on-an-intel-nuc-i7-5557u/
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
post_views_count:
  - "190"
dsq_thread_id:
  - "4792972106"
categories:
  - Misc
---
I have just configured ESXi on my new Intel NUC &#8211; NUC5i7RYH (Intel NUC i7-5557U 3.1GHz 16GB 256GB SSD).

<img class="wp-image-3519 aligncenter" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo-300x286.png?resize=106%2C101" alt="VMWare ESXi" width="106" height="101" srcset="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?resize=300%2C286&ssl=1 300w, https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?resize=600%2C571&ssl=1 600w, https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?resize=262%2C250&ssl=1 262w, https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?resize=524%2C499&ssl=1 524w, https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?resize=574%2C547&ssl=1 574w, https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/09/vmware-esxi-logo.png?w=630&ssl=1 630w" sizes="(max-width: 106px) 100vw, 106px" data-recalc-dims="1" />

Due to incompatibility with ESXi-Customizer on Windows 10  &#8211; I used the now recommended: ESXi-Customizer-PS Power CLI script.

Following the instructions at the ESXi-Customizer website: <http://www.v-front.de/p/esxi-customizer-ps.html> with installing the VMWare Power CLI PowerShell dependencies onto my workstation _(you need a register My VMWare account to download this directly from VMware)_.

I was able to use the following command from the directory where the PowerShell script was saved:

<pre class="lang:ps decode:true ">.\ESXi-Customizer-PS-v2.4.ps1 -v60 -vft -load sata-xahci,net55-r8168</pre>

This will make the script connect to the V-Front Online Depot and add the sata-xahci and net55-r8168 packages from there to the latest ESXi 6.0 Imageprofile.

Entirely with no user interaction it was able to download the latest v6 ESXi release and slipstream the sata-xahci drivers leaving a clean ISO I was then able to use [Rufus](https://rufus.akeo.ie/) with the default settings to deploy the ISO to my USB Flash drive which was then used to install on the Intel NUC successfully.