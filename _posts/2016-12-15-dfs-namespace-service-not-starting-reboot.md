---
title: Using PowerShell to start the DFS Namespace service
permalink: /win/dfs-namespace-service-not-starting-reboot/
categories:
  - Windows
  - PowerShell
---
Distributed File System (DFS) has some service dependencies - so if those don't start the DFS Namespace service will also not start.

<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0835_DFSNamespac1.png?resize=584%2C112" alt="DFS Namespace" width="584" height="112" data-recalc-dims="1" />

The dependencies are:

  * Remote Registry
  * Security Accounts Manager
  * Server
  * Workstation

I have seen the Remote Registry service become the culprit of the DFS-N service not starting.

In my experience, this had been caused by antivirus software changing the Remote Registry service to Disabled start-up type so when the DFS-N server restarts, one of the dependency services:

Remote Registry does not start so if you have issues with the DFS-N service not starting – check the Remote Registry Start-up type is configured to Automatic and click Start to confirm there are no errors and try starting the DFS-N service again.

*Note: RemoteRegistry – although it is Automatic, will only Start when it is being used so don't be alarmed if it is in a 'Stopped' state.*
  
<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0835_DFSNamespac2.png?resize=377%2C267" alt="Remote Registry" width="377" height="267" data-recalc-dims="1" />

I have also created a PowerShell script to do some general checking for the DFS namespace service – which sets the Remote Registry service to Automatic startup then gets the other DFS dependency services and changes the startup type to Automatic and starts them and finally tries to start the DFS Namespace service.

{% gist d2d5123967c4fbb76b1912a09dc7f9cd %}

*Note: Script is also hosted on my Github repository. Feel free to
clone/recommend improvements or fork.*