---
title: Using phpmyadmin to remove WordPress posts
date: 2013-02-25 21:38:37 +13:00
permalink: "/misc/using-phpmyadmin-to-remove-wordpress-posts/"
categories:
- Misc
id: 2695
author: Luke
layout: post
guid: http://incinerate.co.nz/?p=2695
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
dsq_thread_id:
- '1102777430'
mfn-post-love:
- '0'
post_views_count:
- '13'
---

Warning:  _This will remove all posts on your wordpress installation. Make sure you have a backup or simply don’t want them anymore&#8230; when they are gone they are gone!_

&nbsp;

  1. Login to PHPMyAdmin
  2. On the left hand side – select your wordpress database
  3. Click on the Posts stable
  4. Click Operations (top menu bar)
  5. Click Empty the table (TRUNCATE)
  6. Click Ok

&nbsp;

Note: Clearing the postsmeta table will delete the references to your images and post tags.