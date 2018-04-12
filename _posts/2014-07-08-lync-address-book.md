---
id: 3354
title: How to get the Lync client to redownload the address book
date: 2014-07-08T17:33:32+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3354
permalink: /win/lync-address-book/
mfn-post-love:
  - "0"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
dsq_thread_id:
  - "4983068201"
post_views_count:
  - "19"
categories:
  - Windows
---
**Lync 2010**

Log off of the Lync client and delete the profile from:

**%userprofile%AppDataLocalMicrosoftCommunicator**

Then run the following command into an elevated command prompt to add the registry that forces the Lync client to immediately download the address book:

**reg add HKLMSoftwarePoliciesMicrosoftCommunicator /v GalDownloadInitialDelay /t REG_DWORD /d 0 /f**

&nbsp;

**Lync 2013**

Log off of the Lync client and delete the profile from:

**%userprofile%appdataLocalMicrosoftOffice15.0Lync**

Then run the following command into an elevated command prompt to add the registry that forces the Lync client to immediately download the address book:

**reg add HKLMSoftwarePoliciesMicrosoftOffice15.0Lync /v GalDownloadInitialDelay /t REG_DWORD /d 0 /f**

&nbsp;

_Note: The Lync address book is saved in the following files on the local workstations:  GalContacts.db & GalContacts.db.idx._