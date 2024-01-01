---
title: Load needed DLLs for Kernel
layout: post
tags:
  - Windows
---
  1. First thing you need to have a Windows XP CD
  2. Put CD in drive and **boot** from it, you may have to press ESC or F8 to open Boot Prompt to select CD Drive.
  3. Once it has loaded choose Recovery Console
  4. Type: **_chkdsk /r /f c:_**
  5. Press Y
  6. This may take an hour or two to complete, once it has completed type: BOOTCFG /rebuild (Press Enter for prompt)
  7. Type: **_fixboot_** and press Enter
  8. Type: **_fixmbr_** and press Enter
  9. Restart your computer which should now be loading Windows properly.
