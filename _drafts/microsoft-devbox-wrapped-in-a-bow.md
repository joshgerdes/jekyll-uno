---
date: 2022-12-15 00:00:00 +1300
title: Microsoft Dev Box wrapped in a bow
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/festivetechcalendar2022.png"

---
**![Festive Tech Calender - Microsoft Dev Box](/uploads/festivetechcalendar2022.png "Festive Tech Calender - Microsoft Dev Box")**

It's that time of year again! The time to be jolly and experience the Month of December, by looking at the [Festive Tech Calendar](https://festivetechcalendar.com/ "Festive Tech Calender")!

> This year the Festive Tech Calendar Team is **raising money** for the charity [@missingpeople](https://www.missingpeople.org.uk/).
>
> We believe its important to support charities that do great work. Without fundraising Missing People wouldn’t be able to find vulnerable missing people and reunite families.
>
> #### If you would like to donate please visit our [Just Giving Page](https://www.justgiving.com/fundraising/festivetechcalendar2022).

Today, we are going to unwrap our present and take a peek inside the box - at Microsoft Dev Box!

#### Overview

[Microsoft Dev Box](https://azure.microsoft.com/products/dev-box/?WT.mc_id=AZ-MVP-5004796#overview "Microsoft Dev Box") provides self-service access for developers to high-performance, cloud-based workstations preconfigured and ready-to-code for specific projects—all while maintaining security and corporate governance. With Microsoft Dev Box, organizations can:

* Maximize dev productivity with ready-to-code, self-service Dev Boxes.
* Centralize governance of workstations running anywhere to maintain greater security, compliance, and cost efficiency.
* Customize dev boxes with everything developers need for their current projects.

Microsoft Dev Box supports any developer IDE, SDK, or tool that runs on Windows. Developers can target any development workload that can be built from Windows including desktop, mobile, IoT, and web applications. Microsoft Dev Box even supports building cross-platform apps thanks to Windows Subsystem for Linux and Windows Subsystem for Android. Remote access gives developers the flexibility to securely access dev boxes from any device, whether it’s Windows, macOS, Android, iOS, or a web browser.

![High-level Azure Devbox workflow](/uploads/hl-devbox_workflow.png "High-level Devbox workflow")

Essentially, [Microsoft Dev Box](https://learn.microsoft.com/azure/dev-box/?WT.mc_id=AZ-MVP-5004796 "Microsoft Dev Box documentation") is a managed service that enables developers to create on-demand, high-performance, secure, ready-to-code, project-specific workstations in the cloud.

Microsoft Dev Box is available today as a [preview ](https://azure.microsoft.com/en-us/updates/public-preview-microsoft-dev-box/?WT.mc_id=AZ-MVP-5004796 "Public preview: Microsoft Dev Box")from the Azure Portal. During this period, organizations get the first 15 hours of the dev box 8vCPU and 32 GB Memory SKU for free every month, along with the first 365 hours of the dev box Storage SSD 512 GB SKU.

Beyond that, organizations pay only for what they use with a consumption-based pricing model. With this model, organizations are charged on a per-hour basis depending on the number of Compute and Storage that are consumed.

To use Microsoft Dev Box, each user must be licensed for Windows 11 or 10 Enterprise, Microsoft Endpoint Manager, and Azure Active Directory P1. These licenses are included in M365 F3, E3, E5, A3, A5, and Microsoft Business Premium and Microsoft 365 Education benefit plans.

![Microsoft Dev Box](/uploads/microsoft_devbox_selfservicedevelopment.png "Microsoft Dev Box")

> _Disclaimer: At the time of writing, this service is still in Public Preview, some services and license requirements may change by the time this becomes generally avaliable._

So where does Microsoft Dev Box fit in?

Microsoft offers a plethora of services, from [Azure Virtual Desktop](https://azure.microsoft.com/products/virtual-desktop/?WT.mc_id=AZ-MVP-5004796 "Azure Virtual Desktop"), [Windows 365](https://www.microsoft.com/en-us/windows-365?WT.mc_id=AZ-MVP-5004796 "Windows 365 Cloud PC"), and now [Microsoft Dev Box](https://azure.microsoft.com/products/dev-box/?WT.mc_id=AZ-MVP-5004796#overview "Microsoft Dev Box") - where would you use Microsoft Dev Box over another service, such as Windows 365?

General scenarios at a high level are:

| Scenario | Product |
| --- | --- |
| Production multi-session, supporting Windows Server and Client OS, Published Aps | Azure Virtual Desktop |
| Production dedicated personal PCs, for shift/party time users - or small environments | Windows 365 |
| Dev/Test Ondemand Windows machines for Testing and development with custom image support | Azure Dev Box |

![Microsot Windows Experiances Strategy](/uploads/ms_microsoftwindowsexperiances_strategy.png "Microsoft Windows Experiances Strategy")

Microsoft Dev box can help project and development teams get up and running quickly, independent of what hardware a developer or contractor has, whether they prefer Mac, Windows, or Linux - the Microsoft Dev box can be used to get developers and contractors up and running in a secure environment that supports Intune!

##### Concepts & Roles

| Concepts | Notes |
| --- | --- |
| Dev center | A dev center is a collection of projects that require similar settings. Dev centers enable dev infrastructure managers to manage the images and SKUs available to the projects using dev box definitions and configure the networks the development teams consume using network connections. |
| Projects | A project is the point of access for the development team members. When you associate a project with a dev center, all the settings at the dev center level will be applied to the project automatically. Each project can be associated with only one dev center. |
| Dev box definition | A dev box definition specifies a source image and size, including compute size and storage size. You can use a source image from the marketplace, or a custom image. |
| Network connection | Network connections store configuration information like Active Directory join type and virtual network that dev boxes use to connect to network resources. |
| Dev box pool | A dev box pool is a collection of dev boxes that you manage together and to which you apply similar settings. |
| Dev box | A dev box is a preconfigured ready-to-code workstation that you create through the self-service developer portal. The new dev box has all the tools, binaries, and configuration required for a dev box user to be productive immediately |

![DevBoxHierarchy](/uploads/festivetechcalendar2022_devboxhierarchy.png "DevBoxHierarchy")

The following are common, Azure Dev Box roles.

| Role | Responsibilities | Permissions |
| --- | --- | --- |
| Dev Infra Admins | Providing developer infrastructure and tools to the development teas | Can create and manage dev centers, can create projects and define images that are used to create the dev boxes |
| Project Admins | Does administrative tasks for the Dev Box solution and assist with day to day tasks. | Can create and manage dev box pools across different regions |
| Dev Box Users | Members of your development teams | Can self-service and create one or more dev boxes, depending on the projects assigned. |

#### Deployment

##### Create Dev Center

First, we need to create our [Dev Center](https://learn.microsoft.com/azure/dev-box/concept-dev-box-concepts?WT.mc_id=AZ-MVP-5004796#dev-center "Microsoft Dev Box Preview key concepts"). A Dev Center, allows us to centrally manage our developer environments and enable development teams with self-service capability. Dev Center is used by more than just Microsoft DevBox - an example is [Azure Deployment Environments](https://azure.microsoft.com/products/deployment-environments/?WT.mc_id=AZ-MVP-5004796#overview "Azure Deployment Environments") - which allows devs to spin up templated _(ARM)_ application infrastructure quickly - but we will just be focussing on components of Dev Center - used by Microsoft Dev Box.

> Please confirm what [region](https://azure.microsoft.com/products/dev-box/?WT.mc_id=AZ-MVP-5004796#faq "Frequently asked questions about Microsoft Dev Box") you can deploy Dev Box. As this is in Public Preview at the time of writing - only certain regions are supported.

In your favorite browser, let us create a standard Dev Box environment - starting with the Dev Center...

1. Log in to the Microsoft [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
2. Click **+ Create a resource**
3. Search for: Dev center, select your Dev center, and click **Create**
4. ![Microsoft Azure Portal - Dev center](/uploads/azuredevbox-createdevcentermarketplace.png "Microsoft Azure Portal - Dev center")
5. Select the **Subscription** and **ResourceGroup** you want to deploy your Dev Center into, you can use this opportunity to create a new Resource Group.
6. Type in the **name** of your **DevCenter **_(in my example, it is named DevCenter-Devs)_
7. Then select the **location** _(region)_, in which you want to deploy your DevCenter into.
8. ![Azure Portal - Create a dev center](/uploads/azuredevbox-createdevcenterbasicspage.png "Azure Portal - Create a dev center")
9. Click **Review + Create,** then **Create**

_Deployment of the Microsoft Dev Center will take a few minutes._

##### \[Optional\] - Create Virtual Network

In order to use Microsoft Dev Boxes - like any Virtual Machine in Azure, you need a Virtual Network! The Dev Boxes can connect to already existing Virtual Networks, which could be peered with other VNETs, have connectivity to on-premises - or have standalone connectivity! In my demo, I don't currently have a Virtual Network - so I will create a Virtual Network from scratch.

1. Log in to the Microsoft [**Azure Portal**](https://portal.azure.com/#home "Microsoft Azure Portal")
2. Click **+ Create a resource**
3. Search for: **Virtual Network**
4. **Create** a **Virtual Network** 
5. **Select** your Virtual Network **name** and **region** _(make sure the region aligns to your workloads and Azure DevCenter location)_
6. ![Azure Portal - Create VNET](/uploads/azuredevbox-createvnetbasicspage.png "Azure Portal - Create VNET")
7. Click **Next: IP Addresses**
8. 