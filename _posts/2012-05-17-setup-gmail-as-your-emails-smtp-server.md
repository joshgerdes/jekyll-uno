---
id: 1317
title: Setup Gmail as your emails SMTP Server
date: 2012-05-17T10:07:59+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1317
permalink: /misc/setup-gmail-as-your-emails-smtp-server/
dsq_thread_id:
  - "4999304767"
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "16"
categories:
  - Misc
  - Windows
---
Having problems sending mail when using a different internet connection then the email address you have? Perhaps you are running on a T-Stick or Vodem and not able to send mail, some ISPs offer this service for an additional charge _(Telstra do for about $5.00 a month)_one of the ways you can get around this is by using Gmail as an SMTP server.

&nbsp;

First things first, you need a Gmail account so click on “<a title="Gmail" href="https://mail.google.com" target="_blank">here</a>” to go to the Gmail webpage and create an account (Remember to jot down your Username & Password.

  1. Once your Gmail account is setup you will be greeted to the Inbox page on the right hand side you will see small little gear which you need to click then select Settings.
  2. This will open up Gmails setting page, click on [Forwarding and POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop) and click Enable Pop for mail that arrives from now on. Click Save Changes
  3. Now open up your mail client, assuming you are using Outlook Express click Tools
  4. Click Accounts
  5. Click the mail tab and select your email account and choose Properties.
  6. Change the Reply to address to your email provider (non gmail) email address.
  7. Click on the servers tab, keep the incoming mail settings the same, but change the Outgoing mail server to:  smtp.gmail.com (use authentication and SSL)
  8. Click Use Authentication and select Use the follow Username & Password
  9. Type in your Gmail Username (including full email address, <example@gmail.com>) and your password.
 10. Click Ok
 11. Click Advanced
 12. In the Outgoing mail field click on use SSL and make sure the port is: 465
 13. Click Apply
 14. Now you can send emails on any service providers network!