---
title: Unable to Remote Desktop into Computer
tags:
  - Windows
date: 2014-04-27 00:00:00 +1300
---
There can be various reasons why people are unable to Remote Desktop into a Computer – one of the reasons could be they are not in the Remote Desktop users group on the local machine or the necessary services – for Remote Desktop connectivity aren’t enabled. Follow the guide below to make sure the services are fully enabled and up and running you can test one at a time.

  1. Open **Run**
  2. Type in: **services.msc**
  3. Click **Action**
  4. Click **Connect to another computer**
  5. **Type** in the **hostname** of the **PC** you are connecting to and press **Enter** to connect
  6. In the Services list **navigate** **to** the **following** and make sure they are started by double clicking to open the Services Property box –changing the Start-up type to Automatic and select Start:
  
    •    Remote Access Auto Connection Manager
  
    •    Remote Access Connection Manager
  
    •    Routing and Remote Access
  7. Once those have been changed navigate to the: Windows Firewall/Internet Connection Sharing (ICS) service and change Start-up type to: Disabled and stop the service.
