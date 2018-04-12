---
id: 3184
title: Unable to right click in Microsoft Excel
date: 2014-03-28T10:23:31+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3184
permalink: /win/unable-to-right-click-in-microsoft-excel/
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
  - "4876651084"
mfn-post-love:
  - "0"
post_views_count:
  - "13"
categories:
  - Windows
---
This is fixed by removing the Excel11.xlb excel template file located in the following locations:

&nbsp;

Win7 32bit:

C:Program FilesMicrosoft OfficeOffice14XLSTART

C:UsersUserNameAppDataRoamingMicrosoftExcelXLSTART

Win7 64bit:

C:Program Files(x86)Microsoft OfficeOffice14XLSTART

C:UsersUserNameAppDataRoamingMicrosoftExcelXLSTART

&nbsp;

Note: Make sure Excel is closed before attempted to remove this file – Excel will automatically generate a new Excel11.xlb template.