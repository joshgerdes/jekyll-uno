---
title: Deactivating Windows XP
permalink: /win/deactivating-winxp/
categories:
  - Windows
---
Deactivating Windows XP can be useful especially when moving the Windows XP install from one computer to another as it makes Windows activation easier and more automated.

Follow the simple guide below to make the necessary Registry change to deactivate your Windows XP version.

**Deactivating Windows XP**

<ol style="font-family: sans-serif; font-size: medium; font-style: normal; line-height: normal;">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type &#8216;<strong>regedit</strong>&#8216;
  </li>
  <li>
    Navigate to
  </li>
  <li>
    <strong><em>HKEY_LOCAL_MACHINE/Software/Microsoft/WindowsNT/Current Version/WPAEvents</em></strong>
  </li>
  <li>
    <strong>Double</strong>&#8211;<strong>click <em>OOBETimer</em></strong>, when the box comes up, <strong>change</strong> the <strong>LAST</strong> <strong>TWO</strong> HEX <strong>VALUES</strong> to nulls(<strong><em>00 00</em></strong>)
  </li>
</ol>

**Reactivating Windows XP**

<ol style="font-family: sans-serif; font-size: medium; font-style: normal; line-height: normal;">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type &#8220;<strong>c:\windows\system32\oobe\msoobe.exe /a</strong>&#8220;
  </li>
  <li>
    Press <strong>Enter</strong>
  </li>
</ol>
