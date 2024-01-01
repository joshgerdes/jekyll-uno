---
title: Using phpmyadmin to remove WordPress posts
date: 2013-02-25 00:00:00 +1300
authors: [Luke]
tags:
  - Misc
---

Warning:  _This will remove all posts on your wordpress installation. Make sure you have a backup or simply don’t want them anymore&#8230; when they are gone they are gone!_

  1. Login to PHPMyAdmin
  2. On the left hand side – select your wordpress database
  3. Click on the Posts stable
  4. Click Operations (top menu bar)
  5. Click Empty the table (TRUNCATE)
  6. Click Ok

Note: Clearing the postsmeta table will delete the references to your images and post tags.