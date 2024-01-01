---
title: x800703F0 installing Vista SP1
date: 2012-10-02T13:06:32+00:00
authors: [Luke]
tags:
  - Windows
---
_Trying to install Service Pack 1 for Windows Vista and getting “x800703F0” error? Follow the guides below to fix it._

_Enable the Windows Module Installer Service_

<ol start="1">
  <li>
    Click on the Vista Orb (<strong>Start</strong>)
  </li>
  <li>
    In the <strong>search</strong> field type: <strong><em>services.msc</em></strong> > Press Enter
  </li>
  <li>
    A list of Windows Services will appear, scroll down the list and <strong>find</strong> <strong><em>Windows Module Installer</em></strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> <strong>Service</strong> and select <strong>Properties</strong>
  </li>
  <li>
    Click on <strong>Start</strong><em> (also change the startup to Automatic)</em>
  </li>
  <li>
    Click <strong>Ok</strong>
  </li>
  <li>
    Attempt SP1 <strong>setup</strong> again.
  </li>
</ol>

_Set registry entries_

_ _Click on the Vista Orb (**Start**)

<ol start="1">
  <li>
    In the <strong>search</strong> field <strong>type</strong>: <strong><em>regsvr32 wintrust.dll</em></strong> > Press Enter
  </li>
  <li>
    In the search field type: <strong><em>regsvr32 rsaenh.dll</em></strong>  > Press Enter
  </li>
  <li>
    In the search field type:<strong><em> regsvr32 cryptdlg.dll</em></strong> > Press Enter
  </li>
  <li>
    In the search field type: <strong><em>regsvr32 softpub.dll</em></strong>> Press Enter
  </li>
  <li>
    Attempt SP1 <strong>setup</strong> again.
  </li>
</ol>