---
title: Unable to right click in Microsoft Excel
categories:
  - Windows
---
This is fixed by removing the Excel11.xlb excel template file located in the following locations:

Win7 32bit:

C:/Program Files/Microsoft Office/Office14/XLSTART

C:/Users/UserName/AppData/Roaming/Microsoft/Excel/XLSTART

Win7 64bit:

C:/Program Files(x86)/Microsoft Office/Office14/XLSTART

C:/Users/UserName/AppData/Roaming/MicrosoftExcel/XLSTART

Note: Make sure Excel is closed before attempted to remove this file – Excel will automatically generate a new Excel11.xlb template.
