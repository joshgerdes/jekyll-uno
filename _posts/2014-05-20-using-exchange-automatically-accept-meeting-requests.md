---
id: 3323
title: Using exchange to automatically accept meeting requests
date: 2014-05-20T10:51:00+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3323
permalink: /win/using-exchange-automatically-accept-meeting-requests/
dsq_thread_id:
  - "5186188858"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
mfn-post-love:
  - "0"
post_views_count:
  - "13"
categories:
  - Windows
---
Having multiple mailboxes and calendars can be hard to manage &#8211; especially when meeting requests don&#8217;t automatically accept themselves.

Using a quick powershell cmdlet from the Exchange Management Shell you can quickly set a calender to AutoAccept meeting requests

`Set-MailboxCalendarSettings "mailbox name" -AutomateProcessing AutoAccept```

Note: Remember to run the Management Shell as Administrator.