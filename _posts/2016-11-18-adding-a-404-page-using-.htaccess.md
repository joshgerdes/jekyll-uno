---
layout: post
title: Adding a 404 page to your website using .htaccess
published: true
---

So, you've designed a great looking and unique 404 error page but what do you do with it?

### What is a 404 page?
A 404 is an error message displayed by the browser to indicate that an internet address cannot be found. I.e. the page does not exist.

### How to include a 404 page in your website's file directory?
Just add the following code to your .htaccess. You will find your .htaccess file in the root folder of your website. (The same folder all your other markup, i.e. index.html, about.html...). If you don't have one, simply create one.

    ErrorDocument 404 /404.html

A 404 page doesn't need to be boring, just check out these [examples](http://www.creativebloq.com/web-design/best-404-pages-812505).