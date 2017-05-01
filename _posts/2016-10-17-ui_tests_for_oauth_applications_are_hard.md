---
title:  "UI tests for OAuth applications are hard"
date:   2016-10-17
excerpt: "A look at the issues I faced writing UI tests for dotdev and why I built NoAuth to make testing easier"
redirect_from:
  - 2016/10/17/ui_tests_for_oauth_applications_are_hard
---
Automated testing systems with authentication is tricky. You need to make fake users and let them login to your system or fake the token itself. This is even harder if you are using OAuth systems.

For [DotDev](https://dotdev.io) I have a set of UI tests that cover many common actions that users perform on the site. It's important to have several user accounts to test all of the different scenarios. In addition account creation and login is an important aspect which I want to prove against every deployment.

As I do not provide any local login to the site I had to create dummy social accounts. This doesn't seem too bad but all of the social providers I used have measures in place to prevent bot logins. This made my tests unstable and frustrating to manage.

### The alternatives aren't great

At this point I had two options to try and resolve the issues with UI Test logins.

**To build a new way of logging in users for my tests which bypassed OAuth.**

This would have been a bit of work, but more to the point it would have been work which had no relevance outside of testing. It also would obscure several critical login systems which I specifically want to test.

**Find a provider which did not do all of the bot prevention stuff**

This seemed like a better option however It was very hard to find a provider fitting this description. It's not the kind of thing that a provider would list about themselves and it would have been trial and error to find one. To spite this I tried a few, all of which I eventually discovered had some annoying countermeasure.


Enter NoAuth
------------

I felt the second option was still the right answer to this problem. So I decided to do a mini project to write my own OAuth provider specifically for testing.

NoAuth is an OAuth provider for testing which offers no security guarantees at all. You can log in with any claims you like without the hassles of passwords or security checks.

![noauth](http://i.imgur.com/uIakt9N.png)

During your login loop instead of being prompted for a username/password you can enter in a list of claims you want to make. Alternately you can populate a random user from [RandomUser.me](https://randomuser.me/) (which is super awesome by the way). This allows for quick and easy creation of test users with some realistic data, and the ability to test some more complex login paths by using different claims.

**NoAuth is [open source](https://github.com/lukemcgregor/noauth) and avaliable to use for testing your own sites.**

In addition to the actual OAuth site, I have build [owin bindings](https://www.nuget.org/packages/Owin.Security.Providers.NoAuth) to easially integrate noauth into a .net application and some [Selenium helpers](https://www.nuget.org/packages/NoAuth.Selenium) to make using noauth in your tests easy. I would love some pull requests for integrations with other languages.

I hope it goes without saying, but **do not use noauth in production** or you're gunna have a bad time.
