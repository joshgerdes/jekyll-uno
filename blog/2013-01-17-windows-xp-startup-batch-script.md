---
title: Windows XP Startup Batch Script
date: 2013-01-17 00:00:00 +1300
authors: [Luke]
tags:
  - Misc
  - Windows
---

Save the following into a notepad document and name it with .bat at the end &#8211; for example WinXPStartup.BAT. You can then run the batch script directly from the recovery console on a Windows XP CD.

`<br />
@echo off<br />
CD ..<br />
ATTRIB -H C:boot.ini<br />
ATTRIB -S C:boot.ini<br />
ATRIB -R C:boot.ini<br />
del boot.ini<br />
BOOTCFG /Rebuild<br />
CHKDSK /R /F<br />
FIXBOOT<br />
`
