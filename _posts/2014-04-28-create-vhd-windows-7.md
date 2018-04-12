---
id: 3290
title: Create VHD in Windows 7
date: 2014-04-28T17:13:44+00:00
author: Luke
layout: post
guid: http://localhost/techremedy/?p=3290
permalink: /win/create-vhd-windows-7/
slide_template:
  - default
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4834615800"
mfn-post-love:
  - "0"
post_views_count:
  - "16"
categories:
  - Windows
---
Want to create a VHD in Windows 7? Why? You may ask&#8230; would you use a VHD?

Using a VHD as a “virtual disk” you can easily use it as a self-contained “folder” or storage mechanism, you can also use it to install operating systems onto allowing to run dual booted operating systems with only one hard drive and not having to worry about partition ids. Creating VHD files in Windows 7 is remarkably easy – follow the guide below:

  1. Click the Start button in Windows 7, type in diskmgmt.msc, and hit Enter.
  
    2. Click the **Action** menu and select **Create VHD**.
  
    3. Enter a location, such as C:VHDWindows.vhd. Set the size. _Dynamic VHD files start out small and only grow with data written to the virtual disk._
  2. Click **OK** and the file is created.