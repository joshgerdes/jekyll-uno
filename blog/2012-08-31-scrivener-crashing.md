---
title: Scrivener Crashing
date: 2012-08-31T10:58:32+00:00
authors: [Luke]
tags:
  - Mac OSX
---
Attempting to open Scrivener and having the application closing on you, the common way to fix this is adjust the file permissions follow the instructions below to repair.

<ol start="1">
  <li>
    <strong>Open</strong> a <strong>Terminal</strong><em> (Applications/Utilities) </em>
  </li>
  <li>
    <strong>Type</strong>: <em>sudo chmod -R 0755 /Applications/Scrivener.app</em>
  </li>
  <li>
    Press <strong>Enter</strong>
  </li>
  <li>
    <strong>Open</strong> <strong>Scrivener</strong> again.
  </li>
</ol>

Note: _This fix has also been able to work on other OSX Applications that have problems launching._