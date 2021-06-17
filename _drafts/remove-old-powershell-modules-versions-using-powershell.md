---
date: 2021-06-18 00:00:00 +1200
title: Remove old powershell modules versions using powershell
author: Luke
categories:
- PowerShell
toc: false
header:
  teaser: ''

---
Did you know, that if you update PowerShell modules, the old versions can sometimes get left behind?

This little snippet with remove any old PowerShell modules (that are not the latest version), which are installed.

    #requires -Version 2.0 -Modules PowerShellGet
    function Remove-OldModules
    {
      <#
    <#
        Author: Luke Murray (Luke.Geek.NZ)
        Version: 0.1
        Purpose: Basic function to remove old PowerShell modules which are installed
    #>
    
      #>
      $Latest = Get-InstalledModule 
      foreach ($module in $Latest) { 
        
        Write-Verbose -Message "Uninstalling old versions of $($module.Name) [latest is $( $module.Version)]" -Verbose
        Get-InstalledModule -Name $module.Name -AllVersions | Where-Object {$_.Version -ne $module.Version} | Uninstall-Module -Verbose 
      }
    }
    
    Remove-OldModules