---
title: 'How To: Fix &#8216;Cryptographic Service&#8217; error when installing Windows
  XP Updates'
date: 2012-03-05 00:00:00 +13:00
permalink: "/win/how-to-fix-cryptographic-service-error-when-installing-windows-xp-updates/"
categories:
- Windows
---

Open a command prompt window _(click Start, Run, type cmd and hit Enter)_ and then type the following commands:

_**regsvr32 softpub.dll**_
  
_ **regsvr32 wintrust.dll**_
  
_ **regsvr32 initpki.dll**_
  
_ **regsvr32 dssenh.dll**_
  
_ **regsvr32 rsaenh.dll**_
  
_ **regsvr32 gpkcsp.dll**_
  
_ **regsvr32 sccbase.dll**_
  
_ **regsvr32 slbcsp.dll**_
  
_ **regsvr32 cryptdlg.dll**_

Restart Cryptographic Services by clicking the Start button again, and try installing the service pack or security patch once more.

If the above solution&#8217;s do not work. You can use a tool called [Dial A Fix](http://wiki.lunarsoft.net/wiki/Dial-a-fix) to repair the Cryptographic & Windows Update services with a few clicks.
