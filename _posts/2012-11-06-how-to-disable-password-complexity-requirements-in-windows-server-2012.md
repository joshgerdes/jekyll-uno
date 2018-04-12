---
id: 2513
title: How to disable password complexity requirements in Windows Server 2012
date: 2012-11-06T19:28:59+00:00
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2513
permalink: /win/how-to-disable-password-complexity-requirements-in-windows-server-2012/
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
  - "5044489968"
mfn-post-love:
  - "0"
post_views_count:
  - "12"
categories:
  - Windows
---
  1.  **Open** Server **Manager**
  2. Click **Tools** _(top right)_
  3. Click **Local Security Policy**
  4. **Navigate** to Account Policies/**Password** **Policy**
  5. Double click “**_Password must meet complexity requirements_**”
  6. Click **Disable**
  7. Click **Ok**

&nbsp;

Note: You can also Group Policy which includes Local security policies by pressing the Windows Key+R at the same type and typing: _gpedit.msc_ into the run dialog.