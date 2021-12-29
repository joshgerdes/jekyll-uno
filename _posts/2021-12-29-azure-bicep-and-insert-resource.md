---
date: 2021-12-29 00:00:00 +1300
title: Azure Bicep and Insert Resource
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/images/AzureBicepBanner.jpg"

---
Azure Bicep is a Domain Specific Language (DSL) for deploying Azure resources declaratively. Azure Bicep is a transparent abstraction over ARM and ARM templates, which means anything that can be done in an ARM Template can be done in Bicep.

Azure Bicep has recently _(December 2021)_ been updated to: v0.4.1124, along with various other hotfixes and enhancements; this version supports 'Insert Resource' functionality.

Insert Resource simplifies ARM to Bicep conversion without exporting entire ARM templates, then compiles them to Bicep when you are only after export for a single resource.

To use Insert Resource, you will need to have:

* Bicep version greater than v0.4.1124
* Azure CLI
* Visual Studio Code with the Bicep extension

You can easily install both or upgrade following the Microsoft documentation on the: [Install Bicep tools](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install){:target="_blank"} page.

#### Import Resources into Bicep using Azure CLI and Bicep

 1. Open a new file in **Visual Studio Code**
 2. Set the Language mode to **Bicep**
 3. ![Visual Studio Code - Bicep](/uploads/bicep.png "Visual Studio Code - Bicep")
 4. Now we need to **login** to **Azure**; in Visual Studio code, click **View** and **Terminal.**
 5. In the terminal, type in: **az login**
 6. Login to Azure using the credentials that have read access to the Resource you want to export.
 7. Once you are logged in, type in: **az resource list**
 8. In the JSON output in the terminal, **copy** the **resource ID** _(inside the commas from the id value)_
 9. Now we need to **open** the **Command Palette**, press: CTRL+Shift+P on your keyboard _(or click on View, Command Palette)_
10. **Start typing** in **Bicep**; if you have the latest version, **you should see: Bicep: Insert Resource.**
11. ![Azure Bicep - Insert Resource](/uploads/bicepinsertresource.png "Azure Bicep - Insert Resource")
12. Enter in the resource ID you copied earlier.
13. ![](/uploads/bicepinsertresourceenterresourceid.png)
14. Azure Bicep should have connected and exported your Resource straight into Bicep! As below, it had imported a Log Analytics workspace in my subscription straight into Bicep.
15. ![](/uploads/bicepinsertedresource.png)

#### To find the resource ID using the Azure Portal.

You can use the Azure CLI to find the Resource ID, but you can also use the Azure Portal by navigating to it below:

1. Log in to the **Azure Portal**
2. **Navigate** to the **Resource** you want to export to Bicep
3. On the **Overview** pane, click on **JSON view**

I had problems connecting to export an App Service and App Service plan, so for some resources with multiple dependencies, you may be better off exporting the ARM template from the resources/resource groups and decompiling that way, but the Insert Resource functionality is a very quick way to bring your resources into Bicep!