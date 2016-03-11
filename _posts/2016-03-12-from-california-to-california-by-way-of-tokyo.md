---
title:  "From California to California by way of Tokyo"
date:   2016-03-12 00:00:00
categories: [Tech]
tags: [infrastructure]
description: "The story of a confused request who made it's way from California to Tokyo only to be sent right back to California."
published: true
---

From California to California by way of Tokyo
--------------------------------------------------
The story of a confused request who made it's way from California to Tokyo only to be sent right back to California.

##Here's the problem...
When using one of the Level3 Public DNS resolvers in San Francisco, CA Cloudfront routes the request to an edge node in Tokyo. This means that the request is traveling across the ocean only to come back to the origin server in Northern California (us-west-2 region). This is obviously not an ideal situation and it must be a problem with Cloudfront right!? Wrong... The cause of this issue is actually even more complex than it seems.

##Lets dig in...
We start by configuring a Cloudfront distribution with all Edge locations enabled.

Now lets spin up an EC2 instance in Northern California (us-west-2). We can also just use any ISP in the bay area.
```
ubuntu@ip-172-31-14-87:~$ curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone
us-west-1c
```

Let's see which edge location our new distribution resolves to using a few well known public dns resolvers...
```
ubuntu@ip-172-31-14-87:~$ host -t A alexmgraham.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases:

alexmgraham.com has address 54.192.145.46
alexmgraham.com has address 54.192.145.116
alexmgraham.com has address 54.192.145.39
alexmgraham.com has address 54.192.145.25
alexmgraham.com has address 54.192.145.106
alexmgraham.com has address 54.192.145.36
alexmgraham.com has address 54.192.145.4
alexmgraham.com has address 54.192.145.88

ubuntu@ip-172-31-14-87:~$ host -t A alexmgraham.com 208.67.222.222
Using domain server:
Name: 208.67.222.222
Address: 208.67.222.222#53
Aliases:

alexmgraham.com has address 54.192.145.88
alexmgraham.com has address 54.192.145.4
alexmgraham.com has address 54.192.145.106
alexmgraham.com has address 54.192.145.46
alexmgraham.com has address 54.192.145.36
alexmgraham.com has address 54.192.145.25
alexmgraham.com has address 54.192.145.116
alexmgraham.com has address 54.192.145.39

ubuntu@ip-172-31-14-87:~$ host -t A alexmgraham.com 4.2.2.2
Using domain server:
Name: 4.2.2.2
Address: 4.2.2.2#53
Aliases:

alexmgraham.com has address 54.192.234.126
alexmgraham.com has address 54.192.234.27
alexmgraham.com has address 54.192.234.188
alexmgraham.com has address 54.192.234.83
alexmgraham.com has address 54.192.234.226
alexmgraham.com has address 54.192.234.253
alexmgraham.com has address 54.192.234.23
alexmgraham.com has address 54.192.234.169
```

Now lets check the location of each of those IPs...

**Google DNS:**
All of the cloudfront edge nodes are located in SFO, this is good!
```
ubuntu@ip-172-31-14-87:~$ host 54.192.145.46
46.145.192.54.in-addr.arpa domain name pointer server-54-192-145-46.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.116
116.145.192.54.in-addr.arpa domain name pointer server-54-192-145-116.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.39
39.145.192.54.in-addr.arpa domain name pointer server-54-192-145-39.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.25
25.145.192.54.in-addr.arpa domain name pointer server-54-192-145-25.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.106
106.145.192.54.in-addr.arpa domain name pointer server-54-192-145-106.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.36
36.145.192.54.in-addr.arpa domain name pointer server-54-192-145-36.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.4
4.145.192.54.in-addr.arpa domain name pointer server-54-192-145-4.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.88
88.145.192.54.in-addr.arpa domain name pointer server-54-192-145-88.sfo4.r.cloudfront.net.
```

**OpenDNS:**
We resolve to the same edge nodes as Google DNS... These are of course all still located in San Francisco.
```
ubuntu@ip-172-31-14-87:~$ host 54.192.145.88
88.145.192.54.in-addr.arpa domain name pointer server-54-192-145-88.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.4
4.145.192.54.in-addr.arpa domain name pointer server-54-192-145-4.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.106
106.145.192.54.in-addr.arpa domain name pointer server-54-192-145-106.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.46
46.145.192.54.in-addr.arpa domain name pointer server-54-192-145-46.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.36
36.145.192.54.in-addr.arpa domain name pointer server-54-192-145-36.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.25
25.145.192.54.in-addr.arpa domain name pointer server-54-192-145-25.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.116
116.145.192.54.in-addr.arpa domain name pointer server-54-192-145-116.sfo4.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.145.39
39.145.192.54.in-addr.arpa domain name pointer server-54-192-145-39.sfo4.r.cloudfront.net.
```

**Level3:**
Now this is strange... All of the edge nodes are located in Tokyo. This does not seem right at all, but why is Level3 the only resolver affected by this? The answer will probably surprise you!

```
ubuntu@ip-172-31-14-87:~$ host 54.192.234.126
126.234.192.54.in-addr.arpa domain name pointer server-54-192-234-126.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.27
27.234.192.54.in-addr.arpa domain name pointer server-54-192-234-27.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.188
188.234.192.54.in-addr.arpa domain name pointer server-54-192-234-188.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.83
83.234.192.54.in-addr.arpa domain name pointer server-54-192-234-83.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.226
226.234.192.54.in-addr.arpa domain name pointer server-54-192-234-226.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.253
253.234.192.54.in-addr.arpa domain name pointer server-54-192-234-253.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.23
23.234.192.54.in-addr.arpa domain name pointer server-54-192-234-23.nrt12.r.cloudfront.net.
ubuntu@ip-172-31-14-87:~$ host 54.192.234.169
169.234.192.54.in-addr.arpa domain name pointer server-54-192-234-169.nrt12.r.cloudfront.net.
```

Believe it or not there is actually a good reason for this! 

###How Amazon routes Cloudfront Requests
To the best of my understanding, here's what happens when you attempt to resolve the IP of a Cloudfront distribution.
1. The request is made, and it travels to the DNS Resolver configured on the client node.
2. The resolver responds with a cached request or ends up asking the Authoritative DNS servers for the domain. We could go into detail here but that is a blog post on it's own. The important bit is that we end up asking the authoritative DNS server at some point.
3. Amazon's DNS server makes a best attempt to determine the location of the client and responds with the IPs of the PoP (Point of Presence) with the lowest latency to the client.

This all sounds really simple, but it is actually not simple at all!
- The resolver is the server that makes the request to Amazon, similar to the behavior of a caching proxy.
- Resolvers located all over the world using anycast so you cannot determine the geographical location by simply using the IP address.
- You can determine the real IP of the client if the resolver supports edns-client-subnet.
- If the resolver does not support edns-client-subnet the only choice is to fail back to the resolver IP as the cloest location.

### What is edns-client-subnet and why is it important for public resolvers?
Traditionally, for performance and security reasons, DNS resolvers are typically located in very close geographical proximity to the client making the request. This means that when Amazon is attempting to determine the closest PoP they can pretty safely use the IP of the resolver itself. A new class of resolvers have popped up and they make this assumption less true. Public DNS resolvers are accessible on the Internet and are using anycast IP addresses to route the client to the server with the lowest latency. This means that the client might actually be 1000s of miles away from the resolver. Using the IP address of the resolver is not really a good indication of the nearest edge node for the client but it still should be OK in most cases.
This is where edns-client-subnet comes in to help out. Most public resolvers support edns-client-subnet, which means they pass along the real IP of the client when asking the authoritative DNS server for a response. The authoritative server is able to make it's decision based on the real IP address of the client, this should result in the best possible outcome for the client as they should be served the IPs of a PoP with the lowest latency to them. With a little bit of research we are able to determine that the Level3 public resolvers do not support edns-client-subnet, which is probably why we are seeing interesting results.

### Ok then where is the level3 resolver located... It must be Tokyo right?
Wrong. The level3 resolver that we are hitting is actually located in San Jose, CA

Here's the proof:
```
ubuntu@ip-172-31-14-87:~$ mtr -r 4.2.2.2
Start: Fri Mar 11 06:00:02 2016
HOST: ip-172-31-14-87             Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 216.182.236.108            0.0%    10    0.5   0.5   0.4   0.5   0.0
  2.|-- 72.21.222.20               0.0%    10    0.5   0.5   0.4   0.6   0.0
  3.|-- 72.21.222.16               0.0%    10    1.7   1.7   1.6   1.8   0.0
  4.|-- 54.240.242.146             0.0%    10   72.1 267.7   7.1 933.0 365.4
  5.|-- 54.240.242.133             0.0%    10    1.9   2.0   1.8   2.1   0.0
  6.|-- ae53.edge2.SanJose3.Level  0.0%    10    1.7   2.5   1.7   9.2   2.2
  7.|-- ae-1-60.edge2.SanJose1.Le  0.0%    10    2.5   2.5   2.4   2.6   0.0
  8.|-- ae-1-60.edge2.SanJose1.Le  0.0%    10    2.5   2.5   2.4   3.0   0.0
  9.|-- b.resolvers.Level3.net     0.0%    10    2.2   2.3   2.2   2.3   0.0
```

Lets obtain the IP of the server behind the Anycast address just to be safe... Amazon has some handy troubleshooting utilities for Cloudfront. If we resolve `resolver-identity.cloudfront.net` it will give us back the IP address of the server that Amazon sees making the request. This means that we are able to see the real IP of the server hidden behind the Anycast address.
```
ubuntu@ip-172-31-14-87:~$ host identity.cloudfront.net 4.2.2.2
Using domain server:
Name: 4.2.2.2
Address: 4.2.2.2#53
Aliases:

identity.cloudfront.net has address 216.137.42.23

ubuntu@ip-172-31-14-87:~$ host resolver-identity.cloudfront.net 4.2.2.2
Using domain server:
Name: 4.2.2.2
Address: 4.2.2.2#53
Aliases:

resolver-identity.cloudfront.net has address 192.221.162.8

ubuntu@ip-172-31-14-87:~$ host 192.221.162.8
8.162.221.192.in-addr.arpa domain name pointer DNS-192-221-162-8.SanJose1.Level3.net.

ubuntu@ip-172-31-14-87:~$ mtr -r 192.221.162.8
Start: Fri Mar 11 06:12:25 2016
HOST: ip-172-31-14-87             Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 216.182.236.108            0.0%    10    0.5   1.3   0.4   8.6   2.5
  2.|-- 72.21.222.18               0.0%    10    1.9   1.9   1.8   1.9   0.0
  3.|-- 54.240.243.106             0.0%    10   14.2  16.1   2.2  23.4   7.6
  4.|-- 54.240.243.93              0.0%    10    2.2   2.3   2.1   3.3   0.3
  5.|-- ae-5.r06.plalca01.us.bb.g  0.0%    10    2.3   2.9   2.3   5.4   0.9
  6.|-- ae-15.r02.snjsca04.us.bb.  0.0%    10    3.1   3.4   3.0   4.9   0.5
  7.|-- ???                       100.0    10    0.0   0.0   0.0   0.0   0.0
  8.|-- ae-1-60.edge2.SanJose1.Le  0.0%    10    2.9   3.2   2.9   5.2   0.7
  9.|-- ae-1-60.edge2.SanJose1.Le  0.0%    10    4.0   3.2   2.9   4.0   0.3
 10.|-- DNS-192-221-162-8.SanJose  0.0%    10    2.8   2.9   2.7   4.0   0.0
```
This resolver is definitely not located in Tokyo, it is just a few hops away from me in San Jose, California. My first thought was that Amazon must be making a mistake here, surely you would not want to route traffic from a resolver in California across the ocean and then back again. At this point I decided to open a support ticket with AWS to report this issue.

### Why does Level3 behave like this?
At this point I am still convinced that this is a just a Cloudfront bug. Even without edns support they can see that the resolver is located in San Jose, CA. The solution is simple, they should be routing my traffic to the POP with the lowest latency to the resolver in San Jose, CA. This is where I was wrong!

Amazon support tells me that this is actually the correct behavior because most clients from this resolver are located in Toyko. This makes no sense at all and don't buy it, is AWS lying to me!? A kind Cloudfront engineer hopped on the phone with me after I inquired for a technical explanation for this crazy behavior.

This is where I learned that Amazon also keeps track of the resolver a client is using along with their geographical location whenever they visit an Amazon owned website. This data is then used to make an even better decision about where to route the traffic. Using this data they found that a large majority of users who were using the Level3 resolver in San Jose, CA were actually located in Japan. In fact, there were more people connecting to this resolver from Japan than California. This means that it would actually make more sense for Amazon to respond with the IPs of the POP in Tokyo because a larger percentage of users of this DNS resolver are probably located there. 

Surely Level3 has a resolver in Japan or somewhere nearby... They are Anycasted from everywhere right!?
At the time of this blog post Level3 does not appear to have any DNS servers in japan. I fired up a EC2 instance in Japan to verify this.

From an EC2 instance in Tokyo:
```
ubuntu@ip-172-31-23-29:~$ curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone
ap-northeast-1b

ubuntu@ip-172-31-23-29:~$ host resolver-identity.cloudfront.net 4.2.2.2
Using domain server:
Name: 4.2.2.2
Address: 4.2.2.2#53
Aliases:

resolver-identity.cloudfront.net has address 8.0.22.0

ubuntu@ip-172-31-23-29:~$ host 8.0.22.0
0.22.0.8.in-addr.arpa domain name pointer cns1.LosAngeles1.Level3.net.

ubuntu@ip-172-31-23-29:~$ mtr -r 8.0.22.0
Start: Fri Mar 11 08:07:55 2016
HOST: ip-172-31-23-29             Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- ec2-175-41-192-134.ap-nor  0.0%    10    0.6   0.8   0.6   2.0   0.3
  2.|-- 27.0.0.210                 0.0%    10    2.4   2.4   2.3   2.5   0.0
  3.|-- 54.239.52.174              0.0%    10    2.4   2.7   2.4   3.5   0.0
  4.|-- 54.239.52.140              0.0%    10   12.2   9.3   8.8  12.2   1.0
  5.|-- 54.239.53.33               0.0%    10   15.9  14.9   8.7  19.7   2.8
  6.|-- 54.239.53.80               0.0%    10    9.6   9.1   8.7  10.4   0.3
  7.|-- ae-7.r00.osakjp02.jp.bb.g  0.0%    10    9.5   9.4   9.3   9.6   0.0
  8.|-- ae-1.r22.osakjp02.jp.bb.g  0.0%    10   11.5  15.8   9.1  56.6  14.5
  9.|-- ae-8.r20.osakjp02.jp.bb.g  0.0%    10   14.1  14.5   9.1  24.0   5.4
 10.|-- ae-2.r21.sttlwa01.us.bb.g  0.0%    10  121.3 123.3 121.2 140.5   6.0
 11.|-- ae-2.r05.sttlwa01.us.bb.g  0.0%    10  118.2 118.7 118.2 121.4   0.9
 12.|-- ae-0.level3.sttlwa01.us.b  0.0%    10  130.8 133.7 130.8 158.2   8.6
 13.|-- ae-2-70.edge3.LosAngeles1  0.0%    10  138.5 138.6 138.2 140.2   0.5
 14.|-- ae-2-70.edge3.LosAngeles1 10.0%    10  138.1 138.3 138.1 138.4   0.0
 15.|-- cns1.LosAngeles1.Level3.n 10.0%    10  140.6 139.8 139.5 140.6   0.0
```

This is interesting! There really is not a Level3 resolver in Japan, it's either that or something has gone wrong in network land. Regardless, we are routed to a resolver 140ms away in California which is certainly not ideal.

### How Do we Fix this?
1. The simple solution is to use a public resolver that supports edns-client-subnet or run your own resolver configured to hit the root servers.
2. CDNs who are using Anycast instead of DNS would not be affected by this particular issue because the Anycast IPs are always routed based on latency.
3. Amazon could make this a little more accurate by using real user metrics from my website instead of amazon.com. This would be overly complicated to configure and would still not solve the issue, so I think this would be a waste of time.
4. This is actually a feature and is not a bug. Think about it this way; this is actually improving the performance for a greater number of users in most cases. Users in Japan who are using the Level3 resolver will actually have a better experience. You can argue that this is not true since their DNS server is all the way across the ocean, and you are probably right about that. Their browsing experience would be much better without high latency to the resolver. There are a select few unlucky individuals in California but they can easily fix this by changing their DNS server.
5. Level3 could put some Anycasted resolvers in Japan. If they did this then the clients from Japan would end up hitting the resolvers in Japan and would never be routed to the US. This would give Level3 users in Japan a much better experience and Amazon would recalculate the stats to find that most users who hit the San Jose, CA Resolver were actually located near California.

### What Did I learn from this?
1. Holy crap, doing latency routed DNS is complicated... There are so many things to think about when attempting to route by latency using DNS.
2. If you have concerns about Data leakage due to the edns-client-subnet providing your real IP then don't use a public resolver. Run your own caching DNS server without forwarding and go straight to the root resolvers.
3. If you are using a public DNS server, make sure it supports edns-client-subnet. This is the best way to ensure your Internet browsing performance is optimal.
