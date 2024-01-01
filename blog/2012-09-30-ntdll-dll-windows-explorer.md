---
title: ntdll.dll Windows Explorer
date: 2012-09-30T13:42:29+00:00
authors: [Luke]
tags:
  - Windows
---
Having problems with Windows Explorer with the “ntdll.dll” error? This usually occurs when you are running an AMD system.

&nbsp;

<ol start="1">
  <li>
    <strong>Right</strong> <strong>click</strong> My <strong>Computer</strong>
  </li>
  <li>
    Click <strong>Properties</strong>
  </li>
  <li>
    Click on <strong>Advanced</strong>
  </li>
  <li>
    Click <strong>Environment Variables</strong>
  </li>
  <li>
    Look for “<strong><em>NLSPATH</em></strong>” and <strong>delete</strong>/rename it
  </li>
  <li>
    Press <strong>Ok</strong>
  </li>
</ol>

_Another issue is with Data Execution Prevention, follow the prompts below_:

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Control Panel</strong>
  </li>
  <li>
    Click <strong>System</strong>
  </li>
  <li>
    Click the <strong>Advanced</strong> Tab
  </li>
  <li>
    Click <strong>Settings</strong>
  </li>
  <li>
    <strong>Click</strong> on <strong>Data Execution Prevention</strong>
  </li>
  <li>
    Click on “<strong><em>Turn on DEP for all Programs and Services Except Those I Select</em></strong>”
  </li>
  <li>
    Click <strong>Add</strong>
  </li>
  <li>
    Browse to <strong><em>c:Windowsexplorer.exe</em></strong>
  </li>
  <li>
    Click <strong>Add</strong>
  </li>
  <li>
    Click <strong>Ok</strong>
  </li>
  <li>
    <strong>Restart</strong> your machine.
  </li>
</ol>