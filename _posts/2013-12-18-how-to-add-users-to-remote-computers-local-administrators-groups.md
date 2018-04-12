---
id: 2886
title: How to add users to remote computers local Administrators groups
date: 2013-12-18T15:56:41+00:00
author: Luke
layout:
  - ""
guid: http://www.techremedy.co.nz/?p=2886
permalink: /win/how-to-add-users-to-remote-computers-local-administrators-groups/
dsq_thread_id:
  - "4987905950"
mfn-post-love:
  - "0"
post_views_count:
  - "13"
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
categories:
  - Windows
---
  1. First you need to download &#8211; <a href="http://technet.microsoft.com/en-us/sysinternals/bb897553.aspx" target="_blank">PSEXEC </a> &#8211; a command line tool that will allow you to execute commands on remote workstations.
  2. Once downloaded open My Computer/Computer and navigate to: C:\Windows\System32 on your local machine.
  3. Extract the zip file contents to the System32 folder (this will allow you to run the psexec command from any folder within Command Prompt).
  4. Navigate to your Documents or Desktop and create a new txt file called: computernames.txt
  5. In the computernames.txt document – add (one in each new line) the computer names that you will like to add the user to the Administrators group of.
  6. Once they have been added – save the time with the computer names.
  7. Now we need to create a batch script – open a new Notepad document and in the first line type: PSEXEC.EXE @computernames.txt NET LOCALGROUP Administrators **DOMAIN\****USERID** /ADD
  8. Replace – DOMAIN & USERID with the user you would like to add.
  9. Press File and click Save As and type in: &#8220;addusers_multiple.bat&#8221;
 10. This will save the file as a batch script
 11. Now – run the script to start importing the users into the remote computers local administrators group.

Note: Proper syntac allows for the group name to be set like &#8221; NET LOCALGROUP &#8220;Administrators&#8221; – however my test on a Windows XP workstation didn&#8217;t like the &#8220;&#8221; so I got rid of them – if you encounter an error with unable to find local group – re add them around the group name in the script.

Note: Tested on Windows 7 workstations without an issue.