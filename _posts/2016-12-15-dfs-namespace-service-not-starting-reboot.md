---
id: 3865
title: DFS Namespace service not starting after a reboot
date: 2016-12-15T08:00:07+00:00
author: Luke
layout:
  - ""
guid: http://luke.geek.nz/?p=3865
permalink: /win/dfs-namespace-service-not-starting-reboot/
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
dsq_thread_id:
  - "5376529515"
categories:
  - Windows
---
Distributed file System (DFS) has some service dependencies &#8211; so if those don&#8217;t start the DFS Namespace service will also not start.

<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0835_DFSNamespac1.png?resize=584%2C112" alt="DFS Namespace" width="584" height="112" data-recalc-dims="1" />

The dependencies are:

  * Remote Registry
  * Security Accounts Manager
  * Server
  * Workstation

I have seen the Remote Registry service become the culprit of the DFS-N service not starting.

In my experience &#8211; this has been caused by antivirus software changing the Remote Registry service to Disabled start-up type so when the DFS-N server restarts, one of the dependency services:

Remote Registry does not start so if you have issues with the DFS-N service not starting – check the Remote Registry Start-up type is configured to Automatic and click Start to confirm there are no errors and try starting the DFS-N service again.

_Note: RemoteRegistry – although it is Automatic, it will only Start when it is being used so don&#8217;t be alarmed if it is in a Stopped state.
  
_ 

<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0835_DFSNamespac2.png?resize=377%2C267" alt="Remote Registry" width="377" height="267" data-recalc-dims="1" />

I have also created a quick PowerShell script to do some general checking for the DFS namespace service – sets the Remote Registry service to Automatic startup, Gets the other DFS service dependancy services and changes the startup type to Automatic and starts them and finally tries to start the DFS Namespace service.

<div class="oembed-gist">
  <noscript>
    View the code on <a href="https://gist.github.com/lukemurraynz/d2d5123967c4fbb76b1912a09dc7f9cd">Gist</a>.
  </noscript>
</div>