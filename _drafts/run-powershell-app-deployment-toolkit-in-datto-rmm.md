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

![](/uploads/powershell_app_deploymenttoolkit.png)

Unfortunately, due to some technical limitations, you can't run the PowerShell App Deployment Toolkit, directly from the Datto RMM package store.

I was able to get to run by using the following command script: