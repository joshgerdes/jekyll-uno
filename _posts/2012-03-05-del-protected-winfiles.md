---
title: Deleting protected files in Windows
permalink: /win/del-protected-winfiles/
categories:
  - Windows
---
The Windows operating system is known for many things – including its ability to protect system and user protected files.

Using the TakeOwn _(built into Windows)_ command you can easily use the utility to take ownership of files which would otherwise be system or user protected.

Follow my simple guide below to take ownership of files:

  1. First you need an elevated command prompt – Run Command Prompt as Administrator.
  2. To take ownership of the file, you&#8217;ll need to use the takeown command for example:
  3. **`takeown /f c:/Windows/system32/AdobePDF.dll`**
  4. That will give you ownership of the file, but you still have no rights to delete it.
  5. Now you can run the cacls command to give yourself full control rights to the file:

  6. **cacls c:/Windows/system32/AdobePDF.dll /G test:F**

Note that my username is test, so you will substitute your username there.

You should be able to delete the file<em>. If you still can't do so, you may need to reboot into Safe Mode and try it again.
