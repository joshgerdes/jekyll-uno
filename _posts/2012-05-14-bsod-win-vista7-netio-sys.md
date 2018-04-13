---
title: Black Screen of Death Windows Vista/7 NETIO.SYS
permalink: /win/bsod-win-vista7-netio-sys/
categories:
  - Windows
---
Caused when your network driver has become corrupted or changed for NetBIOs with an incompatible version from either Windows Updates or a filter from your Firewall (most commonly Zone Alarm).

You can “repair” this by using System Restore to go back to a previous driver, follow the guide below to do this:

  1. Restart your computer
  2. While it is starting up and just before the computer starts to load Windows continuously tap F8.
  3. A text-based menu will appear and using the Arrow Keys and the Enter key select Repair My Computer (up the top of the menu)
  4. Now it will prompt with your install selection, choose your Windows install and User Account and press Ok
  5. It will now come up with a dialog Window displaying a few options, click System Restore (it will take a while to actually load)
  6. Select Next
  7. Choose a valid System Restore point (the most recent while the computer was going is the best bet)
  8. Select Next and Ok
  9. Wait for the restore to finish and restart your computer. It should now be going (If it does not work, you might have to go to a System Restore point more previous then the one you used).


<div>
  If System Restore cannot find the Windows operating system, you need to run a file system check called a CHKDSK.  Follow the same prompts as above till Step 5, but instead of pressing System Restore, press Command Prompt. Type in: chkdsk /r /f c: and press Enter.
</div>

<div>
  This is also caused by the Quality of Service network protocol in Windows.
</div>

<div>
  Assuming you have a bootable Windows install follow the instructions below:
</div>

Click Start

  1. Click Control Panel
  2. Click Network & Sharing Center
  3. Click Manage Network Connection (on the left hand side menu)
  4. Right click on the Local Area Connection
  5. Left click Properties
  6. You will now have a list of protocols and services related to your networking device, leave the rest alone and uncheck QoS  Packet Scheduler
  7. Click Ok

Note: If you have any valid Firewalls such as Zone Alarm installed, your best bet is once you have regained access to Windows is to uninstall it, the Windows Firewall does a good enough job and you do not need a third party one.

Note: Also make sure you are running the latest Windows service pack which helps reduce this issue.
