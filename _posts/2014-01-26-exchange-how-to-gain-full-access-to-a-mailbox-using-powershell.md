---
title: Using Powershell to gain full access to an Exchange mailbox
author: Luke 
categories:
  - Windows
  - PowerShell	
date: 2014-01-26 00:00:00 +1300
---

PowerShell command:

{% highlight PowerShell %}

Add-MailboxPermission “Mailbox Name” -User name -AccessRights FullAccess

{% endhighlight %}
