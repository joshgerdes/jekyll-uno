---
date: 2021-07-04T00:00:00.000+12:00
title: Add shortcut to Azure Virtual Desktop in the Microsoft 365 waffle
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/avddesktopfull.png"

---
If you are like me, use the application launchers in the Microsoft 365 waffle daily, if not hourly! Then having it as a place to access all your applications is a no-brainer!

That includes access to the HTML Azure Virtual Desktop client! Microsoft has given us the ability to add Custom App Launchers to the Application Launchers in the waffle!

> Create custom tiles that will appear in the All apps section of the ‎Office 365‎ app launcher for all of your users. Users can pin the custom tiles directly to their app launcher for quick access.

![](/uploads/m365_waffle_default.png)

1. Open the [**Microsoft 365 Admin Panel**](https://admin.microsoft.com/#/homepage "M365 Admin")
2. Expand **Settings**
3. Click on **Org Settings**
4. Select **Organisation Profile**
5. Click on **Custom app launcher tiles**

![](/uploads/m365_customapplaunchertitle.png)

1. Click **+ Add a custom title**
2. Type in the name of your Desktop, in my example it is: **Contoso Desktop**
3. For the **URL** of the website type in: [**https://aka.ms/wvdarmweb**](https://aka.ms/wvdarmweb "https://aka.ms/wvdarmweb") _(this is the shortened URL for the Azure Virtual Desktop HTML client)_
4. Type in a **URL** of the **icon** you want the App Launcher to have _(I am using the Azure Virtual Desktop -_ [_https://azure.microsoft.com/svghandler/virtual-desktop/?width=600&height=315_](https://azure.microsoft.com/svghandler/virtual-desktop/?width=600&height=315 "https://azure.microsoft.com/svghandler/virtual-desktop/?width=600&height=315") _PNG as an example, however, make sure this is a location that you have access to and can manage (ie even sitting on your website or Azure Storage account as long as its publically available))._
5. **Add** a **description**
6. ![](/uploads/m365_customapplaunchertitle1.png)
7. Click **Save**
8. Log out of your Admin account and into an account that has an Exchange license, attached to it. It may take some time for the Custom App Launcher to display.
9. 