---
title: No Sound in Adobe Flash Videos
permalink: /win/no-sound-in-adobe-flash-vids/
categories:
  - Windows
---
  1. Click Start
  2. Click Run
  3. Type in:  cmd.exe
  4. Press Enter
  5. Type: sfc /scannow

_Wait for scan to complete, you may need your Windows CD/DVD for this if it needs to copy data from it._

If the above did not work, try the following below:

  1.  Open Notepad (Start, Programs, Accessories, Notepad)
  2. Select the text below and right click it and choose Copy.

_Windows Registry Editor Version 5.00_

_[HKEY\LOCAL\MACHINE\SOFTWARE\Microsof\tWindows NT\CurrentVersion\Drivers32]_

_&#8220;midimapper&#8221;=&#8221;midimap.dll&#8221;_

_&#8220;msacm.imaadpcm&#8221;=&#8221;imaadp32.acm&#8221;_

_&#8220;msacm.msadpcm&#8221;=&#8221;msadp32.acm&#8221;_

_&#8220;msacm.msg711&#8243;=&#8221;msg711.acm&#8221;_

_&#8220;msacm.msgsm610&#8243;=&#8221;msgsm32.acm&#8221;_

_&#8220;msacm.trspch&#8221;=&#8221;tssoft32.acm&#8221;_

_&#8220;vidc.cvid&#8221;=&#8221;iccvid.dll&#8221;_

_&#8220;VIDC.I420&#8243;=&#8221;i420vfw.dll&#8221;_

_&#8220;vidc.iv31&#8243;=&#8221;ir32_32.dll&#8221;_

_&#8220;vidc.iv32&#8243;=&#8221;ir32_32.dll&#8221;_

_&#8220;vidc.iv41&#8243;=&#8221;ir41_32.ax&#8221;_

_&#8220;VIDC.IYUV&#8221;=&#8221;iyuv_32.dll&#8221;_

_&#8220;vidc.mrle&#8221;=&#8221;msrle32.dll&#8221;_

_&#8220;vidc.msvc&#8221;=&#8221;msvidc32.dll&#8221;_

_&#8220;VIDC.YVYU&#8221;=&#8221;msyuv.dll&#8221;_

_&#8220;wavemapper&#8221;=&#8221;msacm32.drv&#8221;_

_&#8220;msacm.msg723&#8243;=&#8221;msg723.acm&#8221;_

_&#8220;vidc.M263&#8243;=&#8221;msh263.drv&#8221;_

_&#8220;vidc.M261&#8243;=&#8221;msh261.drv&#8221;_

_&#8220;msacm.msaudio1&#8243;=&#8221;msaud32.acm&#8221;_

_&#8220;msacm.sl\_anet&#8221;=&#8221;sl\_anet.acm&#8221;_

_&#8220;msacm.iac2&#8243;=&#8221;C:WINDOWSsystem32iac25_32.ax&#8221;_

_&#8220;vidc.iv50&#8243;=&#8221;ir50_32.dll&#8221;_

_&#8220;wave&#8221;=&#8221;wdmaud.drv&#8221;_

_&#8220;midi&#8221;=&#8221;wdmaud.drv&#8221;_

_&#8220;mixer&#8221;=&#8221;wdmaud.drv&#8221;_

_&#8220;VIDC.WMV3&#8243;=&#8221;wmv9vcm.dll&#8221;_

_&#8220;VIDC.VP40&#8243;=&#8221;vp4vfw.dll&#8221;_

_&#8220;msacm.voxacm160&#8243;=&#8221;vct3216.acm&#8221;_

_&#8220;MSVideo&#8221;=&#8221;vfwwdm32.dll&#8221;_

_&#8220;MSVideo8&#8243;=&#8221;VfWWDM32.dll&#8221;_

_&#8220;wave1&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;midi1&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;mixer1&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;aux&#8221;=&#8221;wdmaud.drv&#8221;_

_&#8220;vidc.VP70&#8243;=&#8221;vp7vfw.dll&#8221;_

_&#8220;vidc.X264&#8243;=&#8221;x264vfw.dll&#8221;_

_&#8220;VIDC.FPS1&#8243;=&#8221;frapsvid.dll&#8221;_

_&#8220;vidc.VP60&#8243;=&#8221;vp6vfw.dll&#8221;_

_&#8220;vidc.VP61&#8243;=&#8221;vp6vfw.dll&#8221;_

_&#8220;vidc.VP62&#8243;=&#8221;vp6vfw.dll&#8221;_

_&#8220;vidc.DIVX&#8221;=&#8221;DivX.dll&#8221;_

_&#8220;VIDC.UYVY&#8221;=&#8221;msyuv.dll&#8221;_

_&#8220;VIDC.YUY2&#8243;=&#8221;msyuv.dll&#8221;_

_&#8220;VIDC.YVU9&#8243;=&#8221;tsbyuv.dll&#8221;_

_&#8220;VIDC.DRAW&#8221;=&#8221;DVIDEO.DLL&#8221;_

_&#8220;VIDC.YV12&#8243;=&#8221;yv12vfw.dll&#8221;_

_&#8220;wave2&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;midi2&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;mixer2&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;aux1&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;wave3&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;midi3&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;mixer3&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;aux2&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;VIDC.MSUD&#8221;=&#8221;msulvc05.dll&#8221;_

_&#8220;wave4&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;midi4&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;mixer4&#8243;=&#8221;wdmaud.drv&#8221;_

_&#8220;aux3&#8243;=&#8221;wdmaud.drv&#8221;_

Click File and Save As
3. Save as: registry.reg
4. Save it as missing.reg
5. Run: missing.reg

If the above did not work, try the following below:

Another issue is due to some Wavemapper windows registry files. You need to open Registry Editor.

  1. Click Start
  2. Click Run
  3. Type: regedit
  4. Press Enter
  5. Navigate to:  HKEY\LOCAL\MACHINE\SOFTWAR\EMicrosof\tWindows NT\CurrentVersion\Drivers32
  6. Click on My Computer and on the right hand side click New/String Value and type: wavemapper then press Enter and type: msacm32.drv
  7. Click Ok and restart machine.
