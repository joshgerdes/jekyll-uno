---
title: Network Map Windows startup Script
authors: [Luke]
tags:
  - Windows
date: 2013-02-23 00:00:00 +1300
---
`<br />
echo off<br />
cls<br />
net use z: /delete /y<br />
net use z: "192.168.1.1share" /y<br />
` 

Note:  &#8220;Z is the drive letter I have assigned for this example &#8211; you can however change this to what you want _(if it already is not in use of course)_.)