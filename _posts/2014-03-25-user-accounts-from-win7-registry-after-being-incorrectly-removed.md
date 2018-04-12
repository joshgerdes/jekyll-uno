---
id: 3177
title: How to remove user accounts from Windows 7 registry after being incorrectly removed
date: 2014-03-25T08:08:08+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3177
permalink: /win/user-accounts-from-win7-registry-after-being-incorrectly-removed/
tie_hide_meta:
  - ""
tie_hide_author:
  - ""
tie_hide_share:
  - ""
tie_hide_related:
  - ""
tie_sidebar_pos:
  - default
tie_sidebar_post:
  - ""
tie_post_head:
  - ""
tie_googlemap_url:
  - ""
tie_video_url:
  - ""
tie_embed_code:
  - ""
tie_audio_m4a:
  - ""
tie_audio_mp3:
  - ""
tie_audio_oga:
  - ""
tie_audio_soundcloud:
  - ""
tie_banner_above:
  - ""
tie_banner_below:
  - ""
post_color:
  - ""
tie_review_position:
  - ""
tie_review_style:
  - stars
tie_review_summary:
  - ""
tie_review_total:
  - ""
tie_review_criteria:
  - ""
tie_blog_cats:
  - ""
post_background:
  - 'a:6:{s:3:"img";s:0:"";s:5:"color";s:0:"";s:6:"repeat";s:0:"";s:10:"attachment";s:0:"";s:3:"hor";s:0:"";s:3:"ver";s:0:"";}'
tie_authors:
  - ""
dsq_thread_id:
  - "4917948385"
mfn-post-love:
  - "0"
post_views_count:
  - "26"
categories:
  - Windows
---
_Note: This usually needs to be done when the Windows 7 profile has been manually deleted and not properly removed – as Windows 7 uses a security identifier attached to the user account in the registry and this needs to be cleared as well_

_Note: It is also recommend making a backup of the registry before this change – and you may need to restart the PC for the registry entry to be able to be removed._

_ _

  1. Press Windows Key + R to open the **Run** dialog window.
  2. Type in: **regedit** and press Enter or click Ok
  3. Press yes to accept UAC prompt.
  4. Navigate to: **HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindows NTCurrentVersionProfileList******
  5. ******This lists the SID (security identifier) that is linked to your account – scroll down the list and on the right hand side under CentralProfile and ProfileImagePath find the correct user profile you would like to remove.******
  6. ******Once you have found the correct one – right click the SID key you would like to remove and select Delete.******
  7. **Exit out of the Registry Editor and restart the workstation – the user should now be able to login and generate a new profile folder and security identifier.**