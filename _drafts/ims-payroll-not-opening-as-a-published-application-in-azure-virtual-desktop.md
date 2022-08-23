---
date: 
title: IMS Payroll not opening as a published application in Azure Virtual Desktop
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/imspayroll_avdpublishedapp.png"

---
Azure Virtual Desktop allows you to access a full desktop or a published application, with shortcuts and an appearance like it was running locally; depending on the requirements, I prefer published applications where possible to keep the user experience on the desktop and keep the cost down.

One of the applications I published for a customer is [MYOB IMS Payroll](https://www.myob.com/nz/enterprise/ims-payroll " MYOB IMS Payroll "). IMS Payroll is used by small-medium businesses for their payroll.

This worked well as a published application for months until one day; it didn't seem to open for the user, whether as a published application or in the Full Desktop.

![](/uploads/imspayroll_avdpublishedapp.png)

One noticeable difference we found in our testing - was that it opened for us using our account.

After some digging, we discovered that the user had gone to another branch office site and used a different monitor setup and IMS Payroll was out of drawing range, usually windows would be able to snap this back into view however, after doing a comparison of the registry keys for our user vs the user who had the issue we discovered that IMS Payroll sets the location in the registry.