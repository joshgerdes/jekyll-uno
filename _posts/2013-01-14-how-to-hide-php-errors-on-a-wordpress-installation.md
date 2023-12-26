---
title: How to hide PHP errors on a WordPress installation
date: 2013-01-14 00:00:00 +1300
author: Luke
categories:
  - Misc
---

  1. Using an FTP client – such as <a title="FileZilla" href="http://filezilla-project.org/" target="_blank">Filezilla</a> log in to your website.
  2. Navigate to your WordPress directory
  3. Right click **_wp-config.php_**
  4. Select **Edit**
  5. Add:  **_@ini\_set(&#8216;display\_errors&#8217;, 0); _**to the wp-config document – up the top is fine.
  6. Now save the document, your FTP client should now upload the changes and any PHP errors you may be displaying will be hidden.
