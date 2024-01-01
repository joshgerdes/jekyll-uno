---
title: How to fix Telecom T-Stick/Vodafone Vodem Initializing issues
date: 2012-08-22T10:29:18+00:00
authors: [Luke]
tags:
  - Windows
---
_Make sure you have credit on your Vodem/T-Stick. This is the common cause of why the modems will not load webpages._

<ol start="1">
  <li>
    <strong>Disconnect</strong> the <strong>T-Stick/Vodem</strong>
  </li>
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Programs/All Programs</strong>
  </li>
  <li>
    Click <strong>Accessories</strong>
  </li>
  <li>
    Click <strong>Command Prompt</strong>
  </li>
  <li>
    Type:  <strong><em>set devmgr_show_nonpresent_devices=1</em></strong> <em>(this will reveal hidden device drivers in device manager) </em>> Press <strong>Enter</strong>
  </li>
  <li>
    Now we need to load Device Manager, click <strong>Start</strong>
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> <strong>Computer/My Computer</strong>
  </li>
  <li>
    Click the <strong>hardware</strong> tab
  </li>
  <li>
    Click <strong>Device Manager</strong>
  </li>
  <li>
    Click <strong>View</strong>
  </li>
  <li>
    Click <strong>Show Hidden Devices</strong>
  </li>
  <li>
    Device Manager will now display a list of devices that look transparent
  </li>
  <li>
    Go through the list, clicking “<strong>+</strong>” next to each one, mainly in the <strong>Network Adapters</strong> and <strong>Universal Serial Bus controllers</strong> sub-section.
  </li>
  <li>
    <strong>Look</strong> for anything <strong>related</strong> to <strong>ZTE/Vodafone/Telecom T-Stick</strong>
  </li>
  <li>
    Now <strong>right</strong> <strong>click</strong> the <strong>devices</strong> that indicate they are for the device and select <strong>Uninstall</strong>, click Ok to <strong>confirm</strong>
  </li>
  <li>
    Once you have removed the devices relating to the mobile broadband device, <strong>close</strong> <strong>Device</strong> <strong>Manager</strong>.
  </li>
  <li>
    <strong>Reconnect</strong> the <strong>T-Stick/Vodem</strong> and your computer should recognise it as a new device and install. It should now be up and running.  If not repeat step 14.
  </li>
</ol>