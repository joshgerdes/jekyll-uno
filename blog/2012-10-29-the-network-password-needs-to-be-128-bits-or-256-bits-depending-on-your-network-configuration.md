---
title: The network password needs to be 128 bits or 256 bits depending on your network configuration
date: 2012-10-29 00:00:00 +1300
authors: [Luke]
tags:
  - Windows
---
Attempting to enter in your wireless passkey and getting “The network password needs to be 128bits or 256bits depending on your network configuration “error? This usually occurs when the networking stack has been damaged/corrupted. Follow the instructions below to repair:

  1. Click **Start**
  2. Click **Run**
  3. Type in: _**cmd**_
  4. Press **Enter**
  5. The windows Command Prompt should launch, type in: **_netsh winsock reset_**
  6. Press **Enter**
  7. **Restart** your **computer** and attempt wireless connectivity.