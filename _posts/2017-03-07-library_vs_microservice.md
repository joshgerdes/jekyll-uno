---
title:  "Library vs microservice"
date:   2017-03-07
excerpt: "Microservices and libraries both have benefits in terms of providing reusable components. This article looks at the differences between microservices and libraries and looks at why you might choose one over another."
redirect_from:
  - 2017/3/7/library_vs_microservice
---
Both libraries and microservices provide a way of providing a functionality behind a versioned interface. In the case of a microservice the versioning needs to be supported by the service on its external interfaces (eg versioned messages or apis), in the case of a library the version is applied by the version of the package. In each case we have decoupled functionality.

Each method has particular advantages and scenarios which it suits best.


### TL;DR

![Library or Microservice]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/library-or-microservice.png)

### Opt in vs automatic updates

Libraries and microservices have one defining difference which is who makes the decision to change the running implementation. In the case of a library the consumer opts for a new implementation, in the case of microservices the provider provides a new implementation at will (hopefully) meet the previous version contracts.

To use an analogy a microservice is similar to a SaaS application whereas a library is like an installed application.

### Globally vs internally consistent implementation

Microservices provide a consistent implementation for all consumers at any given time. This means that changes to the implementation are immediately applied everywhere.  However if an application makes two calls to a microservice the implementation may differ between these calls. In contrast two calls to the same library are guaranteed to use the same implementation, however two applications using the same library are not guaranteed to be using the same implementation.

To look at it another way if you want repeated calls to return the same result then a library is the best answer, however if you want all consumers to receive the same result then a microservice is best.

### Versioned vs unversioned internal persisted state

Internal state is state which is used by the implementation, not passed by the caller and shared between all instances of the implementation (for example data in a database). For a library to use internal state it must be backward compatible with all previous versions, so that any version of the implementation can write valid state. This practically means that any new data added by new implementations must be nullable, and old data cannot change its format. In my opinion this restriction means that it's best not to use internal persisted state with library code. If you require persisted state get it passed in by the caller, who is responsible for handling any version mutations.

In comparison microservice can have un-versioned internal persisted state without causing an update problem when changing the representation of that state. This allows a microservice to confidently change its internal state representation without breaking any of the consumers of the service.

In my opinion this is the biggest separator of microservices and libraries.

### Failure conditions

Libraries and microservices have different failure conditions. These largely depend on the transport used to consume the microservice. In most cases a library will have far fewer failure scenarios as microservices have more moving parts (for example web servers, other running processes etc.) however if you are using asynchronous communication (such as messaging) microservices have some benefits in terms of failure scenarios. For example if an error occurs in a library the consumer must handle that failure, however if an error occurs inside a microservice consuming a message, the message can be deferred and replayed automatically allowing the error to be resolved rather than handled. This can be a big benefit in some scenarios.

If your microservice uses synchronous communication (such as http), it is exposed to many more failure conditions, such as what do you do if its is unavailable, slow, or there is some kind of infrastructure issue.


### Low overheads vs horizontal scaling

Libraries naturally have lower overheads as they operate without requiring serialisation and other cross process/machine costs which microservice transports are subject to. While there are techniques to mitigate these costs, microservices will always have some kind of overhead which may affect synchronous communication. However when it comes to asynchronous communication microservices allow the processing to be spread across multiple machines easily which gives a horizontal scaling characteristic.
