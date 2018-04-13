---
title: 'Windows Vista Black Screen &#038; Slow to Boot Repair'
permalink: /win/winvistablack/
categories:
  - Windows
---

Ever had the problem where Windows Vista has a Black screen, while trying to boot? I have. This is how I fixed it (For Advanced users only).

  1. Delete the following folders/files
  2. _**C:/windows/system32/drivers/pcmcia.sys**_
  3. _**C:/windows/system32/drivers/1394bus.sys**_
  4. _**C:/windows/system32/driversohci1394.sys**_
  5. _**C:/windows/system32/driverstore/filerepository/pcmcia.***_
  6. _**C:/windows/system32/driverstore/filerepository/1394.infblablabla**_
  7. _**C:/windows/system32/driverstore/filerepository/sdbus.infblablabla***_
  8. _**C:/windows/infsdbus.inf***_
  9. _**C:/windows/infsdbus.PNF***_
 10. Restart your computer and choose to edit boot options. You will see a screen which shows default windows boot options: /noexecute=optin. After optin, _**add /debug**_ command and press esc. (There needs to be a space between optin and /debug.)
 11. Find and delete the following files
 12. Delete _**sptd.sys**_
 13. Delete _**sptd.sy**_
 14. Delete _**sptd.sys**_
 15. Delete _**sptd.sys**_
 16. Go to a command prompt and run the following commands
 17. _**cd windows**_
 18. _**del \*pcmcia\*.* /s/p**_
 19. _**del \*1394\*.* /s/p**_
 20. Restart computer.

Still not working? Try these additional options below.

  1. Press **F2** to enter **BIOS** mode
  2. 2. Under &#8220;**Onboard Devices**&#8221; select &#8220;**Flash Cache Module**&#8221; and set it to &#8220;**Off**&#8221; (you cannot disable SATA unless this is set to &#8220;Off&#8221; mode.
  3. Move up to **&#8220;SATA Operation**&#8221; and change from &#8220;AHCI&#8221; to &#8220;**ATA**&#8220;.
  4. Restart the computer.
