---
date: 2021-04-09T00:00:00.000+12:00
title: Azure Resource Graph Explorer and the PowerShell Azure Resource Graph
author: Luke
categories:
- PowerShell
- Azure
toc: true

---
Every now and again you come across something that you pay little attention to until you actually spend the time to sit down, work through and try to break stuff! The Azure Resource Graph was that for me!

The idea was to create an export of Azure Recommendations, directly from the Azure Advisor into PowerShell, Microsoft Azure has this functionality out of the box with a few tools:

* Azure Resource Graph Explorer
* The Az.ResourceGraph PowerShell module

* TOC
{:toc}

### Azure Graph Resource Explorer

The Azure Graph Resource Explorer is built into the Azure Portal, it can be found by going to [https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade](https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade "https://portal.azure.com/#blade/HubsExtension/ArgQueryBlade"){:target="_blank"}

or by logging into [https://portal.azure.com]( "Azure Portal"){:target="_blank"} and typing in 'Resource Graph' and select Explorer.

![](/uploads/azureresourcegraphsearch.png)

The Azure Resource Graph Explorer, allows you to explore the Microsoft Azure Resource Graph, using inbuilt Sample Queries and the Kusto Query language. The Powershell queries mentioned in the section below, started by implying click on the 'microsoft.advisor/recommendations' field and selecting Run Query.

    advisorresources
    | where type == "microsoft.advisor/recommendations"

![Azure Resource Graph Explorer](/uploads/azureresourcegraph.png "Azure Resource Graph Explorer")

I then clicked on the 'See Details' on the right-hand side to see all the details that were being brought in, in each object or row. Example below:

    {
        "recommendationTypeId": "7262dc51-c168-41b5-b99b-b5b98f8fe50a",
        "extendedProperties": {
            "assessmentKey": "7262dc51-c168-41b5-b99b-b5b98f8fe50a",
            "score": "0"
        },
        "resourceMetadata": {
            "resourceId": "/subscriptions/0673a0bd-0c9b-483f-9aee-c44795ae739f",
            "singular": null,
            "plural": null,
            "action": null,
            "source": "/subscriptions/0673a0bd-0c9b-483f-9aee-c44795ae739f/providers/Microsoft.Security/assessments/7262dc51-c168-41b5-b99b-b5b98f8fe50a"
        },
        "shortDescription": {
            "solution": "Subscriptions should have a contact email address for security issues",
            "problem": "Subscriptions should have a contact email address for security issues"
        },
        "suppressionIds": null,
        "impactedField": "Microsoft.Subscriptions/subscriptions",
        "impactedValue": "0673a0bd-0c9b-483f-9aee-c44795ae739f",
        "lastUpdated": "2021-04-08T13:15:54.2870000Z",
        "category": "Security",
        "metadata": null,
        "impact": "Low"
    }

And no, that isn't my real Subscription ID etc, I've replaced the field with randomly generated GUIDs.

We can see that there is a good amount of actionable data here:

* This is a Security Category, recommendation.
* It is Low Impact
* The problem is that the Azure subscription should have a contact email address to be used for Security alerts and it does not have one set up (Oops!)

So we need to turn it into something a bit more useable, I know that the Azure Advisor has the following categories:

* Cost
* HighAvailability
* OperationalExcellence
* Performance
* Security

The same syntax can be used for any of these categories, for my example, we will continue with Security, Looking at the Details (or Example above) we can see that Category is simply listed on its own at the top level, inside the 'microsoft.advisor/recommendations' field, so we now need to add another pipe to the query:

    | where properties['category'] == 'Security'

This will now only select the 'Security' category. However as you can see below, it's hardly something you can action on or read.

![Azure Resource Graph - Category 'Security'](/uploads/azureresourcegraph_category.png "Azure Resource Graph - Category 'Security'")

The next step is to look into making it a bit more readable because we know this is a Kusto Language, its time to hit the Microsoft Docs page and read up about the 'Project Operator' - [https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/projectoperator](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/projectoperator "https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/projectoperator"){:target="_blank"}. Project = "Select the columns to include, rename or drop, and insert new computed columns." That sounds like what we want.

If we take a gander back at the 'Full Details' (or Example above) there are 3 fields I am looking at that would add the most value to a report or digest for the security posture of my Azure ecosystem:

* Solution
* impactedField
* impactedValue

We now need to add our final pipe to remove everything we don't want and add the properties that make the most sense to use, because we are using multiple properties we will do it separated by commas. It's worth noting that unlike the 'Security' property above (and the impactedField, impactedValue), which was a top-level property, the Solution property is a sub-properties of 'shortDescription', so we have to select the shortdescription property and then expand out to the extended solution property like below:

    | project properties.shortDescription.solution

That now gives us a list of the security alerts on the subscription, but without a heading that makes sense:

![](/uploads/azureresourcegraphheader.png)

To add a header called: Recommendation, we need to do the following

    | project Recommendation=tostring(properties.shortDescription.solution)

Now we are ready to add the impactedField and impactedValue.

The final query should look like this:

    advisorresources
    | where type == 'microsoft.advisor/recommendations'
    | where properties['category'] == 'Security'
    | project Recommendation=tostring(properties.shortDescription.solution), ImpactedType=tostring(properties.impactedField), ImpactedResources=tostring(properties.impactedValue )

and the Azure Resource Graph Explorer should display something like this:

![](/uploads/azuregraphexplorerfinalquery.png)

### Azure Graph PowerShell

Using the Azure Resource Graph Explorer is a good way to create the Kusto queries you want, which you can then run the queries in PowerShell and turn them into PowerShell objects, which opens up a few possibilities for things like:

* Automated Reporting on Cost, Security etc
* Proactive remediation actions.

First things first you need to install the Az.ResourceGraph module, then you can use the Search-AzGraph to run the queries that you created above. I am going to rely on the gist below to give you a few examples.

![](/uploads/azuregraphpowershell.png)

{% gist b350b5c73ef7fb0ad63f5797e4055f56 %}