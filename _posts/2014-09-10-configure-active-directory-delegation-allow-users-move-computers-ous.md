---
title: How to configure Active Directory delegation to allow users to move computers between OUs
permalink: /win/configure-active-directory-delegation-allow-users-move-computers-ous/
categories:
  - Windows
---
  1. Open Active Directory Users & Computers with AD rights
  2. Right click on the organisation unit you want to give access to and click Delegate Control
  3. Add the group want to give this access to, for example “IT HelpDesk”
  4. Select “Create a custom task to delegate” and click Next
  5. Select “Only the following objects in this folder”
  6. Check “Computer Objects”
  7. Check “Create selected objects in this folder”
  8. Check “Delegate selected objects in this folder” and click Next
  9. Make sure Write is checked and click Next
 10. Click Finish

Repeat steps 2 to 10 again on other OUs you would like to delegate move rights to.
