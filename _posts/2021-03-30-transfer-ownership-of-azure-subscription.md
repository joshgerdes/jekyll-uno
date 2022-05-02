---
date: 2021-03-31 00:00:00 +1300
title: Transfer Ownership of an Azure Subscription
author: Luke
categories:
- Azure
toc: true
permalink: /transfer-ownership-of-azure-subscription
header: 
  teaser: "images/iazure-marketplace-banner.png"

---
Imagine you want to transfer Azure resources to another person or company? This could be because something may have been created in an external third-party subscription, to begin with, or you have created a product using Azure resources that you have just sold to the highest bidder!

Before you start rolling in that money bin of cash, you need to be able to give that person the Azure resources. The best way to do this is to transfer ownership of an Azure subscription.

It may be best to create a new Azure subscription, and then transfer _(using the Move Resources in the Azure Resource Group)_ the resources to that new subscription. That way it is clean, then the recipient can just migrate the resources to their own Production subscription later, etc as they see fit.

Just a heads up IF you are selling services you have created in Microsoft Azure, whether freelance or professionally make sure you have spent time working on Azure governance to make sure you have a proper Azure Landing Zone stood up for standardization and naming conventions in place if you are a transferring a resource that has a Global Scope (ie these are usually Public-facing, the last thing you want is to transfer the resources to someone else and find out that you can't reuse the same unique name.

**_Please read this carefully,_** there are certain limitations when transferring Subscription Ownership - especially across to another tenancy that you need to be aware of, these limitations are the Type of Subscription it is and the type of resources, encryption status, etc.[Transfer an Azure subscription to a different Azure AD directory](https://docs.microsoft.com/en-gb/azure/role-based-access-control/transfer-subscription?WT.mc_id=AZ-MVP-5004796#understand-the-impact-of-transferring-a-subscription) In some cases, you may need to look at alternative ways, such as redeploying or recreating the resources in the other subscription/tenancy manually - via redirecting an Azure DevOps deployment or manual backup export and import.

## Transfer a Subscription

Once you are ready to transfer a subscription, you can do the rest, simply through the Azure Portal:

1. In the Azure Portal, navigate to [Subscriptions](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade)
2. Click on the Subscription you want to migrate
3. Click on Transfer billing ownership
4. Type in the Recipient's email address, in the email address field
5. If you are moving the Azure subscription to another Azure AD tenancy (in this article, I am assuming we are), select the 'Move Subscription Tenant toggle: Yes
   ![Transfer Billing Ownership](/uploads/2021-03-28-18_56_27-transfer-billing-ownership-microsoft-azure-mozilla-firefox.png)
6. Click on Send Transfer Request, acknowledge the prompt and click Yes
7. This will send an email to the recipient with a link to transfer the Azure subscription and all the resources.
   ![Transfer Billing Ownership](/uploads/transferrequest.png)

Note: The Transfer Request is not permanent, the recipient has only a few weeks to accept the transfer before you will need to it again, you can see the expires date in the screenshot above.

Note: Something to be aware of, only the user in the new account who accepted the transfer request will have access to manage the resources, they will need to add the necessary groups and rights on their end.

## Cancel an Azure Subscription Transfer

If the recipient hasn't accepted the transfer, you can revoke or cancel the transfer request. To do this, do the following:

1. In the Azure Portal, navigate to [Subscriptions](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade)
2. Click on the Subscription you want to migrate
3. Click on Transfer billing ownership
4. You will now get a Window indicating the Transfer Request is pending
5. Click on Cancel the Transfer Request (bottom of the Blade)
   ![Transfer Billing Ownership](/uploads/transferrequest_cancel.png)
6. Accept the prompt to cancel the transfer request.

Note: You can now click on the Transfer billing ownership, to confirm the request was canceled and if needed, open a new request. Just a heads up as well, that canceling the transfer, will also email the recipient.
