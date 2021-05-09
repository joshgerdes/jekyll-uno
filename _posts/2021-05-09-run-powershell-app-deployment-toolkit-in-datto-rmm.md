---
date: 2021-05-09 00:00:00 +1200
title: Run PowerShell App Deployment Toolkit in Datto RMM
author: Luke
categories:
- PowerShell
toc: false
header:
  teaser: "/uploads/powershell-blog-feature-banner.png"

---
The PowerShell App Deployment Toolkit provides a set of functions to perform common application deployment tasks and to interact with the user during deployment. It simplifies the complex scripting challenges of deploying applications in the enterprise, provides a consistent deployment experience and improves installation success rates.

![PowerShell App Deployment Toolkit](/uploads/powershell_app_deploymenttoolkit.png "PowerShell App Deployment Toolkit")

Although the PowerShell App Deployment Toolkit, makes application installation a lot more visible and gives your users more control over how and when the Application is installed,  due to some technical limitations, you can't run the PowerShell App Deployment Toolkit, directly from the Datto RMM package store. 

This is a brief blog article, intended to help other people who may be using the App Deployment Toolkit with Datto RMM.

{% gist 93ac9f29ddf7db2327e356480f1c7478 %}

Note: You may also need to navigate to: AppDeployToolkitConfig.xml, and change the: <Toolkit_RequireAdmin> attribute to False, to avoid issues with UAC (User Access Control).

I also ran my component as:

* Only Run when the user is logged in
* Only run if User has Administrator rights