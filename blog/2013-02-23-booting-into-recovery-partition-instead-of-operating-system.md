---
title: Booting into Recovery Partition instead of Operating System
authors: [Luke]
tags:
  - Windows
date: 2013-02-23 00:00:00 +1300
---

Having issues with your computer booting into the Recovery Partition instead of the Windows operating system? Try the guide below to repair.


  1. First download <a title="GParted (Gnome Partition Manager)" href="http://gparted.sourceforge.net/download.php" target="_blank">Gparted</a> and burn it to a CD
  2. Boot from the Gparted CD _(F12 or Esc are common hotkeys to bring up the boot menu during system startup)_
  3. Just press Enter through the default options to boot into the user interface.
  4. You should see several partitions on your computer – this usually consists of System, Operating System (C:) and Data.
  5. Right click the Operating System partition
  6. Left click Flags
  7. Left click Boot _(the boot flag will set the OS partition to bootable – it is probably set to System or the Recovery partition at the moment)_
  8. Click ok
  9. Now shutdown gparted and restart your computer. It should now boot into the operating system.