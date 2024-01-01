---
title: NTLDR Windows XP
date: 2012-09-25T18:47:01+00:00
authors: [Luke]
tags:
  - Windows
---
To repair this issue you need to have a Windows XP CD.

<ol start="1">
  <li>
    First you need to <strong>boot</strong> from the <strong>Windows</strong> <strong>CD</strong>
  </li>
  <li>
    Once at the first “welcome” screen, press <strong>R</strong> to enter the Recovery Console
  </li>
  <li>
    Press the number of the Windows install you would like to repair (ie 1)
  </li>
  <li>
    Type in your Administrator password if there is one, if not press Enter.
  </li>
  <li>
    Now we need to <strong>copy</strong> two <strong>files</strong> from the Windows <strong>CD</strong> to your Windows install folders, type in the commands below:
  </li>
  <li>
    <strong><em>copy d:I386ntldr C</em></strong>: (Press Enter)
  </li>
  <li>
    <strong><em>copy d:I386ntdetect.com C</em></strong>: (Press Enter)
  </li>
  <li>
    Type: <strong>exit</strong>
  </li>
</ol>

Your computer will now restart, remove the Windows CD and you should now have a bootable Windows installation.