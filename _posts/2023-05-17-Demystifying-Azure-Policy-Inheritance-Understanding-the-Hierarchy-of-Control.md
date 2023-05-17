---
title: Demystifying Azure Policy Inheritance
author: Luke
categories: Azure
description: Look into Azure Policy inheritance and how it works.
header:
  teaser: /images/posts/AzurePolicy_Effects.png
date: 2023-05-16T12:00:00.000Z
---

Today, we are going to look into demystifying Azure Policy inheritance and how it works, so let’s do some testing.

In my tests – I have a single resource group named: AzPolicy-Test. This resource group has been placed in the Australia East region.

Now that we have a Resource Group to use in our testing, I need a policy – to keep things simple, I am going use the built-in policy of: [AllowedLocations](https://www.azadvertizer.net/azpolicyadvertizer/e56962a6-4747-49cd-b67b-bf8b01975c4c.html). This policy will allow us to control which region we can deploy our Azure resources into.

##### **Scenario #1 – Policy assigned to the subscription with Allow Australia East ONLY.**

I have assigned my Azure Policy to a Subscription, that contains my AzPolicy-Test Resource Group. I have set the Allowed Locations to: Australia East.

![Azure Policy - Allowed locations](/images/posts/AzurePolicy-AllowedLocations-DenyAll\(AustraliaE\).png "Azure Policy - Allowed locations")

Let us do some testing, and try to deploy an Azure Resource (in my example, an Azure Storage account) into my Resource Group:

| Can I deploy to Australia East? | Yes |
| ------------------------------- | --- |
| Can I deploy to UK South?       | No  |

As you can see my storage account deployed into Australia East successfully… as expected!

![Azure Portal - filtered by location](/images/posts/AzurePolicy-FilterLocations_AustraliaEast.png "Azure Portal - filtered by location")

Now, lets try and deploy a Storage account into the same Resource Group, but in the UK South region.

As Azure Resource Manager is analysing and verifying the inputs give it – it now knows there is an Azure Policy – enforcing specific locations and preventing my deployment into the UK South.

![Azure Storage Account - Deny UK South deployment](/images/posts/AzurePolicy_DenyUKSouth.png "Azure Storage Account - Deny UK South deployment")

This is as expected, and even if I were to use another resource group – I still won’t be able to create resources in other regions.

##### **Scenario #2 – Policy assigned to the subscription with Allow Australia East but another policy with Allow UK South only on the Resource Group.**

Now that we know, we can create resources in Australia East – lets assign the same ‘Allowed Locations’ policy to the Resource Group, but Denying Australia East, and Allowing UK South. The policy allowing Australia East will
still remain assigned to the subscription.

![Azure Policy - Allowed locations - UK South](/images/posts/AzurePolicy-AllowedLocation_UkSouth.png "Azure Policy - Allowed locations - UK South")

Let us do some testing, and try to deploy an Azure Resource (in my example, an Azure Storage account) into my Resource Group:

| Can I deploy to Australia East? | No |
| ------------------------------- | -- |
| Can I deploy to UK South?       | No |

![Azure Storage account deployment - Policy validation error](/images/posts/AzurePolicy-DisableUKSouthDeployment.png "Azure Storage account deployment - Policy validation error")

![Azure Storage account deployment - Policy validation error](/images/posts/AzurePolicy-DisableAustraliaEastDeployment.png "Azure Storage account deployment - Policy validation error")

I can’t deploy to either UK South or Australia East, even though I have 2 separate policies, one policy allowing Australia East (deployed at the subscription) and one policy allowing UK South (deployed at the Resource
Group).

In this case, the policies have worked together, with the most restrictive of them both in effect – which is Deny.

##### Review&#xA;So lets review, originally you might think that like Group Policy – the last policy wins – this is not always the case, when conflicting policies are assigned at different levels, the policy at the highest level in the hierarchy takes precedence over policies at lower levels. When preforming a Modify or Create on a resource – the Azure resource provider checks with the Azure Policy engine..




There are, however, various effects which are analysed first.

![Azure Policy Effects](/images/posts/AzurePolicy_Effects.png "Azure Policy Effects")





1. Disabled is checked first to determine
   whether the policy rule should be evaluated.
2. Append and Modify are then
   evaluated. Since either could alter the request, a change made may prevent an
   audit or deny effect from triggering. These effects are only available with a
   Resource Manager mode.
3. Deny is then evaluated. By evaluating
   deny before audit, double logging of an undesired resource is prevented.
4. Audit is evaluated.
5. Manual is evaluated.

After the Resource Provider returns a success code on a Resource Manager mode request, AuditIfNotExists and DeployIfNotExists evaluate to determine whether additional compliance logging or action is required.

Remember that policy enforcement occurs during resource deployment or updates. Existing resources are not retroactively affected unless a manual remediation is performed.

##### &#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;&#xA;
