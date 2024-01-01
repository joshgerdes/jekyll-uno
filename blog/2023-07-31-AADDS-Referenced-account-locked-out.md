---
title: Entra ID Domain Services - Referenced account locked out
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: /images/posts/AADDS_ReferencedAccount.png
date: '2023-07-31 00:00:00 +1300'
slug: azure/AADDS-Referenced-account-locked-out
---

So you have just stood up [Entra ID Domain Services](https://learn.microsoft.com/azure/active-directory-domain-services/?WT.mc_id=AZ-MVP-5004796) _(formally - or still known as of July 2023 as: Active Directory Domain Services (AAD DS)_) and trying to login and join a computer to the AAD DS domain and you get the following error:

> The referenced account is currently locked out and may not be logged on to.

![The referenced account is currently locked out and may not be logged on to.](/images/posts/AADDS_ReferencedAccount.png)

This is commonly due to the following:

> Entra ID doesn't generate or store password hashes in the format that's required for NTLM or Kerberos authentication until you enable Azure AD DS for your tenant. For security reasons, Entra ID also doesn't store any password credentials in clear-text form. Therefore, Azure AD can't automatically generate these NTLM or Kerberos password hashes based on users' existing credentials.

Essentially this means, that the password hashes are not comaptible with Entra ID Domain Services, and the fix is to **reset the password of an Entra ID account** used to access Entra ID services, to allow Entra ID Domain Services, to hash and validate the Entra ID credentials. The reset only needs to happen, if the password for the accounts haven't been reset since Entra ID Domain Services has been deployed.

After resetting the password to my Entra ID account, and waiting an hour for replication I was successfully able to login and join a Windows Server to Entra ID Domain Services.

![Entra ID Domain Services - Join account](/images/posts/AADDS_JoinAccount.png)
