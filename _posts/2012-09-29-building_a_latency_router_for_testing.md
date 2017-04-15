---
title:  "Building a latency router for testing"
date:   2012-09-29
canonical: http://blog.staticvoid.co.nz/2012/9/29/building_a_latency_router_for_testing
redirect_from:
  - 2012/9/29/building_a_latency_router_for_testing
---
I recently needed to test SQL insert performance under latency scenarios. As part of this I needed a good way of introducing latency between my test harness and database server. I also wanted to control the latency and if possible have a way to run several different levels of latency at the same time.&nbsp;To do this I built a latency emulating router with Ubuntu server and IPTables.<br />
<br />
I decided to set up create the router with a bunch of network interfaces and apply a different level of delay to each interface. What this means is that based on which IP address I accessed my SQL box with the connection was delayed by a set amount of latency.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-QEWrUkjH690/UEhqOTvQj3I/AAAAAAAAAT4/K0XJhayu-CQ/s1600/Latency+Router.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="126" src="http://3.bp.blogspot.com/-QEWrUkjH690/UEhqOTvQj3I/AAAAAAAAAT4/K0XJhayu-CQ/s640/Latency+Router.png" width="640" /></a></div>
<br />
I found this approach to work really well for me so I thought I would do a bit of a write up on how I went about it.<br />
<br />
The 5 step program to artificial latency:<br />
<br />
<span style="font-size: large;">Step 1:</span><br />
<br />
Setup your VM with a bunch of NICs (in my example I used five 1 for an entry point and four for different amounts of latency)<br />
<br />
<span style="font-size: large;">Step 2:</span><br />
<br />
<a href="http://www.ubuntu.com/download/server">Install Ubuntu Server</a>&nbsp;(I just used the latest version from the&nbsp;Ubuntu&nbsp;site) and make sure each of your NICs has an address on a&nbsp;separate&nbsp;subnet (I made each subnet the amount of latency that network would provide)<br />
<br />
You can modify your network configs by editing the following:<br />
<br />
<span style="background-color: white; color: #333333; line-height: 17px;"><span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;sudo nano /etc/network/interfaces</span></span><br />
<span style="background-color: #f9f9f9; color: #333333; font-family: Verdana; font-size: 14px; line-height: 17px;"><br /></span>
For example to setup eth1 (my second network card) to run subnet 10.1.5.0/24 I used the following config:<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;iface eth2 inet static</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;address 10.1.5.1</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;netmask 255.255.255.0</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;broadcast 10.1.5.255</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;network 10.1.5.0</span><br />
<div>
<br /></div>
<span style="font-size: large;">Step 3:</span><br />
<br />
Setup some routing. This means that when we send traffic via our router which we want to go to a specific subnet it will know which NIC to push that traffic out through. Below is a rule to route traffic from 10.1.1.0/24 to 10.1.5.0/24:<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;sudo iptables -t nat -A POSTROUTING -s 10.1.1.0/24 -d 10.1.5.0/24 -j SNAT --to 10.1.5.1</span><br />
<div>
<br /></div>
<br />
Once all of your rules are setup you can save them (so they persist over a reboot) using the following:<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;sudo apt-get install iptables-persistent</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;sudo iptables-save &gt; /etc/iptables/rules.v4</span><br />
<div>
<br /></div>
<div>
<span style="font-size: large;">Step 4:</span></div>
<div>
<br /></div>
<div>
Set up your server and client to route through the router. In windows on my local PC I added in a route to send data bound for my latency network to the latency router. You can do this from an administrator command prompt with:</div>
<div>
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;route ADD 10.1.5.0 MASK 255.255.255.0 &nbsp;10.1.1.3&nbsp;</span></div>
<br />
This will send all traffic bound for 10.1.5.0/24 to my routers address on my subnet (10.1.1.3).<br />
<br />
On the server end I simply added a new NIC on the 10.1.5.0/24 subnet with an address of 10.1.5.10.<br />
<br />
Once you have this configuration you should be able to run a ping to test your routing, and you should get something similar to the below:<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Pinging 10.1.5.10 with 32 bytes of data:</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time<span style="background-color: white;">&lt;</span>1ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time<span style="background-color: white;">&lt;</span>1ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time<span style="background-color: white;">&lt;</span>1ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time<span style="background-color: white;">&lt;</span>1ms TTL=127</span><br />
<br />
Awesome we have connectivity. Its important to note here the path that our data will follow, especially because it may not be what you are expecting.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-sRiaOCqmqvI/UGbMi8EJBwI/AAAAAAAAAUY/MYkLm6GZd5w/s1600/Response+path.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="95" src="http://2.bp.blogspot.com/-sRiaOCqmqvI/UGbMi8EJBwI/AAAAAAAAAUY/MYkLm6GZd5w/s640/Response+path.png" width="640" /></a></div>
<br />
This is because when we request the routing tells us that because we are sending it to a different subnet it should go through our router but when we respond our SQL box is already part of the destination subnet so&nbsp;doesn't&nbsp;need to route the message at all.<br />
<br />
<span style="font-size: large;">Step 5:</span><br />
<br />
The last thing we need to do is to set up the latency. This turns out to be pretty easy with linux traffic shaping tools.<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;sudo tc qdisc add dev eth1 root netem delay 5ms&nbsp;</span><br />
<span style="font-family: Courier New, Courier, monospace;"><br /></span>
What this says is that we want to delay all packets out of eth1 by 5ms. Great, so if we take a look at our ping test again:<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Pinging 10.1.5.10 with 32 bytes of data:</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time=5ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time=5ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time=5ms TTL=127</span><br />
<span style="font-family: Courier New, Courier, monospace;">&nbsp; &nbsp; &nbsp;Reply from 10.1.5.10: bytes=32 time=5ms TTL=127</span><br />
<br />
<div>
And we have our required latency.</div>
<div>
<br /></div>
<div>
Whats really great about this method is that we can add multiple levels of latency at the same time based on the IP we use to access our SQL box. What this means with my test harness is that we can test to the same SQL server with the same data, at&nbsp;practically&nbsp;the same time so our results can be much more accurate and less prone to environmental features.</div>
<div>
<br /></div>
<br />
<b>Disclaimer:</b> I am by no means a nix guy so I'm sure there are many things I could do better with this config, I would love to hear some feedback on how to improve on this configuration. However practically this example has worked brilliantly for me an my use case.
