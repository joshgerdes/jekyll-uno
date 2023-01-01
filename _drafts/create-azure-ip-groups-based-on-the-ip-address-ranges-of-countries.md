---
date: 2023-01-02 00:00:00 +1300
title: Create Azure IP Groups based on the IP address ranges of countries
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
An [IP Group](https://learn.microsoft.com/azure/firewall/ip-groups?WT.mc_id=AZ-MVP-5004796 "IP Groups in Azure Firewall") in Microsoft Azure is a logical container of IP address ranges for private and public addresses.

> IP Groups allow you to group and manage IP addresses for Azure Firewall rules in the following ways:
>
> * As a source address in DNAT rules
> * As a source or destination address in network rules
> * As a source address in application rules
>
> An IP Group can have a single IP address, multiple IP addresses, one or more IP address ranges or addresses and ranges in combination.

The IP Group allows you to define an IP address that can be used in conjunction with Azure Firewall, to allow or deny internal or external traffic from a perspective set of IP addresses.

> The following IPv4 address format examples are valid to use in IP Groups:
>
> * Single address: 10.0.0.0
> * CIDR notation: 10.1.0.0/32
> * Address range: 10.2.0.0-10.2.0.31

By default, the Azure Firewall blocks outbound and inbound traffic; however, you may want to enable _(or block)_ traffic to and from specific countries - there is no built-in geo-filtering with Azure Firewall, as you can use other services, such as the Web Application Gateway and with the [Application Gateway ](https://learn.microsoft.com/azure/application-gateway/overview?WT.mc_id=AZ-MVP-5004796 "What is Azure Application Gateway?")and [Azure Front Door](https://learn.microsoft.com/azure/web-application-firewall/afds/waf-front-door-geo-filtering?WT.mc_id=AZ-MVP-5004796 "What is geo-filtering on a domain for Azure Front Door Service?") to block and allow access, and other third party services such as Cloudflare. This script can be adapted for any list of IP ranges; it doesn't need to be country IP addresses.

However, you may want to control access to and from specific countries _(or other services)_ with Azure Firewall - this is where the IP Groups can be effective, and because we won't be editing the Firewall directly - we won't run into issues with delays without having to wait for the Azure Firewall policies to be updated.

To solve the issue of creating the IP groups and finding and keeping the IP groups up-to-date with various countries' IP ranges - I have created a PowerShell function to retrieve supported [countries](https://www.ipdeny.com/ipblocks/data/aggregated/ "IP Deny aggregated list")' IP CIDR ranges and create the relevant IP groups.

![Azure IP Group - Country IP ranges](/uploads/azureipgroupscript.png "Azure IP Group - Country IP ranges")

With IP Groups, there are a few things to keep in mind:

* You can have 200 IP Groups per firewall with a maximum of **5000 individual IP addresses or prefixes per each IP Group**.

For a country like New Zealand, the 5000 limit for the address ranges is acceptable - but for other countries, like the United States or United Kingdom, this can be an issue, where the total IP ranges can grow to over 20k - to deal with this, the script will create multiple IP Groups, and append a number to the end.

Suppose IPs are manually added to the groups. In that case, they won't be added - the script will add in any different or new IP ranges, ignoring any current IP ranges (_this means it won't delete any IP ranges that are removed from the source IP list from IPDeny)_; however, I recommend that anything added outside of this script is kept in a separate IP group.

_As with any script, I recommend this is tested in a test environment first._

Before we run it, we need a few prerequisites.

* At least [PowerShell 3.0+](https://learn.microsoft.com/powershell/scripting/install/installing-powershell?view=powershell-7.3&WT.mc_id=AZ-MVP-5004796 "Install PowerShell on Windows, Linux, and macOS")
* Azure [Az PowerShell Modules](https://learn.microsoft.com/powershell/azure/new-azureps-module-az?view=azps-9.2.0&WT.mc_id=AZ-MVP-5004796 "Introducing the Azure Az PowerShell module") _(specifically Az.Network, Az.Resources)_

The function assumes you have [connected to Microsoft Azure and your relevant subscription](https://luke.geek.nz/azure/powershell/Using-PowerShell-to-connect-to-Azure/ "Using PowerShell to connect to Microsoft Azure").

Before we import the function, I am going to check if any IP groups already exist quickly _(this isn't required) -_ but it's a good opportunity to check that you are connected to your Azure subscription and that the AzIPGroup cmdlets exist -  and whether you have any IP groups already existing.

    Get-AzIpGroup

![Get-AzIpGroup](/uploads/checkexistingipgroups_empty.gif "Get-AzIpGroup")

I have received no errors or existing IP groups in my subscription, so I will continue importing my function.

The function can be found here:

GIST

Once saved to your computer, it's time to import it into your active PowerShell terminal and run it _(after you have verified you have connected to the correct Azure subscription)_.

So I will navigate to the script and import it:

    cd D:\git
    . .\New-AzCountryIPGroup.ps1
    New-AzCountryIPGroup

![Import New-AzCountryIPGroup.ps1](/uploads/import_countryipgrpfunction.gif "Import New-AzCountryIPGroup.ps1")

The 'New-AzCountryIPGroup' Azure function relies on 4 parameters:

| Parameters | Values |
| --- | --- |
| CountryCode | NZ |
| IPGroupName | IPGrpNZ |
| IPGroupRGName | NetworkRG |
| IPGroupLocation | AustraliaEast |

Make sure that the values change to your environment; in my example, I am specifying an IP Group and Resource Group that doesn't exist so that the script will create it for me - and the location I will be deploying to will be the Australia East region.

    New-AzCountryIPGroup -CountryCode NZ -IPGroupName IPGrpNZ -IPGroupRGName NetworkRG -IPGroupLocation AustraliaEast

![New-AzCountryIPGroup](/uploads/run_countryipgrpfunctionnz.gif "New-AzCountryIPGroup")

As you can see, the script created an Azure Resource Group and imported the New Zealand IP ranges to a new IP Group...

Not required - but if I rerun it, it will simply override any IP addresses that are the same and add any new addresses to the same IP Group that already exists, as below:

![Rerun New-AzCountryIPGroup](/uploads/rerun_countryipgrpfunctionnz.gif "Rerun New-AzCountryIPGroup")

The Azure IP Group is visible in the Azure Portal as below:

![Azure Portal - Azure IP Group ](/uploads/azureportal_ipgrpnz.png "Azure Portal - Azure IP Group ")

And a Tag was added to include the country:

![Azure IP Group - Tag](/uploads/azureportal_ipgrpnztag.png "Azure IP Group - Tag")