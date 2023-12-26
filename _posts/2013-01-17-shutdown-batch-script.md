---
title: Shutdown Batch Script
date: 2013-01-17 00:00:00 +1300
author: Luke
categories:
  - Misc
  - Windows
---
Save the following into a notepad document and name it with .bat at the end &#8211; for example shutdown.BAT. You can then either set it to the desktop or add it to a scheduled task to turn your computer off at a certain time.

`<br />
@echo off<br />
shutdown.exe -s -t 00<br />
exit<br />
` 

Note: Changing &#8220;-s&#8221; to &#8220;-r&#8221; will restart the computer, instead of turning it off and adjusting the &#8220;-t&#8221; will change the time in seconds till it shuts down. Useful if you are wanting the computer to shutdown after an hour or so.