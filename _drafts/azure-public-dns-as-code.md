---
date: 2022-01-07 00:00:00 +1300
title: Azure Public DNS as Code
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
The Microsoft Azure ecosystem offers a lot of capabilities that empower individuals and businesses, one of those capabilities that is often overlooked is [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) _(Domain Name System)_.

> _Azure DNS allows you to host your DNS domain in Azure, so you can manage your DNS records using the same credentials, billing, and support contract as your other Azure services. Zones can be either public or private, where Private DNS Zones (in Managed Preview) are only visible to VMs that are in your virtual network._
>
> _You can configure Azure DNS to resolve hostnames in your public domain. For example, if you purchased the contoso.xyz domain name from a domain name registrar, you can configure Azure DNS to host the contoso.xyz domain and resolve `www.contoso.xyz` to the IP address of your web server or web app._

In this article, we are going to focus on [Azure Public DNS](https://docs.microsoft.com/en-us/azure/dns/dns-overview).

A few years ago, I had my personal external DNS under source control using Terraform and the Cloudflare provider, I wanted to see if I use source control and continuous integration to do the same thing using Azure DNS and Azure Bicep.

My theory was I could make a change to a file and then commit it and have the Azure DNS records created or modified automatically, allowing changes to DNS to be gated, approved, scheduled and audited allowing changes and rollback a lot easier – without having to give people access to be able to create DNS records with no auditability, turns out you can!

Using an Azure DevOps pipeline and repository and Azure Bicep, we are going to deploy an Azure Public DNS zone to a resource group automatically on a successful commit, and any records.

![Azure Bicep - Pipeline High Level](/uploads/azurebicep_dns_hld.png "Azure Bicep - Pipeline High Level")

## Create Azure Public DNS as Code