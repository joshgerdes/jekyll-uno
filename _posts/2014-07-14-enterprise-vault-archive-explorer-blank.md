---
id: 3360
title: Enterprise Vault Archive Explorer Blank
date: 2014-07-14T17:57:35+00:00
author: Luke
layout: post
guid: http://techremedy.co.nz/?p=3360
permalink: /win/enterprise-vault-archive-explorer-blank/
mfn-post-love:
  - "0"
sidebar_value:
  - Default Sidebar
sidebar_position_value:
  - right
post_views_count:
  - "51"
dsq_thread_id:
  - "4841058045"
categories:
  - Windows
---
Note: This needs to be done from the Enterprise Vault archiving server.

&nbsp;

  1. Stop the EnterpriseVaultIndexingService <em style="font-family: sans-serif;font-size: medium">(this will stop the other services as well)</em>
  2. Kill the IndexBroker.exe process running on the server if running.
  3. Start EnterpriseVaultIndexingService
  4. Run an elevated command prompt and type: IISRESET /RESTART and press Ok