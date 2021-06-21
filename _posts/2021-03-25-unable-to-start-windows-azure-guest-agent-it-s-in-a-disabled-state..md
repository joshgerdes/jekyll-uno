---
date: 2021-03-25T00:00:00.000+13:00
title: Unable to start Windows Azure Guest Agent (it's in a disabled state)
author: Luke
categories:
- Azure
toc: true
header: 
  teaser: "images/iazure-marketplace-banner.png"
---
![](https://csharpcorner.azureedge.net/article/an-overview-of-azure-backup/Images/An%20Overview%20Of%20Azure%20Backup01.png)

* TOC
{:toc}

## Issue Description

Unable to start Windows Azure Guest Agent (it's in a disabled state). When trying and set the service to auto the following error occurs 'The specified service has been marked for deletion.'

VM Agent is unable to communicate with the Azure Backup service.

## Root Cause

This may occur if Windows Communication Framework (WCF) profiling is enabled. WCF profiling should only be enabled while debugging a WCF issue. It should not be left enabled while running a production workload.

## Resolution #1

1\. Restart your workload, I would recommend to Stop (deallocate first) to make sure that the workload starts correctly on a new hypervisor, the Azure Backup agent starts and checks for agent updates during the boot process.

## Resolution #2

Disable WCF profiling:

1\. Launch an elevated CMD prompt.
2\. Run the following commands to back up the existing: C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\Config\\machine.config file:

       cd C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config

       copy machine.config machine.config.bak
3\. Run notepad machine.config to edit the file in Notepad.

Remove this text, being careful not to also remove any additional text that may be on the same line:

    <add name="Microsoft.VisualStudio.Diagnostics.ServiceModelSink.Behavior" type="Microsoft.VisualStudio.Diagnostics.ServiceModelSink.Behavior, Microsoft.VisualStudio.Diagnostics.ServiceModelSink, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"/>

Also remove this text, being careful not to also remove any additional text that may be on the same line:

    <commonBehaviors><endpointBehaviors><Microsoft.VisualStudio.Diagnostics.ServiceModelSink.Behavior/></endpointBehaviors><serviceBehaviors><Microsoft.VisualStudio.Diagnostics.ServiceModelSink.Behavior/></serviceBehaviors></commonBehaviors>

4\. Save and close the file.
5\. Restart the guest agent services:

    net stop Rdagent
    
    net stop WindowsAzureGuestAgent
    
    net stop WindowsAzureTelemetryService
    
    net start Rdagent

6\. In some cases the VM may need to be restarted for the WCF disablement to take effect.

## Resolution #3

From time to time the Azure backup agent may fail. Sometimes this will self-resolve but on the odd occasion, additional steps may be needed.

1\. Uninstall the agent via the Control Panel.
2\. Open CMD as Admin.
3\. Stop the following services:

    net stop rdagent
    
    net stop WindowsAzureGuestAgent
    
    net stop WindowsAzureTelemetryService 

4\. Delete all the services of the agent:

    sc delete rdagent
    
    sc delete WindowsAzureGuestAgent
    
    sc delete WindowsAzureTelemetryService 
   
5\. Create a folder called OLD in "C:\ WindowsAzure" and move the old version of the agent to it and the folders that say Packages. 
6\. Install the service again using the link: [https://go.microsoft.com/fwlink/?LinkID=394789&clcid=0x409](https://go.microsoft.com/fwlink/?LinkID=394789&clcid=0x409 "https://go.microsoft.com/fwlink/?LinkID=394789&clcid=0x409") or the latest agent available.  
7\. Restart the server.

## Resolution #4

1\. Migrate the Pagefile to a new disk
2\. Set a limit on the pagefile