---
title: How to see what users are currently logged into a Windows system
categories:
  - Windows
date: 2014-09-06 00:00:00 +1300
---

Being able to determine who is currently logged into a particular Windows system – such as a server can be useful for identify performance problems and notifying the relevant users of an impending restart.

### <span id="Method_1">Method 1</span>

  1. Open a command prompt on the machine
  2. Type in: **quser**
  3. This will list the users currently logged in and what type of session are they using.

Note: If you have opened an elevated command prompt you can use: **quser /server:Servername** to show logged on users on remote machines.

### <span id="Method_2">Method 2</span>

  1. Open Task Manager (by clicking CTRL+ALT+DEL) on the PC
  2. Click on the Users Tab – up the top.
  3. This will list the users currently logged in and what type of session are using.
