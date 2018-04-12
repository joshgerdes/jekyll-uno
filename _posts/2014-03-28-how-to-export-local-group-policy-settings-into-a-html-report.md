---
id: 3186
title: How to export local group policy settings into a HTML report
date: 2014-03-28T10:39:19+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3186
permalink: /win/how-to-export-local-group-policy-settings-into-a-html-report/
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
  - "4798637549"
mfn-post-love:
  - "0"
post_views_count:
  - "39"
categories:
  - Windows
---
  1. Press the Windows Key + R to open the Run dialog box
  2. Type in: cmd and press Enter
  3. This will load the Windows Command Prompt
  4. Using the CD _(change directory)_ command – change your directory to where you want to save the report&#8230; for example “cd Desktop” will change to your Desktop.
  5. Type in: **gpresult /h LocalGrpPolReport.html** and press Enter

This will then load the group policy snap-in in the background and generate a HTML page called: &#8220;LocalGrpPolReport.html&#8221; that you will be able to open and see what policies have been applied to that local machine and which policies are taking precedence over others.