---
date: '2023-02-23 00:00:00 +1300'
title: Azure Availability Zone Peering
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /uploads/availability-zones.png
_template: new_post
---

In most [regions ](https://learn.microsoft.com/azure/reliability/availability-zones-service-support?WT.mc_id=AZ-MVP-5004796 "Availability zone service and regional support"){:target="_blank"}_(and odds are, if your area doesn't have Avalibility Zones, it's on the roadmap to be set up)_, Microsoft Azure has [Availability Zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview?WT.mc_id=AZ-MVP-5004796 "What are Azure regions and availability zones?"){:target="_blank"}.

Each Azure region features data centres deployed within a latency-defined perimeter. At a high level, these zones consist of 3 separate data centres with independent cooling, power, switching etc.

![Azure availability zones](/uploads/availability-zones.png "Azure availability zones")

> Azure availability zones are connected by a high-performance network with a round-trip latency of less than 2ms. They help your data stay synchronized and accessible when things go wrong. Each zone is composed of one or more datacenters equipped with independent power, cooling, and networking infrastructure. Availability zones are designed so that if one zone is affected, regional services, capacity, and high availability are supported by the remaining two zones.
>
> With availability zones, you can design and operate applications and databases that automatically transition between zones without interruption. Azure availability zones are highly available, fault tolerant, and more scalable than traditional single or multiple datacenter infrastructures.

#### Availability Zone peering

Today we are going to look into Availability Zone peering:

> Each data centre is assigned to a physical zone. Physical zones are mapped to logical zones in your Azure subscription. Azure subscriptions are automatically assigned this mapping when a subscription is created.

##### Physical Zones vs Logical Zones

There are a few things to be aware of here that I will call out:

* **Physical zones** are mapped to **logical zones** in your Azure subscription.
* Azure subscriptions are automatically **assigned** this **mapping** **when** a **subscription** is **created**.

**So what does this mean?**

We know we have three separate data centres within a single region:

| Zone | Region |
| --- | --- |
| 1 | Australia East |
| 2 | Australia East |
| 3 | Australia East |

We can see these zones in the Azure Portal when we create resources:

![Azure Avalibility Zone - Selection](/uploads/avalibilityzone_selection_azportal.png "Azure Avalibility Zone - Selection")

This is great for making your solutions redundant against a single data centre failure and spreading your workloads across different zones; services such as Virtual Networks are zone-redundant by default, allowing access to resources across multiple zones out of the box.

One reason you may have all your resources in a single zone could be latency.

Lets us go back to the paragraphs around physical and logical zones and mapping - what does this mean?

What this means is that each of the three data centres is assigned a physical **AND** logical mapping, so your Azure datacentres look like this:

| Zone (Physical) | Region | Zone (Logical) |
| --- | --- | --- |
| 1 | Australia East | 3 |
| 2 | Australia East | 2 |
| 3 | Australia East | 1 |

When you **deploy a resource into an Azure Avalibility Zone and select Zone 1**, you choose **the Logical Zone, NOT** a **physical zone**.

This means that **FOR EACH** Microsoft **Azure subscription,** whether in the same Microsoft Entra ID tenancy or not, **Zone 1** can be a **different physical data centre**.

So if you have resources deployed across multiple subscriptions, and all your resources are deployed to Zone 1 - they **MAY NOT** be in the same physical data centre.

| Azure Subscriptions | Region | Zone (Logical) | Zone (Physical) |
| --- | --- | --- | --- |
| Sub A | Australia East | 1 | 1 |
| Sub B | Australia East | 1 | 3 |
| Sub B | Australia East | 1 | 1 |

In an example like the above, you have three separate Azure subscriptions, and you have deployed your Virtual Machines and other resources across all Azure subscriptions into Zone 1, 2 of your subscriptions are using the same physical zone for zone 1, and another subscription is using a separate availability zone altogether.

![AzureAvailabilityZones_Logical](/uploads/azureavailabilityzones_logical.png "AzureAvailabilityZones_Logical")

**One of the reasons the logical and physical zones are different is due to capacity management**; out of habit, many people select Zone 1 - this would mean that certain zones become overpopulated while others are underutilized. The logical zones allow Microsoft some ability to spread the load.

It's worth noting that **mapping the Logical to Physical Zones of the Avalibility Zones within your region is done when the subscription is created**.

##### Checking your Zone Peers using PowerShell and the Azure API

**During normal business use - you don't need to know any of this; select a zone and deploy**; if you have resources across subscriptions and run into additional latency - this may be why, although each availability zone is connected through a dedicated regional low-latency network with a round-trip latency of less than 2ms.

But suppose you are curious or want to delve deeper into your Disaster Recovery and resiliency architecture within a single region. In that case, it can be helpful to know the mapping.

This information isn't fed into the Azure Portal. To find the mapping, we need to query the Azure API directly using the [Check Zone Peers](https://learn.microsoft.com/en-us/rest/api/resources/subscriptions/check-zone-peers?tabs=HTTP&WT.mc_id=AZ-MVP-5004796 "Subscriptions - Check Zone Peers"){:target="_blank"} endpoint.

To do this, I have written a rough PowerShell script that will register the AvailabilityZonePeering Azure feature that you need to enable the lookup and query the API for the mappings.

    # Connect to Azure using Get-AzAccount
    Connect-AzAccount
    
    # Set the region to 'Australia East'
    $region = 'Australia East'
    
    # Get all subscriptions that the account has access to
    $subscriptions = Get-AzSubscription | Select-Object -ExpandProperty SubscriptionId
    
    # Get the access token for the authenticated user
    $token = (Get-AzAccessToken).Token
    
    # Check if AvailabilityZonePeering feature is enabled and enable it if it's not
    $azFeature = Get-AzProviderFeature -ProviderNamespace Microsoft.Resources -FeatureName AvailabilityZonePeering
    if (!$azFeature.RegistrationState.Equals("Registered")) {
        do {
            Register-AzProviderFeature -FeatureName AvailabilityZonePeering -ProviderNamespace Microsoft.Resources
            Start-Sleep -Seconds 5
            $azFeature = Get-AzProviderFeature -ProviderNamespace Microsoft.Resources -FeatureName AvailabilityZonePeering
        } until ($azFeature.RegistrationState.Equals("Registered"))
        Write-Host "The AvailabilityZonePeering feature has been enabled."
    } else {
        Write-Host "The AvailabilityZonePeering feature is already enabled."
    }
    
    # Define the request body for the REST API call
    $body = @{
        subscriptionIds= $subscriptions | ForEach-Object { 'subscriptions/' + $_ }
        location = $region
    } | ConvertTo-Json
    
    # Define the request parameters for the REST API call
    $params = @{
        Uri         = "https://management.azure.com/subscriptions/" + $subscriptions[0] + 
                      "/providers/Microsoft.Resources/checkZonePeers/?api-version=2020-01-01"
        Headers     = @{ 'Authorization' = "Bearer $token" }
        Method      = 'POST'
        Body        = $body
        ContentType = 'application/json'
    }
    
    # Invoke the REST API and store the response
    $availabilityZonePeers =  Invoke-RestMethod @Params
    
    # Initialize an empty array for the output
    $output = @()
    
    # Loop through each availability zone and its associated peers and add them to the output array
    foreach ($i in $availabilityZonePeers.availabilityZonePeers.availabilityZone) {
        foreach ($zone in $availabilityZonePeers.availabilityZonePeers[$i-1].peers ) {
            $output += New-Object PSObject -Property @{
                Zone = $i
                MatchesZone = $zone.availabilityZone
                SubscriptionId = $zone.subscriptionId
            }
        }
        $output += ""
    }
    
    # Output the results
    $output |  Format-Table

Once we have connected to Microsoft Azure and run the script, we will get an output like the one below, which I ran across my own three subscriptions:

| SubscriptionId | MatchesZone | Zone |
| --- | --- | --- |
| 3bdfd67e-6280-43af-8121-4f04dc84706c | 2 | 1 |
| 8df7caa2-95cb-44d1-9ecb-e5220ec6a825 | 1 | 1 |
| 119bbbb7-3ab5-4eb3-ab21-3c65f562fbef | 1 | 1 |
| 3bdfd67e-6280-43af-8121-4f04dc84706c | 1 | 2 |
| 8df7caa2-95cb-44d1-9ecb-e5220ec6a825 | 2 | 2 |
| 119bbbb7-3ab5-4eb3-ab21-3c65f562fbef | 2 | 2 |
| 3bdfd67e-6280-43af-8121-4f04dc84706c | 3 | 3 |
| 8df7caa2-95cb-44d1-9ecb-e5220ec6a825 | 3 | 3 |
| 119bbbb7-3ab5-4eb3-ab21-3c65f562fbef | 3 | 3 |

On the right-hand side, we see the 'Zones' - these are the Physical Zones, so Zone 1 to 3.

For each subscription, we can see the Logical Zone mapping as well.

In this example, my subscription of '3bdfd67e-6280-43af-8121-4f04dc84706c', if I were to deploy to Zone 2 in my Azure Portal, would deploy to the same physical datacenter as Zone 1 of: '8df7caa2-95cb-44d1-9ecb-e5220ec6a825'.

As you can also see, my Zone 3 matches the same Zone 3 logically and physically for all my subscriptions, but there are differences between Zone 2 and 1.

Again, during normal business as usual, you don't need to know this - but it's always good to know how this works. If you want confirmation of the resiliency of your architecture across Availability Zones, this is a great way to confirm whether your resources are physically located together - or not.
