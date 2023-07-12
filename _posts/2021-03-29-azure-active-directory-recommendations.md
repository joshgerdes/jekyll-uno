---
date: 2021-03-29 00:00:00 +1300
title: Microsoft Entra ID Recommendations
author: Luke
categories:
- Azure
- M365
toc: false
permalink: /azure-active-directory-recommendations

header: 
  teaser: "images/Office-365-Banner2.png"
  classes: wide


---
Microsoft Entra ID is the foundation, which Microsoft 365 is built-on.

In the words of Microsoft:

> Microsoft Entra ID (Azure AD) is Microsoft’s cloud-based identity and access management service, which helps your employees sign in and access resources in:
>
> * External resources, such as Microsoft 365, the Azure portal, and thousands of other SaaS applications.
> * Internal resources, such as apps on your corporate network and intranet, along with any cloud apps developed by your own organization.

Microsoft Entra ID (AAD) is simply not set and forget, especially given the fact that AAD  services are constantly evolving in terms of features and improved security.

Below is a table of some Microsoft Entra ID and best practice recommendations.

Please keep in mind that like any recommendations, do not blindly follow them, make sure to determine the impact on your users on enabling some of this functionality, there may also be recommendations that you will not be able to apply, do to business constraints.

| Recommendation | Why Consider This | Probability | Impact | Effort |
| --- | --- | --- | --- | --- |
| Change break glass accounts passwords every 90 days | Emergency access accounts are highly privileged, and they are not assigned to specific individuals. Emergency access accounts are limited to emergency or "break glass"' scenarios where normal administrative accounts can't be used. We recommend that you maintain a goal of restricting emergency account use to only the times when it is absolutely necessary. | High | High | Low |
| Review possible stale Guest (B2B) accounts | Guest accounts do not exist by default and pose a potential data exposure vulnerability if left unused.  Guest accounts should only be used with a defined business need and closely monitored to ensure accounts are valid/legitimate. | High | Moderate | Low |
| Remove invited guests who have not accepted invite | Remove invited guests who have not accepted invite as it helps control the scope of identity and access management as it pertains to provisioning users in Azure AD.   In addition, removing stale invites and user from Azure AD is part of the recommended routine account maintenance. | High | Low | Low |
| Enable Windows Hello for Business PIN Reset Service | The Microsoft PIN reset services enables you to help users recover who have forgotten their PIN. Using Group Policy, Microsoft Intune or a compatible MDM, you can configure Windows 10 devices to securely use the Microsoft PIN reset service that enables users to reset their forgotten PIN through settings or above the lock screen without requiring re-enrollment. | Low to Moderate | Moderate | Low |
| Ensure security compliance notification mail is set | Managing security and compliance is a partnership. You are responsible for protecting your data, identities, and devices, while Microsoft vigorously protects Office 365 services. You can use Office 365 and Enterprise Mobility + Security (EMS) together to help you achieve the appropriate level of protection for your organization. | Low to Moderate | Moderate | Low |
| Add owner to legacy Service Principal | Legacy service principals without a defined owner create a challenge for management and accountability. | Low to Moderate | Moderate | Low |
| Add owner to application | Assigning an application owner provides an opportunity for delegation and establishes accountability for management of the resource. | Low to Moderate | Moderate | Low |
| Add owner to cloud-only groups | Assigning a group owner provides an opportunity for delegation and establishes accountability for management of the resource. | Low to Moderate | Moderate | Low |
| Require that users can create security groups is set to no | The creation and management of security groups should be restricted to administrators only to limit proliferation of this security principal.  The default setting is to prevent users from creating security groups in the Azure portal and it is recommended to maintain this configuration unless required by a defined business need. | Low to Moderate | Moderate | Low |
| Delete empty cloud-only groups | Cloud-only groups that contain no members and are not associated with Azure applications should be deleted as they serve no purpose. | Low to Moderate | Low | Low |
| Review Dynamic Groups with membershipRuleProcessingState not turned on | Sometimes you may want to stop the processing of a dynamic group, like when you’re importing a large number of new users or reorganizing your group architecture. To do that, use the MembershipRuleProcessingState parameter to switch processing on and off. | Low to Moderate | Low | Low |
| Review and consider federating all domains | When a domain is federated with Azure AD, several properties are set on the domain in Azure. One important one is IssuerUri. This property is a URI that is used by Azure AD to identify the domain that the token is associated with. | Low to Moderate | Low | Low |
| Review applications with credentials about to expire or are expired | Applications with expired credentials will prevent its use and should be updated before expiration to avoid an outage. If the application's service principal already has newer credentials remove the no longer valid credentials. | Moderate | High | Low |
| Review applications granted with risky OAUTH2 permissions | Depending on the scope of permissions, it can pose a risk to the confidentiality, integrity, or availability of the organization's data.  Periodic review of application permission grants can help identity over-privileged applications and establish access controls that align with the principle of least privilege. | Moderate | High | Low |
| Configure user passwords to never expire | Requesting users to regularly change passwords will lead to weak password practices like patterns or sequential words and numbers. | Moderate | Moderate | Low |
| Review Service Principals using password based credentials | Protect and manage your confidential app credentials for web apps, web APIs and daemon apps. Use certificate credentials, not password credentials (client secrets). | Moderate | Moderate | Low |
| Review Azure AD Guest (B2B) accounts | Guest accounts do not exist by default and pose a potential data exposure vulnerability if left unused.  Guest accounts should only be used with a defined business need and closely monitored to ensure accounts are valid/legitimate. | Moderate | Moderate | Low |
| Review applications consented by admins | Review applications granted consent by admins to ensure this global configuration is desired, which results in authorization for applications to data for all users in the Azure AD tenant. | Moderate | Moderate | Low |
| Review applications consented by one user | Review applications granted consent by a single users to ensure the configuration is desired, which results in authorization for applications to data for individual users as compared to admin consent which is global for the tenant. | Moderate | Moderate | Low |
| Review domain password policies that do not match defaults. | Only passwords for user accounts that are not synchronized through directory synchronization can be configured for password policies.  By default users do not have a password policy defined. | Moderate | Moderate | Low |
| Specify the usage location property for users | Some Microsoft services aren't available in all locations because of local laws and regulations. Before you can assign a license to a user, you must specify the Usage location property for the user. | Moderate | Moderate | Low |
| Require that users can consent to apps accessing company data on their behalf is set to no | Allowing users to provide consent for third-party applications risks exfiltration of personally identifiable information (PII) such as email and phone number, as it's associated with the user's profile. | High | High | Moderate |
| Review group license errors | These errors should be resolved and all users should be assigned expected licenses, for avoiding any loss of productivity. | High | Moderate | Moderate |
| Remove email / mailbox from directory role admins | To help separate internet risks (phishing attacks, unintentional web browsing) from administrative privileges, create dedicated accounts for each user with administrative privileges with no mail enabled to make sure they do not inadvertently open emails or run programs associated with their admin accounts. | Moderate | High | Moderate |
| Remove Skype address from directory role admins | To help separate internet risks (phishing attacks, unintentional web browsing) from administrative privileges, create dedicated accounts for each user with administrative privileges with no Skype Enabled to make sure they do not inadvertently open emails or run programs associated with their admin accounts. | Moderate | High | Moderate |
| Develop plan to migrate or remove legacy Service Principals | ServicePrincipals with ServicePrincipalType of legacy are not associated with an application and should be migrated to an application to improve manageability. | Moderate | Moderate | Moderate |
| Federated domains in Azure AD must have SupportsMFA enabled if ADFS MFA is used | When the configured conditional access policy requires multi-factor authentication, Azure AD defaults to using Azure MFA. If you use the federation service for MFA, you can configure Azure AD to redirect to the federation service when MFA is needed by setting -SupportsMFA to $true in PowerShell. This setting works for federated authentication services that support the MFA challenge request issued by Azure AD | Moderate | Moderate | Moderate |
| Verify all root level domains | Every new Azure AD tenant comes with an initial domain name, domainname.onmicrosoft.com. You can't change or delete the initial domain name, but you can add your organization's names to the list. Adding custom domain names helps you to create user names that are familiar to your users | Moderate | Moderate | Moderate |
| Review user objects no longer syncing with on-premises | Users present in Windows Server AD and no longer syncing to Azure AD impacts users ability to use services provided by Azure AD (Password reset, access to O365 services and cloud based apps etc.) and it also poses administrative challenge in managing the account. | Moderate | Moderate | Moderate |
