---
title: Using exchange to automatically accept meeting requests
permalink: /win/using-exchange-automatically-accept-meeting-requests/
categories:
  - Windows
---
Having multiple mailboxes and calendars can be hard to manage &#8211; especially when meeting requests don&#8217;t automatically accept themselves.

Using a quick powershell cmdlet from the Exchange Management Shell you can quickly set a calender to AutoAccept meeting requests

Set-MailboxCalendarSettings "mailbox name" -AutomateProcessing AutoAccept

Note: Remember to run the Management Shell as Administrator.
