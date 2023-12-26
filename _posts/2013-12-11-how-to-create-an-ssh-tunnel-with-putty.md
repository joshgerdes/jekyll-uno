---
title: How to create an SSH tunnel with PuTTY
categories:
  - Windows
date: 2013-12-11 00:00:00 +1300
---
Open PuTTY

Create a new PuTTY session to the remote server

Enter in the server details

Save session

Click on Connection

Click on SSH and select Tunnels

In the source field enter the port you would like to forward.  In the section below, select Dynamic and Auto.

Click Add

Go to the main PuTTY session dialog, and save the changes you have made.

Press Open to open your Putty session and login if it asks for the details.

Now you need to configure the application you are trying to tunnel

For example, in Internet Explorer, click Tools, Internet Options, click Connections, Choose LAN Settings and change the proxy to localhost

(SOCKS5 as Proxy type if asked) and enter the port that you were forwarding into the port information.

Save and you should now be routing your traffic through the tunnel

Unix
You can use the following command to enable an SSH Tunnel on a Linux machine:
ssh -D localhost:PORT example@example.com
