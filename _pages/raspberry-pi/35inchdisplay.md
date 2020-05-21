---
title: how to install 35inch display
date: 2016-01-08 15:04:23
category: raspberry-pi
tags: [python]

layout: page
---

How to Install 3.5 Inch LCD on Raspberry Pi

Plugging the LCD will not work for the first time (you will get a white screen only) unless you have done some coding in Raspbian OS. Below are the very easy steps how to install a 3.5 inch LCD on Raspberry Pi.

1) Connect your Raspberry Pi to a PC monitor, also connect the 3.5 inch LCD to Pi.
2) Turn on the pi and make sure its connected to the Internet via WiFi or LAN.
3) Open terminal in Raspbian desktop, and type the following commands.

```bash
sudo rm -rf LCD-show 
git clone https://github.com/goodtft/LCD-show.git 
chmod -R 755 LCD-show 
cd LCD-show/
sudo ./LCD35-show
```

But now the display will not visible on the monitor, it will only visible to the Raspberry Pi LCD. If you want revert back to the monitor, Open the terminal and type commands to get back.

```bash
chmod -R 755 LCD-show 
cd LCD-show/ 
sudo ./LCD-hdmi
```
