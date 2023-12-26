---
title: Change the Short Date format using the Windows registry
author: Luke
date: 2013-12-02 00:00:00 +1300
categories:
  - Windows
---

You can edit the registry to change the short date format for all the user accounts on the computer: <br />In Registry Editor, open the following key:

<p>
  <strong>HKEY_USERS.DefaultControl PanelInternational <br /></strong><br /><strong>Add or edit</strong> the <strong>sShortDate</strong> string value using a value data for the short date format contained in the following list:
</p>

<p>
  MM/dd/yyyy<br />M/d/yy<br />M/d/yyyy<br />MM/dd/yy<br />yy/MM/dd<br />yyyy-MM-dd<br />dd-MMM-yy
</p>

<p>
  Quit Registry Editor.
</p>

<p>
  Log off Windows, and then log on to Windows again to save the setting<br /> </span>
</p>