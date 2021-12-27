---
date: 2021-12-27 00:00:00 +1300
title: Azure Storage Account SFTP errors
author: Luke
categories: []
toc: true
header:
  teaser: ''

---
As part of standing up and using an Azure Storage account as an SFTP server, I ran into a few issues. This blog post is merely intended to show my findings in case others run into similar issues.

#### PTY allocation request failed on channel 0

Even though you appear to have connected successfully, you may see the following errors:

* PTY allocation request failed on channel 0
* shell request failed on channel 0

The solution for this was simple, switch from SSH to **SFTP**

If you were like me, I just flicked to SSH as a habit.

#### Home Directory is not accessible.

Make sure that the Home directory _(Folder)_ is created in your container.

Also make sure that the Home directory for the user, references Container/Folder, like the below:

![](/uploads/azureportal_sftplocalusercreate.png)