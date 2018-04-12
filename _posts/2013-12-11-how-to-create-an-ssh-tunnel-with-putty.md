---
id: 3083
title: How to create an SSH tunnel with PuTTY
date: 2013-12-11T14:58:27+00:00
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2832
permalink: /win/how-to-create-an-ssh-tunnel-with-putty/
dsq_thread_id:
  - "4839394079"
mfn-post-love:
  - "0"
post_views_count:
  - "16"
categories:
  - Windows
---
  1. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Open <span style="color:#7baf40"><strong>PuTTY</strong><span style="color:#333333"><br /> </span></span></span>
    </div>

  2. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Create a <span style="color:#7baf40"><strong>new</strong><span style="color:#333333"> PuTTY <span style="color:#7baf40"><strong>session</strong><span style="color:#333333"> to the remote server<br /> </span></span></span></span></span>
    </div>

  3. <div style="background: white">
      <span style="color:#7baf40;font-family:Times New Roman;font-size:10pt"><strong>Enter</strong><span style="color:#333333"> in the server <span style="color:#7baf40"><strong>details</strong><span style="color:#333333"><br /> </span></span></span></span>
    </div>

  4. <div style="background: white">
      <span style="color:#7baf40;font-family:Times New Roman;font-size:10pt"><strong>Save</strong><span style="color:#333333"> session<br /> </span></span>
    </div>

  5. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Click on <span style="color:#7baf40"><strong>Connection</strong><span style="color:#333333"><br /> </span></span></span>
    </div>

  6. <div style="background: white">
      <span style="color:#7baf40;font-family:Times New Roman;font-size:10pt"><strong>Click</strong><span style="color:#333333"> on <span style="color:#7baf40"><strong>SSH</strong><span style="color:#333333"> and select <span style="color:#7baf40"><strong>Tunnels</strong><span style="color:#333333"><br /> </span></span></span></span></span></span>
    </div>

  7. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">In the <span style="color:#7baf40"><strong>source</strong><span style="color:#333333"> field enter the <span style="color:#7baf40"><strong>port</strong><span style="color:#333333"> you would like to forward.  In the section below, <span style="color:#7baf40"><strong>select</strong><span style="color:#333333"> <span style="color:#7baf40"><strong>Dynamic</strong><span style="color:#333333"> and <span style="color:#7baf40"><strong>Auto</strong><span style="color:#333333">.<br /> </span></span></span></span></span></span></span></span></span></span></span>
    </div>

  8. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Click <span style="color:#7baf40"><strong>Add</strong><span style="color:#333333"><br /> </span></span></span>
    </div>

  9. <div style="background: white">
      <span style="color:#7baf40;font-family:Times New Roman;font-size:10pt"><strong>Go</strong><span style="color:#333333"> to the main PuTTY <span style="color:#7baf40"><strong>session</strong><span style="color:#333333"> dialog, and <span style="color:#7baf40"><strong>save</strong><span style="color:#333333"> the <span style="color:#7baf40"><strong>changes</strong><span style="color:#333333"> you have made.<br /> </span></span></span></span></span></span></span></span>
    </div>

 10. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Press <span style="color:#7baf40"><strong>Open</strong><span style="color:#333333"> to open your Putty session and <span style="color:#7baf40"><strong>login</strong><span style="color:#333333"> if it asks for the details.<br /> </span></span></span></span></span>
    </div>

 11. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">Now you need to <span style="color:#7baf40"><strong>configure</strong><span style="color:#333333"> the <span style="color:#7baf40"><strong>application</strong><span style="color:#333333"> you are trying to tunnel<br /> </span></span></span></span></span>
    </div>

 12. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt">For example, in Internet Explorer, click Tools, Internet Options, click Connections, Choose LAN Settings and change the proxy to localhost (SOCKS5 as Proxy type if asked) and enter the port that you were forwarding into the port information.<br /> </span>
    </div>

 13. <div style="background: white">
      <span style="color:#7baf40;font-family:Times New Roman;font-size:10pt"><strong>Save</strong><span style="color:#333333"> and you should now be routing your traffic through the tunnel<br /> </span></span>
    </div>

<p style="background: white">
  <span style="color:#333333;font-size:10pt"><span style="font-family:Helvetica"> </span><span style="color:#7baf40"><span style="font-family:Times New Roman"><strong>Unix</strong></span><span style="color:#333333;font-family:Helvetica"><br /> </span></span></span>
</p>

<p style="background: white">
  <span style="color:#333333;font-size:10pt"><span style="font-family:Times New Roman"><em>You can use the following command to enable an SSH Tunnel on a Linux machine:</em></span><span style="font-family:Helvetica"><br /> </span></span>
</p>

  1. <div style="background: white">
      <span style="color:#333333;font-family:Times New Roman;font-size:10pt"><em>ssh -D localhost:PORT example@example.com</em><br /> </span>
    </div>