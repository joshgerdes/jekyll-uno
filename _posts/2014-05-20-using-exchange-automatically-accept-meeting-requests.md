---
title: Using exchange to automatically accept meeting requests
categories:
  - Windows
date: 2014-05-20 00:00:00 +1300
---

Having multiple mailboxes and calendars can be hard to manage &#8211; especially when meeting requests don&#8217;t automatically accept themselves.

Using a quick powershell cmdlet from the Exchange Management Shell you can quickly set a calender to AutoAccept meeting requests

    Set-MailboxCalendarSettings "mailbox name" -AutomateProcessing AutoAccept

Note: Remember to run the Management Shell as Administrator.
