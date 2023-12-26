---
title: How to get the Lync client to redownload the address book
categories:
  - Windows
date: 2014-07-08 00:00:00 +1300 
---

**Lync 2010**

Log off of the Lync client and delete the profile from:

**%userprofile%/AppData/Local/Microsoft/Communicator**

Then run the following command into an elevated command prompt to add the registry that forces the Lync client to immediately download the address book:

**reg add HKLM/Software/Policies/MicrosoftCommunicator /v GalDownloadInitialDelay /t REG_DWORD /d 0 /f**

**Lync 2013**

Log off of the Lync client and delete the profile from:

**%userprofile%/appdata/Local/Microsoft/Office/15.0/Lync**

Then run the following command into an elevated command prompt to add the registry that forces the Lync client to immediately download the address book:

**reg add HKLMSoftwarePoliciesMicrosoftOffice15.0Lync /v GalDownloadInitialDelay /t REG_DWORD /d 0 /f**

Note: The Lync address book is saved in the following files on the local workstations:  GalContacts.db & GalContacts.db.idx.
