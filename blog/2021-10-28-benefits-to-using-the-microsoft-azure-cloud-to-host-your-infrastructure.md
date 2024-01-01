---
date: 2021-10-28T00:00:00.000+13:00
title: Benefits to using the Microsoft Azure Cloud to host your Infrastructure
authors: [Luke]
tags:
  - Azure
toc: true
header:
  teaser: images/iazure-marketplace-banner.png

---
Cloud computing offers many benefits, from your traditional on-premises infrastructure, ecosystems such as Microsoft Azure, have an underlying fabric built for today's 'software as a service' or 'software defined' world.

The shift of technologies from managing on-premises Exchange environments for mail to consuming Microsoft 365 services has allowed more time for the IT and businesses to adopt, consume and improve their technology and continuously improve - to get the most use of it and remain competitive in this challenging world.

Below is a high-level list of what I consider some of the benefits of using the Microsoft Azure ecosystem:

* Each Azure datacentre 'region' has 3 Availability Zones, each zone acts as a separate datacentre, giving redundant power and networking services, quickly allowing you to separate your services across different fault domains and zones, providing better resiliency, while also giving you the ability to keep them logically and physically close together.
* Geo-redundant replication of backups for Virtual Machines, PaaS/File Shares, and ability to do cross-region restore functionality (i.e., Australia/Australia East).
* A multitude of hosts (supporting both AMD and Intel workloads), which are continually patched and maintained, and tuned for virtualisation performance, stability and security, no longer do we need to spend hours patching, maintaining, licensing on-premises hypervisors, ever so increasing as these systems get targeted for vulnerabilities and architecting how many physical hosts, we may need to support a system.
* Consistent, up-to-date hardware, no need to worry about lead times for new hardware, purchasing new hardware every three years and procurement and implementation costs of hardware, allowing you to spend the time improving on the business and tuning your services _(scaling up and down, trying new technologies, turning off devices etc.)_
* For those that like to hoard every file that ever existed, the Azure platform allows scale _(in and out to suit your file sizes)_ along with cost-saving opportunities and tweaks with Automation and migrating files between cool/hot tiers.
* No need to pay datacentre hosting costs
* No need to worry about redundant switching
* With multiple hosts, there is no risk around air conditioning leaks, hardware failure; you don't need to worry about some of these unfortunate events occurring.
* No need to pay electricity costs to host your workloads.
* Reduced IT labour costs and time to implement and maintain systems
* OnDemand resources available can stand up separate networks unattached to your production network for testing or other devices easily without working out through VLANs or complex switching and firewalls.
* Azure Network have standard DDOS protection enabled by default
* Backups are secure by default; they are offline and managed by Microsoft, so if a ransomware attack occurs, won't be able to touch your backups.
* Constant Security recommendations, improvements built into the platform.
* Azure Files is geo-redundant and across multiple storage arrays, encrypted at rest.
* Windows/SQL licensing is all covered as part of the costings, so need to worry about not adhering to MS licensing, Azure helps simplify what can sometimes be confusing and complex licensing.
* Extended security updates for out-of-date Server OS such as Windows Server 2008 R2, Windows Server 2021 R2 without having to pay for extended update support.
* Ability to leverage modern and remote desktop and application technologies such as Windows 365 and Azure Virtual Desktop, by accessing services hosted in Azure.
* Having your workloads in Azure gives you a step towards, removing the need for traditional domain controllers and migrating to Microsoft Entra ID joined devices.
* Azure AutoManage functionality is built in to automatically patch Linux (and Windows of course!), without having to manage separate patching technologies for cross-platform infrastructure.
* Azure has huge support for Automation, via PowerShell, CLI and API, allowing you to standardize, maintain, tear down and create infrastructure and services, monitoring, self-users on an as needed basis.
* Azure datacentres are sustainable and run off renewable energy where they can, Microsoft has commitments to be fully renewable.
* No need for NAS or Local Backups, the backups are all built into Azure.
* Compliant datacentre across various global security standards - [https://learn.microsoft.com/en-us/compliance/assurance/assurance-datacenter-security](https://learn.microsoft.com/en-us/compliance/assurance/assurance-datacenter-security?WT.mc_id=AZ-MVP-5004796 "https://learn.microsoft.com/en-us/compliance/assurance/assurance-datacenter-security?WT.mc_id=AZ-MVP-5004796")
* Ability to migrate or expand your resources from Australia to ‘NZ North’ or other new or existing data centres! Azure is global and gives you the ability to scale your infrastructure to a global market easily or bring your resources closer to home if a data centre becomes available.
* We all know that despite the best of intentions, we rarely ever test, develop, and improve disaster recovery scenarios, sometimes this is because of the complexity of the applications and backup infrastructure. Azure Site Recovery, Geo-Redundant backup, Load Balancers and automation helps make this a lot easier.
* Ability to better utilise Cloud security tools _(ie such as the Azure Security Center)_, across Cloud and on-premises workloads consistently using Azure Arc and Azure policies.
* And finally - more visibility into the true cost and value of your IT infrastructure, the total cost of your IT Infrastructure is hidden behind electricity costs, outages and incidents that would not have impacted cloud resources, slow time to deployment or market, outdated and insecure technologies and most likely services you are running which you don't need to run!

\#ProTip - Resources such as the [Azure Total Cost of Ownership (TCO)](https://azure.microsoft.com/en-us/pricing/tco/calculator/?WT.mc_id=AZ-MVP-5004796 "Total Cost of Ownership (TCO) Calculator") can help you calculate the true cost of your workloads.
