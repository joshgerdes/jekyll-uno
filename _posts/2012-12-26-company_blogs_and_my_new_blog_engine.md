---
title:  "Company blogs and my new blog engine"
date:   2012-12-26
excerpt: "Blogs are an important way we as developers can contribute to the development of our industry and grow our own personal skill sets. For this reason I believe development companies should invest in blogging as a way of developing their employees. This software is about doing this in a way that promotes writing for personal blogs as well as a company blog."
redirect_from:
  - 2012/12/26/company_blogs_and_my_new_blog_engine
---
As you guys may have seen I have a brand new blog engine, which I've just finished building. Its been a pretty interesting journey to get to the point of writing my own blog engine but I thought I might share a little of why I wrote this blog engine and what it does differently.

I've been blogging some of my technical discoveries for a few years now and its been a really rewarding experience for me, both in helping me get to a deeper level with the technology I work with and also giving back to the development community as a whole. Its definitely something which I personally find valuable and a key part of growing my own technical expertise.

One of the things I have been really keen to do is to help the company I work for ([Enlighten Designs](http://www.enlighten.co.nz/)) encourage blogging as a way of getting in touch with our local development community and building our reputation as passionate developers. As part of this I have been planning to start an Enlighten Technical Blog, to showcase the work and discoveries of our own developers and encourage writing as a way of expressing our enthusiasm for development.

I feel that a key factor for the success of a company blog is to share the benefits of blogging between both the author and the company itself. One of the ways to do this is to allow content articles to be re-posted from a company blog to a personal blog, and vice versa. By doing this we can allow the authors credit and recognition for their content and a personal reputation (via their own personal blog) while still showcasing the company as a whole and the development skills of the whole organisation. Historically however this has been a bit of a no-no in terms of SEO due to [Duplicate Content](http://support.google.com/webmasters/bin/answer.py?hl=en&answer=66359) penalties.

### Syndication and *rel="canonical"*
Replicating content across multiple sites is referred to as syndication and up until recently there was no way of doing it without incurring some kind of duplicate content penalty. However recently Google decided to allow cross-site rel canonical links. These indicate to the search crawler the authoritative source of a pages content. This effectively means that Google will attribute search rankings to the original page over the copied content. This is really important for our syndicated content as it means that if we share our content we are unlikely to suffer any negative side effects, and may actually get a boost to our SEO ranking from the linking. This is great news as it means that sharing content between our personal and company blogs can be good for both parties.

### Markdown
Markdown is great, as a developer I really like writing in markdown as a web editor. I especially like that if the formatting I need isn't built in I can just use HTML inline to get what I'm after, and of course some great sites which I use regularly (StackOverflow and Github) are also heavily markdown based. For this reason it was important to me that when writing articles I'm still able to use this great edit tool. Below is a little of how this editor works in my blog engine. The engine also has an instant preview window so I can get a good idea of how stuff looks.

![Markdown Editor]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/markdown-editor.png)

### Redirects and URL manipulation
A key requirement for me was that all of the links from my old blog still worked when I changed over to the new software. This means that I either needed to use the same URL structure or build in a redirect engine. I chose the latter as it gives me more options in terms of URL structure and allows me to be able to customise URLs after posting an article.

### Great Plugins
There are some awesome pre-made plugins for developing websites, and I used a few developing this software. Stuff like [Bootstrap](http://twitter.github.com/bootstrap/), [DotNetOpenAuth](http://www.dotnetopenauth.net/), [Disqus](http://disqus.com/) and [Google Analytics](http://www.google.com/analytics/) save a lot of work and provide great solutions to common web problems. By using these I was able to greatly reduce the work required.

### Azure
I have been wanting to give Azure a go for a while but up until now hadn't had a particularly good use case. But given most of my readers are in the US I thought this would be a great opportunity. I was really impressed at how easy Azure has been to get going, and it has some great management tools for running web applications and databases. I was particularly impressed with how easy and intuitive it was to build and deploy my site automatically from github. It took under 15 mins to go from not getting an account to having a working site with automated deployment and I didn't even need a tutorial.

### Use it Yourself
As with most of my @home work this software is open source (under [LGPL](http://www.opensource.org/licenses/lgpl-3.0.html)) and [available via Github](https://github.com/lukemcgregor/StaticVoid.Blog). The admin section isn't polished (but it is functional), and there's plenty more to add, so fork it and let me know what you think.
