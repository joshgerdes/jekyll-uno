---
id: 3199
title: How to point Active Directory Administrative Center to another domain in Server 2012
date: 2014-04-05T18:20:04+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3199
permalink: /win/how-to-point-active-directory-administrative-center-to-another-domain-in-server-2012/
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
  - "4987896737"
mfn-post-love:
  - "0"
post_views_count:
  - "20"
categories:
  - Windows
---
  1. Click Start
  2. Click Administrative Tools
  3. Click Active Directory Administrative Center
  4. Click on Add Navigation Node
  5. Click Connect to other domains.. _(on the lower right of the window)_
  6. Type the domain name you want to connect to and click ok.

Note: This is only valid for trusted federated domains &#8211; this method of connecting uses your local credentials and in order to run as separate credentials you will need to launch the Administrative Center using Runas.