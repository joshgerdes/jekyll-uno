---
title: How to export local group policy settings into a HTML report
permalink: /win/how-to-export-local-group-policy-settings-into-a-html-report/
categories:
  - Windows
---
  1. Press the Windows Key + R to open the Run dialog box
  2. Type in: cmd and press Enter
  3. This will load the Windows Command Prompt
  4. Using the CD _(change directory)_ command – change your directory to where you want to save the report&#8230; for example “cd Desktop” will change to your Desktop.
  5. Type in: **gpresult /h LocalGrpPolReport.html** and press Enter

This will then load the group policy snap-in in the background and generate a HTML page called: &#8220;LocalGrpPolReport.html&#8221; that you will be able to open and see what policies have been applied to that local machine and which policies are taking precedence over others.
