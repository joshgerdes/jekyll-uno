---
title:  "Manual decisions are the the enemy of consistency"
date:   2016-10-11
excerpt: "On why continuous deployment is better than continuous delivery"
redirect_from:
  - 2015/10/8/when-deploying-decisions-are-liabilities
---
Many of our modern software development methodologies focus on short iteration loops to be able to quickly and safely change and build our software. These iterative methodologies work particularly well with our modern SaaS and automatically deployed applications. Iterative development allows us to fail earlier and fix issues faster. I'm a believer.

Many organisations adopt some form of continuous delivery whereby as code is checked in, it is tested and packaged for deployment. It may then go through various test and pre-production environments for further manual or automated testing. Deployment is done by someone (normally a developer) pushing that package into production. We are the masters of the system so we know that this deploy will work, we got this, it's all good, Ship it.

![Ship it](http://i.memecaptain.com/gend_images/zyCwXg.jpg)

The problem is that we often aren't the masters we think we are. I have often found (and I'm sure you have too) situations where the decision to deploy was wrong because we did not take into account some obscure failure condition. These often seem to originate from system interop not necessarily the lines of code we are so sure are ok. This really sucks.

We must have made a mistake, we will do better next time I promise. We now understand the system a bit better, its all good now. Just watch this deploy will go OK...

The problem here is that we as humans, and especially developers are ill equipped to perform the kind of checks necessary to deploy a piece of software. These checks are really a collection of many years of requirements and interop. We can at best check only a small portion of the system if we want to keep our iterations short. Worse than that we have a nasty habit of not checking things we are sure will be fine. The net effect is that we may be able to pick up problems with obvious interactions but we are terrible at finding obscure interaction problems or issues with unexpected areas of the system.

**If we want to deploy consistently stable software we need to take the human element out of deployment.**

This means automating the decision to put code into production (continuous deployment). If that thought currently scares you it's probably because you don't have confidence in your automated testing. The problem is that it's very hard to be confident in your automated test suite before you give it any formal responsibility.

So how do you go from fear of automating deployment to confidence?

The first thing to realise is that automated tests don't need to be perfect, they just need to be better than the tests you would do. Start building up your automated tests with the goal that they will replace your decision on deployment, check out my article on [Useful Tests](http://blog.staticvoid.co.nz/2015/5/28/useful_tests) for some ideas about what your tests should include.

The next step is to keep a journal of the state of the tests vs your decisions about deployments. Every time your tests are green but you decided not to deploy is an example of a place you may be missing an automated test. By keeping a journal you will gain confidence that your tests are picking up issues which could prevent a stable deploy. When the tests status always matches your deployment decision you are ready for continuous deployment. After you are doing continuous deployment you can measure the success of the system by comparing your journal of deployments pre and post.

Manual decisions are the the enemy of consistency.
