---
title: Exchange – How to gain full access to a mailbox using PowerShell
permalink: /misc/exchange-how-to-gain-full-access-to-a-mailbox-using-powershell/

author: Luke 
categories:
  - Windows
  - PowerShell	
---

PowerShell command:

{% highlight PowerShell %}

Add-MailboxPermission “Mailbox Name” -User name -AccessRights FullAccess

{% endhighlight %}
