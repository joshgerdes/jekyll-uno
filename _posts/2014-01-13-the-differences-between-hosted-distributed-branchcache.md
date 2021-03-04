---
title: The differences between Hosted &#038; Distributed Branchcache
date: 2014-01-13 00:00:00 +13:00
permalink: "/misc/the-differences-between-hosted-distributed-branchcache/"
categories:
- Misc
- Windows
---

Branchcache is one of those things – that can either be a blessing or a curse depending on how your network is setup.

Supported by Windows 7/Windows 8 & Server 2008 R2/Server 2012 – Branchcache is one of those technologies that I believe should be setup as default from the start – especially in larger organisations or enterprises.

First off – Branchcache is a method of &#8220;transparent caching&#8221; popular files from a network share to a more locally centralized – to the requesting computer – without increasing network bandwidth for a file that continuously gets pulled from a fileserver.


#### <span id="Hosted">Hosted</span>

Branchcache hosted is a method of actually having a Branchcache server &#8211; on an actual physical remote site away from the main fileserver.

Say you request a file &#8220;Untitled.docx&#8221; from the fileserver (at the main location – which may be on the opposite side of the country from your location) – however some of your colleagues also have requested the same file. The hosted Branchcache server that is usually located closer to your physical location then the main fileserver – holds a &#8220;cached&#8221; copy which your computer will grab first. If no one had requested the &#8220;Untitled.docx&#8221; previously your Windows workstation will then retrieve the file from the main fileserver and the Branchcache server will then host the file for an amount of time – specified by your systems administrator – this allows faster read times on the files you are commonly working on and reduces overall network latency.

#### <span id="Distributed">Distributed</span>

Branchcache Distribution is a method in which there is no local branchcache server available. This method is commonly used for smaller external remote sites – compared to the hosted method which requires a server setup. Through the use of the Local Group Policy distributed branchcache allows you to retrieve commonly used documents from other branchcache supported Windows workstations without the use of a dedicated server.

The files get &#8220;cached&#8221; onto the local workstations – allowing any supported Branchcache workstation to pick up the cached files without having to download the files from the network fileserver – reducing the continuous pull from the network fileserver and allowing for faster start – this method however is not recommended in a highly secure environment as files are stored on the local workstations.


_Note: Both methods do a file check to make sure the file version you are opening – is the most up to date. If the file you are opening is out of date – to the one stored on the fileserver then Branchcache will automatically run the latest version and update it&#8217;s cache._
