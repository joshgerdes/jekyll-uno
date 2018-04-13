---
title: 'Hybserv2 &#8220;Unable to open SET PATH&#8221;'
permalink: /linux/hybserv2-setpath/
categories:
  - Linux
  - Windows
---
Getting the Hybserv2 &#8220;Unable to open SETPATH&#8221; error? Follow the instructions below to repair.

**Windows**

  1. **Right** **click** on My **Computer**
  2. **Left** **click** on **Properties**
  3. Left click on **Advanced** **System** **Settings**
  4. Left click on **Environment** **Variables**.
  5. **Enter** **new** system **variable** with **name** &#8220;**PATH**&#8221; and **value** (The **path** for your **Perl/bin folder**).

**Linux**

  1. **Open** a **Terminal**
  2. **Type**: **cd include**
  3. Press **Enter**
  4. **Type pico config.**h
  5. Type: **\# define SETPATH &#8220;/home/USER/hybserv/etc/settings.conf**
  6. **Save **
