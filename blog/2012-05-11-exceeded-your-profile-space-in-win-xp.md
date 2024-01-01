---
title: You have exceeded your profile space in Windows XP
permalink: /win/exceeded-your-profile-space-in-win-xp/
tags:
  - Windows
---
You need to make a registry file and load it to fix the issues causing this problem, follow the instructions below:

  1. Click Start
  2. Click Programs
  3. Click Accessories and click Notepad
  4. Copy and paste the following:

    Windows Registry Editor Version 5.00

    [HKEY_CURRENT_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem] &#8220;EnableProfileQuota&#8221;=-      &#8220;ProfileQuotaMessage&#8221;=- &#8220;MaxProfileSize&#8221;=-&#8220;IncludeRegInProQuota&#8221;=- &#8220;WarnUser&#8221;=- &#8220;WarnUserTimeout&#8221;=-


  1. Click File
  2. Click Save
  3. Save as: fix.reg
  4. Run the fix.reg
  5. Restart your computer
