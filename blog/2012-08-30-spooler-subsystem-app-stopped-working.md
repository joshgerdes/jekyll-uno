---
title: Spooler SubSystem App Stopped Working
date: 2012-08-30T11:57:54+00:00
authors: [Luke]
tags:
  - Windows
---
Follow the guides below to fix the spooler issues:

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click<strong> My Computer/Computer</strong>
  </li>
  <li>
    <strong>Navigate</strong> to: C:WindowsSystem32spool<strong>Printers</strong>
  </li>
  <li>
    <strong>Delete</strong> <strong>everything</strong> in this folder.
  </li>
  <li>
    <strong>Restart</strong> the computer and attempt printing again.
  </li>
</ol>

_If that does not work, attempt the following:_

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type: <strong>regedit</strong> > Press Enter
  </li>
  <li>
    <strong>Navigate</strong> to: <strong>HKEY_LOCAL_MACHINESYSTEMCONTROLSET001CONTROLPRINTENVIRONMENTSWINDOWSNTx86DRIVERSVERSION-3</strong>
  </li>
  <li>
    <strong>Right</strong> click and <strong>delete</strong> the printer <strong>registry</strong> <strong>keys</strong>
  </li>
  <li>
    <strong>Restart</strong> the computer.
  </li>
</ol>

_If that does not work, attempt the following:_

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Control</strong> <strong>Panel</strong>
  </li>
  <li>
    Click <strong>Add/Remove Programs</strong> or Uninstall a Program
  </li>
  <li>
    Click Turn<strong> Windows Features On/Off</strong> <em>(left hand side menu)</em>
  </li>
  <li>
    Navigate down to <strong>Print Services</strong>
  </li>
  <li>
    Make sure<strong> LPD</strong> and <strong>LPR</strong> are <strong>ticked</strong>, if not tick them.
  </li>
  <li>
    <strong>Restart</strong> your computer.
  </li>
</ol>

&nbsp;