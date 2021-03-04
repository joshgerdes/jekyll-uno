---
title: Windows 7 – Authentication prompt for cached credentials in a domain environment
permalink: /win/windows-7-authentication-prompt-for-cached-credentials-in-a-domain-environment/
categories:
  - Windows
---
  1. In order to fix this – you need to close all Internet Explorer windows.
  2. Open Credential Manager (start type in: Credential Manager)
  3. Under Windows Credentials – select & remove all associated Username & Passwords
  4. Once removed log the user out and get the user to login again.
  5. They should now be able to access the Intranet & Internet.

<em style="font-family: sans-serif; font-size: medium;">Note: I have come across this when the users – password has reached expiry so when attempting to login again the user is usually asked to reset his or her password.</em>
  
<em style="font-family: sans-serif; font-size: medium;">Note: Also make sure the proxy details in Internet Explorer are set correctly for your environment.</em>
  
<em style="font-family: sans-serif; font-size: medium;">Note: Also – Windows 8 compatible.</em>
