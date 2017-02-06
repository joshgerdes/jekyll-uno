---
layout: post
title: Useful little batch file for opening frequently used applications in Windows 10
published: true
---

As a web designer there are several applications I need to run on a daily basis clocking up plenty of RAM. How many do you run? I personally found it a rather tedious task to have to double-click on every application, one after the other, each morning I was in the office, wasting valuable minutes. Fortunately, you can create a batch file (.bat) to launch your programs with a pair of clicks.

"It may only be seconds saved but shaving any time from your daily grind can help to improve your working life".

        *This post is applicable for Windows 10
        
### CREATING A BATCH FILE
1. OPEN UP A NEW FILE IN NOTEPAD OR SIMILAR
2. SAVE AS 'NAMEOFFILE' + THE EXTENSION .BAT. E.G _**NAMEOFFILE.BAT**_

### Populating the batch file
You can now add all the applications and their respective file paths you wish to launch. Below, you will see an example file.

        @echo off
        start "Outlook" "C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
        start "Brackets" "C:\Program Files (x86)\Brackets\Brackets.exe"
        start "Chrome" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        start "Firefox" "C:\Users\w.law\AppData\Local\Mozilla Firefox\firefox.exe"
        start "Photoshop" "C:\Program Files\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe"
        start "Bridge" "C:\Program Files\Adobe\Adobe Bridge CS6 (64 Bit)\Bridge.exe"
        start "Dreamweaver" "C:\Program Files (x86)\Adobe\Adobe Dreamweaver CS6\Dreamweaver.exe"
        start "WinSCP" "C:\Program Files (x86)\WinSCP\WinSCP.exe"
        start "OneDrive" "C:\Users\w.law\AppData\Local\Microsoft\OneDrive\OneDrive.exe"
        start "CMD" "%windir%\syswow64\WindowsPowerShell\v1.0\PowerShell_ISE.exe"
        start "Sourcetree" "C:\Program Files (x86)\Atlassian\SourceTree\SourceTree.exe"

### Establish the location of the application
In the list you can see that I run Outlook, Chrome, Brackets, Photoshop, just to name a few. You need to find to locations for these programs and add it to the batch file as shown.

To do this, locate the application in 'All Apps', right click it, hover over 'more' and click on 'open file location'

![Alt text](/images/post/20160908030717-programs.jpg)

The location is in the target field which you can copy and paste.

![Alt text](/images/post/20160908030836-app-target.jpg)



