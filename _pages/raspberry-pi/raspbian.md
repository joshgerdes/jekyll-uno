

## Getting started

Download image

Burn SD card

boot

## Docker

```
sudo apt-get install docker.io docker-compose
```

## Startup

### Bashrc

```
nano .bashrc
```

### Autostart

If you need access to elements from the X Window System (e.g. you are making a graphical dashboard or game), then you will need to wait for the X server to finish initializing before running your code. One way to accomplish this is to use the autostart system.

```bash
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/clock.desktop
```

```bash
[Desktop Entry]
Type=Application
Name=Clock
Exec=/usr/bin/python3 /home/pi/clock.py
```

