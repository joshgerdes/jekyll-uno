---
id: 3275
title: Accessing the Ricoh printer maintenance shell
date: 2014-04-27T20:47:48+00:00
author: Luke
layout: post
guid: http://localhost/techremedy/?p=3275
permalink: /misc/how-to-access-the-ricoh-printer-maintenance-shell/
slide_template:
  - default
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4794531676"
mfn-post-love:
  - "0"
post_views_count:
  - "466"
categories:
  - Misc
---
Most Ricoh network capable printers include a Telnet server that is used by Ricoh for maintenance of their printers allowing you to access the Ricoh Printer maintenance shell. Using telnet or in my guide – I am using the third party tool pUTTY _(as in my domain environment – telnet hasn’t been installed on most workstations)_ you can access the Maintenance Shell.

&nbsp;

  1. Download and run [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
  2. **Open** **PuTTY** and choose **Telnet** under Connection Type.
  3. **Type** **in** the IP **address** or hostname in the Host Name (or IP address field).
  4. Click **Open**.
  5. This will then start the RICOH Maintenance Shell – type in the login name _(default is using admin as the username – and a blank password)._
  6. You will be greeted with the maintenance shell.