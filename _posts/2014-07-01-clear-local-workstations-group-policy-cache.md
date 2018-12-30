---
title: How to clear the local workstations Group Policy cache
permalink: /win/clear-local-workstations-group-policy-cache/
categories:
  - Windows
  - PowerShell
---

## <span id="Option_1">Option 1</span>

  1. Open My Computer/Computer
  2. In the URL or address bar paste: %windir%\system32\GroupPolicy
  3. Right click and delete the: Machine and User folders to clear local group policy cache
  4. Restart the computer to reapply the group policies

Note: You can also run: gpupdate /force on the machine to force the policy to reapply.

You can also run the little PowerShell oneliner as Administrator to remove the Group Policy folder and all files below:

{% highlight powershell %}

#requires -Version 1.0
#Requires -RunAsAdministrator

Remove-Item "$env:windir\system32\GroupPolicy" -Force -Recurse


{% endhighlight %}

## <span id="Option_2">Option 2</span>

  1. Delete the &#8220;HKLM\Software\Policies\Microsoft&#8221; Key (looks like a folder).
  2. Delete the &#8220;HKCU\Software\Policies\Microsoft&#8221; Key
  3. Delete the &#8220;HKCU\Software\Microsoft\Windows\CurrentVersion\Group Policy Objects&#8221; Key.
  4. Delete the &#8220;HKCU\Software\Microsoft\Windows\CurrentVersion\Policies&#8221; Key.

## <span id="Option_3">Option 3</span>

  1. Remove the computer from the domain &#8211; (change to a Workgroup)
  2. Restart computer
  3. Run gpupdate /force
  4. Rejoin the domain
