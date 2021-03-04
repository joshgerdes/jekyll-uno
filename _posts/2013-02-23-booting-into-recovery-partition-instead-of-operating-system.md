---
title: Booting into Recovery Partition instead of Operating System
date: 2013-02-24 10:10:43 +13:00
permalink: "/win/booting-into-recovery-partition-instead-of-operating-system/"
categories:
- Windows
id: 2682
author: Luke
layout: post
guid: http://incinerate.co.nz/?p=2682
omc_review_enable:
- '0'
omc_user_ratings_visibility:
- '0'
omc_review_type:
- stars
omc_criteria_display:
- n
omc_featured_post:
- '0'
omc_comment_type:
- wp
dsq_thread_id:
- '1100258346'
mfn-post-love:
- '0'
post_views_count:
- '13'
---

&nbsp;

Having issues with your computer booting into the Recovery Partition instead of the Windows operating system? Try the guide below to repair.

&nbsp;

  1. First download <a title="GParted (Gnome Partition Manager)" href="http://gparted.sourceforge.net/download.php" target="_blank">Gparted</a> and burn it to a CD
  2. Boot from the Gparted CD _(F12 or Esc are common hotkeys to bring up the boot menu during system startup)_
  3. Just press Enter through the default options to boot into the user interface.
  4. You should see several partitions on your computer – this usually consists of System, Operating System (C:) and Data.
  5. Right click the Operating System partition
  6. Left click Flags
  7. Left click Boot _(the boot flag will set the OS partition to bootable – it is probably set to System or the Recovery partition at the moment)_
  8. Click ok
  9. Now shutdown gparted and restart your computer. It should now boot into the operating system.