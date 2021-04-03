---
date: 2021-04-03 00:00:00 +1300
title: Keep up to date with latest changes on Azure using PowerShell
author: Luke
categories:
- PowerShell
- Azure
toc: false

---
Keeping up with what is happening with changes and previews in Microsoft Azure is difficult, change happens all the time - and being able to stay informed on what is happening with the Azure ecosystem is half the battle, whether it is a new feature or security fix.

Microsoft publishes the latest updates on Azure Products and features to their Azure Updates blog: [https://azure.microsoft.com/en-us/updates/](https://azure.microsoft.com/en-us/updates/ "https://azure.microsoft.com/en-us/updates/")

So you can browse the website each week, or... monitor the RSS feeds. Sometimes this isn't enough, you may want to do something with this information such as:

* Create Alerts or Notifications to specific teams who may work with Azure SQL, or Azure Automation and not care about any other product.
* Not have to go to the website to keep up-to-date with what is happening, maybe your happy with it popping up in your PowerShell session each time you open it.
* Publish the information to Microsoft Teams channels to keep people informed.

I have created a PowerShell function, that will retrieve the latest updates from the Microsoft Azure Updates RSS Feed and turn it into a PowerShell object you can actually use to keep informed.

* TOC
  {:toc}

## The Script - Get-AzureBlogUpdates

The script is hosted on my Github repository. Feel free to clone/recommend improvements or fork:

{% gist 7bf30a1f0f5f12e622e2bbe11ff7033d %}

## Examples

    #Runs the actual Function:
    Get-AzureBlogUpdates

![](/uploads/windowsterminal_5oqnizj8ko.png)

    #EXAMPLE - Gets Azure Blog Updates, that have been published in the last 7 days.
    $PublishedIntheLastDays = (Get-Date).AddDays(-7)
    Get-AzureBlogUpdates | Where-Object 'Published Date' -GT $PublishedIntheLastDays

![](/uploads/windowsterminal_duphvuiqpz.png)

    #EXAMPLE - Gets all Azure Blog Updates, and displays it as a Table, organised by Category
    Get-AzureBlogUpdates | Sort-Object Category -Descending | Format-Table

![](/uploads/windowsterminal_xrskcraov0.png)

    #EXAMPLE -Gets the latest 10 Azure Blog Articles
    Get-AzureBlogUpdates | Select -Last 10

![Get-AzureBlogUpdates - Select Last 10 Articles](/uploads/windowsterminal_bxxy0lnrjc.png "Get-AzureBlogUpdates - Select Last 10 Articles")

    #EXAMPLE - Gets the Azure Blog Update articles, where the title has Automation in it.
    Get-AzureBlogUpdates | Where-Object Title -match 'Automation'

![Get-AzureBlogUpdates - Title matches Automation](/uploads/windowsterminal_qitgwrqfm9.png "Get-AzureBlogUpdates - Title matches Automation")