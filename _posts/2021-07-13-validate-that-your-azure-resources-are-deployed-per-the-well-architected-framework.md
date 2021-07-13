---
date: 2021-07-13T00:00:00.000+12:00
title: Well-Architected Framework Azure infrastructure review with PSRule for Azure
permalink: azure/WAF-Azure-infrastructure-review-with-PSRule-for-Azure/

author: Luke
categories:
- Azure
- PowerShell
toc: true
header:
  teaser: "/uploads/windowsterminal_data_psrules-azure.png"

---
Imagine that you could validateyour Azure Resources are deployed per the Well-Architected Framework (WAF).. just **imagine**!

**Of a way of validating your services are secure and deployed following the Azure Architecture framework, both before and after the resources have been created!**

Imagine no longer! There is a PowerShell module designed specifically for that purpose: **PSRule for Azure**.

PSRule is a suite of rules to validate resources and infrastructure as code _(IaC)_ using PSRule, and the Azure component uses the base PSRule module.

Features of [PSRule for Azure](https://azure.github.io/PSRule.Rules.Azure/ "PSRule for Azure"){:target="_blank"}
 include:

* Leverage over 200 pre-built rules across five WAF pillars:
  * Cost Optimization
  * Operational Excellence
  * Performance Efficiency
  * Reliability
  * Security
* Validate resources and infrastructure code pre or post-deployment using Azure DevOps or Github!
* It runs on macOS, Linux, and Windows.

With over 200 inbuilt rules _(and you can add your own),_ there is a lot of resource types covered, such as _(but not limited to)_:

* Azure App Service
* Azure Key vault
* Azure Virtual Machine
* Azure Storage
* Azure Network
* Azure Public IP

Azure PSRules has been in development since 2019 and is under constant updates and fixes.

PSRule for Azure provides two methods for analyzing Azure resources:

* Pre-flight - Before resources are deployed from Azure Resource Manager templates.
* In-flight - After resources are deployed to an Azure subscription.

Pre-flight validation is used to scan ARM (Azure Resource Manager) templates before services are deployed and allow for quality gaps and better information in pull requests to improve and implement your infrastructure as code components.

The in-flight method can also be used in Azure DevOps for validation of Terraform resource deployments etc. Still, in this demo, I will run you through installing the Module and doing an export and scan from your PowerShell console!

We are going to install the PSRule.Azure _(based on the Well-Architected Framework & Cloud Adoption Framework)_.

I recommend keeping the Modules _(and as such the in-built rules)_ up-to-date and do scans at least every quarter or after a major deployment or project to help verify your resources are set up according to some best-practice rules. This does not replace Security Center and Azure Advisor; this is intended to be a supplement.

### Install PSRule.Azure & PSRule.Rules.CAF

1. Open **PowerShell** console and **run** the following **commands**:

       #The main Module and base rules to validate Azure resources..
       Install-Module PSRule.Rules.Azure -Scope CurrentUser
2. Press '**Y**' to **accept PSGallery** as a trusted repository; just a note, you can prevent the confirmation prompt when installing Modules from the PSGallery, by classifying it as a 'Trusted Repository' by running the following. Just be wary that won't get rechallenged:

       Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
3. You should now have the following modules installed:

* PSRule
* PSRule.Rules.Azure

### Extract Azure Subscription PSRule JSON files

Now that PSRule has been installed, it's time to log in to Azure and extract information regarding your Azure resources for analysis; these extracted files are JSON files containing information, such as your resource names, subscription ID, etc. resource groups in plain text.

As you can see from the screenshot below, we can target specific Subscriptions, Tenancies _(yes, as long as the account you have access to has access to the subscription, you can export those as well)_, Resource Groups and Tags.

![Export-AzRuleData](/uploads/powershellise_exportazruledata.png "Export-AzRuleData")

Because I want to get the most data available across all resources, I will Target everything with the '-All' parameter.

1. First, we need to connect to the Azure subscription and then **connect** to the **Azure** subscription we have access to or are targeting by running the following:

       Connect-AzAccount
       
       Get-AzSubscription  | ogv -PassThru | Set-AzContext
2. Now that you have connected its time to export the Azure resource information, **run** the following **PowerShell** cmdlet, and **point** it towards an **empty folder**:

       Export-AzRuleData -OutputPath c:\temp\AzRuleData -All
3. If the **folder doesn't** **exist**, _don't worry_ - the Export command will **create** it **for you**. Depending on how many resources and subscriptions you are extracting, this may take a few minutes.

You should **see** the **JSON files** appearing if you open one of these. In addition, you should be able to see information about the resources it has extracted.

### Run PSRule across your JSON files

Now that you have extracted the JSON files of your Azure resources, it's now time to analyse them following Microsoft Cloud Adoption and Well Architectured framework and the rules builtin into PSRule.Azure!

You don't need to be connected to Azure; for this analysis, have the PSRule modules installed and access the JSON files.

PSRule.Azure has a few [baselines](https://azure.github.io/PSRule.Rules.Azure/en/baselines/Azure.All/ " PSRule for Azure - All Baselines"){:target="_blank"}; these baselines contain the rules used to analyse your resources and range from Preview to newly released rules; again, we will target ALL rules, as we are after all recommendations.

1. In **PowerShell, run** the following:

       Invoke-PSRule -Module 'PSRule.Rules.Azure' -InputPath 'C:\temp\AzRuleDataExport\*.json' -Baseline 'Azure.All'
2. This will trigger **PSRules** to **scan** your **extracted JSON** files with the **ALL** rules, and you will get **output** like below:
3. ![Invoke-PSRules](/uploads/windowsterminal_data_psrules-azure.png "Invoke-PSRules")
4. Although it is good being able to see a high level, I prefer to look at it all at once in Excel, so run the following to **export** the rules to a **CSV**:

       Invoke-PSRule -Module 'PSRule.Rules.Azure' -InputPath 'C:\temp\AzRuleDataExport\*.json' -Baseline 'Azure.All' | Export-csv C:\temp\AzRuleDataExport\Exported_Data.csv
5. You should now have a CSV file to review and look for common issues, concerns and work on improving your Azure infrastructure setup!

![PS Rules Azure - Export CSV](/uploads/export_azruledata_excel.png "PS Rules Azure - Export CSV"){:target="_blank"}

_Note: The export contains the Subscription/Resource Names, so you can definitely see what resources can improve upon; however, I removed it from my screenshot._

**Congratulations**! You now have more visibility and, hopefully, some useful recommendations for improving your Azure services!

_If you want to get a good understanding of the type of data rules, check out my extracted CSV '_[_here_](http://luke.geek.nz/uploads/files/Exported_Data_PSRuleAzure.csv){:target="_blank"}_'._

### Additional Resources

* If you found PSRules.Azure interesting; how about getting any Failed rules? How about getting any failed rules pushed to Azure Monitor?

[PSRule to Azure Monitor](https://github.com/microsoft/PSRule.Monitor "PSRule to Azure Monitor"){:target="_blank"}

* If you are interested in the CI (Continous Integration) options, check out the links below:

[Azure DevOps Pipeline & Github Actions](https://microsoft.github.io/PSRule/ "PSRule"){:target="_blank"}

* Extend the PSRules to include Cloud Adoption Framework as well?

[PSRule for Cloud Adoption Framework](https://github.com/microsoft/PSRule.Rules.CAF "PSRule for Cloud Adoption Framework"){:target="_blank"}

* And finally, creating Custom Rules for your organisation, including Tagging, Naming conventions etc.?

[PSRule.Azure Custom Rules](https://azure.github.io/PSRule.Rules.Azure/customization/ "Organization specific rules"){:target="_blank"}