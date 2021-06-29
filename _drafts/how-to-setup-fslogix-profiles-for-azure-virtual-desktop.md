---
date: 2021-06-29 00:00:00 +1200
title: How to setup FSLogix profiles for Azure Virtual Desktop
author: Luke
categories: []
toc: false
header:
  teaser: ''

---
If you have a few Azure Virtual Desktop machines, you need some way to keep user persistence's and application customisations, which would usually be stored in the user profile locally across multiple machines (or even the same machine if using Ephemeral OS), this is where FSLogix Profile Containers can assist.

We are going to implement FSLogix using an Azure File Share, to store the profiles.

I am going to assume you already have an Azure Virtual Desktop farm (and Azure ADDS), if not you can check out my guide here.

This article will be based on the Azure Virtual Desktop farm created in a previous article, however, you can just follow along and replace the Resource Names and Groups with your own.