---
date: 2021-07-05 00:00:00 +1200
title: Add a shortcut to the Azure Virtual Desktop Web Client to the Microsoft 365 waffle
author: Luke
categories:
- Azure
toc: false
header:
  teaser: "/uploads/m365_pin.png"

---
If you are like me, you use the application launchers in the Microsoft 365 waffle daily, if not hourly! Then having it as a single pane of glass to access all your applications is a no-brainer!

That includes access to the Azure Virtual Desktop Web client! In addition, Microsoft has given us the ability to add Custom App Launchers for applications that are accessible to a URL to the Launchers in the waffle!

> Create custom tiles that will appear in the All apps section of the Office 365 app launcher for all of your users. Users can pin the custom tiles directly to their app launcher for quick access.

You can add much more than the Azure Virtual Desktop web client to help improve your user's experience, but this quick guide will focus on adding the Azure Virtual Desktop Web Client.

![M365 Waffle](/uploads/m365_waffle_default.png "M365 Waffle")

1. Open the [**Microsoft 365 Admin Panel**](https://admin.microsoft.com/#/homepage "M365 Admin"){:target="_blank"}
2. Expand **Settings**
3. Click on **Org Settings**
4. Select **Organisation Profile**
5. Click on **Custom app launcher tiles**

![M365 - Organisation Profile](/uploads/m365_customapplaunchertitle.png "M365 - Organisation Profile")

 1. Click **+ Add a custom title.**
 2. Please type in the name of your Desktop; in my example, it is **Contoso Desktop.**
 3. For the **URL** of the website, type in: [**https://rdweb.wvd.microsoft.com/arm/webclient/index.html**](https://rdweb.wvd.microsoft.com/arm/webclient/index.html "https://rdweb.wvd.microsoft.com/arm/webclient/index.html"){:target="_blank"}
 4. Type in a **URL** of the **icon** you want the App Launcher to have _(Make sure this is a location that you have access to and can manage (i.e. even sitting on your website or Azure Storage account as long as it's publically available))._
 5. **Add** a **description** _(such as Contoso Desktop, used for Line of Business Applications)_
 6. ![M365 - Custom App Launcher](/uploads/m365_customapplaunchertitle1.png "M365 - Custom App Launcher")
 7. Click **Save**
 8. ![M365 - Custom App Launcher](/uploads/m365_contosoapp.png "M365 - Custom App Launcher")
 9. Log out of your Admin account and **log** into an **account** with an Exchange license attached to it. It may take some time for the Custom App Launcher to display.
10. Once the **Custom App Launcher** has displayed, your users can **pin** it to the **launcher,** so it is always right on top.
11. **Click** on your Azure Virtual Desktop **launcher,** and you should be **redirected** to the Azure Virtual Desktop **Web client**!
12. ![M365 Waffle - App Launcher](/uploads/m365_pin.png "M365 Waffle - App Launcher")

Just some notes on additional testing:

* I attempted copying the Azure Virtual Desktop RDP file (C:\\Users\\%UserAccount%\\AppData\\Local\\rdclientwpf) to my website to access directly however received an error, even opening up the RDP file directly failed, to test the Remote Desktop client.
* I had some success opening that RDP up with the Remote Desktop application directly using 'Open With' C:\\Users\\%UserAccount%\\AppData\\Local\\Apps\\Remote Desktop\\msrdcw.exe, instead of the default Remote Desktop Connection client locally.
* This will add it for all M365 users, if you want to restrict it to Users/Groups, I would look at testing and creating an App Registration.

At this stage, having a launcher to the Web Client is the best bet vs a shortcut directly to the RDP file as you don't have to worry about users having the Remote Desktop agent installed when working remotely.