---
title: Virtual Box   &#8216;Failed, trying without DKMS&#8221;
date: 2012-03-08 00:00:00 +13:00
permalink: "/linux/virtual-box-failed-trying-without-dkms/"
categories:
- Linux
---

This means simply, you are missing the <a title="Dynamic Kernel Module Support" href="http://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support" target="_blank">dkms </a>package.

**Ubuntu**

  1. **Open** a **Terminal** type: **apt-get install dkms**
  2. Press **Enter**
  3. Wait for it to **download** & **install**. Try **opening** **Virtual** **Box** Again

**Fedora**

  1. **Open** a **Terminal** type: **yum install dkms**
  2. Press **Enter**
  3. Wait for it to **download** & **install**. Try **opening** **Virtual** **Box** Again
