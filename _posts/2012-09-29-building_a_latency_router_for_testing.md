---
title:  "Building a latency router for testing"
date:   2012-09-29
excerpt: "In my previous post I tested the effect of latency on MSSQL insert performance. This post discusses how I built my test harness which allows me to test with multiple levels of latency from the same application."
redirect_from:
  - 2012/9/29/building_a_latency_router_for_testing
  - 2012/09/building-latency-router-for-testing.html
---
I recently needed to test SQL insert performance under latency scenarios. As part of this I needed a good way of introducing latency between my test harness and database server. I also wanted to control the latency and if possible have a way to run several different levels of latency at the same time. To do this I built a latency emulating router with Ubuntu server and IPTables.

I decided to set up create the router with a bunch of network interfaces and apply a different level of delay to each interface. What this means is that based on which IP address I accessed my SQL box with the connection was delayed by a set amount of latency.

![Latency router]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/latency-router.png)

I found this approach to work really well for me so I thought I would do a bit of a write up on how I went about it.

The 5 step program to artificial latency:

### Step 1

Setup your VM with a bunch of NICs (in my example I used five 1 for an entry point and four for different amounts of latency)

### Step 2

[Install Ubuntu Server](http://www.ubuntu.com/download/server) (I just used the latest version from the Ubuntu site) and make sure each of your NICs has an address on a separate subnet (I made each subnet the amount of latency that network would provide)

You can modify your network configs by editing the following:

``` bash
sudo nano /etc/network/interfaces
```

For example to setup eth1 (my second network card) to run subnet 10.1.5.0/24 I used the following config:

```
iface eth2 inet static
	address 10.1.5.1
	netmask 255.255.255.0
	broadcast 10.1.5.255
	network 10.1.5.0
```

### Step 3

Setup some routing. This means that when we send traffic via our router which we want to go to a specific subnet it will know which NIC to push that traffic out through. Below is a rule to route traffic from 10.1.1.0/24 to 10.1.5.0/24:

```
sudo iptables -t nat -A POSTROUTING -s 10.1.1.0/24 -d 10.1.5.0/24 -j SNAT --to 10.1.5.1
```

Once all of your rules are setup you can save them (so they persist over a reboot) using the following:

```
sudo apt-get install iptables-persistent
sudo iptables-save > /etc/iptables/rules.v4
```

### Step 4
Set up your server and client to route through the router. In windows on my local PC I added in a route to send data bound for my latency network to the latency router. You can do this from an administrator command prompt with:

```
route ADD 10.1.5.0 MASK 255.255.255.0  10.1.1.3
```

This will send all traffic bound for 10.1.5.0/24 to my routers address on my subnet (10.1.1.3).

On the server end I simply added a new NIC on the 10.1.5.0/24 subnet with an address of 10.1.5.10.

Once you have this configuration you should be able to run a ping to test your routing, and you should get something similar to the below:

``` text
Pinging 10.1.5.10 with 32 bytes of data:
	Reply from 10.1.5.10: bytes=32 time >1ms TTL=127
	Reply from 10.1.5.10: bytes=32 time >1ms TTL=127
	Reply from 10.1.5.10: bytes=32 time >1ms TTL=127
	Reply from 10.1.5.10: bytes=32 time >1ms TTL=127
```

Awesome we have connectivity. Its important to note here the path that our data will follow, especially because it may not be what you are expecting.

![Response path]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/response-path.png)

This is because when we request the routing tells us that because we are sending it to a different subnet it should go through our router but when we respond our SQL box is already part of the destination subnet so doesn't need to route the message at all.

### Step 5

The last thing we need to do is to set up the latency. This turns out to be pretty easy with linux traffic shaping tools.

``` text
sudo tc qdisc add dev eth1 root netem delay 5ms
```

What this says is that we want to delay all packets out of eth1 by 5ms. Great, so if we take a look at our ping test again:


``` text
Pinging 10.1.5.10 with 32 bytes of data:
	Reply from 10.1.5.10: bytes=32 time=5ms TTL=127
	Reply from 10.1.5.10: bytes=32 time=5ms TTL=127
	Reply from 10.1.5.10: bytes=32 time=5ms TTL=127
	Reply from 10.1.5.10: bytes=32 time=5ms TTL=127
```

And we have our required latency.

What's really great about this method is that we can add multiple levels of latency at the same time based on the IP we use to access our SQL box. What this means with my test harness is that we can test to the same SQL server with the same data, at practically the same time so our results can be much more accurate and less prone to environmental features.

**Disclaimer:** I am by no means a nix guy so I'm sure there are many things I could do better with this config, I would love to hear some feedback on how to improve on this configuration. However practically this example has worked brilliantly for me an my use case.
