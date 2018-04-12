---
id: 1500
title: Nvlddmkm.sys/dxgkrnl.sys/dxgmms1.sys Issues
date: 2012-10-01T09:35:59+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1500
permalink: /win/nvlddmkm-sysdxgkrnl-sysdxgmms1-issues/
dsq_thread_id:
  - "2441232911"
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "28"
categories:
  - Windows
---
_These issues are usually caused by damage and/or faulty nVidia drivers and DirectX components within Windows. Follow the instructions below to repair:_

&nbsp;

<ol start="1">
  <li>
    Firstly you need to <strong>download</strong> a tool called “<strong>Driver Sweeper</strong>”
  </li>
  <li>
    Download and <strong>install</strong> Driver Sweeper
  </li>
  <li>
    <strong>Download</strong> the latest version of the <a title="nVidia English Drivers" href="http://www.nvidia.com/Download/index.aspx?lang=en-us" target="_blank">nVidia driver</a> <em>(but do not install yet)</em> make sure you have the correct one for your OS and architecture <em>(ie 32Bit or 64Bit).</em>
  </li>
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Control Panel</strong>
  </li>
  <li>
    Click <strong>Add/Remove Programs</strong> <em>(or Uninstall a program)</em>
  </li>
  <li>
    <strong>Select</strong> <strong>nVidia</strong> and <strong>Uninstall</strong>.
  </li>
  <li>
    Once uninstalled, reboot your computer into <strong>Safe Mode</strong> <em>(Press <strong>F8</strong> at Windows start-up to get to the Safe Mode)</em>
  </li>
  <li>
    Run <strong>run</strong> <strong>Driver Sweeper</strong> <em>(which should be located Start, Programs, Driver Sweeper)</em>
  </li>
  <li>
    You should have a list with checkboxes in front of you ignore the rest and <strong>check</strong> <strong>NVIDIA</strong> <strong>Display</strong>.
  </li>
  <li>
    Click <strong>Clean</strong>
  </li>
  <li>
    <strong>Restart</strong> your computer <em>(in Normal Mode)</em>
  </li>
  <li>
    Now <strong>install</strong> the nVidia <strong>drivers</strong>
  </li>
  <li>
    Restart and you should be good-to-go!
  </li>
</ol>

&nbsp;

_If the above does not work, then you need to update <a title="DirectX " href="http://www.microsoft.com/en-us/download/details.aspx?id=35" target="_blank">DirectX</a> and/or run a <a title="Memtest x86" href="http://www.memtest.org/#downiso" target="_blank">RAM</a> scan._