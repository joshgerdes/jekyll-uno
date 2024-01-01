---
title: Remove Sidebar ads on Handycafe Client
date: 2012-09-13T10:39:52+00:00
authors: [Luke]
tags:
  - Windows
---
In order to remove the Ads on the sidebar, we need to block them using an inbuilt list called the HOST file.

&nbsp;

<ol start="1">
  <li>
    Go to a machine with Handycafe installed
  </li>
  <li>
    Click on My Computer/Computer
  </li>
  <li>
    Goto: C:WindowsSystem32drivers
  </li>
  <li>
    Find the “<strong>hosts</strong>” file
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> the <strong>host</strong> file and left click <strong>Properties</strong>
  </li>
  <li>
    <strong>Uncheck</strong> Use <strong>Read</strong> <strong>Only</strong> and left click <strong>Apply</strong>
  </li>
  <li>
    Right click the hosts file and left click <strong>Open</strong> <strong>With</strong>
  </li>
  <li>
    Select <strong>Notepad</strong>
  </li>
  <li>
    Ignoring everything listed in the file, go to the bottom of the file and enter in the following:
  </li>
  <li>
    <strong><em>127.0.0.1 ad.handycafe.com</em></strong><strong></strong>
  </li>
  <li>
    <strong><em>127.0.0.1 search.handycafe.com</em></strong><strong></strong>
  </li>
  <li>
    Click File
  </li>
  <li>
    Click <strong>Save</strong>
  </li>
  <li>
    <strong>Restart</strong> the machine and the Ads should now vanish, do the same procedure on all your Café machines.
  </li>
</ol>

Note: Using a local firewall on the machine you could also block the Domains as another method of blocking them.