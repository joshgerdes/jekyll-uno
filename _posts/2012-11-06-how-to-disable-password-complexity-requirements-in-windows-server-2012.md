---
title: How to disable password complexity requirements in Windows Server 2012
author: Luke
categories:
  - Windows
date: 2012-11-06 00:00:00 +1300
---

  1.  **Open** Server **Manager**
  2. Click **Tools** _(top right)_
  3. Click **Local Security Policy**
  4. **Navigate** to Account Policies/**Password** **Policy**
  5. Double click “**_Password must meet complexity requirements_**”
  6. Click **Disable**
  7. Click **Ok**

&nbsp;

Note: You can also Group Policy which includes Local security policies by pressing the Windows Key+R at the same type and typing: _gpedit.msc_ into the run dialog.
