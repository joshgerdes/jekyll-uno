---
title: Application Security Groups in Microsoft Azure
author: Luke
categories:
  - Azure
date: 2022-01-21 00:00:00 +1300
toc: true
header:
  teaser: /uploads/highleveldiagram_asg.png
---

Azure Application Security Groups (ASG) allow you to define what workloads _(Virtual Machines)_ you are running in Azure has access to what resource - without being tied by managing complex IP address rules inside a [Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview?WT.mc_id=AZ-MVP-5004796 "Network security groups"){:target="_blank"}.

> Application security groups enable you to configure network security as a natural extension of an application's structure, allowing you to group virtual machines and define network security policies based on those groups. You can reuse your security policy at scale without manual maintenance of explicit IP addresses.

These Azure Application Security groups allow you to define your workloads, for example, Azure Virtual Desktop Session Hosts as a 'group' and what they may have access to in your Azure Virtual Network without opening up the service to everything inside of that VNET or creating overly complex rules that could make it hard to troubleshoot.

There are a few things to be mindful of:

* Azure Application Security Groups are Virtual Network-specific, so they can work to allow resources across subnets, but not in separate Virtual Networks, even if they have peered.
* As with most Azure resources, there are Subscription level[limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits?toc=%2Fazure%2Fvirtual-network%2Ftoc.json&WT.mc_id=AZ-MVP-5004796#azure-resource-manager-virtual-networking-limits "Networking limits - Azure Resource Manager"){:target="_blank"}; you cannot have more than 3,000 Azure Application Security groups in a single subscription and region.
* The rules that specify an application security group as the source or destination are only applied to the network interfaces that are members of the application security group; this does not affect anything not in this group, even though your Network Security Group is based on the subnet.
* You can assign more than one Application Security group to a resource

In my example, I have a single virtual network, with 2 subnets _(one subnet, has an Azure Virtual Desktop session host and the other one has a webserver running IIS)_, using Azure Application Security Groups, we will restrict IIS access to the webserver from the Azure Virtual Session hosts only - so IIS won't be accessible from any other machine in the Virtual Network.

![High Level  - Diagram ASG](/uploads/highleveldiagram_asg.png "High Level  - Diagram ASG")

#### Create Application Security Group

Let's get started by creating an Application Security Group.

1. Open the **Azure Portal**
2. Click on [**+ Create a resource**](https://portal.azure.com/#create/hub "Azure Portal - Create a resoruce"){:target="_blank"}
3. Search for: **Application security group** and select it
4. Click **Create**
5. **Select** the **subscription** that the Application Security group will be created in
6. **Select** the **Resource Group** _(in my example, I am selecting AVD)_
7. ![Create an Application Security Group](/uploads/create-applicationsecuritygroup.png "Create an Application Security Group")
8. Click **Review + create**
9. Click **Create**

#### Assign Application Security Group

Now that the Application Security group has been created it's time to assign it this our Azure Virtual Desktop session hosts.

1. Open the **Azure Portal**
2. **Navigate** to your **Azure Virtual Desktop** session host _(or other workloads you are going to use)_
3. Select **Networking**
4. Select **Application security groups**
5. Click **Configure the application security groups**
6. **Select** the Application Security **group** created earlier
7. ![Assign Application Security Group](/uploads/assign-applicationsecuritygroup.png "Assign Application Security Group")
8. Click **Save**

#### Assign Block Rule Security Group

Now it's time to assign a block rule to our web server, for port 80 as by default it is allowed through the 'AllowVnetInBound' default rule.

1. Navigate to the **Network Security Group** that holds your web server _(I am going to make the change on a Network Security group that is tied to the Network Interface of the web server, but the same principle applies if it was applied to a Network Security Group on the subnet - you just need to add the destination IP of the webserver)_
2. Click on **Inbound security rules**
3. Click **+ Add**
4. Add a **Deny** port **rule** for port **80** for all source
5. ![Assign Block Network Security Group Rule](/uploads/create-blocknsg80rule.png "Assign Block Network Security Group Rule")
6. Click **Save**

After a few minutes, traffic from any workloads on the virtual network will now be blocked from accessing the web server on port 80.

![Port 80 blocked](/uploads/avd-testport80_deny.png "Port 80 blocked")

#### Create Allow rule using Application Security Group

Just a note around the priorities of Network Security Group rules: 

> Rules are processed in priority order _(using a number between 100 and 4096)_, with lower numbers processed before higher numbers, because lower numbers have higher priority. Once traffic matches a rule, processing stops. 
>
> As a result, any rules that exist with lower priorities (higher numbers) that have the same attributes as rules with higher priorities are not processed.

1. Navigate to the **Network Security Group** that holds your web server _(I am going to make the change on a Network Security group that is tied to the Network Interface of the web server, but the same principle applies if it was applied to a Network Security Group on the subnet - you just need to add the destination IP of the webserver)_
2. Click on **Inbound security rules**
3. Click **+ Add**
4. For **Source**, select the **Application Security Group** 
5. Select **HTTP** as the service
6. Select **Allow** as the action
7. Set the **Priority** to be **lower** than the block rule, ie 4095
8. Click **Save**
9. ![Create Network Security Rule Allow](/uploads/avd-testport80_allow.png "Create Network Security Rule Allow")

After a few minutes, traffic from any workloads on the virtual network will now be allowed for any workloads from your Azure Virtual Desktop farm only _(assigned to the Application Security group)_.

![AVD - Test Port 80 Allow](/uploads/avd-testport80_edgeallow.png)

If I attempted to access the webserver from my application server, it fails:

![AVD - Test Port 80 Deny](/uploads/avd-testport80_deny.png)

Hopefully, this helps you avoid overly complex security rules that are reliant on knowing and managing the IP of your workloads and help secure your networks.
