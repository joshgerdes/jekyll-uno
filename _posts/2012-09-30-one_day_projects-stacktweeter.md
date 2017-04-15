---
title:  "One Day Projects - StackTweeter"
date:   2012-09-30
canonical: http://blog.staticvoid.co.nz/2012/9/30/one_day_projects-stacktweeter
redirect_from:
  - 2012/9/30/one_day_projects-stacktweeter
---
As professional developers we are encouraged to follow a bunch of patterns and practices for getting the best lifespan out of our applications, stuff like coding for reuse modularity and understandability for those who will perhaps be maintaining our codebases. We follow patterns such as <a href="http://en.wikipedia.org/wiki/Inversion_of_control">Inversion of Control</a>, <a href="http://en.wikipedia.org/wiki/Single_responsibility_principle">Single&nbsp;Responsibility</a>&nbsp;and <a href="http://en.wikipedia.org/wiki/DRY">DRY</a>. All of these patterns help us write and maintain large code bases which can allow our apps to last longer and cause less pain as they change. These principals are great and I am a solid believer in applying them to our applications.<br />
<br />
But sometimes as developers we get bogged down by processes, practices and patterns. We spend lots of time&nbsp;tweaking,&nbsp;re-factoring, tidying, handling every error condition and perfecting our patterns and&nbsp;perhaps&nbsp;forget how to just whip something up in an afternoon, quick and dirty.<br />
<br />
I think its really important to be able to just hack something&nbsp;together&nbsp;quickly without needing to worry about all of the extra bits. Its a rapid prototyping skill we often loose and something I personally should do more often.<br />
<br />
So last weekend I decided to just spend one day writing an app from start to finish. I&nbsp;didn't&nbsp;focus on testing, reuse or&nbsp;maintainability, I just coded until it was working and had a lot of fun. Its a bit like a <a href="http://en.wikipedia.org/wiki/Hackathon">hack day</a> but just for me.<br />
<br />
<span style="font-size: large;">The Concept</span><br />
I spend quite a bit of time on <a href="http://stackoverflow.com/">StackOverflow</a> because I think its a great way to contribute to the development community and plenty of the questions have helped me out personally. One of the things I find hard is to find questions which&nbsp;I'm&nbsp;interested&nbsp;in responding to on&nbsp;StackOverflow.&nbsp;I would also really like to get some kind of notification when there is a question which I care about. So I&nbsp;decided&nbsp;to write a twitter bot which looks at all of the new questions from&nbsp;StackOverflow&nbsp;and tweets any which are in the tags I care about.&nbsp;This also let me play with two APIs I've never interfaced with before (StackOverflow&nbsp;and Twitter).<br />
<br />
Because I'm a bit of an EF guy I made my bot tweet all of the questions tagged with EF relevant tags.<br />
<br />
<span style="font-size: large;">How it works</span><br />
I poll&nbsp;StackOverflow&nbsp;for new questions every&nbsp;minute&nbsp;and when there is a new question. When there is I check each of the tags attached to the question against a database to see if anyone cares about the question. If someone cares I look up the twitter credentials for that user in my database and post the title and a link to that twitter account. This means I can have different topics automatically posted to different twitter bots.<br />
<br />
<span style="font-size: large;">The time</span><br />
I spent around 6hrs on this (start to finish) and most of that time was working out how the two APIs work and finding decent interface libraries.<br />
<br />
<span style="font-size: large;">Build quality</span><br />
The app is by no means high quality, it has no tests and no error handling. Its not terribly stable either as it crashes every few days. But I&nbsp;don't&nbsp;really mind too much (well not enough to actually put in a catch statement).<br />
<br />
<span style="font-size: large;">Was it&nbsp;successful?</span><br />
Absolutely, I use it all the time.&nbsp;I've&nbsp;chained it up with <a href="https://chrome.google.com/webstore/detail/ikknnkomiokeodcdkknnhgjmncfiefmn">Twitter Notifier</a>&nbsp;so that I get a popup within a&nbsp;minute&nbsp;of an EF question getting added to&nbsp;StackOverflow&nbsp;. This also means I&nbsp;don't&nbsp;feel like I need to be constantly refreshing&nbsp;StackOverflow&nbsp;for new questions. And I suppose the main point was to have a bit of fun doing it.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-7ZnxMpJc27A/UGfbYP5SE-I/AAAAAAAAAUw/Ts4tXsVJgbk/s1600/StackTweeter.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-7ZnxMpJc27A/UGfbYP5SE-I/AAAAAAAAAUw/Ts4tXsVJgbk/s1600/StackTweeter.PNG" /></a></div>
<br />
<br />
<span style="font-size: large;">If&nbsp;you're&nbsp;interested</span><br />
If you too are interested in EF questions on StackOverflow, follow my bot on twitter,&nbsp;<a href="https://twitter.com/StkTwtr_EF">@StkTwtr_EF</a>.<br />
<br />
If you want to have your own tags tweeted send me some twitter API keys for an account to tweet to and a list of the tags you want and I'll hack them in there.<br />
<br />
If you want to look at the code let me know and ill put it onto github.<br />
<br />
And most of all go and do an app in a day yourself, have fun and tell me how it works out.
