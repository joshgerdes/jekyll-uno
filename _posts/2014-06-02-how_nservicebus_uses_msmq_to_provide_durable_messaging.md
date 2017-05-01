---
title:  "How NServiceBus uses MSMQ to provide durable messaging"
date:   2014-06-02
excerpt: "NServiceBus is a great messaging technology, in this post we look at how the message handshaking interacts with MSMQ under the the scenes to provide durable messaging."
redirect_from:
  - 2014/6/2/how_nservicebus_uses_msmq_to_provide_durable_messaging
---
NServiceBus is a great tool and lets us send messages between applications. Messaging allows our communications between processes to be resilient to different types of failures. In this post we are going to look specifically about how NServiceBus uses MSMQ. Its useful to understand the underlying mechanisms used to diagnose and debug your NServiceBus based applications.

NServiceBus has two types of messaging, direct messaging and publish/subscribe messaging. We are going to start off looking at direct messaging as its has less moving parts. When talking about direct messaging what we are talking about is the following where we are sending to a specific destination.

#### Sending to a local queue

Were going to start off looking at what happens when we send a message to a queue on our local machine. The format of such a send command in NServiceBus is something like the below:

``` csharp
bus.Send("service2.input",myMessage);
```

When our process `Service1` gives NServiceBus this message, it serialises the object `myMessage` and gives that to MSMQ. MSMQ will then put that message into a queue on the local machine named `service2.input`. At the other end we may have another process `Service2` running NServiceBus which is listening to the `service2.input` queue and when the message appears deserialises it, executes the handler code and removes the message from the queue. This is the simplest case of sending a message with NServiceBus.

![How NServiceBus uses MSMQ to provide durable messaging]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/how_nsb_uses_msmq_to_provide_durable_messaging%201.png)

If we look at how this works for us for reliability what we see is that as soon as we have sent the message it is persisted to disk. If `Service2` isn't running the message is not lost it simply waits until the service is next available. If `Service2` errors while handling the message (and our queue is enabled as transactional) the message stays on the queue until processing is complete so it isn't lost due to a failure. One of the interesting side effects of this is that messages may be handled more than once in a transactional system if the transaction was not completed before the error occurred.

#### Sending to a queue on another machine

The second scenario we will look at is what if we are sending a message to another machine.


``` csharp
bus.Send("service2.input@machine2",myMessage);
```

MSMQ introduces a new concept in order to deal with this flow; an outgoing queue. For every remote queue a machine sends messages to MSMQ keeps a local outgoing queue. When we send our message MSMQ writes it first to the outgoing queue and it is then transmitted to the remote machine once the transmission is complete the message is removed from the outgoing queue. This means we get the same durability but across the network. If machine 2 is not contactable the message remains in the outgoing queue until it becomes available and has been sent.

![]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/how_nsb_uses_msmq_to_provide_durable_messaging%202.png)

#### Publish subscribe

Publish subscribe is a little more complex as there are two separate flows which occur.

The first is the subscription flow. When you start a subscribing application it sends a message to the publishing application with details of what messages you are subscribing to and the address of the subscribing input queue (where to send the messages to). The publishing application receives these subscription messages and updates its local subscription store (in our case a queue).

![]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/how_nsb_uses_msmq_to_provide_durable_messaging%20subscribe.png)

The second stage occurs when a message is published.

``` csharp
bus.Publish(myMessage);
```

 When a message is published the publisher first checks its local subscription storage and finds a list of subscribers which are interested in the particular published message. It then loops through and sends the message to each of the listed subscribers.

![]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/how_nsb_uses_msmq_to_provide_durable_messaging%203.png)

In the case where a remote machine is subscribed to a message the same flow occurs with the addition of an outgoing queue.

![]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/how_nsb_uses_msmq_to_provide_durable_messaging%204.png)

 So what does all of this mean and why does it matter. By understanding the paths that messages go through debugging your applications becomes much simpler. When you find a message isnt being delivered where you expect you can look in the following places to work out where things went wrong:

 - The subscription storage queue (if its a subscription), make sure your subscriber is listed
 - If sending remotely, the outgoing message queue (with the remote machine offline)
 - The service 2 input queue (with the receiving service turned off)

 I also find some tools are useful to see where things are going. I personally use the windows MSMQ tools (under Services and Applications in Computer Management) [Service Bus MQ Manager](http://blog.halan.se/post/Service-Bus-MQ-Manager-v3-Released.aspx).

 ![Service Bus MQ Manager](http://blog.halan.se/image.axd?picture=2012%2f12%2fmainScreen2.png)
