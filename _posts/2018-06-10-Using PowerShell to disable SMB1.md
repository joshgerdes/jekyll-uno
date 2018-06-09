---
date: "2018-06-10"
title: Using PowerShell to disable SMB1
author: Luke
categories:
  - PowerShell
  - Windows
---

Although the new versions of Windows Server 2016 and Windows 10 no longer
install SMB1 as default, the majority of us are still using older systems, such
as earlier versions of Windows 10, Windows 7 and Server 2012 R2 which still has
SMB1 enabled.

Unfortunately, you may still find legacy systems in your environments that might
rely on SMB1, such as legacy Windows Server 2003 or Linux systems, so this is
something you shouldn’t just do on systems without validating beforehand, the
downside is this is a VERY insecure protocol *(as evidenced by WannaCry and
other attacks which targeted that protocol)* which needs to be eradicated from
any use! To be clearer all you need to do is read this article from Ned Pyle
from Microsoft back in 2016.

-   [Stop using
    SMB1](https://blogs.technet.microsoft.com/filecab/2016/09/16/stop-using-smb1/){:target="_blank"}

-   [SMB1 Product
    Clearinghouse](https://blogs.technet.microsoft.com/filecab/2017/06/01/smb1-product-clearinghouse/){:target="_blank"}

There are a lot of resources out there to disable SMB1, included is a PowerShell
script I wrote back in 2017 that I used to assist with disabling SMB1 across
workstations and used it to disable SMB1 as part of my Windows 10 Enterprise MDT
builds.

To run it, save the script below as PS1 and open it PowerShell as Administrator
*(To open an elevated PowerShell prompt, in the Start Menu, type PowerShell.
Windows PowerShell should appear on the top. Right-click on it and select Run as
Administrator and navigate to where the PS1 has been saved and run it)*

![DisableSMB1]/images/posts/DisableSMB1.gif "DisableSMB1"

{% gist d0a4c7d06fe3b0120798535fb6c7eb53 %}