---
date: 2022-08-18 00:00:00 +1200
title: Microsoft Azure - Cost Optimization Tasks
author: Luke
categories:
- Azure
toc: true
header:
  teaser: ''

---
Like doing service on your car, the Microsoft Azure platform is not a set-and-forget ecosystem!

Although Microsoft takes a lot of traditional infrastructure management and security concerns off your hand, you are still responsible for the spending and making sure the value of the technologies and services you consume, match your business goals and agility.

Today we are going to go back to basics and look at the Cost Optimization Pillar of the Microsoft Well-Architected Framework.

> “The cost optimization pillar provides principles for balancing business goals with budget justification to create a cost-effective workload while avoiding capital-intensive solutions. Cost optimization is about looking at ways to reduce unnecessary expenses and improve operational efficiencies.”
>
> “Use the pay-as-you-go strategy for your architecture, and invest in scaling out, rather than delivering a large investment-first version. Consider opportunity costs in your architecture and the balance between first-mover advantage versus fast follow.”

As mentioned earlier, the right governance and oversight can help prevent Cloud sprawl and wasted consumption costs.

To help get you started, I have put together a list of some optimization opportunities, that should be run regularly, items such as reviewing unassociated public IPs should be done Monthly _(along with Azure Advisor checks)_, and Azure Reservation reviews at least quarterly. 

This is not an exhaustive list, and the use of Azure Policy and [Azure Advisor](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview?WT.mc_id=AZ-MVP-5004796 "Introduction to Azure Advisor") help supplement these tasks.

MicrosoftGraph can also be used in conjunction with PowerShell to pull recommendations straight out of Advisor, which can then be fed into reports, and the use of community tools such as the [Azure Optimization Engine](https://luke.geek.nz/azure/azure-optimization-engine "Azure Optimization Engine ") cannot be undervalued.