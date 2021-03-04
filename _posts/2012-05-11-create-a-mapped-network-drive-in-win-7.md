---
title: How to create a mapped Network drive in Windows 7
date: 2012-05-11 00:00:00 +12:00
permalink: "/win/create-a-mapped-network-drive-in-win-7/"
categories:
- Windows
---

Follow the instructions to create a mapped network drive in Windows 7 without windows indexing like a local folder?

  1. Create a new folder for your network shares (ie c:Shared)
  2. Go into the folder you created and make a new folder  (ie c:SharedMovies)
  3. Now you need to link the library into the folder you create in the second step  (ie c:SharedMovies) by going into Documents and up the top click &#8220;Includes: 2 locations&#8221; and click Add and add the folder.
  4. Now go back to your original folder you created  (ie c:Shared) and delete the folder you made in the second step (ie c:SharedMovies)
  5. Now we make a link to link the folder to the remote folder and to do that we need the Command Prompt, click Start, Run type: cmd and press Enter
  6. Type in: mklink /d c:Shared remotemachinefolder and press Enter
  7. Now your Documents folder should include your remote folder mapped through the c:Shared folder you created earlier like it is a normal folder.
