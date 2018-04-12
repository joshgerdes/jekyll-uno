---
id: 3650
title: Windows Update Task Sequence (Patching) – SCCM 2012 R2
date: 2016-01-01T09:53:00+00:00
author: Luke
layout:
  - ""
guid: http://luke.geek.nz/?p=3650
permalink: /win/windows-update-task-sequence-patching-sccm-2012-r2/
post_views_count:
  - "2108"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4791340715"
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
image: /wp-content/uploads/2016/01/123115_2137_WindowsUpda1.png
categories:
  - Windows
---
With monthly server patching, the process is currently manual due to the number of clusters and very application specific servers that is patched – including an issue with failed updates caused by Trend Officescan &#8211; and an issue that has been done manually for months.

It was time to automate this process – and without Orchestrator or SMA I had to use what I already had – a SCCM 2012 R2 Infrastructure, and the use of the Task Sequence and PowerShell.

<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/01/123115_2137_WindowsUpda1.png?resize=624%2C563" alt="WinUpdate TS TS (Patching)" width="624" height="563" data-recalc-dims="1" />

The Windows Update Task Sequence process goes like this (updates are deployed to the servers as Available): Disables Trend OfficeScan Start-up type to: Disabled, run a Scheduled Task on the server _(this could be emailing a business user notifying their server is going down for patching or shutting down an application – this is intended to be Server SPECIFIC so the task sequence doesn&#8217;t need to be modified for every new server getting patched),_ Restart the computer _(this is done to make sure OfficeScan is not running and make sure the server is in a clean state for patching),_ and begin the patching process _(see more information on the steps below)_.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Task_Sequence_Patching_Steps_are_as_follows"><span class="toc_number toc_depth_1">1</span> Task Sequence Patching Steps are as follows:</a><ul>
        <li>
          <a href="#Disable_Trend_Office_scan_Services"><span class="toc_number toc_depth_2">1.1</span> Disable – Trend Office scan Services </a>
        </li>
        <li>
          <a href="#Run_SCHTask"><span class="toc_number toc_depth_2">1.2</span> Run SCHTask </a>
        </li>
        <li>
          <a href="#Restart_Computer"><span class="toc_number toc_depth_2">1.3</span> Restart Computer </a>
        </li>
        <li>
          <a href="#Scan_for_Updates"><span class="toc_number toc_depth_2">1.4</span> Scan for Updates | </a>
        </li>
        <li>
          <a href="#Wait_for_the_Scan_to_Finish"><span class="toc_number toc_depth_2">1.5</span> Wait for the Scan to Finish | </a>
        </li>
        <li>
          <a href="#Install_Software_Updates"><span class="toc_number toc_depth_2">1.6</span> Install Software Updates </a>
        </li>
        <li>
          <a href="#Restart_Computer-2"><span class="toc_number toc_depth_2">1.7</span> Restart Computer </a>
        </li>
        <li>
          <a href="#Scan_for_Updates-2"><span class="toc_number toc_depth_2">1.8</span> Scan for Updates || </a>
        </li>
        <li>
          <a href="#Wait_for_the_Scan_to_Finish-2"><span class="toc_number toc_depth_2">1.9</span> Wait for the Scan to Finish || </a>
        </li>
        <li>
          <a href="#Install_Software_Updates-2"><span class="toc_number toc_depth_2">1.10</span> Install Software Updates </a>
        </li>
        <li>
          <a href="#Restart_Computer-3"><span class="toc_number toc_depth_2">1.11</span> Restart Computer </a>
        </li>
        <li>
          <a href="#Scan_for_Updates-3"><span class="toc_number toc_depth_2">1.12</span> Scan for Updates ||| </a>
        </li>
        <li>
          <a href="#Wait_for_the_Scan_to_Finish-3"><span class="toc_number toc_depth_2">1.13</span> Wait for the Scan to Finish ||| </a>
        </li>
        <li>
          <a href="#Install_Software_Updates-3"><span class="toc_number toc_depth_2">1.14</span> Install Software Updates </a>
        </li>
        <li>
          <a href="#Restart_Computer-4"><span class="toc_number toc_depth_2">1.15</span> Restart Computer </a>
        </li>
        <li>
          <a href="#Scan_for_Updates_V"><span class="toc_number toc_depth_2">1.16</span> Scan for Updates |V </a>
        </li>
        <li>
          <a href="#Wait_for_the_Scan_to_Finish_V"><span class="toc_number toc_depth_2">1.17</span> Wait for the Scan to Finish |V </a>
        </li>
        <li>
          <a href="#Install_Software_Updates-4"><span class="toc_number toc_depth_2">1.18</span> Install Software Updates </a>
        </li>
        <li>
          <a href="#Restart_Computer-5"><span class="toc_number toc_depth_2">1.19</span> Restart Computer </a>
        </li>
        <li>
          <a href="#Software_Update_Deployment_Re-Eval"><span class="toc_number toc_depth_2">1.20</span> Software Update Deployment Re-Eval </a>
        </li>
        <li>
          <a href="#Enable_Trend_Office_scan_Services"><span class="toc_number toc_depth_2">1.21</span> Enable – Trend Office scan Services </a>
        </li>
      </ul>
    </li>
  </ul>
</div>

# <span id="Task_Sequence_Patching_Steps_are_as_follows">Task Sequence Patching Steps are as follows:</span>

## <span id="Disable_Trend_Office_scan_Services"><strong>Disable – Trend Office scan Services<br /> </strong></span>

This calls a PowerShell script which changes the Startup Type of: Office Scan NT Real-time Scan and Office Scan NT Listener services to Disable. This is changed to prevent the Trend Antivirus solution from interfering with the download and installation of Software Updates. Note: Some servers encountered issues stopping the Trend service, the restart step after this stops the Trend service from starting

<pre class="lang:ps decode:true ">Get-Service tmlisten, ntrtscan | Set-Service -StartupType disabled</pre>

## <span id="Run_SCHTask"><strong>Run SCHTask<br /> </strong></span>

This step starts a Scheduled Task &#8220;PreShutdown&#8221; that has been setup on the deployed server. This scheduled task allows for server based automation _(application shutdown, business communication etc)_ and is specific to the server. This is a Command Line Step.**
  
** 

<pre class="lang:default decode:true ">schtasks /run /TN "\WinUpdate\PreShutdown"</pre>

## <span id="Restart_Computer"><strong>Restart Computer<br /> </strong></span>

This step counts down for 60 seconds and notifies the user &#8220;This server is undergoing Windows patching. Please save your work and log off&#8221; before then Restarting the computer

## <span id="Scan_for_Updates"><strong>Scan for Updates |<br /> </strong></span>

This step does a WMI call to do a Software Update re-evaluation to determine if there are any new Windows Updates that are required by the system

<pre class="lang:default decode:true">WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000113}" /NOINTERACTIVE</pre>

## <span id="Wait_for_the_Scan_to_Finish"><strong>Wait for the Scan to Finish |<br /> </strong></span>

This step is a PowerShell command to sleep the system for 30 seconds. This step is set to allow the Software Update re-evaluation cycle from the previous step to complete

<pre class="lang:ps decode:true">Powershell.exe -command start-sleep 30</pre>

## <span id="Install_Software_Updates"><strong>Install Software Updates<br /> </strong></span>

Installs all required and available Windows Updates on the Windows server

## <span id="Restart_Computer-2"><strong>Restart Computer<br /> </strong></span>

This step Restarts the computer after the first batch of patches have been installed

## <span id="Scan_for_Updates-2"><strong>Scan for Updates ||<br /> </strong></span>

This step does a WMI call to do a Software Update re-evaluation to determine if there are any new Windows Updates that are required by the system

<pre class="lang:default decode:true">WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000113}" /NOINTERACTIVE</pre>

## <span id="Wait_for_the_Scan_to_Finish-2"><strong>Wait for the Scan to Finish ||<br /> </strong></span>

This step is a PowerShell command to sleep the system for 30 seconds. This step is set to allow the Software Update re-evaluation cycle from the previous step to complete

<pre class="lang:ps decode:true">Powershell.exe -command start-sleep 30</pre>

## <span id="Install_Software_Updates-2"><strong>Install Software Updates<br /> </strong></span>

Installs all required and available Windows Updates on the Windows server

## <span id="Restart_Computer-3"><strong>Restart Computer<br /> </strong></span>

This step Restarts the computer after the first batch of patches have been installed

## <span id="Scan_for_Updates-3"><strong>Scan for Updates |||<br /> </strong></span>

This step does a WMI call to do a Software Update re-evaluation to determine if there are any new Windows Updates that are required by the system

<pre class="lang:default decode:true">WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000113}" /NOINTERACTIVE</pre>

## <span id="Wait_for_the_Scan_to_Finish-3"><strong>Wait for the Scan to Finish |||<br /> </strong></span>

This step is a PowerShell command to sleep the system for 30 seconds. This step is set to allow the Software Update re-evaluation cycle from the previous step to complete

<pre class="lang:ps decode:true">Powershell.exe -command start-sleep 30</pre>

## <span id="Install_Software_Updates-3"><strong>Install Software Updates<br /> </strong></span>

Installs all required and available Windows Updates on the Windows server

## <span id="Restart_Computer-4"><strong>Restart Computer<br /> </strong></span>

This step Restarts the computer after the first batch of patches have been installed

## <span id="Scan_for_Updates_V"><strong>Scan for Updates |V<br /> </strong></span>

This step does a WMI call to do a Software Update re-evaluation to determine if there are any new Windows Updates that are required by the system

<pre class="lang:default decode:true">WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000113}" /NOINTERACTIVE</pre>

## <span id="Wait_for_the_Scan_to_Finish_V"><strong>Wait for the Scan to Finish |V<br /> </strong></span>

This step is a PowerShell command to sleep the system for 30 seconds. This step is set to allow the Software Update re-evaluation cycle from the previous step to complete

<pre class="lang:ps decode:true">Powershell.exe -command start-sleep 30</pre>

## <span id="Install_Software_Updates-4"><strong>Install Software Updates<br /> </strong></span>

Installs all required and available Windows Updates on the Windows server

## <span id="Restart_Computer-5"><strong>Restart Computer<br /> </strong></span>

This step Restarts the computer after the first batch of patches have been installed

## <span id="Software_Update_Deployment_Re-Eval"><strong>Software Update Deployment Re-Eval<br /> </strong></span>

This step forces the SCCM agent to &#8220;check in&#8221; and run a Compliance check on the Software Update deployment allowing for SCCM have accurate Compliance data at the end of the Task Sequence

<pre class="lang:default decode:true">WMIC /namespace:\\root\ccm path sms_client CALL TriggerSchedule "{00000000-0000-0000-0000-000000000114}" /NOINTERACTIVE</pre>

## <span id="Enable_Trend_Office_scan_Services"><strong>Enable – Trend Office scan Services<br /> </strong></span>

This calls a PowerShell script which changes the Startup Type of: Office Scan NT Real-time Scan and Office Scan NT Listener services to Enable. This PowerShell script also Starts the services.

<pre class="lang:ps decode:true">Get-Service tmlisten, ntrtscan |
Set-Service -StartupType automatic -PassThru |
Start-Service</pre>