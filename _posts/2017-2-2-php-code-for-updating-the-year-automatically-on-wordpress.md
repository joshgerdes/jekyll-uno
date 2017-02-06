---
layout: post
title: PHP code for updating the year automatically in WordPress
published: true
---

Loading more than one Google font in one request can help to speed up page load time and keep your code tidy.

### How is it done?
In your footer.php add:

    &copy; Copyright <?php echo date("Y"); ?>
        

__NOTE:__ Your hosting account must be able to run PHP.
