---
title: Set the Macbook Keyboard Back-light to be on permanently
date: 2012-08-21T11:56:34+00:00
authors: [Luke]
tags:
  - Mac OSX
---
<ol start="1">
  <li>
    <strong>Open</strong> <strong>Finder</strong>
  </li>
  <li>
    <strong>Navigate</strong> to: <strong><em>Users/YourUser/NameHere/Library/Preferences</em></strong>
  </li>
  <li>
    <em>Warning: Be mindful of changing the wrong file or touching incorrect settings in this folder. This could go wrong!</em>
  </li>
  <li>
    <strong>Open<em>: com.apple.bezelservice.plist</em></strong>
  </li>
  <li>
    <strong>Change</strong> <strong><em>kHWMin</em></strong> to have a value of: <strong>1</strong>
  </li>
  <li>
    Close and <strong>save</strong>
  </li>
</ol>

_You have now adjusted the minimum light the light sensor needs to activate the back-light on the keyboard. _

_Note: Only valid for Macbook Pros, normal Macbooks do not contain keyboard back-lights._