---
title: How to hide PHP errors on a WordPress installation
date: 2013-01-14 20:34:41 +13:00
permalink: "/misc/how-to-hide-php-errors-on-a-wordpress-installation/"
categories:
- Misc
id: 2635
author: Luke
layout: post
guid: http://localhost/incinerate/?p=2622
dsq_thread_id:
- '1056345420'
mfn-post-love:
- '0'
post_views_count:
- '6'
---

  1. Using an FTP client – such as <a title="FileZilla" href="http://filezilla-project.org/" target="_blank">Filezilla</a> log in to your website.
  2. Navigate to your WordPress directory
  3. Right click **_wp-config.php_**
  4. Select **Edit**
  5. Add:  **_@ini\_set(&#8216;display\_errors&#8217;, 0); _**to the wp-config document – up the top is fine.
  6. Now save the document, your FTP client should now upload the changes and any PHP errors you may be displaying will be hidden.