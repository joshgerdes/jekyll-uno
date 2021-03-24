---
date: 2021-03-25 00:00:00 +1300
title: 'Unable to start Windows Azure Guest Agent (it''s in a disabled state). '
author: Luke
categories:
- Azure
toc: true

---

## Issue Description

Unable to start Windows Azure Guest Agent (it's in a disabled state). When trying and set the service to auto the following error occurs 'The specified service has been marked for deletion.

VM Agent is unable to communicate with the Azure Backup service.

## Root Cause

This may occurr if Windows Communication Framework (WCF) profiling is enabled. WCF profiling should only be enabled while debugging a WCF issue. It should not be left enabled while running a production workload.

## Resolution

* Disable WCF profiling:

1. Launch an elevated CMD prompt.

* Run the following commands to back up the existing: C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\Config\\machine.config file:

    cd C:\Windows\Microsoft.NET\Framework\v4.0.30319\Config

    copy machine.config machine.config.bak

2. Run notepad machine.config to edit the file in Notepad.

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