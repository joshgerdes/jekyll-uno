---
date: '2023-02-14 00:00:00 +1300'
title: Azure Architecture - Solution Requirement Consideration Checklist
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /uploads/az_architecture_solutionchecklistheader.png
_template: new_post
---

Building a cloud solution on Azure can be an exciting yet daunting task.

The key to a successful implementation is carefully planning and considering solution requirements using the guidance of the [Microsoft Cloud Adoption](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/?WT.mc_id=AZ-MVP-5004796 "Microsoft Cloud Adoption Framework for Azure"){:target="_blank"} and [Well Architecture frameworks](https://learn.microsoft.com/en-us/azure/architecture/framework/?WT.mc_id=AZ-MVP-5004796 "Microsoft Azure Well-Architected Framework"){:target="_blank"}.

But knowing what questions to ask and data to capture to give you the bigger picture - to not only consider the solution for the short term and long term, can be difficult. This is where the [Azure architecture solution requirements checklist](https://github.com/lukemurraynz/Azure_Checklists){:target="_blank"} comes in.

Leaning on the great frameworks already in place to assist with the Cloud Adoption and Azure Well Architecture frameworks, the solution requirements checklist is intended to act as a way of asking and capturing the requirements of your solutions. It can be a great reminder to discover some of those requirements _(whether functional or non-functional)_ that you may have forgotten about!

I am using the [Azure Review Checklist](https://github.com/Azure/review-checklists "Azure/review-checklists"){:target="_blank"} - as a building block! I created a custom checklist intended to work alongside the review checklists - but aimed more at the discovery and requirements-gathering stage to assist with designing the proper outcomes for the business.

At the time of this article, there are 8 main categories, and various sub categories:

* AI
* Business
* Data
* Governance
* Infrastructure
* Microservices
* Observability
* Resiliency

Examples of some questions are:

| Main Area | Sub Area  | Checklist item                                                                                    | Description (optional)                                                                                                                                                                                                       |
| --------- | --------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Business  | Goals     | Why are we moving the solution to Azure?                                                          | Understand the reasoning behind the decision to move to a cloud platform like Azure. Helps to validate the end result reaches this goal.                                                                                     |
| Business  | Goals     | What are the business objectives or quantifiable business goals?                                  | What is the business objectives (ie Increased sales revenue, cost reduction, customer satisaction, employee productivity                                                                                                     |
| Business  | Goals     | What outcomes will you achieve for customer?                                                      | What is the  objectives for the customer? What do they want to achieve using this solution                                                                                                                                   |
| Business  | Goals     | Is there a timeline for building the solution Azure?                                              | Asking about the timeline for building a solution in Azure is important to determine resource allocation, budgeting, prioritization, and setting stakeholder expectations.                                                   |
| Business  | Goals     | How many people will be accessing the solution?                                                   | Asking about the number of people accessing the solution helps to determine the necessary resources and scalability required to accommodate the expected traffic and usage.                                                  |
| Business  | Goals     | Is there a targeted event or date for an announcement about the solution's availability on Azure? | Timeline for architecture, deployment, testing can help determine what risks, resource requirements and cost and the delivery of solution.                                                                                   |
| Business  | Goals     | Does the solution impact a Team, Department or organization?                                      | Impact on a team, department, or organization helps determine the scope and potential consequences of the solution, ensuring that all relevant stakeholders are considered and accounted for in the decision-making process. |
| Business  | Customers | What are the customer expecations?                                                                | Customer expectations helps ensure that the solution meets the needs and desires of the end-users, and make sure business outcomes match customer expectations.                                                              |
| Business  | Customers | Is there a deal or customer opportunity associated with having the solution in Azure?             | Any associated deals or customer opportunities helps to understand the potential financial benefits, vendor offerings and growth opportunities of using Azure as a platform for the solution.                                |

![Azure Architecture - Solution requirement considerations](/uploads/azurearchitecture_considerations.png "Azure Architecture - Solution requirement considerations")

> The Azure Architecture - Solution Requirement Consideration checklist, is intended to be a living resource, I am not an expert in all fields so there may be gaps or questions you feel is relevant or missing! Feel free to open a Pull Request to contribute! This is for you!
>
> You can find the **latest version of the checklis**t on GitHub here: [lukemurraynz/**Azure_Checklists**](https://github.com/lukemurraynz/Azure_Checklists "lukemurraynz/Azure_Checklists"){:target="_blank"}

Using this is simple! 

1. **Download** the [latest version of the excel](https://github.com/Azure/review-checklists/releases/latest/download/review_checklist.xlsm "Azure Review Checklists"){:target="_blank"} spreadsheet from: [Azure/review-checklists](https://github.com/Azure/review-checklists "Azure Review Checklists"){:target="_blank"}.
2. **Download** the latest version of the [**Azure Architecture checklist**](https://github.com/lukemurraynz/Azure_Checklists/tree/main "azure_architecture_checklist.en.json")**.**
3. Open up the review_checklist excel document and click **Import checklist from JSON**
4. ![Import checklist from file](/uploads/import-azurearchitecturechecklistjson.png "Import checklist from file")
5. ![Import checklist from file](/uploads/select-azurearchitecturechecklist.png "Import checklist from file")
6. Select the downloaded: azure_architecture_checklist.en.json

Once imported, you can now save the excel document, and start adjusting the **Severity**, **Status** and add **Comments** - to capture the information, to then use to architect your solutions!

> **Note: I do not create, edit or modify the Excel spreadsheet, created by for the Azure Reviews - I simply use it to run my custom checklist. Make sure to check out the** [**Azure Review Checklists**](https://github.com/Azure/review-checklists "Azure Review Checklists")**!**

There are some settings that you might need to change in your system to run **macro-enabled Excel spreadsheet**s. When initially opening the file you may see the following error, which prevents Excel from loading:

> Excel cannot open the file 'review_checklist.xlsm' because the file format or file extension is not valid. Verify that the file has not been corrupted and that the file extension matches the format of the file.

In other cases the file opens with the following message, which prevents you from being able to load the checklist items:

### Unblock file or add an exception to Windows Security

1. You might need to unblock the file from the file properties in the Windows File Explorer, so that you can use the macros required to import the checklist content from github.com:
2. Additionally, you might want to add the folder where you cloned this repo to the list of exceptions in Windows Security (in the Virus & Threat Protection section):
