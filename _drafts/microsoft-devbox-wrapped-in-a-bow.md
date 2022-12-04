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

##### Concepts

| Concepts | Notes |
| --- | --- |
| Dev center | A dev center is a collection of projects that require similar settings. Dev centers enable dev infrastructure managers to manage the images and SKUs available to the projects using dev box definitions and configure the networks the development teams consume using network connections. |
| Projects | A project is the point of access for the development team members. When you associate a project with a dev center, all the settings at the dev center level will be applied to the project automatically. Each project can be associated with only one dev center. |
| Dev box definition | A dev box definition specifies a source image and size, including compute size and storage size. You can use a source image from the marketplace, or a custom image. |
| Network connection | Network connections store configuration information like Active Directory join type and virtual network that dev boxes use to connect to network resources. |
| Dev box pool | A dev box pool is a collection of dev boxes that you manage together and to which you apply similar settings. |
| Dev box | A dev box is a preconfigured ready-to-code workstation that you create through the self-service developer portal. The new dev box has all the tools, binaries, and configuration required for a dev box user to be productive immediately |

#### Deployment

sdsd