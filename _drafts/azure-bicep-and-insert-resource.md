---
date: 2021-12-29 00:00:00 +1300
title: Azure Bicep and Insert Resource
author: Luke
categories:
- Azure
toc: false
header:
  teaser: ''

---
Azure Bicep is a Domain Specific Language (DSL) for deploying Azure resources declaratively. Azure Bicep is a **transparent abstraction** over ARM and ARM templates, which means anything that can be done in an ARM Template can be done in Bicep.

Azure Bicep has recently _(December 2021)_ been updated to: v0.4.1124, along with various other hotfixes and enhancements, this version supports ‘Insert Resource’ functionality.

Insert Resource simplifies ARM to Bicep conversion without having to export entire ARM templates then compile them to Bicep when you are only after export for a single resource.

In order to use Insert Resource, you will need to have:

* Bicep version greater than v0.4.1124
* Visual Studio Code with the Bicep extension

You can easily install both or upgrade following the Microsoft documentation on the: [Install Bicep tools](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) page.

Let's import resources!

 1. Open a new file in **Visual Studio Code**
 2. Set the Language mode to **Bicep**
 3. ![Visual Studio Code - Bicep](/uploads/bicep.png "Visual Studio Code - Bicep")
 4. Now we need to **login** to **Azure**, in Visual Studio code click **View** and **Terminal**
 5. In the terminal type in: **az login**
 6. Login to Azure using the credentials that have read access to the resource you want to export.
 7. Once you are logged in type in: **az resource list**
 8. In the JSON output in the terminal, **copy** the **resource ID** _(inside the commas from the id value)_
 9. Now we need to **open** the **Command Palette**, press: CTRL+Shift+P on your keyboard _(or click on View, Command Palette)_
10. **Start typing** in **Bicep**, if you have the latest version **you should see: Bicep: Insert Resource**
11. ![Azure Bicep - Insert Resource](/uploads/bicepinsertresource.png "Azure Bicep - Insert Resource")
12. Enter in the resource ID you copied earlier
13. ![](/uploads/bicepinsertresourceenterresourceid.png)
14. All going well, Azure Bicep should have connected and exported your resource straight into Bicep!
15. ![](/uploads/bicepinsertedresource.png)