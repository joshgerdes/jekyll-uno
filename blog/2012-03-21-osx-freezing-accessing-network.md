---
title: OSX Freezing when accessing Network Preferences
permalink: /osx/osx-freezing-accessing-network/
tags:
  - Mac OSX
---
This usually happens, when some of the OSX settings become corrupted. OSX can regenerate new settings, which should resolve your problem. Follow the settings below:

  1. Open **Finder**
  2. **Navigate** to your **hard****drive**
  3. **Go** to /**Library**/**Prefences**
  4. Drag **System****Configuration** folder to **Trash**
  5. Now **open****Network****Preferences**, the System Configuration folder should reappear and OSX should not freeze.

If the above doesn&#8217;t work then delete these files:

_Library/Preferences/com.apple.systempreferences.plist_

_Library/Preferences/com.apple.NetworkUtility.plist_
