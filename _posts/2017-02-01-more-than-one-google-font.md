---
layout: post
title: Loading more than one Google font in one request
published: true
---

Loading more than one Google font in one request can help to speed up page load time and keep your code tidy.

### How is it done?
In the head of your HTML add:

    <link href="http://fonts.googleapis.com/css?family=Lato:300,400,400italic,600,700|Raleway:300,400,500,600,700|Crete+Round:400italic" rel="stylesheet" type="text/css" />

This is the recommended best practice on all websites. It is simple to implement and will help web pages to load just that little bit quicker.
