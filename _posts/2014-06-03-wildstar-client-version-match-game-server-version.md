---
title: 'Wildstar &#8211; Client version does not match the game server version'
permalink: /win/wildstar-client-version-match-game-server-version/

categories:
  - Windows
---
This error seems to be happening mostly to us New Zealand players.. looks like a DNS issue. The fix is to use a VPN tunnel for when you first open a launcher or edit the host file.

To edit the Host file do the following:

  1. Click Start
  2. All Programs
  3. Accessories
  4. Right click Notepad and select Run as administrator
  5. Click Continue on the &#8220;Windows needs your permission&#8221; UAC window.
  6. When Notepad opens Click File -> Open
  7. In the filename field type C:WindowsSystem32Driversetchosts
  8. Click Open
  9. Paste in and save the host file:

`174.35.56.164 wildstar.patcher.ncsoft.com``<br />
` `174.35.56.164 wildstar.patcher.ncsoft.com.cdngc.net`

<p style="color: #333333">
