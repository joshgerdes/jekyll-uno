---
title: Microsoft Copilot for Azure - Preview
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/BlobHeading_Microsft_Copilot_Azure_Preview.PNG
date: 2023-12-26 00:00:00 +1300
---

[Copilot for Azure](https://azure.microsoft.com/en-us/products/copilot?WT.mc_id=AZ-MVP-5004796) is an AI companion that simplifies how you design, operate, optimize, and troubleshoot apps and infrastructure from cloud to edge.

With Copilot, gain new insights, discover more benefits of the cloud, and orchestrate data across both the cloud and the edge. Copilot AI assistance **utilizes language models**, the **Azure control plane**, and **insights** about **your** **Azure** and **Arc–enabled** assets.

This is carried out within Azure's steadfast commitment to safeguarding your data security and privacy.

> This article contains my own personal thoughts and experiences; make sure you approach this capability with an open eye; my views may not necessarily be your own.

## Overview

Microsoft Copilot for Azure is designed to generate the best possible responses within the context it can access.

**However, like any AI system, Microsoft Copilot for Azure's responses will not always be perfect. All of Microsoft Copilot for Azure's responses should be carefully tested, reviewed, and vetted before making changes to your Azure environment.**

> Microsoft Copilot for Azure *(preview)* requires registration and is only available to approved enterprise customers and partners. Customers who wish to use Microsoft Copilot for Azure *(preview)* must submit a registration form.
> Access to Microsoft Copilot for Azure *(preview)* is subject to Microsoft's sole discretion based on eligibility criteria and a vetting process, and customers must acknowledge that they have read and understand the Azure terms of service for Microsoft Copilot for Azure *(preview)*.

![Microsoft Copilot for Azure - Mission Statement](/images/posts/MicrosoftCopilotForAzure_MissionStatement.PNG)

Copilot for Azure can be accessed directly in the Azure Portal.

![Microsoft Copilot for Azure](/images/posts/MicrosoftCopilotForAzure_PortalView.PNG)

### Limitations

> It is in preview! But there are some [limitations](https://learn.microsoft.com/azure/copilot/capabilities?WT.mc_id=AZ-MVP-5004796#current-limitations), to be aware of.

| **Limitation**                                                | **Notes**                                                                                                                                             |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10 questions per conversation (5 convos per day)              | Essentially, 10 prompts (and competitions) per memory-aware conversation and 5 conversations. Reducing potential hallucinations and API exhaustion. |
| Responses that use lists are limited to the top 5 | When requesting a list of resources, the completions will be restricted to 5. The token length for hundreds of resources can be very slow           |
| Some tasks won't accept Resource Names, Resource ID required | Resource ID of the resources may need to be specified when referencing a resource.                                                                           |
| Available in English only                                     | English only                                                                                                                                          |
| Cost management scope at Subscription (not Management Group)  | Able to reference Cost analysis against Subscription and Resource Groups but not across multiple subscriptions across Management Groups            |
| Limited number of skills                                      | Can only complete a certain amount of tasks; no doubt more will be added over time due to increasing capabilities and user feedback.                  |

### Copilot Stack

So, how does Microsoft Copilot for Azure work? Let us take a closer look:

![Microsoft Copilot for Azure](/images/posts/MicrosoftCopilotforAzure_CopilotStack.gif)

| **Step** | **Stack** | **Action** |
|---|---|---|
| 1 | Apps | User enters prompt in portal web interface |
| 2 | Apps | Microsoft Bot Framework takes the prompt and sends it to AI orchestration |
| 3 | AI orchestration | Does prompt filtering (i.e. Content Safety) |
| 4 | AI orchestration | Brings in context (i.e. Azure resource/blade that is opened) |
| 5 | AI orchestration | RAG (Retrieval Augmented generation), brings in Microsoft Learn documentation, Azure Resource Graph, Cost Management, Skills, Guardrials (i.e. Azure policy, RBAC (Role Based Access Control), Budgets |
| 6 | AI orchestration | Added additional context to Prompt (i.e. metapromot) and ground the data |
| 7 | Foundational Model | Metaprompt, supplied to foundational model. |
| 8 | Foundational Model | Competition prompt response from foundational model (based on Copilot system prompt and context) |
| 9 | Apps | Competition prompt, supplied to user |

## Functionality

Microsoft Copilot for Azure is designed to help with the following:

* Design
* Operate
* Optimize
* Troubleshoot

![Microsoft Copilot for Azure](/images/posts/MicrosoftCopilotforAzure_Circle.PNG)

So let us go through trialling this! All tests below will be done with an account with Owner permissions across Azure.

### Design

> **Design** - Configure and create the right services.

To test the design pillar of Microsoft Copilot for Azure, I will be using the following prompts to ease in and look at my design elements:

* I want to set up a new web application for Internet shopping; what infrastructure should I use?
* When setting up a new web service that allows people to purchase my products using Azure services, what infrastructure should I use?
* List all suggested Azure services for my internet shopping service and how they could connect together, including considerations.
* Create these services
* Are there any services I am missing? Also, list all the suggested services in a table, including a column on what each service could be used for when looking at my internet shopping application
* What are the recommended requirements that I need to gather to create my scalable and secure Internet shopping application? List requirements, as a list
* Give me examples of security requirement questions.

Although these prompts are very high-level and not as specific as they could be, I approached this as someone who was new to Azure design, with a specific outcome I wanted, with one prompt building on the next.

![Microsoft Copilot for Azure - Design](/images/posts/MicrosoftCopilotforAzure_PillarTest_Design.gif)

> Overall, Copilot for Azure responded to each prompt, and starting off with a generic prompt, I was able to use the completition prompts, supplied back to me. I did like how most prompts included links to additional Microsoft Learn documentation *(including Azure architecture centre references)* based on the subjects at the time. I did ask Microsoft Copilot for Azure to create a range of Cloud-native services, and it failed, so from my perspective, it is missing either additional error handling or the Skills/Tasks to complete the creation of these services *(which would have been my ideal state)*.

### Operate

> **Operate** - Answer questions, author complex commands, and manage resources.

To test the Operate pillar of Microsoft Copilot for Azure, I will be using the following prompts to ease in and look at the Operate elements:

* Take me to view all resources
* Change portal theme to light
* Change back
* Create a table of all resources and their region?
* Give me a list of the top resource types?
* List all virtual machines and their power state?
* Shutdown all virtual machines currently running
* Start all virtual machines currently stopped

![Microsoft Copilot for Azure - Operate](/images/posts/MicrosoftCopilotforAzure_PillarTest_Operate.gif)

> Copilot for Azure responded to each prompt; it did a great job of taking us to the resources within the Azure Portal when prompted *(i.e. take me to view all resources)*; it even successfully changed our portal theme and reverted the change. However, I ran into a bug when attempting to shut down and start running Virtual Machines, where the selection prompt wasn't fully loaded, and I had to reset the selection to get it to display. Multiple times, I ran into issues with Azure Resource Graph, not being fully capable of creating and running queries, such as listing all resources and their regions, which I know is accessible by a Resource Graph query. However, Copilot, for Microsoft Azure, was able to successfully stop and start my virtual machines in bulk, making it a lot easier to make adjustments at scale; overall, I believe there are some improvements needed in this area to make it more functional.

### Optimize

> **Optimize** - Improve costs, scalability, and reliability through recommendations for your environment.

To test the Optimize pillar of Microsoft Copilot for Azure, I will be using the following prompts to ease in and look at the Optimize elements:

* List all recommendations from Azure Advisor?
* Show me the highest resource costs for the past 12 months?
* How can I optimize my environment?
* Create a naming convention for SQL databases?
* How can I protect my storage accounts?

> Copilot for Azure responded to each prompt, and it was able to achieve and display the highest resource costs for the past 12 months; once my scope was set *(as per current limitations)*, it gave me recommendations on how I could generally optimize my environment, Copilot was also able to give recommendations on *(non-Azure)* SQL Database naming standards and implementations. Being able to review and recommend security recommendations is an enhanced Azure Copilot skill; so glad to know this worked and came back with valid recommendations for my test storage account; the automated implementation of security recommendations, however, isn't currently implemented.

![Microsoft Copilot for Azure - Optimize](/images/posts/MicrosoftCopilotforAzure_PillarTest_Optimize.gif)

### Troubleshoot

> **Troubleshoot** - Orchestrate across Azure services for insights to summarize issues, identify causes and suggest solutions.

In this section, one of my Virtual Machines *(VM-1)* is turned off, so I am unable to RDP to it; let us see if we can use Microsoft Copilot for Azure to troubleshoot this.

To test the Troubleshoot pillar of Microsoft Copilot for Azure, I will be using the following prompts to ease in and look at the Troubleshoot elements:

* How can I troubleshoot not being able to RDP to VM-1?
* Check if port 3390 is open on VM-1?
* What are the security implications of opening port 3389?
* Create a PowerShell script to test 3389 is opened on VM-1
* Adjust the script to use its public IP instead
* Take me to VM-1
* What is the Public IP of VM-1?
* What is this resource?
* What are the open alerts?

> Overall, using Microsoft Copilot for Azure, to Troubleshoot RDP to connectivity to 'VM-1' would have helped, though the scenario that Copilot had come back with was due to being unable to RDP due to a potential brute force attack, had I followed the recommendations, it would have directed me to the appropriate blades, where I saw that the Virtual Machine was turned off, however Copilot itself didn't have a status check that the Virtual Machine was even started, or triggered any alerts that the Virtual Machine was deallocated. There was a delay, when I first prompted for how I troubleshoot, enough of a delay that I cancelled it and then reprompted again, which returned a result, resulting in 2 of my 10 requests being used up. It was able to supply information on what the resource was, that I had opened in the portal, and any active alerts on that resource *(had I been at the All Resources blade, it would have viewed all alerts)*.

![Microsoft Copilot for Azure - Troubleshoot](/images/posts/MicrosoftCopilotforAzure_PillarTest_Troubleshoot.gif)

## Conclusion

Overall, I feel Copilot for Microsoft Azure, is a suitable companion to working with Microsoft Azure as a *copilot* in the Azure Portal, however, it is clear, that this is very much in Preview, and I would argue unfortunately not for Commercial or Generally available functionality yet, although I could have high standards on what this could be capable of, so make sure you draw your own conclusions and run your own tests.

As with any prompt, working with LLM *(Large Language Models)*, context is key - and having a curious mindset in your questioning can help draw out more information.

If you are a beginner user of Azure, I feel that Microsoft Copilot for Azure can help point you in the right direction, and to the right information.

Context is key – the service, takes context on what resource you are at in the Azure Portal, so the more context it has on the resource the better outputs you will get.

As with all generative AI services, clear prompts are key and don’t trust the outputs, not all Graph queries are right.

In terms of more intermediate and advanced services, it won’t replace full-on Azure management capabilities and troubleshooting yet, remember this is a copilot, an assistant.

> The more feedback can be offered, using the built-in feedback buttons as part of the user interface, as part of its use – the better it will be, and the more skills and tasks it will be able to complete.

Remember, that users can only use Microsoft Copilot for Azure, to view resource data, and make changes to areas they already have the privilege to do! So as you prepare to roll this out, use it as an opportunity to increase your security, and apply just in time and with just enough practice. If you using Infrastructure as Code, then your users may only need Reader access to view data regardless, then Copilot cannot make any changes outside of the toolsets like Terraform you may be deploying.

Overall, this is a product, I will be following and cannot wait to see what it becomes, and where this product shines at the moment is really in the Enchanced Skills, and being able to bring the right Microsoft Learn documentation straight to you, while you are in the Azure Portal, making your learning and engagement alot more streamlined!

![Microsoft Copilot for Azure - Enchanced SKills](/images/posts/MicrosoftCopilotforAzure_CopilotEnchancedSkills.PNG)

## Reference

The links below are some relevant reference material for further reading.

* [What is Microsoft Copilot for Azure?](https://learn.microsoft.com/azure/copilot/overview?wt.mc_id=copilot_1a_webpage_gdc&WT.mc_id=AZ-MVP-5004796)
* [Join the Preview](https://learn.microsoft.com/azure/copilot/overview?wt.mc_id=copilot_1a_webpage_gdc&WT.mc_id=AZ-MVP-5004796#join-the-preview)
* [Enchanced Scenarios](https://learn.microsoft.com/azure/copilot/get-information-resource-graph?WT.mc_id=AZ-MVP-5004796)
* [Simplify IT management with Microsoft Copilot for Azure – save time and get answers fast](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/simplify-it-management-with-microsoft-copilot-for-azure-save/ba-p/3981106?WT.mc_id=AZ-MVP-5004796)
