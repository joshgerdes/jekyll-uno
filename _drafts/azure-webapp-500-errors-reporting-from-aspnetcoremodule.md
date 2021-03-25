---
date: 2021-03-27 00:00:00 +1300
title: Azure WebApp 500 Errors reporting from AspNetCoreModule
author: Luke
categories:
- Azure
toc: false

---
## Issue Description

Intermittent issues with Azure WebApp constantly stop functioning, a Stop/Start operation brings it back online.

## Root Cause

Further investigation using Azure Application Insights, reveals the Azure WebApp was experiencing a few FailedRequestCount, with HTTP 500 Errors. An exception was thrown by a TaskScheduler. Exception of type 'System.OutOfMemoryException' was thrown.

## Resolution

In my case, the service that was running on the Azure WebApp was using .NET Core 2.0, the fix was to upgrade to the latest version.

. .NET Core 2.0 is an unsupported version and we highly recommend upgrading to the latest version (3.1). Please take a look at this information of the .NET Core official support policy: [https://dotnet.microsoft.com/platform/support/policy/dotnet-core](https://dotnet.microsoft.com/platform/support/policy/dotnet-core "https://dotnet.microsoft.com/platform/support/policy/dotnet-core")

For .NET Core applications I suggest enabling the stdout logs, as those will capture some important errors: [https://docs.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-2.2#aspnet-core-module-stdout-log-azure-app-service-1](https://docs.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-2.2#aspnet-core-module-stdout-log-azure-app-service-1 "https://docs.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-2.2#aspnet-core-module-stdout-log-azure-app-service-1")

If those OutOfMemory exceptions come with a 5xx status code, I would suggest as well using the AutoHeal feature as it will allow setting rules based on that status code to capture a Memory Dump, you can check more information here: [https://azure.github.io/AppService/2018/09/10/Announcing-the-New-Auto-Healing-Experience-in-App-Service-Diagnostics.html](https://docs.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-2.2#aspnet-core-module-stdout-log-azure-app-service-1 "https://docs.microsoft.com/en-us/aspnet/core/test/troubleshoot-azure-iis?view=aspnetcore-2.2#aspnet-core-module-stdout-log-azure-app-service-1")