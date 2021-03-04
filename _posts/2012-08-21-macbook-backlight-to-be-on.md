---
title: Set the Macbook Keyboard Back-light to be on permanently
date: 2012-08-21 23:56:34 +12:00
permalink: "/osx/macbook-backlight-to-be-on/"
categories:
- Mac OSX
id: 1571
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1571
dsq_thread_id:
- '945625980'
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
- '4'
---

<ol start="1">
  <li>
    <strong>Open</strong> <strong>Finder</strong>
  </li>
  <li>
    <strong>Navigate</strong> to: <strong><em>Users/YourUser/NameHere/Library/Preferences</em></strong>
  </li>
  <li>
    <em>Warning: Be mindful of changing the wrong file or touching incorrect settings in this folder. This could go wrong!</em>
  </li>
  <li>
    <strong>Open<em>: com.apple.bezelservice.plist</em></strong>
  </li>
  <li>
    <strong>Change</strong> <strong><em>kHWMin</em></strong> to have a value of: <strong>1</strong>
  </li>
  <li>
    Close and <strong>save</strong>
  </li>
</ol>

_You have now adjusted the minimum light the light sensor needs to activate the back-light on the keyboard. _

_Note: Only valid for Macbook Pros, normal Macbooks do not contain keyboard back-lights._