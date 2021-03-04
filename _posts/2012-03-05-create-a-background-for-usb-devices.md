---
title: Create a background for USB Devices
permalink: /win/create-a-background-for-usb-devices/
categories:
  - Windows
---
Follow the instructions below to assign a picture to a folders background, commonly used to personalise USB flash drives.

  1. First, open notepad. _(Start, Run, type in: notepad, press Enter_
  2. Copy the below coding to the notepad:

[ExtShellFolderViews]
  
{BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}

[{BE098140-A513-11D0-A3A4-00C04FD706EC}]
  
Attributes=1
  
IconArea_Image=back/back.jpg
  
IconArea_Text=0x00ffffff

Save as autorun.inf and exit
  
Edit the:

IconArea_Image=back/back.jpg _(The location of the JPG image you want to use)_
  
IconArea_Text=0x00ffffff _(Edit this colour in hex to display the Icons text colour)_
