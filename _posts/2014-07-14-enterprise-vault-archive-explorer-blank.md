---
title: Enterprise Vault Archive Explorer Blank
categories:
  - Windows
date: 2014-07-14 00:00:00 +1300
---
Note: This needs to be done from the Enterprise Vault archiving server.

  1. Stop the EnterpriseVaultIndexingService <em style="font-family: sans-serif;font-size: medium">(this will stop the other services as well)</em>
  2. Kill the IndexBroker.exe process running on the server if running.
  3. Start EnterpriseVaultIndexingService
  4. Run an elevated command prompt and type: IISRESET /RESTART and press Ok
