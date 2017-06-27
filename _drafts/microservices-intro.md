Over the last 5 years I have been working with microservices in some form.

>The microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies. _-- [Martin Fowler & James Lewis](https://martinfowler.com/articles/microservices.html)_

As a software system grows it becomes harder to understand the consequences of a particular change. This has the flow on effect of increasing the cost of development in that system and increasing the risk of a failure. There are many strategies to overcome this codebase scaling problem but by far my favorite is microservices. The heart of microservices is building smaller systems which can be easily understood and then composing these systems together into a larger application. Or as one of my colleagues put it

> The secret to building large systems is not to build large systems _-- Mark Sargent_

I think that microservices is the best answer we have to building a sufficiently large system. But the practical details of how to go about this can be non trivial. In this series I will look at some of my experiences with microservices and how I approach building them.

## Microservice or library

Microservices and libraries both have benefits in terms of providing reusable components. This article looks at the differences between microservices and libraries and looks at why you might choose one over another.

## When should I start?

- dont start too soon but dont leave it too late.

## What size?

- not too big not too smaller
- Too big = takes a developer more than a day to pick up the service and confidently make a change.

## Deployment independence

One of the critical traits of a microservice is that each service can be deployed without requiring other services to also be deployed at the same time. This is incredibly important

## Versioning

Interface versioning is vital for successful microservices.

## What can/cant they do?

## How can they communicate?

## How much should I know about consumers?

## Deployment

## Failure

## Scale

## The microservice social contract
