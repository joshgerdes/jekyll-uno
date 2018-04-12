---
id: 2445
title: 'Using Clonezilla &#8211; Clone to Image'
date: 2012-10-04T15:19:09+00:00
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2445
permalink: /misc/using-clonezilla-clone-to-image/
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
dsq_thread_id:
  - "4887771759"
mfn-post-love:
  - "0"
post_views_count:
  - "10"
categories:
  - Misc
---
  1. Download <a title="Clonezilla" href="http://clonezilla.org/downloads.php" target="_blank">Clonezilla</a>
  2. Burn to CD
  3. Boot from CD
  4. Select Clonezilla VGA mode _(top option)_
  5. Wait for Clonezilla to extract the files from the CD into the computers RAM
  6. Select your language ie English
  7. If using a different keyboard, choose Select Keymap from Arch List, otherwise leave Don&#8217;t touch key map as default, press Enter
  8. Select Start Clonezilla If you are cloning directly onto another drive choose device-device in this case we are cloning to an image so select device-image
  9. This is where you specify where the device will save to select: _local_dev_
 10. Insert the USB device when prompted, press Enter
 11. Select the device to mount
 12. Select the directory; I just leave it as top level
 13. Leave beginner
 14. Select SaveDisk (Save local disk as an image)
 15. Type in the name of the image, it is safe to leave it the default time/date
 16. Select the disk or drive you would like to clone, press Enter
 17. Select Skip Checking, unless you have reason to believe the drive might be failing.
 18. To avoid mistakes restoring images make sure you select Yes, Check the Save image (this will take a bit of extra time but worth it in case of problems restoring)
 19. Press Enter to continue
 20. It will then do a last scan of the hardware and ask you for confirmation (make sure that the drives you are trying to clone are the right one, this is your last chance) press Y and enter to continue

&nbsp;