---
title: An error occurred while using SSL configuration for socket address Error
permalink: /win/sslsocket/
tags:
  - Windows
---
&#8220;An error occurred while using SSL configuration for socket address %2. The error status code is contained within the returned data.&#8221;

This error occurs when the SSL certificates that allow you to access secure content, such as Emails & Internet Banking becomes damaged or corrupted. Follow the instructions below to fix.

  1. Click Start click All Programs, click Accessories
  2. **Right**&#8211;**click** **Command** **Prompt** & click **Run** **as** **Administrator**  then click Continue.
  3. Type **_netsh http show sslcert_**,  press Enter to view the installed certificates.
  4. Type **_netsh http delete sslcert_**, press Enter to delete the incorrectly installed certificate.
  5. Type **_netsh http add sslcert_**, press Enter to re-install the certificate.
