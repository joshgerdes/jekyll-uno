---
id: 3182
title: .NET Framework not installing through SCCM
date: 2014-03-28T10:19:24+00:00
author: Luke
layout:
  - ""
guid: http://techremedy.co.nz/?p=3182
permalink: /win/net-framework-not-installing-through-sccm/
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
  - "5363434313"
mfn-post-love:
  - "0"
post_views_count:
  - "10"
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
categories:
  - Windows
---
  1. Click Start
  2. Click Run and type in: services.msc
  3. Stop the Automatic Update service
  4. Navigate to: C:\Windows
  5. Delete the: SoftwareDistribution folder
  6. Start the Automatic Update service
  7. Double click on the SCCM Update icon in the notification tray and select Install & Install now.