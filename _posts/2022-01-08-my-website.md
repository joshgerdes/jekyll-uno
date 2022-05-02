---
date: 2022-01-08 00:00:00 +1300
title: My Website Setup
author: Luke
categories: [Misc]
toc: false
header:
  teaser: "images/cover.jpg"

---
Pretty simple article today regarding 'My website setup'.

I've had a few people ask what CMS _(Content Management System)_ my website runs on - and no it's not running on an Azure App Service!  
  
I am using:  

* Github Pages (running Jekyll and Ruby on Rails)  
* Cloudflare as my DNS CDN (which also allows me to set HTTPS) and cache the website across the planet  
  
Because the pages are in a git repository, I have version control across my pages, can roll back or make any changes easily and allow others to submit pull requests for changes, or issues natively.  
  
The pages are created using Markdown, I usually have a OneNote page with an idea or blurb, then Forestry to do the initial post, and then manually edit the files and verify the syntax is correct, add tables into the page and fix any issues that may have been caused (Forestry doesn't support markdown tables and can make some content look a bit weird and unstructured, but its usually an easy fix editing the markdown manually).  
  
Having it on Github pages, helped me learn a lot more about using git and source control, versioning methodologies.  
  
Then for comments, I use Disqus and for analytics, Google Analytics and Bing Webmaster Tools.  
  
* [Markdown](https://www.markdownguide.org/getting-started/ "https://www.markdownguide.org/getting-started/"){:target="_blank"}
* [https://pages.github.com/](https://pages.github.com/ "https://pages.github.com/"){:target="_blank"}
* [What CMS is this site using?](https://whatcms.org/?s=luke.geek.nz "https://whatcms.org/?s=luke.geek.nz"){:target="_blank"}
* [https://forestry.io/](https://forestry.io/ "https://forestry.io/"){:target="_blank"}
* [https://disqus.com/](https://disqus.com/ "https://disqus.com/"){:target="_blank"}  
  
All in all - I just have to pay for the domain, everything else is free and because it's stateless, caching content is a lot easier and I don't have to worry about keeping a CMS up to date/patched or a database tuned!  
  
If you're wondering why it's not running on an Azure App Service? I wanted something cheap, could further challenge and learn from, at the end of the day I wanted a stateless website (static websites in Storage account, wasn't available when I set this up) and I wanted to reserve my limited Azure credits to be able to actually learn and play more. I have no regrets in putting it in Github Pages and depending on your requirements - recommend you try it out!  
