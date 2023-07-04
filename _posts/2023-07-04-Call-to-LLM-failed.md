---
title: Azure OpenAI - Call to LLM failed
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/CalltoLLMFailed_AzureOpenAIError.png
date: '2023-07-04 00:00:00 +1300'
---

I recently, ran into an error  when attempting to use Azure OpenAI and custom data, in the Chat Playground.
The error I was getting was:

> Error
> Cannot connect to host aidocsopenaiaccount.openai.azure.com:443 ssl:default [Name of Service not known]
> Call to LLM failed.

![Call to LLM failed.](/images/posts/CalltoLLMFailed_AzureOpenAIError.png "Azure OpenAI - Call to LLM failed.")

As I was calling data, that was indexed by Azure Cognitive Search, I thought the index was corrupted or invalid, but after mulitple index attempts, continuted to have the same error, all other prompts (not using my custom data) succeeded.

I recreated the Azure OpenAI service, and was able to succesffuly call the custom data, so started to look at the comparisons between the Azure OpenAI instance, that was working and the Azure OpenAI instance that wasn't.

I did this by taking a look at the JSON of each Azure OpenAI instance, then did a comparison, and discovered a major difference.

![Azure OpenAI - Diff](/images/posts/AzureOpenAI_CalltoLLMFailed_ErrorJSON.png "Azure OpenAI - Diff")

*Note: The one on the left is the working one, the one of the right is the failed one.*

The version that was working, had an endpoint of https://*.openai.azure.com , and the version that didn't work, had a different endpoint: eastus.api.cognitive.microsoft.com.

You can check the JSON output of a resource, by navigating to it on the Azure Portal, in the Overview Pane, clicking JSON view.

![Azure OpenAI - JSON View](/images/posts/CalltoLLMFailed_AzureOpenAI_JSON_View.png "Azure OpenAI - JSON View")

So why would this have been the case?

When I originally created the Azure OpenAI instance that had this issue, I used PowerShell to create the instance:

    $skuName = "S0"
    $kind = "OpenAI"
    # Create Cognitive Services resource
    New-AzCognitiveServicesAccount -ResourceGroupName $resourceGroupName -Name $accountName -Location $location -SkuName $skuName -Kind $kind

This seemed to call an older API or different schema.

The version that worked, I created using the Azure Portal - which was correct.

**If you run into the same problem, then recreate your Azure OpenAI instance using the Azure Portal, or one of the currently supported methods: [Create a resource and deploy a model using Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=AZ-MVP-5004796{:target="_blank"}), currently (as of the 4th of July 2023) PowerShell is not a supported method of creating an Azure OpenAI instance, until the cmdlets have been updated.**
