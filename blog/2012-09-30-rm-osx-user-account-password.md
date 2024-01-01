---
title: How to remove OSX User Account Password
date: 2012-09-30T10:42:21+00:00
authors: [Luke]
tags:
  - Mac OSX
---
**With CD**

<ol start="1">
  <li>
    Put your OSX CD/DVD into your optical drive.
  </li>
  <li>
    Restart the Mac and hold down the C key while the Mac is starting
  </li>
  <li>
    Now you should be greeted with a start-up menu select the Install (DVD/CD)
  </li>
  <li>
    Once it has booted click Utilities in the upper Menu
  </li>
  <li>
    Select Password Reset/Reset Password
  </li>
  <li>
    Now select your OSX HDD
  </li>
  <li>
    Select the User Account you want to remove/change the password of and enter in a new password.
  </li>
  <li>
    Click Save
  </li>
  <li>
    Now restart your Mac and remove the OSX CD/DVD from the drive.
  </li>
</ol>

&nbsp;

**Without CD Method**

Note: You may lose all your Data, documents etc. Please backup first!

_Tested on 10.5.6_

Following the steps below you will create a new User Account which will override your old User Account and take precedence over logging in you will then remove the password from your old User Account and set it to log in.

<ol start="1">
  <li>
    Restart OSX
  </li>
  <li>
    Hold down the Apple Key+S <em>(or Command+S on newer Macs)</em> key as the computer first turns on.
  </li>
  <li>
    Once the Mac starts showing lines of text and a terminal you can release the keys.
  </li>
  <li>
    Once you see a blinking cursor type: “mount -uw /” press Enter
  </li>
  <li>
    Type: “rm /var/db/.AppleSetupDone” press Enter
  </li>
  <li>
    Type: “shutdown -h now” press Enter
  </li>
  <li>
    Turn the computer back on
  </li>
  <li>
    You will now be greeted with for a new user creation, follow the prompts to create a new User
  </li>
  <li>
    You would have noticed that there is no option to login to your old account, this is normal.
  </li>
  <li>
    Once you are within OSX
  </li>
  <li>
    Click the Apple Logo<em> (top left)</em>
  </li>
  <li>
    Click System Preferences
  </li>
  <li>
    Click Users
  </li>
  <li>
    Click Unlock <em>(little lock, down the bottom of the dialog)</em>
  </li>
  <li>
    Select your old User Account
  </li>
  <li>
    Click Change Password <em>(here you can remove and/or change it depending on what you want to do)</em>
  </li>
  <li>
    Click Login Options <em>(down the bottom)</em>
  </li>
  <li>
    Click Change Automatic Options to Disabled
  </li>
  <li>
    Restart OSX
  </li>
  <li>
    Now you will be greeted to a login dialog, select your old User Account
  </li>
  <li>
    Login and you can go back to System Preferences/Users to delete the account you had created.
  </li>
</ol>