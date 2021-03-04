---
title: How to install OSX from a USB Drive (PowerPC)
date: 2012-03-28 00:00:00 +13:00
permalink: "/osx/how-to-install-osx-from-a-usb-drive-powerpc/"
categories:
- Mac OSX
---

  1. First you need the DMG of OSX, which you can either create using the Retail DVD you have (Using Disk Utility) or acquire through other means. Place the DMG somewhere you can get too easily, for example the Desktop.
  2. Connect your USB HDD to the computer & open the Disk Utility (Applications/Utilities/).
  3. On the left hand side of the Disk Utility, click Restore.
  4.  In the Source field, you need to point it to your OSX DMG. You can either click browse or drag the DMG into the field.
  5. In the Restore field you need to choose your USB HDD, you can either click browse or drag the HDD partition (which should be Erased using the Disk Utility) into the field.
  6.  Click Restore
  7. Once it is completed, you need to dot down the partition information for your external HDD so grab a piece of paper and pen.
  8.  Right click on your HDD partition (which should now be labeled the OSX install) and select Information, this will display information on the external HDD and partition information look for partition number, write this down.
  9.  Now restart your Mac and hold down Command+Option+O+F when starting, this will open the iMacs firmware, be careful in this area.
  
    Type: dev / ls (this will open a list of the devices in your computer)
 10.  In the list, look for information under usb such as /usb@a/disk@0, once you find this, wrote down the full path for example /@p/pci@1/usb@a/disk@0.
 11.  Type: devalias ud (The path you wrote down in the step above)
 12.  Type: dir ud:0,  (0 is the partition number, written down in while in the Disk Utility)
 13. Now look for a file with tbxi attribute usually “SystemLibraryCoreServicesBootX”
 14. Once you find it you need to change to the directory type:
 15. dir ud:0,SystemLibraryCoreServices (again the “0” is your partition number)
 16. Now is time to boot from the USB HDD type:
 17. boot ud:0,SystemLibraryCoreServicesBootX ((again the “0” is your partition number)
 18. Press Enter
