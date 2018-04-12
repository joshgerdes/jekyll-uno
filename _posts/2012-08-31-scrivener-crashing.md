---
id: 1604
title: Scrivener Crashing
date: 2012-08-31T10:58:32+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1604
permalink: /osx/scrivener-crashing/
dsq_thread_id:
  - "2547277125"
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
  - "10"
categories:
  - Mac OSX
---
Attempting to open Scrivener and having the application closing on you, the common way to fix this is adjust the file permissions follow the instructions below to repair.

<ol start="1">
  <li>
    <strong>Open</strong> a <strong>Terminal</strong><em> (Applications/Utilities) </em>
  </li>
  <li>
    <strong>Type</strong>: <em>sudo chmod -R 0755 /Applications/Scrivener.app</em>
  </li>
  <li>
    Press <strong>Enter</strong>
  </li>
  <li>
    <strong>Open</strong> <strong>Scrivener</strong> again.
  </li>
</ol>

Note: _This fix has also been able to work on other OSX Applications that have problems launching._