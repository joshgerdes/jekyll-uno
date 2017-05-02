---
title:  "Migrating my blog to Jekyll and GitHub Pages"
date:   2017-05-03
excerpt: "How I moved my blog to Jekyll and Github pages and the lessons I learnt along the way."
---
Over the last 5 years I have been using a blog engine I wrote myself. Its not bad but I'm no designer and I would really like it to have a better style and typography. I also wanted to put the content in GitHub so that if people find mistakes they can [fix them with a pull request](https://github.com/lukemcgregor/lukemcgregor.github.io).

This makes [GitHub pages] (free static site hosting) and [Jekyll](https://jekyllrb.com/) (a static site generator GitHub runs) a great solution for running my blog.

In this article I'm going to talk about my experience with moving to Jekyll and what I liked/disliked about the process.

## Before
![Before]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/old-blog.png)

## And after
![After]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/new-blog.png)


## The Theme
One of the nice things about Jekyll is the number of themes available for blogs. It looks like a lot of people use Jekyll for tech blogs so there are many themes available. In terms of themes you can either use a [bundled theme](https://pages.github.com/themes/), or get a [theme someone else has made](http://jekyllthemes.org) from GitHub and fork it to run your blog.

Bundled themes are pretty nice in that you can set them up very easily, eg in your `_config.yaml`:

``` yaml
theme: jekyll-theme-architect
```

But there is far less selection available. It also doesn't offer a great experience if you want to fix or change things about the theme to suit your use case which I ended up needing to do.

There are thousands of Jekyll themes available on GitHub but I picked [jekyll-uno](https://github.com/joshgerdes/jekyll-uno) by [@joshgerdes](http://joshgerdes.com/2016/jekyll-uno-a-minimal-responsive-theme-for-jekyll/) as I liked the way it looked.

## The upgrade process

Setting up Jekyll and migrating my content was reasonably easy. I spent most of my time refactoring old posts into markdown as many of theme dated back to when I used blogspot.

### Creating a test site

Once I had decided on a theme the next step was to set it up on [GitHub pages]. To do this I forked the Jekyll-Uno repository. By default this creates a repository named `<username>/jekyll-uno`.

GitHub pages requires a repository with a name `<username>/<username>.github.io` in order to create a site at the root of a domain like my blog, so I renamed the repository as above. To do this go to the settings on the forked repository.

![Rename github repo]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/github-rename.png)

**NOTE** After the rename it took a check-in to get GitHub pages to create the site.

### Migrating the content

From here I imported all of my posts (and removed the default one). This meant creating a markdown file for each post in the `_posts` directory. Each post needs to be named `yyyy-mm-dd-name_of_the_article.md`, By default with Jekyll-uno this creates a post hosted at `/jekyll-uno/yyyy/name_of_the_article`. As my old blog was already using markdown this wasn't too bad but some of my older articles were still in HTML so I fixed them up at the same time.


I added support for setting the canonical link for the page, this allowed me to run my blog on github pages before I migrated the URL without having a duplicate content problem. By default the theme does set the canonical link but in my case I wanted this to point back to my old blog. While I imported each post I took care to add a canonical header to ensure if the new site was crawled at `username.github.io` it wouldn't affect the existing content hosted on my blog.

```yaml
canonical: http://blog.staticvoid.co.nz/2012/3/24/entity_framework_comparative_performance
```

Next I corrected the URL structure by setting a baseurl of `''` in the `_config.yaml` file.

**NOTE** jekyll-uno had some bugs around setting an empty baseurl, you will need [this pull request](https://github.com/joshgerdes/jekyll-uno/pull/60) to make it all work properly

The URL structure was slightly different from my old blog which uses `/yyyy/m/d/title` as the format. I quite like just having the year in the URL so instead of re-implementing my old URL scheme I decided to add in redirects from the original URLs to the new ones. To do this I installed a redirection plugin [jekyll-redirect-from]. This allows the addition of front matter to list all of the URLs this page is known by. For some of my older pages this also includes redirects from when I used blogspot.

``` yaml
redirect_from:
  - 2012/3/24/entity_framework_comparative_performance
  - 2012/03/entity-framework-comparative.html
```

### Personalising

I made several modifications to the theme itself to suit what I was wanting for a blog.

The default theme had a very narrow max content width. This means on a large screen the content band is (IMO) too narrow. I upped this from 640px to 800px, which I felt looks a lot nicer especially with the default font size of 16px (which does make it nice to read).

I got rid of the full screen landing page and went directly to the post list. While the landing page looked really nice I didn't think it was terribly functional and as a reader I would just want to see an index. It was also implemented in javascript so if you go to any of the index pages without javascript enabled you see the landing page and cant get access to the actual index. This probably wouldn't have stopped search bots but I don't think it would be great for SEO to have your actual content not visible.


I renamed the 'Blog' button to 'Archive' as without the landing page it makes more sense that you are going to the index of old posts rather than the blog section of a larger site.

Images are by default left aligned, I didn't really like this so I centered everything by default.

There was no default tab width set for code blocks so it used the default 8 wide tabs, this made all my code samples look super indented, so I set a default tab width of 4 on code blocks (which is now settable in CSS3).

``` css
pre
{
    -moz-tab-size: 4;
    -o-tab-size:   4;
    tab-size:      4;
}
```

I customised the look to bring some of my old blog through (like the logo and favicon) and also added a different background image. For anyone who is interested this image was taken at [Lake Louise](https://www.google.co.nz/maps/place/Lake+Louise,+AB,+Canada/@51.4139042,-116.2406884,15.25z/data=!4m5!3m4!1s0x53775d28a0e1ce11:0x3c373c7b6365bce6!8m2!3d51.4253705!4d-116.1772552) in Alberta. I love the snow (which we don't get much of in New Zealand) and this brings back good memories of our trip there a few years ago.

![Lake Louise]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/cover.jpg)


I also did a bunch of minor fixes as pull requests back to the original theme:

 - [Markdown table style](https://github.com/joshgerdes/jekyll-uno/pull/64)
 - [Cache busters](https://github.com/joshgerdes/jekyll-uno/pull/62)
 - [No tags render](https://github.com/joshgerdes/jekyll-uno/pull/61)
 - [Corrected baseurl conventions](https://github.com/joshgerdes/jekyll-uno/pull/60)

It was great to be able to make these fixes back into the original repository.

### Making it live

The next step was to make the new blog live on my real URL. The first step of this was to go to the repository settings in github and set a custom domain.

![Github custom domain]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/github-custom-domain.png)

This makes the github site respond to requests with my blogs URL. The final step was to create a CNAME from my `blog.staticvoid.co.nz` to `lukemcgregor.github.io`. This sends traffic to github instead of my old instance. Once the DNS propagated my blog was now live.

I then made the canonical links point to the new URL scheme (by removing the manual canonical setting on each post). This allows search engines to update their index to point to the new URL scheme avoiding the need for a redirect when someone browses from search results.

### Moving the comments

Given I had changed the URLs for all my posts I also needed to update the paths for Disqus to point old comments to the correct pages. This can be done with the [Diqus migration tool](https://disqus.com/admin/discussions/migrate/). This process was a bit fiddly as the automated mapping tool only respects 30* redirects. As this is a static site when [jekyll-redirect-from] performs a redirect it uses a flat file method (aka meta `HTTP-REFRESH`). This means you need to use a csv mapping old to new URLs which was easiest to compile manually.

### Testing things out
As soon as the blog was live I did a manual test (including some of the redirected links) and checked analytics. This let me know that everything was up and running and I was still getting people visit the blog.

I also have live monitoring on the site with [Uptime Robot](https://uptimerobot.com) which emails me when it goes down. It also tracks some basic performance stats for the blog. It was really nice to see a significant performance boost from moving to a static generated site.

![Uptime and performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/uptime-and-performance.png)

Once the new blog had been live for a few days I took a look at [Google webmaster tools](https://www.google.com/webmasters/tools/) to make sure the site was getting correctly indexed. Organic search accounts for 2/3 of my traffic so I like to do all I can to ensure that my search results in Google are the best they can be.

![Acquisition]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/acquisition.png)

What I saw in webmaster tools was a big jump in the number of pages indexed.

![Indexed pages]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/indexed-pages.png)

This number should ideally equal the number of unique content pages in the static site (eg the number of posts). Unfortunately it was also indexing the redirect pages and navigational pages (index, tags, categories). This is something I will need to correct, as google thinks your site is most awesome when your content is unique and each page adds unique value.

### What's next

There are still a few things I would like to do around my blog itself.

 - Exclude non-post pages from google index
 - Look at what happens if I use [cloudflare](https://www.cloudflare.com) (and perhaps enable https)
 - Take a look at [structured data](https://developers.google.com/search/docs/guides/intro-structured-data) for [blog posts](http://jsonld.com/blog-post/)
 - Add a link to correct issues via a pull request

[jekyll-redirect-from]: https://github.com/jekyll/jekyll-redirect-from
[GitHub pages]: https://pages.github.com
