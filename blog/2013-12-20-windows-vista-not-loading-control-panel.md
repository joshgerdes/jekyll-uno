---
title: Windows Vista – Not loading Control Panel
tags:
  - Windows
date: 2013-12-20 00:00:00 +1300
---

Having problems when you try opening the Vista Control panel and all you see is the outline of the window? 

Follow the instructions below to repair it. 

1. Left Click the Vista &#8220;Orb&#8221; 

2. Left Click All Programs 

3. Left Click Accessories 

5. Left Click Notepad 

6. Copy & paste the following into Notepad (To copy, select the text below and click Copy. To paste, right click on where you would like to paste it and select Paste) 


net stop readyboost 

net stop slsvc 

net start slsvc 

net start readyboost 

@cls 


7. Click File 

8. click Save 

9. Save the file as &#8220;ControlPanelFix.bat&#8221; and close Notepad 

10. Run the ControlPanelFix.bat file. 

Note: You can also try accessing parts of Control Panel by going to Computer, and in the left hand pane, select Control Panel
