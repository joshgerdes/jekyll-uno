---
date: 2021-07-03 00:00:00 +1200
title: Create Custom Roles for Microsoft Azure
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Microsoft Azure uses Role's to define who can access what - Role-Based Access Control (_RBAC)_.

You may be familiar with some of the more common ones such as:

* Owner
* Contributor
* Reader

Behind the scenes, each role is a separate grouping of permissions that determine what level of permissions someone or something has in Azure, these permissions are usually in the form of:

* Read
* Write
* Delete
* Action

Each role can be assigned to a specific Resource, Subscription, Management Group or Resource Group, through what is called an 'Assignment' _(you are assigning a role if you give someone Contributor rights to a Resource Group for example)_.

These permissions can be manipulated and custom roles created.