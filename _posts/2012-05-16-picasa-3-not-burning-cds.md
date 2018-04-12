---
id: 1308
title: Picasa 3 Not Burning CDs
date: 2012-05-16T07:34:13+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1308
permalink: /win/picasa-3-not-burning-cds/
dsq_thread_id:
  - "5346998866"
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
mfn-post-love:
  - "0"
post_views_count:
  - "8"
categories:
  - Windows
---
First  you need to uninstall Picasa, follow the guide below to do this:

  1. Click Start
  2. Click Control Panel
  3. Click Add or Remove Programs/Uninstall a Program
  4. Click Picasa and select Uninstall and when prompted select No to delete the database to avoid loss of your picture file locations.

&nbsp;

Once the uninstall has completed you need to delete a DLL file so follow the steps below:

  1. Click Start
  2. Click My Computer/Computer
  3. Navigate to: C:WindowsSystem32drivers
  4. Delete the &#8220;Pxhelp20.sys&#8221; file _(Make sure not to touch anything else)_.
  5. Now reinstall <a title="Picasa" href="http://picasa.google.com/" target="_blank">Picasa</a>
  6. Restart your computer once Picasa has finished installing and you now should be able to burn a CD