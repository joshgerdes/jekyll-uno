---
id: 1472
title: Reset Windows 7 Security Permissions
date: 2012-09-30T15:12:42+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1472
permalink: /win/reset-windows-7-security-permissions/
dsq_thread_id:
  - "2487885282"
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
  - "7"
categories:
  - Windows
---
<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    <strong>Navigate</strong> <strong>to Programs/Accessories</strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> Command <strong>Prompt</strong> and <strong>select</strong> <strong><em>Run As Administrator</em></strong>
  </li>
  <li>
    <strong>Type</strong>: <strong><em>secedit /configure /cfg %windir%infdefltbase.inf /db defltbase.sdb /verbose</em></strong>
  </li>
  <li>
    Press <strong>Enter</strong>
  </li>
  <li>
    <strong>Wait</strong> for it to complete the operation and the <strong>permissions</strong> should be <strong>reset</strong> back to <strong>Factory</strong> <strong>Settings</strong>.
  </li>
</ol>

If the above does not work, try this <a title="Security_Restore" href="http://www.softpedia.com/get/Security/Security-Related/Security-Restore.shtml" target="_blank">Security Restore Utility</a>.

_This has also been reported as the fix for Windows Update Error #8007005_