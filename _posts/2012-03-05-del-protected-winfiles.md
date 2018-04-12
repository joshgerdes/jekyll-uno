---
id: 3057
title: Deleting protected files in Windows
date: 2012-03-05T15:28:48+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=963
permalink: /win/del-protected-winfiles/
dsq_thread_id:
  - "928105896"
  - "928105896"
  - "928105896"
  - "928105896"
omc_review_enable:
  - "0"
  - "0"
  - "0"
  - "0"
omc_user_ratings_visibility:
  - "0"
  - "0"
  - "0"
  - "0"
omc_review_type:
  - stars
  - stars
  - stars
  - stars
omc_criteria_display:
  - 'n'
  - 'n'
  - 'n'
  - 'n'
omc_featured_post:
  - "0"
  - "0"
  - "0"
  - "0"
omc_comment_type:
  - wp
  - wp
  - wp
  - wp
slide_template:
  - default
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
mfn-post-love:
  - "0"
post_views_count:
  - "5"
categories:
  - Windows
---
The Windows operating system is known for many things – including its ability to protect system and user protected files.

Using the TakeOwn _(built into Windows)_ command you can easily use the utility to take ownership of files which would otherwise be system or user protected.

Follow my simple guide below to take ownership of files:

  1. First you need an elevated command prompt – Run Command Prompt as Administrator.
  2. To take ownership of the file, you&#8217;ll need to use the takeown command for example:
  3. **_ `takeown /f c:/Windows/system32/AdobePDF.dll`_**
  4. That will give you ownership of the file, but you still have no rights to
  
    delete it.
  5. Now you can run the cacls command to give yourself full control
  
    rights to the file:
  6. **_`cacls c:Windows/system32/AdobePDF.dll /G test:F` _**

_Note that my username is test, so you will substitute your username there._

<ol start="5">
  <li>
    You should be able to delete the file<em>. If you still can&#8217;t do so, you may need to reboot into Safe Mode and try it again.</em>
  </li>
</ol>