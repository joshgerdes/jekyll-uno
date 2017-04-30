---
title: "Cross process communication with queues"
excerpt: "A short introduction to why queueing technologies can be a great way to architect your cross process communication, and a quick look into how NServiceBus can help."
---

###A distributed world
As applications grow and especially get used by larger numbers of users it becomes apparent that scaling and redundancy become critical concerns when developing applications. Vertical scaling (eg a faster server) becomes exponentially more expensive as the load on that server grows. This leads to a need to build applications in a modular and distributed fashion so that they can scale horizontally (eg many small servers).

One of the challenges with distributing your workload is the communication between each of the components. There are many methods for cross process communication, such as web services, RPC, sockets. However in this article I will look at message queues, specifically MSMQ, when to use it and what benefits it specifically gives. I will also give a simple introduction to NServiceBus, one library which you can use with MSMQ.

If web services are the phone calls of the digital world requiring immediate attention and response, queues are the instant messages. By this I mean a message may be dealt with at some point in the future and even if the receiver was busy when the message came in they will get to it and process it eventually.

###Why message queues
Message queues are an asynchronous communication mechanism which allows you to send a message to a destination queue. The message can then be picked up at some point in the future by another process and handled accordingly.

Microsoft implements a message queuing framework (MSMQ) which ships with windows. This is a transactional framework and allows guaranteed (at least once) delivery across a network of messages to other machines. This means if you send a message to a queue on a remote machine it will be delivered even if the remote machine was down at the time of sending the message.

####When not to use a message queue
Message queues are an asynchronous communication mechanism. This means that when you need something to be done immediately, for example a user requesting something on the web, message queues are not a good mechanism. In this example a synchronous mechanism (such as a web service) may be more appropriate.

###A practical example
Unfortunately any simple example using this technology will be a little contrived as it is geared toward larger systems which run across multiple running processes, however I have concocted an example which will demonstrate the technology and you can use your imaginations on where this fits into your real life scenarios.

Concider the following,
