---
title:  "The Authentication Proxy"
date:   2016-11-16
excerpt: "When we break down systems duplication and boiler plate drastically increases complexity. Authentication is one area where complexity can be introduced across all of our services at once. In this post I look at a pattern to decouple authentication from your system and allow a richer authentication experience without introducing complexity to every API in the system."
redirect_from:
  - 2016/11/16/the_authentication_proxy
---
SOA and Microservices promote API centric applications where we can build complex sophisticated systems out of smaller simpler ones. This allows us to build bigger and less error prone systems by enabling developers to better understand the impacts of a change. When we break down systems duplication and boiler plate drastically increases complexity. Authentication is one area where complexity can be introduced across all of our services at once. In this post I look at a pattern to decouple authentication from your system and allow a richer authentication experience without introducing complexity to every API in the system.

### Multiple authentication paths

As applications grow many different types of consumers may use APIs. Different consumers have different needs and authentication methods which work well. For example a website may consume your API and it makes sense to use cookies to do so. An automated process may also consume the API and it might make sense to use an API Key type of authentication for that use case. A native mobile application may use OAuth or JWT directly to consume your APIs.

Each of these scenarios make sense internally but having multiple authentication mechanisms across our APIs make things complex. This gets worse as we have more APIs in our system, especially if they are deployed independently.

#### Authentication is a global concern authorisation a local one

Authentication is essentially the same anywhere throughout our applications, identifying **who** is using the system is a global concern across the whole system. Allowing access to certain functions on the other hand is a local concern which can only be decided by the function which is currently being executed. Authorisation is not about who but rather about can some(one/thing) like this do that. This is a subtle but important distinction.

These concerns should be separated and dealt with at the appropriate scope.

## The Authentication Proxy
The authentication proxy pattern separates the global concern of Authentication from the local concern of authorisation by intercepting all requests to APIs and replacing the specific by reference authentication with a standardised by value claims based token. This means that individual APIs need only validate and check authorisation on one token type.

![Authentication proxy]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/authentication-proxy.png)

The authentication proxy has the following behavior/pseudocode

 1. Receive request
 2. Decode authentication used by caller
 3. Produce relevant claims for the authenticated user
 4. Replace the Authentication on the incoming request with a signed set of claims (eg JWT by value)
 5. Forward the request to the API implementation
 6. Send the response back to the caller

### By reference and by value

There are two different types of authentication token, each has their place. By reference tokens simply have a key contained in the token which needs to get looked up server side to get the actual permissions, they are opaque meaning only the server understands the actual information this token contains. By value tokens contain information directly within the token, this means if the token contains the information you need you don't need to look up any information later. By value tokens can either by opaque or transparent depending on if they are encrypted or signed. By reference tokens are tiny, but require a second lookup stage and by value tokens are bigger but avoid subsequent lookups.

By reference tokens are useful when they are appended onto every request and bandwidth is important. There is no point transmitting lots of information when a little could do. By value tokens are better when we want to remove a lookup later in the system. With the authentication proxy it makes sense to use by reference tokens externally and by value tokens internally (where bandwidth is less relevant).

### Authorisation

The API implementation can then ignore the actual user lookup and authentication handshake and simply examine the claims to authorise a behavior. For example instead of looking up the user ID and seeing if they are assigned the edit blog post permission we can simply check the claims to see if they have an edit blog post claim. This scales far better especially if we have non-user things in our system as well (such as an API key) which may use an entirely different permission model.

More importantly that user lookup component (which previously had to be in every API) can now be performed centrally decoupling the permission tree from every API.

### Routing

Routing is an important component when multiple APIs are at play, how does the authentication proxy know where to send the request. There are many ways to approach this problem but I like the following the best.

Get your API proxy to receive requests for api.example.con, reserve all subdomains for your actual APIs (it's important that you control the DNS lookup of `*.api.example.con` from your proxy machine for security reasons). Then use the first segment of the url to select the API subdomain to use. eg a request for [https://api.example.con/posts/v1/edit](#) might get routed to the API [https://posts.api.example.con/v1/edit](#). This kind of URL routing is readable and presents a contiguous api front to consumers. In this example there is no need to publish the posts.api.example.con API publically, only the proxy needs to be able to access it directly. However in some cases it may be desirable to allow APIs to call each other internally as well as the authentication proxy.

###Costs
As with any proxy system the Authentication proxy introduces synchronous latency into your applications, [Latency is not zero](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) so it is important to understand, measure and minimise the impact of this on your application. While the request overhead may not be controllable in this pattern there are several techniques you can use to minimise latency.

Tip 1:
Host the APIs on the same server as the proxy, and always request the instance of the API running on the local machine. This essentially removes the network cost from the latency. You can then load balance the proxy which will in turn load balance the APIs. Do note when you deploy an API you will also need to take the proxy out of the load balancer during the deploy to avoid a failure.

Tip 2:
Introduce caching on your claims generation. The generation step is probably the most costly part of the proxy and by caching this lookup you can remove time out of your requests. If you weren't previously caching the authentication check in your application this may well improve performance overall. Do note you will also need a good invalidation mechanism.
