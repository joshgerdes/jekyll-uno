---
layout: post
title: Remove url extensions from static site pages using .htaccess
published: true
---

So you have built yourself a static website, uploaded the files to your favourite host and deployed it. You think it looks great but there is one thing that is still bothering you. 


### What can you do about it?
My preferred solution is to write a short bit of code and save it in my .htaccess. Please note that your server must be able to run Apache for it to work. I use Bluehost.


### What is the URL Extension?
At the end of each page url there is what we call a url extension illustrated in bold below.

    Example: www.mywebsite.com/about.html
    
### How to remove it using the .htaccess file

Open up your .htaccess file from the root of your website and enter the following code:

You will find your .htaccess file in the root folder of your website. (The same folder as all your other markup, i.e. index.html, about.html…). If you don’t have one, simply create one.

    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^([^\.]+)$ $1.html [NC,L]
    
This bit is a little inconvenient but you will now need to go into your markup and rewrite your hyperlinks excluding the extension .html. The line in the code above 'RewriteRule ^([^\.]+)$ $1.html [NC,L]' requests that all extensions of '.html' are removed from the display url. So all your navigation link HTML will need to look something like this:

#### Correct

    <li><a href="http://www.mywebsite.com/home">Home</a></li> or
    <li><a href="about">About</a></li>..
    ....................................
    
#### Incorrect

    <li><a href="http://www.mywebsite.com/home.html">Home</a></li> or
    <li><a href="about.html">About</a></li>..
    ....................................