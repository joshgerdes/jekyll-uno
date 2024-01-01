---
title: How to change your MAC address in Linux
permalink: /linux/how-to-change-your-mac-address-in-linux/
tags:
  - Linux
---
  1. Open a **Terminal**
  2. Type: **_ifconfig eth0 down_**
  3. Type: **_ifconfig eth0 hw ether THISISWHEREYOUENTERNEWMACADDRESS_**
  4. Type: **_ifconfig eth0 up_**

The mac address change is only temporary, until you restart
