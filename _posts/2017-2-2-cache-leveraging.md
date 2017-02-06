---
layout: post
title: Cache Leveraging
published: true
navigation_weight: 1
---

I recently came across another great article on the [Varvy](https://varvy.com/pagespeed/leverage-browser-caching.html) website which describes in simple to understand language the best methods cache leveraging.

### What is cache leveraging?
This is when you give instructions to the browser on how to deal with your websites resources.

When a browser caches something it simply means, it has remember what resources have been loaded. So the objective with leveraging the browser cache is to get your web files stored in the browser cache thus allowing your page to load faster for repeat users.

### How does it work?
Varvy explains in greater detail about various methods that can be applied such as setting caching times and cache control.

For my personal website I used the caching for .htaccess method.

### Caching for .htaccess
Open or create a .htaccess file and place it in the root of your website. You can then enter the data as below but with the paths of files that you wish to cache for your website.

Here's what I added to my .htaccess file. The code tells the browser what to cache and the length of time to remember it for.


        **EXPIRES CACHING**
        ExpiresActive On
        ExpiresByType css/custom.min.css "access 1 month"
        ExpiresByType css/foundation.min.css "access 1 month"
        ExpiresByType images/hero-1600x150.jpg "access 1 month"
        ExpiresByType js/app.js "access 1 month"
        ExpiresByType js/vendor/foundation.min.js "access 1 month"
        ExpiresByType js/vendor/jquery.min.js "access 1 month"
        ExpiresByType js/vendor/what-input.min.js "access 1 month"
        ExpiresDefault "access 1 month"
        **EXPIRES CACHING**

### Remember to save it
Save the file, refresh your browser and you are done.
