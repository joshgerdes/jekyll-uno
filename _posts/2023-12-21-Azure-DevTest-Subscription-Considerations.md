---
title: Azure Dev/Test Subscription considerations
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlobHeading_Azure-DevTest-Considerations.gif
date: 2023-12-21 00:00:00 +1300
---

When looking at your Dev/Test workloads in Azure, you may be considering the [Azure Plan for Dev/Test Enterprise](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0148p?WT.mc_id=AZ-MVP-5004796) subscription type, avaliable on both the [Microsoft Customer Agreement (MCA)](https://learn.microsoft.com/azure/cost-management-billing/understand/mca-overview?WT.mc_id=AZ-MVP-5004796) and [Enterprise Agreement (EA)](https://www.microsoft.com/en-us/licensing/licensing-programs/enterprise?WT.mc_id=AZ-MVP-5004796) billing account types.

## Overview

So lets look at what this actually entails...

> You get **Azure Plan for DevTest** when you sign the **Microsoft Customer Agreement**. The **Enterprise DevTest** offer is available only to **Enterprise Agreement** customers, but they are *essentially* the **same plan**. The SKU value for Enterprise Dev/Test is: [ms-azr-0148p](https://azure.microsoft.com/en-in/pricing/offers/ms-azr-0148p?WT.mc_id=AZ-MVP-5004796) and Azure Plan for Dev/Test Enterprise is: [ms-azr-0148g](https://azure.microsoft.com/pricing/offers/ms-azr-0148g?WT.mc_id=AZ-MVP-5004796), but as usual **make sure you clarify and confirm with your direct Microsoft licensing/customer success manager, as these could change**.

There are a few gotchas, to using the Dev/Test Enterprise Azure Plan that you need to be aware of, but before we go into that - lets take a look at some of the benefits:

Run your development and testing workloads on Azure by using the Azure Plan for DevTest, which includes:

* Access to exclusive DevTest images in the gallery, including Windows 8.1 and Windows 10/11 images.
* Lower DevTest rates running Windows on Azure Virtual Machines, Azure App Service, Azure Cloud Services, Azure HDInsight, Azure Logic Apps, and Azure SQL Database.
* Centralized management via the Azure portal.
* The ability to create multiple subscriptions, making the plan ideal for development teams.

When looking at the DevTest plan, this particular one, will catch your eye:

> **Lower DevTest rates** running Windows on Azure Virtual Machines, Azure App Service, Azure Cloud Services, Azure HDInsight, Azure Logic Apps, and Azure SQL Database. Save even more with reservations.

What this means, is that items like Azure Virtual Machines running Windows as an example, you won't be charged the OS *(Operating System)* license costs, so essentially the same cost as if you were running a Linux workload, the same for the SQL services, although this is a small number of resources *(in comparison to the entire set of services offered by Microsoft Azure)*, this covers standard services, that over time can make a huge difference to the cost of running these services.

> Provision fast, lean, and highly secure dev/test workloads on Azure—and realize substantial cost savings compared to your production workloads. Your dev/test discounted rates continue as long as you maintain your Visual Studio subscription.

It is worth noting, that although the intended readers of this, are those with MCA or Enterprise Agreements with Microsoft, for those Visual Studio subscribers, you can go down the Dev/Test subscription route with [PayAsYouGo/DevTest](https://azure.microsoft.com/en-gb/pricing/offers/ms-azr-0023p/?WT.mc_id=AZ-MVP-5004796) with a credit card as well, keep in mind the considerations below.

I believe CSP (Cloud Solution Provider), doesn't currently have a DevTest offer, but you could potentially fall back to the Pay As You Go route.

## Considerations

Now that we know some of the benefits of the DevTest plans, there are a few things to keep in mind, that I have found a few people either didn't know *(and these subscriptions were deployed like candy at halloween across organisations)*, or were confused about, so lets cover it here.

![VisualStudio Subscription Types](/images/posts/BlobHeading_Azure-DevTest-Considerations.gif)

I want it to be perfectly clear, if you met the criteria to use the DevTest subscriptions - you should! But you might find you will end up with a mix of Pay As You Go and DevTest subscriptions, depending on your requirements *(and thats ok!)*.

> Remember: The Dev/Test plan is exclusively intended for your development and testing your applications.

The considerations that you need to consider, when selecting a Dev/Test subscription type over a Pay As You Go is as follows:

* The Dev/Test Azure Plan doesn't contain a financially backed service-level agreement *(SLA)*. The only exceptions are Azure DevOps, Azure Monitor and Visual Studio App Center. When you consider the entire purpose of this subscription, is to give you the ability to trial and test services - and NOT run production workloads or services, this makes sense.
* Only active Visual Studio subscribers with standard subscriptions can use the Azure resources running within an Enterprise Dev/Test subscription (yes, thats right everyone who has access to modify/create/delete resources needs to be a Visual Studio subscriber). This is the one that usually catches people out, although there are no technical guardrails, preventing the subscription use by un-licensed users, doesn't mean that you are complying with the license agreement. Althgough, its worth pointing out, end users can also access the applications you build on top of the platform, to provide feedback or perform acceptance tests without requiring a license.

Those are the 2 main considerations, that you need to consider when deciding on what subscription type to use, you will find for some teams that have relevant Visual studio subscriptions, DevTest will work fine, but for others Pay As You Go will be the right choice - your environment, may end up with a mix of both subscription types - just make sure its clear what subscription license type it is, an example is I usually encourage subscriptions to be standing by pre-created ready to go, and named something like 'PLACEHOLDER-PAYASYOUGO' or 'PLACEHOLDER-DEVTEST', although you can use Tags for this as well - the Overview pane of the Subscription resource also indicates the Subscription type.

The last thing, I will cover - is what does *Visual Studio subscribers* actually mean. To do that, we will take a look at the [Visual Studio subscriptions](https://visualstudio.microsoft.com/subscriptions?WT.mc_id=AZ-MVP-5004796).

If you navigate down the page, you will see a dropdown list with all the Visual Studio subscription types.

![VisualStudio Subscription Types](/images/posts/VisualStudio_Subscription-Types.png)

If you click on the Azure tab, you will see the Azure credit *(for their own isolated subscription)*, and whether they are eligable as a valid Azure Dev/Test subscription user. To make it easier, here is a current table:

| **Visual Studio Subscription Type**                             | **Azure Personal Credit** | **Valid Azure Dev/Test user** |
|-----------------------------------------------------------------|---------------------------|-------------------------------|
| Visual Studio Enterprise monthly subscriptions                  | $0                        | No                            |
| Visual Studio Enterprise subscription                           | $150                      | Yes                           |
| Visual Studio subscriptions with GitHub Enterprise              | $150                      | Yes                           |
| Visual Studio Professional monthly subscriptions                | $0                        | No                            |
|  Visual Studio Professional                                     | $50                       | Yes                           |
| Visual Studio Professional subscriptions with GitHub Enterprise | $50                       | Yes                           |
| Visual Studio Test Professional subscription                    | $50                       | Yes                           |
| MSDN Platforms                                                  | $100                      | Yes                           |

*Azure personal credit is in USD.*

## Reference

The links below, are relevative reference material for further reading.

* [Enterprise Dev/Test](https://azure.microsoft.com/en-us/pricing/offers/ms-azr-0148p?WT.mc_id=AZ-MVP-5004796)
* [Azure Plan for DevTest](https://azure.microsoft.com/pricing/offers/ms-azr-0148g?WT.mc_id=AZ-MVP-5004796)
* [Create an Enterprise Agreement subscription](https://learn.microsoft.com/azure/cost-management-billing/manage/create-enterprise-subscription?WT.mc_id=AZ-MVP-5004796)
* [Create a Microsoft Customer Agreement subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription?WT.mc_id=AZ-MVP-5004796)
* [Visual Studio subscriptions](https://visualstudio.microsoft.com/subscriptions?WT.mc_id=AZ-MVP-5004796)
