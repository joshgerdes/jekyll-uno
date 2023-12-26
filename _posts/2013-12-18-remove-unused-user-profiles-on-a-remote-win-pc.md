---
title: Remove unused user profiles on a remote Windows workstation
categories:
  - Windows
date: 2013-12-18 00:00:00 +1300
---
Note: The intended guide for this audience is a Help Desk or Service Desk – this is intended for a domain setup with the user having local administration rights on the workstation.

  1. First, you need to download tool called: <a href="http://helgeklein.com/free-tools/delprof2-user-profile-deletion-tool/" target="_blank" rel="noopener">Delprof2</a>
(this is a remake of the Microsoft Delprof utility that Microsoft had dropped support & updates for)
  2. Once downloaded open My Computer/Computer and navigate to c:\Windows\System32 on your local machine.
  3. Extract the delprof2 zip file & folder and copy DelProf2.exe to the folder you opened earlier – c:\Windows\System32
  4. Now – open command prompt – click Start, Run and type in cmd and press Enter (For Windows 7 workstations – you can type Command in the search field or press the Windows Key + R to open the run dialog box).
  5. REMEMBER to make sure the profiles are backed up first – this will completely remove the local cache – use the syntax: **delprof2 /u /r /c:computername** and press Enter. This will connect to the remote workstation you specified in the &#8220;computername&#8221; field and remove all locally cached profiles that are not being used. It will also clear up remote registry entries making this a useful & easy tool for clearing up Roaming Profiles in Windows 7-10.

You can also run: delprof2 /u /d:30 /c:computername

_Note: What I have done in the past is create a batch script that will clear up remote profiles from workstations & add this to a scheduled task &#8211; in conjunction with SCCM disk reporting this is useful for keeping on top of workstation&#8217;s HDD space._
