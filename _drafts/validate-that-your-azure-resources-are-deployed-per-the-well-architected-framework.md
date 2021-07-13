---
date: 2021-07-13 00:00:00 +1200
title: Improve your Azure infrastructure  with PSRule for Azure
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/windowsterminal_data_psrules-azure.png"

---
Validate that your Azure Resources are deployed per the Well-Architected Framework.. it is pretty long-winded, but **imagine**!

**Of a way of validating your services are secure and deployed in accordance with your companies governance rules and the Azure Architecture framework, both before and after the resources have been commissioned!**

Imagine no longer! There is a PowerShell module designed specifically for that purpose: **PSRule for Azure**.

PSRule is a suite of rules to validate resources and infrastructure as code (IaC) using PSRule, the Azure component is using the base PSRule module.

Features of PSRule for Azure include:

* Leverage over 200 pre-built rules across five (5) WAF pillars:
  * Cost Optimization


  * Operational Excellence


  * Performance Efficiency


  * Reliability


  * Security


* Validate resources and infrastructure code pre or post-deployment using Azure DevOps or Github!
* Runs on macOS, Linux, and Windows.

With over 200 inbuilt rules _(and you can add your own),_ there is a lot of resource types covered such as _(but not limited to)_:

* Azure App Service
* Azure Key vault
* Azure Virtual Machine
* Azure Storage
* Azure Network
* Azure Public IP

Azure PSRules has been in development since 2019 and is under constant updates and fixes.

PSRule for Azure provides two methods for analyzing Azure resources:

* [Pre-flight ]()- Before resources are deployed from Azure Resource Manager templates.
* In-flight - After resources are deployed to an Azure subscription.

Pre-flight validation is used to scan ARM (Azure Resource Manager) templates before services are deployed and allow for quality gaps and better information in pull requests to improve and implement your infrastructure as code components.

The in-flight method can also be used in Azure DevOps for validation of Terraform resource deployments etc, but in this demo - I am going to run you through installing the Module and doing an export and scan from your PowerShell console!

If you are interested in the CI (Continous Integration) options, check out the links below:

* [Azure DevOps Pipeline & Github Actions](https://microsoft.github.io/PSRule/ "PSRule")

We are going to install the PSRule.Azure _(based on the Well-Architected Framework & Cloud Adoption Framework)_.

I recommend keeping the Modules _(and as such the in-built rules)_ up-to-date and do scans at least every quarter or after a major deployment or project to help verify your resources are set up according to some best-practice rules, this does not replace Security Center and Azure Advisor, this is intended to be of a supplement.

### Install PSRule.Azure & PSRule.Rules.CAF

1. Open **PowerShell** console and **run** the following **commands**:

       #The main Module and base rules to validate Azure resources..
       Install-Module PSRule.Rules.Azure -Scope CurrentUser
2. Press '**Y**' to **accept PSGallery** as a trusted repository, just a note you can prevent the confirmation prompt when installing Modules from the PSGallery, by classifying it as a 'Trusted Repository' by running the following, just be wary that won't get challenged again:

       Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
3. You should now have the following modules installed:

* PSRule
* PSRule.Rules.Azure

### Extract Azure Subscription PSRule JSON files

Now that PSRule has been installed, it's time to log in to Azure and extract information regarding your Azure resources for analysis, these extracted files are JSON files and do contain information, such as your resource names, subscription ID, resource groups in plain text.

As you can see from the screenshot below, we can target specific Subscriptions, Tenancies _(yes as long as the account you have access to, has access to the subscription you can export those as well)_, Resource Groups and Tags.

![](/uploads/powershellise_exportazruledata.png)

Because I want to get the most data available across all resources, I am going to Target everything with the '-All' parameter. 

1. First, we need to connect to the Azure subscription and then **connect** to the **Azure** subscription we have access to or are targeting by running the following:

       Connect-AzAccount

       Get-AzSubscription  | ogv -PassThru | Set-AzContext
2. Now that you have connected its time to export the Azure resource information, **run** the following **PowerShell** cmdlet, and **point** it towards an **empty folder**:

       Export-AzRuleData -OutputPath c:\temp\AzRuleData -All
3. If the **folder doesn't** **exist**, _don't worry_ - the Export command will **create** it **for you**, depending on how many resources and subscriptions you are extracting, this may take a few minutes. 

You should **see** the **JSON files** appearing if you open one of these, you should be able to see information about the resources it has extracted.

### Run PSRule across your JSON files

Now that you have extracted the JSON files of your Azure resources, it's now time to analyse them in accordance with Microsoft Cloud Adoption and Well Architectured framework and the rules builtin into PSRule.Azure!

You don't need to be connected to Azure, for this analysis, just have the PSRule modules installed and can access the JSON files.

PSRule.Azure has a few [baselines](https://azure.github.io/PSRule.Rules.Azure/en/baselines/Azure.All/ " PSRule for Azure - All Baselines"), these baselines contain the rules used to analyse your resources and range from Preview to newly released rules, again, we are just going to target ALL rules, as we are after any and all recommendations.

1. In **PowerShell run** the following:

       Invoke-PSRule -Module 'PSRule.Rules.Azure' -InputPath 'C:\temp\AzRuleDataExport\*.json' -Baseline 'Azure.All'
2. This will trigger, **PSRules** to **scan** your **extracted JSON** files, with the **ALL** rules, and you will get **output** like below:
3. ![](/uploads/windowsterminal_data_psrules-azure.png)
4. Although it is good being able to see a high level, I prefer to look at it all at once in Excel, so run the following to **export** the rules to a **CSV**:

       Invoke-PSRule -Module 'PSRule.Rules.Azure' -InputPath 'C:\temp\AzRuleDataExport\*.json' -Baseline 'Azure.All' | Export-csv C:\temp\AzRuleDataExport\Exported_Data.csv
5. You should now have a CSV file that you can then review and look for common issues, concerns and work on improving your Azure infrastructure setup!

![](/uploads/export_azruledata_excel.png)

_Note: The export, contains the Subscription/Resource Names so you can definitely see what resources can improve upon, however, I removed it from my screenshot._

**Congratulations**! You now have more visibility and hopefully, some useful recommendations for improving your Azure deployment, remember PSRules.Azure is just a supplement to already existing toolsets! 

### Additional Resources

If you found PSRules.Azure interesting, how about getting any Failed rules, how about getting any failed rules pushed to Azure Monitor? 

* [PSRule to Azure Monitor](https://github.com/microsoft/PSRule.Monitor "PSRule to Azure Monitor")

How about running it through a release using Azure DevOps?

* [PSRule extension for Azure Pipelines](https://github.com/microsoft/PSRule-pipelines "PSRule extension for Azure Pipelines")

Extend the PSRules to include Cloud Adoption Framework as well?

* [PSRule for Cloud Adoption Framework](https://github.com/microsoft/PSRule.Rules.CAF "PSRule for Cloud Adoption Framework")

And finally, creating Custom Rules for your organisation, including Tagging, Naming conventions etc?

* [PSRule.Azure Custom Rules](https://azure.github.io/PSRule.Rules.Azure/customization/ "Organization specific rules")