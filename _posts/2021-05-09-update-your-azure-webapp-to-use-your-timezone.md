---
date: 2021-05-09 00:00:00 +1200
title: Update your Azure WebApp to use your timezone
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "images/iazure-marketplace-banner.png"

---
By default, the timezone in Microsoft Azure defaults to UTC (Universal Coordinated Time) as a standard, as a universal and consistent timezone, this makes sense - however when troubleshooting issues or attempting to schedule jobs, having the time in UTC may add additional confusion. An Azure WebApp is no exception to UTC as a standard, however, this can be changed.

As I am in 'New Zealand', I will be setting my WebApp (which is hosted in Australia East) to NZ time from UTC.

I will be using a Windows-based App Service, for this article.

## Find the Timezone

The Azure App Service uses the same naming standard as Windows.

1. To find the correct name, run the following PowerShell snippet on a Windows PC:

       Get-ChildItem -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones' | Select-Object PSChildName

![](/uploads/windowsterminal_timezone.png)

This will list all the compatible Timezone names, because I am in New Zealand, I now know that: 'New Zealand Standard Time' is the correct syntax. 

For your reference, I have exported the list of compatible timezones into a CSV file below:
* [Export of Timezones](https://luke.geek.nz/uploads/files/Timezones.csv "Export of Timezones"){:target="_blank"}

## Set the Timezone

Making a change to the Application Settings, including setting the Timezone will restart the WebApp, so make sure this is scheduled at a time it is acceptable for an intermittent outage.

1. Log in to the [Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites "Azure Portal - App Services"){:target="_blank"}
2. Find your Azure WebApp and open it up
3. On the left-hand side Blade, underneath Settings, click on Configuration
4. Click on + New Application Setting
5. Type in the following Key/Value pair:
WEBSITE_TIME_ZONE | New Zealand Standard Time
6. Click Ok
7. Click Save to confirm and save the change.

![Azure WebApp - Timezone](/uploads/azurewebapp_appsettingstimezone.png "Azure WebApp - Timezone")

## Test the Timezone

1. Log in to the Azure Portal
2. Find your [Azure WebApp](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites "Azure Portal - App Services"){:target="_blank"} and open it up
3. On the left-hand side Blade, underneath Development Tools, click on Console
4. Type in:

* Time
* Date

Into the console to confirm that the Date and Time match your Timezone, the Azure WebApp logs etc will now be updated to use your timezone.

![Azure App Service - Console](/uploads/azurewebapp_console_date.png "Azure App Service - Console")