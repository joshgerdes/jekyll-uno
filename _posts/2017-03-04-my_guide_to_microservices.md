---
title:  "How to Microservice"
date:   2017-03-07
excerpt: "Microservices are a SOA architecture which focuses on breaking a system down into smaller independent systems. I have been working with them for a while and in this series I will look at some of the things I have learnt about how to microservice."
redirect_from:
  - 2017/3/4/my_guide_to_microservices
---
Over the last 5 years I have been working with microservices in some form.

>The microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies. _- [Martin Fowler & James Lewis](https://martinfowler.com/articles/microservices.html)_

As a software system grows it becomes harder to understand the consequences of a particular change. This has the flow on effect of increasing the cost of development in that system and increasing the risk of a failure. There are many strategies to overcome this codebase scaling problem but by far my favorite is microservices. The heart of microservices is building smaller systems which can be easily understood and then composing these systems together into a larger application. Or as one of my colleagues put it

> The secret to building large systems is not to build large systems _- Mark Sargent_

I think that microservices is the best answer we have to building a sufficiently large system. But the practical details of how to go about this can be non trivial. In this series I will look at some of my experiences with microservices and how I approach building them.

### [Microservice or library]({{site.baseurl}}/2017/library_vs_microservice/)

Microservices and libraries both have benefits in terms of providing reusable components. This article looks at the differences between microservices and libraries and looks at why you might choose one over another.

### [Versioning; How to make breaking changes without breaking stuff]({{site.baseurl}}/2017/microservice_versioning;_how_to_make_breaking_changes_without_breaking_stuff/)
Versioning is a tool which allows microservices to gain independence from each other while being able to grow and change. Its critical that when we make changes to a microservice we can do so in a way that we are confident will not break our consumers.

### [Microservice communication]({{site.baseurl}}/2017/microservices-communication-methods/)
Communication between microservices allows us to build complex behaviours out of simple components. Most people tend to think of webservices when thinking of microservices however there are a number of other communication methods which are applicable in different situations.
