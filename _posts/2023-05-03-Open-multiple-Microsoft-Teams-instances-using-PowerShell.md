---
title: Open multiple Microsoft Teams instances using PowerShell
author: Luke
permalink: /m365/Open-multiple-Microsoft-Teams-instances-using-PowerShell/
toc: false
categories:
  - M365
  - PowerShell
description: >-
  Open multiple Microsoft Team instances, for access to multiple accounts with
  PowerShell
header:
  teaser: /images/posts/MS_Teams_logo_ws.png
date: 2023-05-02T12:00:00.000Z
---

There may be circumstances, you need to open up multiple Microsoft Team instances, a reason for this - maybe to chat and join meetings across multiple accounts.

Microsoft are working on a version of [Microsoft Teams](https://techcommunity.microsoft.com/t5/microsoft-teams-public-preview/bd-p/MicrosoftTeamsPublicPreview?WT.mc_id=AZ-MVP-5004796 "Microsoft Teams Public Preview"){:target="blank"} that supports multiple-accounts, but until thats released - you can use a PowerShell script to open up another version of Microsoft Teams in another profile *(or multiple, if you update the profilename)*.  

This script also works within your LocalAppData, so you don't need local administrator rights to run.

```powershell
# Uses the file name as the profile name
$MSTEAMS_PROFILE = 'CustomProfile'

Write-Host "- Using profile '$MSTEAMS_PROFILE'"

# Set the custom profile path
$USERPROFILE = Join-Path $env:LOCALAPPDATA "Microsoft\Teams\CustomProfiles\$MSTEAMS_PROFILE"

# Set the old user profile
$OLD_USERPROFILE = $env:USERPROFILE

# Launch MS Teams with the custom profile
Write-Host "- Launching MS Teams with profile '$MSTEAMS_PROFILE'"
Set-Location "$OLD_USERPROFILE\AppData\Local\Microsoft\Teams"

$teamsProcessStartInfo = New-Object System.Diagnostics.ProcessStartInfo
$teamsProcessStartInfo.FileName = "$OLD_USERPROFILE\AppData\Local\Microsoft\Teams\Update.exe"
$teamsProcessStartInfo.Arguments = "--processStart ""Teams.exe"""
$teamsProcessStartInfo.WorkingDirectory = "$OLD_USERPROFILE\AppData\Local\Microsoft\Teams"
$teamsProcessStartInfo.EnvironmentVariables["USERPROFILE"] = $USERPROFILE
$teamsProcessStartInfo.UseShellExecute = $false

[System.Diagnostics.Process]::Start($teamsProcessStartInfo) | Out-Null

# Set the user profile back to the old user profile
$env:USERPROFILE = $OLD_USERPROFILE

```

When the script is ran, a new profile will be created for Microsoft Teams, and then opened. You can then use that second Microsoft Teams instance, to connect to another account or tenancy.

To make it easier, you could also look at turning this script into an [executable](https://github.com/MScholtes/PS2EXE "PS2EXE"){:target="blank"}.
