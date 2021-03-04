---
title: Black Screen on Windows 7 on an iMac
date: 2012-05-28 00:00:00 +12:00
permalink: "/osx/bsod-win7-imac/"
categories:
- Mac OSX
layout: post
---

_This usually occurs due to problems with the nVidia drivers. Follow the prompts below to repair this._

  1. Put the Windows 7 DVD into your drive and restart and boot from the DVD
  2. When the Windows 7 prompt comes up, select Repair Your Computer (on the lower left)
  3. Select your Windows installation and press Next
  4. Now you should be at the System Recovery Options, select Command Prompt
  5. Once the command prompt opens type: DEL C:WINDOWSSYSTEM32DRIVERSNVLDDMKM.SYS
  6. If you have problems with sound type:  DEL C:WINDOWSSYSTEM32DRIVERSati*.sys
  7. Now reboot
  8. You should now be in Windows 7 (however it will look a bit pale and large, this is normal)
  9. Go to the “nvidia” website and download the GT7 Series Driver for Windows 7
 10. Now install and reboot.
 11. Having done this go to the Nivida web site and download the GT 7 series drivers for Windows 7!
 12. Install the drivers and reboot.
