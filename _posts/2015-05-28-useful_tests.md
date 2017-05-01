---
title:  "Writing valuable automated tests"
date:   2015-05-28
excerpt: "When I started working for myself on dotdev I spent quite a bit of time thinking about testing, and test automation as it's likely the only barrier between me missing something (which humans do) and that bug going live and annoying people. So I designed my test strategy around taking me missing things out of the picture (ie automation). Below are some of my thoughts around good and bad tests and how to get the best bang for your time when building automated tests."
redirect_from:
  - 2015/5/28/useful_tests
---
When I started working for myself on [dotdev](https://dotdev.io) I spent quite a bit of time thinking about testing, and test automation as it's likely the only barrier between me missing something (which humans do) and that bug going live and annoying people. So I designed my test strategy around taking me missing things out of the picture (ie automation). Below are some of my thoughts around good and bad tests and how to get the best bang for your time when building automated tests.

Over the years I have worked on a bunch of projects having all kinds of test strategies, from no tests to manual tests mountains of automated tests. I have come to the conclusion that good testing is a bit of an art and (like most things) there is certainly no check list you can follow to the ideal tests. So instead I'm going to talk about some principals which have helped me.

### Be deliberate about *why* you are testing

Don't just test because it's a good thing to do, test to avoid some specific things. This will make your tests more valuable and potent.

For dotdev I have the following goals (in order):

1. The URL http://dotdev.io always returns a successful status code
2. Never have a whole site outage as a result of a deploy
3. Scenarios are always viewable
4. You can login
5. Proposing a scenario always works
6. Suggesting a tool always works
7. Comments, pros and cons and votes are all usable
8. noscript users get fully rendered pages (for SEO)

If I introduce bugs to do with any of these it will have a major frustration impact, so this is what I want to prove works when running my tests.

### Prove the important things

If you are expecting your automated tests to catch everything, you're in for some disappointment (no matter how many tests you write).

It's far better to prove that some important use cases are still achievable. This wont make you bug free [but hardly anyone will notice them](http://en.wikipedia.org/wiki/Pareto_principle).

![](http://i.stack.imgur.com/ifOwg.gif)

### Common usage scenarios over edge cases

Edge case testing can be important but it's not as important to automate. You are much more likely to stop a major issue by testing common scenarios than edge cases. Edge case bugs are likely to affect fewer users.

### Automated tests are (mostly) cheaper than manual

As with most things if you have to do something more than a few times you will save time by automating it.

### Delete bad or unimportant tests

If it isn't helping it's hurting. Get rid of it.

### Don't test your add function

The classic unit test example is testing an add function. It's a good example of how tests work but in reality testing things that are too simple doesn't prove anything important. If it's easier to look at the code and tell at a glance if it's wrong eg <code title='ahh&nbsp;good&nbsp;you&nbsp;spotted&nbsp;it'>add(a,b){ return a * b; }</code> this isn't worth your while testing (or writing).

### Each test is expensive, be frugal

One of the things I have noticed, especially on larger projects is that the time spent on tests is mostly not on writing them, or even on dealing with failures, it's on keeping them up to date. Code changes, assumptions change, and tests inevitably need updating over time. If that test is not proving something important the question needs to be asked, *is it worth it?*

Just like with all code, write no more than you have to to prove what you need to.

### At the very least, integration test

On dotdev my most important test is a ping to my site every few minutes to make sure I don't get an error code. This takes 2 minutes to set up (check out [Dotdev: The best tool to tell me when my website goes down](https://dotdev.io/scenario/61/the-best-tool-to-tell-me-when-my-website-goes-down)). Every site you run should have this level of monitoring.

Following that my most important tests prove that the deploy I'm about to do is functional in basic usage scenarios. For this I use [Selenium](http://www.seleniumhq.org/) and [Azure site swap](https://azure.microsoft.com/en-us/documentation/articles/web-sites-staged-publishing/) to test the running instance I'm about to swap into production.

### Don't forget to run them

No matter what kind of testing you are doing the most important thing is that you are running your tests. Build them into your CI/CD processes.

It's well worth making it impossible to release your software when tests are failing.

If you have manual tests make sure these have been done before a deploy and there is a suitable audit trail.

### Trust your tests

Whatever tests you decide to do you need to have faith in them. If you are second guessing if your application will run when someone uses it you probably need different tests.

If you have automated tests, ask yourself this *would I be prepared to release without ever looking manually at the application?* What about releasing every build which passes the test? If not, what scares you? Put the scary things on your test goals.
