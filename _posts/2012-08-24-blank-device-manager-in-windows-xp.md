---
title: Blank Device Manager in Windows XP
date: 2012-08-25 01:41:18 +12:00
permalink: "/win/blank-device-manager-in-windows-xp/"
categories:
- Windows
id: 1579
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1579
dsq_thread_id:
- '865042194'
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
mfn-post-love:
- '0'
post_views_count:
- '14'
---

The issue is caused by security permissions in the registry. This is how you fix it.

_You must be logged on as a local administrator to perform this task:_

  1. Click &#8220;**Start**&#8220;, &#8220;**Run**&#8220;, and enter &#8220;**regedt32**&#8220;
  2. **Maximize** the &#8220;**HKEY\_LOCAL\_MACHINE**&#8221; window.
  3. Scroll down to **&#8220;SYSTEMCurrentControlSetEnum**&#8220;
  4. With &#8220;**Enum**&#8221; selected click the &#8220;**Security**&#8220;, &#8220;**Permissions**&#8221; menu.
  5. Click &#8220;**Add**&#8220;.
  6. Add the group &#8220;**Everyone**&#8221; and the user &#8220;**SYSTEM**&#8220;.
  7. Select &#8220;**Everyone**&#8221; and check &#8220;**Read  ONLY**&#8220;
  8. Select &#8220;**SYSTEM**&#8221; and check **&#8220;Full Control**&#8220;
  9. Click the &#8220;**Advanced**&#8221; button at the bottom of the window.
 10.  On the Advanced window check &#8220;**Reset permissions on all child objects&#8230;**&#8220;
 11. Click &#8220;**OK**&#8220;
 12. On the warning dialog click &#8220;**Yes**&#8220;
 13. Close the registry editor

This problem can also be caused when the Plug & Play service is not running. Follow these options below.

1. Click **Start** then click **Run** type **services.msc **then click Ok.
  
2. **Double-click Plug and Play**.

_If you receive a Configuration Manager message then click Ok_
  
3. In the **Startup Type** list, click** Automatic** & then click **OK.**
  
4. Close Services.
  
5. **Restart the computer**.