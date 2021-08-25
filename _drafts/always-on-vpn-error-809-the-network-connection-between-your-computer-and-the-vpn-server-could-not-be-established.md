---
date: 2021-08-25 00:00:00 +1200
title: 'Always on VPN - Error 809 The network connection between your computer and
  the VPN server could not be established '
author: Luke
categories:
- Windows
toc: false
header:
  teaser: ''

---
I ran into a weird issue, troubleshooting an 'Always On' installation running off Windows Server 2019, the clients were getting:

    Error 809 The network connection between your computer and the VPN server could not be established

In my case, the issue wasn't due to [IKEv2 Fragmentation](https://directaccess.richardhicks.com/2019/02/14/troubleshooting-always-on-vpn-error-code-809/ "Troubleshooting Always On VPN Error Code 809") or anything to do with NAT to allow the origin IP to flow to the Always-on VPN server. It was due to the ports being limited to: '2'. I found an old post regarding Windows Server 2008 R2: 

* [The maximum number of WAN Miniport (IKEv2) ports changes from 128 to two after you install Windows Server 2008 R2 SP1](https://support.microsoft.com/en-us/topic/the-maximum-number-of-wan-miniport-ikev2-ports-changes-from-128-to-two-after-you-install-windows-server-2008-r2-sp1-15aeb929-abe9-ece0-5d71-d2223d6a94d0 " The maximum number of WAN Miniport (IKEv2) ports changes from 128 to two after you install Windows Server 2008 R2 SP1")

> "If more than two clients try to connect to the server at the same time, the Routing and Remote Access service rejects the IKEv2 connection requests. Additionally, the following message is logged in the Rastapi.log file:"

This matched my issue, I had never seen more than 2 connections at once.

### Increase Ports

 1. Open **Routing and Remote Access**
 2. **Click** on your Routing and **Remote Access server**
 3. **Right**-**click** on **Ports**
 4. Click on: **WAN Miniport (IKEv2)**
 5. Click **Configure**
 6. **Make sure** that: To **enable remote access**, select Remote access **connections** (inbound only) is **checked**
 7. **Change Maximum ports** from 2 _(as an example)_ to a number that matches how many connections you want - I went with **128**
 8. Click **Ok**
 9. Click **Apply**
10. **Restart** the Routing and Remote Access **server** you should now see more ports listed 'as inactive' until a new session comes along and uses it.

![Routing and Remote Access](/uploads/wan_miniport_ikev2.png "Routing and Remote Access")

![Routing and Remote Access](/uploads/wan_miniport_ports.png "Routing and Remote Access")

### Change Ports