---
title: Change the Short Date format using the Windows registry
date: 2013-12-03 09:35:52 +13:00
permalink: "/win/change-the-short-date-format-using-the-windows-registry/"
categories:
- Windows
id: 2809
author: Luke
layout: post
guid: http://www.techremedy.co.nz/?p=2809
dsq_thread_id:
- '4840090605'
mfn-post-love:
- '0'
post_views_count:
- '24'
---

<span style="font-family:Times New Roman;font-size:12pt">You can edit the registry to change the short date format for all the user accounts on the computer: <br />In Registry Editor, open the following key: </p> 

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