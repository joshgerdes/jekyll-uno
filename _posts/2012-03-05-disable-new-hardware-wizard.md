---
title: Disable New Hardware Wizard in Windows XP to Enable Automatic Device Driver
  Installation
date: 2012-03-05 00:00:00 +13:00
permalink: "/win/disable-new-hardware-wizard/"
categories:
- Windows
---

Want to skip straight to automatic hardware installation? Follow the instructions below to edit the registry.

  1. Click **Start**
  2. Click **Programs**
  3. Click Accessories
  4. Click **Notepad**
  5. Copy the script below:

<div>
  <p>
    <em>REGEDIT4</em>
  </p>
  
  <p>
    <em>[HKEY_LOCAL_MACHINESOFTWAREPoliciesMicrosoftWindowsDriverSearching]</em><br /> <em> &#8220;DontSearchWindowsUpdate&#8221;=dword:00000001</em><br /> <em> &#8220;DontPromptForWindowsUpdate&#8221;=dword:00000001</em><br /> <em> &#8220;DontSearchCD&#8221;=dword:00000001</em><br /> <em> &#8220;DontSearchFloppies&#8221;=dword:00000001</em>
  </p>
  
  <p>
    <em>[HKEY_CURRENT_USERSoftwarePoliciesMicrosoftWindows NTDriver Signing]</em><br /> <em> &#8220;behaviorOnFailedVerify&#8221;=dword:00000000</em>
  </p>
  
  <p>
    <em>[HKEY_USERS.DEFAULTSoftwarePoliciesMicrosoftWindows NTDriver Signing]</em><br /> <em> &#8220;behaviorOnFailedVerify&#8221;=dword:00000000</em>
  </p>
</div>

  1. **Paste** into Notepad
  2. Click File
  3. Click **Save As**
  4. Name the file &#8220;**_DisableHardware.bat_**&#8220;
  5. **Run** the file & accept all changes.
