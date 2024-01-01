---
title: Increase Internet Explorers Download Limit
date: 2012-09-05T21:39:27+00:00
authors: [Luke]
tags:
  - Windows
---
Internet Explorer limits the amount of concurrent downloads. This is how you increase it

  1.  Click **Start**
  2. Click **Run**
  3. Type in &#8220;**notepad**&#8221; and press enter
  4. **Copy** the following and **paste** the HKey Local machine code underneath these instructions.
  5. Save the document as **&#8220;IEDownloads.reg**&#8220;
  6. **Go** to where you **saved** the **document** and double **click** it to **merge** it into the **registry**. If a confirmation prompt appears then **accept** it.
  7. **Restart** the computer and you should be able to download more then 8 files at a time.

&nbsp;

[HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftInternet ExplorerMAINFeatureControlFEATURE_MAXCONNECTIONSPERSERVER]

&#8220;iexplore.exe&#8221;=dword:0000000a