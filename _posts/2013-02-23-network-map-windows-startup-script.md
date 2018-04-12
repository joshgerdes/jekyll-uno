---
id: 2689
title: Network Map Windows startup Script
date: 2013-02-23T21:21:11+00:00
author: Luke
layout: post
guid: http://incinerate.co.nz/?p=2689
permalink: /win/network-map-windows-startup-script/
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
  - "2444566017"
mfn-post-love:
  - "0"
post_views_count:
  - "14"
categories:
  - Windows
---
`<br />
echo off<br />
cls<br />
net use z: /delete /y<br />
net use z: "192.168.1.1share" /y<br />
` 

Note:  &#8220;Z is the drive letter I have assigned for this example &#8211; you can however change this to what you want _(if it already is not in use of course)_.)