---
id: 2927
title: Ubuntu – How to do a Distribution Upgrade
date: 2014-01-01T12:47:03+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2927
permalink: /linux/ubuntu-how-to-do-a-distribution-upgrade/
mfn-post-love:
  - "0"
dsq_thread_id:
  - "2571390845"
post_views_count:
  - "6"
categories:
  - Linux
---
  1. Launch a Terminal 
  2. Type in: **_sudo apt-get update_**
			  
    _(this will ping all the upgrade mirrors to determine if they are live and what upgrade packages are available)._ 
  3. Once completed – type in: sudo apt-get dist-upgrade _(this will start pooling down the various packages to do a distribution upgrade. Keep in mind – apt-get update will just do an update within the same distribution)._ 

Note: Ubuntu now has an Update Manager that is available by launching the Unity search function and typing in – Update Manager. This is a GUI method of upgrading. I have had failure with this method personally so recommend using the command line for distribution upgrades for more visibility.