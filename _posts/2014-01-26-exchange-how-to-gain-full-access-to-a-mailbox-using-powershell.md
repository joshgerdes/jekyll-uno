---
title: Using Powershell to gain full access to an Exchange mailbox
date: 2014-01-26 00:00:00 +13:00
permalink: "/misc/exchange-how-to-gain-full-access-to-a-mailbox-using-powershell/"
categories:
- Windows
- PowerShell
author: Luke
---

PowerShell command:

{% highlight PowerShell %}

Add-MailboxPermission “Mailbox Name” -User name -AccessRights FullAccess

{% endhighlight %}
