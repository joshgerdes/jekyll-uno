---
title:  "One Day Projects - StackTweeter"
date:   2012-09-30
excerpt: "While patterns and practices are an important part of producing quality software, its important that as developers we don't just blindly follow such patterns. Having a hack day and breaking some rules is a great way of having some fun and learning to work outside some of our regular practice. This is my hack day making a twitter bot to tweet Entity Framework questions from Stack Overflow."
redirect_from:
  - 2012/9/30/one_day_projects-stacktweeter
  - 2012/09/one-day-projects-stacktweeter.html
---
As professional developers we are encouraged to follow a bunch of patterns and practices for getting the best lifespan out of our applications, stuff like coding for reuse modularity and understandability for those who will perhaps be maintaining our codebases. We follow patterns such as [Inversion of Control](http://en.wikipedia.org/wiki/Inversion_of_control), [Single Responsibility](http://en.wikipedia.org/wiki/Single_responsibility_principle) and [DRY](http://en.wikipedia.org/wiki/DRY). All of these patterns help us write and maintain large code bases which can allow our apps to last longer and cause less pain as they change. These principals are great and I am a solid believer in applying them to our applications.

But sometimes as developers we get bogged down by processes, practices and patterns. We spend lots of time tweaking, re-factoring, tidying, handling every error condition and perfecting our patterns and perhaps forget how to just whip something up in an afternoon, quick and dirty.

I think its really important to be able to just hack something together quickly without needing to worry about all of the extra bits. Its a rapid prototyping skill we often loose and something I personally should do more often.

So last weekend I decided to just spend one day writing an app from start to finish. I didn't focus on testing, reuse or maintainability, I just coded until it was working and had a lot of fun. Its a bit like a [hack day](http://en.wikipedia.org/wiki/Hackathon) but just for me.

### The Concept
I spend quite a bit of time on [StackOverflow](http://stackoverflow.com/) because I think its a great way to contribute to the development community and plenty of the questions have helped me out personally. One of the things I find hard is to find questions which I'm interested in responding to on StackOverflow. I would also really like to get some kind of notification when there is a question which I care about. So I decided to write a twitter bot which looks at all of the new questions from StackOverflow and tweets any which are in the tags I care about. This also let me play with two APIs I've never interfaced with before (StackOverflow and Twitter).

Because I'm a bit of an EF guy I made my bot tweet all of the questions tagged with EF relevant tags.

### How it works
I poll StackOverflow for new questions every minute and when there is a new question. When there is I check each of the tags attached to the question against a database to see if anyone cares about the question. If someone cares I look up the twitter credentials for that user in my database and post the title and a link to that twitter account. This means I can have different topics automatically posted to different twitter bots.

### The time
I spent around 6hrs on this (start to finish) and most of that time was working out how the two APIs work and finding decent interface libraries.

### Build quality
The app is by no means high quality, it has no tests and no error handling. Its not terribly stable either as it crashes every few days. But I don't really mind too much (well not enough to actually put in a catch statement).

### Was it successful?
Absolutely, I use it all the time. I've chained it up with [Twitter Notifier](https://chrome.google.com/webstore/detail/ikknnkomiokeodcdkknnhgjmncfiefmn) so that I get a popup within a minute of an EF question getting added to StackOverflow . This also means I don't feel like I need to be constantly refreshing StackOverflow for new questions. And I suppose the main point was to have a bit of fun doing it.

![StackTweeter]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/stack-tweeter.png)


### If you're interested
If you too are interested in EF questions on StackOverflow, follow my bot on twitter, [@StkTwtr_EF](https://twitter.com/StkTwtr_EF).

If you want to have your own tags tweeted send me some twitter API keys for an account to tweet to and a list of the tags you want and I'll hack them in there.

If you want to look at the code let me know and ill put it onto github.

And most of all go and do an app in a day yourself, have fun and tell me how it works out.
