---
title: Google Bulk Account Update &#8220;read error&#8221;
date: 2012-10-01 03:01:08 +13:00
permalink: "/misc/google-bulk-account-update-read-error/"
categories:
- Misc
id: 1446
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1446
dsq_thread_id:
- '864818655'
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
- '6'
---

Trying to upload a CSV file to get Google to create multiple users with the email address, first name, and last name & password fields and getting the &#8220;read error&#8221; trying to upload. This is how I fixed it:

<ol start="1">
  <li>
    Locate the file you are uploading and <strong>remove</strong> the &#8220;.csv&#8221; file <strong>extension</strong>. Upload the file without the extension.
  </li>
</ol>

_To get rid of the CSV file extension, you might have to go to a folder, click on Tools, Options, Folder Options and uncheck Show File Extensions._