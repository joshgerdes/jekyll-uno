---
id: 3686
title: Enabling Disk Cleanup in Windows Server 2008 R2
date: 2016-04-30T14:28:08+00:00
author: Luke
layout: post
guid: http://luke.geek.nz/?p=3686
permalink: /win/enabling-disk-cleanup-windows-server-2008-r2/
post_views_count:
  - "35"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4790228615"
categories:
  - Windows
---
<span style="color: #000000">In Server 2008 and Server 2008 R2, Disk Cleanup is Disabled by default. This is how you can enable disk cleanup in Windows Server 2008 R2 – 64bit.</span>

<span style="color: #000000">You can enable the Desktop Experience role (which requires a restart to complete) but the easiest way is to copy the files from the WinSXS directory to the relevant directories &#8211; as mentioned below</span>

<div>
  <table style="border-collapse: collapse;height: 247px" border="0" width="1063">
    <colgroup> <col style="width: 203px" /> <col style="width: 911px" /></colgroup> <tr style="height: 21px;background: #5b9bd5">
      <td style="padding-left: 7px;padding-right: 7px;border-top: solid white 0.5pt;border-left: solid white 0.5pt;border-bottom: solid white 0.5pt;border-right: none">
        <span style="color: black;font-family: Arial;font-size: 10pt"><strong>OS</strong></span>
      </td>
      
      <td style="padding-left: 7px;padding-right: 7px;border-top: solid white 0.5pt;border-left: none;border-bottom: solid white 0.5pt;border-right: solid white 0.5pt">
        <span style="color: black;font-family: Arial;font-size: 10pt"><strong>File Location</strong></span>
      </td>
    </tr>
    
    <tr style="height: 43px">
      <td style="background: #5b9bd5;padding-left: 7px;padding-right: 7px;border-top: none;border-left: solid white 0.5pt;border-bottom: solid white 0.5pt;border-right: solid white 0.5pt">
        <span style="color: black;font-family: Arial;font-size: 10pt"><strong>Windows Server 2008 R2</strong></span>
      </td>
      
      <td style="background: #bdd6ee;padding-left: 7px;padding-right: 7px;border-top: none;border-left: none;border-bottom: solid white 0.5pt;border-right: solid white 0.5pt">
        <span style="color: black;font-family: Arial;font-size: 10pt">C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr_31bf3856ad364e35_6.1.7600.16385_none_c9392808773cd7da\<strong>cleanmgr.exe</strong></span>
      </td>
    </tr>
    
    <tr style="height: 43px">
      <td style="background: #5b9bd5;padding-left: 7px;padding-right: 7px;border-top: none;border-left: solid white 0.5pt;border-bottom: solid white 0.5pt;border-right: solid white 0.5pt">
        <span style="color: black;font-family: Arial;font-size: 10pt"><strong>Windows Server 2008 R2</strong></span>
      </td>
      
      <td style="background: #deeaf6;padding-left: 7px;padding-right: 7px;border-top: none;border-left: none;border-bottom: solid white 0.5pt;border-right: solid white 0.5pt">
        <span style="color: black;font-family: Arial;font-size: 10pt">C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b9cb6194b257cc63\<strong>cleanmgr.exe.mui</strong></span>
      </td>
    </tr>
  </table>
</div>

  1. <span style="color: black;font-family: Arial;font-size: 9pt">Copy<strong> Cleanmgr.exe</strong> to <strong>%systemroot%\System32</strong><br /> </span>
  2. <span style="color: black;font-family: Arial;font-size: 9pt">Copy <strong>Cleanmgr.exe.mui</strong> to <strong>%systemroot%\System32\en-US</strong><br /> </span>
  3. <span style="color: black;font-family: Arial;font-size: 9pt">Run <strong>Cleanmgr.exe</strong> from an elevated Command Prompt<br /> </span>

<span style="color: black;font-family: Arial;font-size: 9pt"><br /> </span>