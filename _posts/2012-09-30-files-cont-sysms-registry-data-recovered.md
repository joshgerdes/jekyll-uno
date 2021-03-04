---
title: One of the files containing the systems registry data had to be recovered
date: 2012-10-01 04:40:36 +13:00
permalink: "/win/files-cont-sysms-registry-data-recovered/"
categories:
- Windows
id: 1502
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1502
dsq_thread_id:
- '5300395979'
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
- '11'
---

_This can someone be the result of bad RAM or Video RAM. Try to change the video memory in the BIOs from the lower number (usually 32MB/64MB) to the higher number (64/128MB) if this does not work try the following below to repair the “NTUser.DAT” file that has become corrupted/damaged on the User Account._

_First we have to reveal Hidden files & folders:_

<ol start="1">
  <li>
    Click Start
  </li>
  <li>
    Click Documents/My Documents
  </li>
  <li>
    Click Tools
  </li>
  <li>
    Click Folder Options
  </li>
  <li>
    Click View
  </li>
  <li>
    Click Show Hidden Files, Folders, and drives.
  </li>
  <li>
    Click Ok
  </li>
</ol>

_Now we have to create a new administrator user account:_

<ol start="1">
  <li>
    Click Start
  </li>
  <li>
    Click Control Panel
  </li>
  <li>
    Click User Accounts
  </li>
  <li>
    Select New Account
  </li>
  <li>
    Set privileges to Administrator
  </li>
  <li>
    Now log out of the damaged account and login to your newly created User Account.
  </li>
  <li>
    Click Start
  </li>
  <li>
    Click My Computer/Computer
  </li>
  <li>
    Click on C:
  </li>
  <li>
    Navigate to Documents & Settings
  </li>
  <li>
    You should have a list of User Accounts on your computer shown; go into the “damaged” User profile folder.
  </li>
  <li>
    Right click ntuser.dat and select rename to: ntuser.bak (bak=backup)
  </li>
  <li>
    Open up a new explorer Window by clicking Start and choose My Computer/Computer
  </li>
  <li>
    Navigate to c:WINDOWSREPAIR
  </li>
  <li>
    Right click ntuser.dat and select Copy
  </li>
  <li>
    Go back to the damaged profile folder right click a blank space and select Paste
  </li>
  <li>
    Now log out
  </li>
  <li>
    Now we need to log back into the damaged User Profile again.
  </li>
  <li>
    Windows will now use the NTUser.dat file we copied across earlier to regenerate a new set of undamaged files, do not worry if your theme has changed or things don’t look quite right.
  </li>
  <li>
    Once the User Account has finished loading we need to log-out and switch back to the newly created account again.
  </li>
  <li>
    Click Start
  </li>
  <li>
    Click My Computer/Computer
  </li>
  <li>
    Click on C:
  </li>
  <li>
    Navigate to Documents & Settings
  </li>
  <li>
    Click on the damaged User Profile account
  </li>
  <li>
    Now right click the NTuser.dat file to:ntuser.old
  </li>
  <li>
    Right click the ntuser.bak file we renamed earlier and select rename and rename it back to NTUser.DAT.
  </li>
  <li>
    Log out of the User account and log back into the damaged User Profile, it should now be fixed.
  </li>
</ol>