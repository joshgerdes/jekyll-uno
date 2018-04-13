---
title: How to enable numlock on startup in Windows 8
permalink: /win/enable-numlock-windows8/
categories:
  - Windows
---
If you are like me – you rely heavily on the Num Lock key and having it disabled on boot is extremely annoying – using a quick registry change you can enable Numlock by default in Windows 8.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#HOW_TO_enableNUMLOCK_ON_STARTUP"><span class="toc_number toc_depth_1">1</span> HOW TO enable NUMLOCK ON STARTUP</a>
    </li>
    <li>
      <a href="#How_to_disable_Numlock_on_Startup"><span class="toc_number toc_depth_1">2</span> How to disable Numlock on Startup</a>
    </li>
  </ul>
</div>

#### <span id="HOW_TO_enableNUMLOCK_ON_STARTUP">HOW TO enable NUMLOCK ON STARTUP</span>

  1. Press the Windows Key to open the Tile (Metro) screen
  2. Type: regedit to search for the Windows Registry Editor and press Enter.
  3. When the Registry Editor loads &#8211; navigate through:
  4. HKEY_USERS,.DEFAULT, Control Panel, and Keyboard.
  5. Locate the InitialKeyboardIndicators entry and right-click it, select Modify.
  6. Enter 2 into the box.
  7. Click OK to save the changes.


#### <span id="How_to_disable_Numlock_on_Startup">How to disable Numlock on Startup</span>

Follow the same steps till: Step 6 than instead of 2 type: 2147483648.
