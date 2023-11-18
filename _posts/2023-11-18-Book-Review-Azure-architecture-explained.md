---
title: Book Review Azure Architecture Explained
author: Luke
categories:
  - Azure
  - Misc
toc: true
header:
  teaser: /images/posts/BlobHeading_Review_AzureArchitectureExplained.gif
date: 2023-11-18 00:00:00 +1300
---

Book review of [Azure Architecture Explained: A comprehensive guide to building effective cloud solutions](https://www.packtpub.com/product/azure-architecture-explained/9781837634811)

> Disclaimer: This is the first book review I have ever done, and this review is entirely my opinion and may not fully reflect the value you may or may not get from this book. Everyone will have their unique viewpoint and priorities of what they want out of a book, so please take my review as an opinionated view from my own viewpoint; I am, of course, happy to discuss different points of view and discussions on this page comments. We are all here to learn something!

Book synopsis:

> "Azure is a sophisticated technology that requires a detailed understanding to reap its full potential and employ its advanced features. This book provides you with a clear path to designing optimal cloud-based solutions in Azure by delving into the platform's intricacies.
> You’ll begin by understanding the effective and efficient security management and operation techniques in Azure to implement the appropriate configurations in Microsoft Entra ID. Next, you’ll explore how to modernize your applications for the cloud, examining the different computation and storage options, as well as using Azure data solutions to help migrate and monitor workloads. You’ll also learn how to build your solutions, including containers, networking components, security principles, governance, and advanced observability. With practical examples and step-by-step instructions, you can work on infrastructure-as-code to effectively deploy and manage resources in your environment."

![Azure Architecture Explained](/images/posts/Review_AzureArchitectureExplained_TitleBoat.jpg)

## Introduction

[Azure Architecture Explained](https://www.packtpub.com/product/azure-architecture-explained/9781837634811) is a Packtpub published (in September 2023) book written by the following authors:

* [David Rendón](https://www.linkedin.com/in/daverndn/)
* [Brett Hargreaves](https://www.linkedin.com/in/bretthargreaves/)

Forward by [Sarah Kong](https://www.linkedin.com/in/konger/)

> Although this book was given to me to review (for free, I have no formal relationship with either Packetpub, although I thank them for allowing me to review this book or the Authors, and I am reviewing this book from an entirely independent view), as someone who architects and builds Azure solutions, this is the type of book, I usually would read, based on the title and synopsis, so let us take under the cover...  

## Overview of Azure Architecture

The book's slogan is "A **comprehensive** guide to **building** effective cloud solutions".

> Architecting solutions in Azure is a **massive** subject, requiring knowledge about the details of specific services, knowledge and understanding of **Cloud adoption**, **well-architected frameworks**, **patterns and practices** and **interoperability** between different services and systems, if one were to use this slogan and book title, I would expect the book to cover across all these areas.

![Azure Architecture Book - Courtesy of Bing Image Creator](/images/posts/AzureBook_AzureArchitectureExplained_AIGenerated.jpg)

So let us look to see if the book meets these details...

### Cloud Adoption

The book includes a section on the Microsoft Cloud Adoption Framework, including links, diagrams and explanations of how the Cloud Adoption framework fits in - not only with Microsoft Azure (which is the focus of this book) but with other Clouds as well!

**What I liked about the representation of the [Cloud Adoption](https://learn.microsoft.com/azure/cloud-adoption-framework/?WT.mc_id=AZ-MVP-5004796) within this book was - it was enough for a beginner and intermediate in Cloud adoption, to get going - without the need for third-party resources (i.e. resources outside of this book), but for those after a bit more advanced information or detail - supplied the relevant internet links, to the relevant Microsoft Learn resources *(in short format, i.e. bit.ly - so easily can be copied from a hard covered paper book into your browser)*, so the authors didn't try to shove a lot of unnecessary detail into the book, but was to the point, as they started the journey into Cloud governance and covered the basics and knowledge at an intermediate level, without a lot of the detail, that you don't necessarily need as part of the book.**

### Well-Architected Framework

In terms of the Well-Architected framework, however, there needed to be more direct representation, which surprised me, as although the Cloud Adoption Framework guides the Cloud adoption journey, the Well-Architected Framework focuses more on helping you make informed decisions for building systems in These frameworks can work side by side - HOWEVER, having said that...

The Microsoft Well-Architected Framework consists of 5 pillars, these are:

* Performance Efficiency
* Reliability
* Security
* Cost Optimization
* Operational Excellence

Underneath these pillars are design principles, such as design for business requirements, design for resiliency, design for recovery, etc.

These design principles were woven throughout the implementation portions of the books and, although not directly called out in some areas, had high-level representation that you can subtly pick up.

**I believe, reading the [Cloud Adoption](https://learn.microsoft.com/azure/cloud-adoption-framework/?WT.mc_id=AZ-MVP-5004796) and [Well-Architected Frameworks](https://learn.microsoft.com/azure/well-architected/?WT.mc_id=AZ-MVP-5004796), directly on the Microsoft Learn website, can help supplement your understanding of this book, and some of the decisions made by the authors.**

### Patterns and practices

Let us look at a particular part of the book; my example is the 'Making the Most of the Infrastructure-as-Code for Azure' section.

When I talk about patterns and practices, I am thinking of 2 things:

1. Does a Pattern provide a prescribed solution to a problem?
2. Does a Practice provide an established method or way of working?

> "Infrastructure-as-code enables organizations to define and manage their infrastructure and application resources in a programmatic and automated manner. Developers and operations teams can use configuration files or scripts to describe their desired Azure infrastructure and deploy it consistently and reliably. This part will discuss how infrastructure-as-code in Azure empowers organizations to optimize their cloud infrastructure, increase productivity, and drive successful digital transformations."

This particular part included Chapters such as:

* Governance in Azure
* Building Solutions using Azure Bicep
* Using Azure Pipelines to Build your Infrastructure in Azure
* Continous integration and deployment using Azure DevOps
and Tips from the Field!

Instead of jumping straight into the build, the authors take the time to explain Azure governance by following the premise of a hypothetical company and that company challenges, and then working on the previous parts of the work, where the authors had done a very prescriptive *(great)* job of the management and creation of relevant Azure resources using the Azure Portal and explain the business challenges that Infrastructure as Code helps with, before jumping into the authoring, management and implementation of Azure Bicep for Infrastructure as Code.

**Patterns and practices, in my opinion, are where this build shone through and where the true value is are the Patterns and practices. Throughout this book, the authors explain the WHY and WHAT before presenting the HOW. It was straightforward to follow and build upon what was learnt and discovered from previous chapters.**

### Interoperability

Interoperability is always very hard to review - the definition of interoperability I am using is *"the ability of computer systems or software to exchange and make use of information."* Commonly, how *systems work together*. In the complex world we live in, systems being able to talk to other systems made by other third-party vendors and individuals can be key to successful business outcomes so that it can be a very technically driven area.

This is hard to review when discussing a book-related specifically to Azure architecture *(i.e., this is not a book about connecting Azure services to AWS, etc.)*.

![Azure Architecture Book - Courtesy of Bing Image Creator](/images/posts/AzureBook_AzureArchitectureExplained_AIGenerated_Interopability.jpg)

However, interoperability is a key area for a topic such as Entra ID, to which this book has entire chapters dedicated.

This book has all the problems that all books have! Information Technology changes so rapidly that there's a potential risk that the book you just purchased may be out of date.
For context, this book was published in September of 2023 *(22 Sept 2023)*, which would mean a lot of writing and work, then peer-review, assuming both from a technical standpoint and writing standpoint, after the authors initial 'pre-prod' draft, before it reaches the public. In mid-July of 2023 *(11 July 2023)* Microsoft announced a rename of Azure Active Directory to Entra ID. There was mention of the rename, but Azure AD was still used in certain areas of the book.

In the context of this book, Entra ID is referred to by its previous name, Azure Active Directory; as a reader who is aware of that rename, it was still incredibly easy to read and follow.

The book explains user identities, the differences between authentication and authorization *(Which I loved!)* and how Azure Active Directory *(i.e. Entrea ID)* can be used to integrate and secure applications and work alongside the rest of the Microsoft Entra ID suite of products, all within the context of a fictitious company, allowing you to follow on.

**Overall, I believe the interoperability portions of Identity in this book are first class, from the creation of your first tenancy to Role Based Access to Azure resources; the authors do a great job in explaining how identity underpins the platforms and enables connectivity and access to multiple services, that even a beginner can get going quickly, with knowing WHY they are doing the stuff, that the book asks of them!**

## Content and Coverage

When considering Content and Coverage, my main concern here is:

* Is the content in this book actually 'actionable'?
* Can I use what I learn in this book in real-world scenarios, or is it entirely hypothetical?

I am pleased to say **Yes** to this book; it is both actionable and useful in the real world! I was pleasantly surprised by this!

Architecture can be a very *dry* subject, and there are so many ways you can approach it, for example:

| Architect Type          | Focus Area                                                |
|-------------------------|----------------------------------------------------------|
| **System Architect**    | Design and structure of individual systems or applications. |
| **Enterprise Architect**| Aligning IT strategy with overall business strategy.       |
| **Solution Architect**  | Designing solutions that meet specific project requirements.|
| **Data Architect**      | Designing and managing an organization's data architecture.|
| **Application Architect**| Designing the structure and interaction of applications.  |
| **Network Architect**   | Designing and implementing computer networks.              |
| **Security Architect**  | Designing and implementing security measures and controls. |
| **Cloud Architect**     | Designing and implementing cloud infrastructure solutions.|
| **Infrastructure Architect**| Designing and managing IT infrastructure components.   |
| **Integration Architect**| Ensuring seamless integration between different systems.   |
| **Business Architect**  | Aligning business processes and IT strategy.              |

![Azure Architects - Courtesy of Bing Image Creator](/images/posts/AzureBook_AzureArchitectureExplained_AIGenerated_Architects.jpg)

**When I look at this book, I am looking at it from a mix of Cloud, Solution and Infrastructure architecture, mainly due to my own personal journey, and this is where I feel the book fits.**

When I look at the slogan of the book again, and the word **comprehensive** is used, I believe this is used accurately; the authors did a great book in discussing the WHY, WHAT and HOW of various solutions in the Networking section of this book, the authors covered design considerations for VNET *(Virtual Networks)*, before delving into more advanced topics, such as Network Security and Azure Virtual Virtual WAN, bringing you on the journey that you would take in real life.

## Clarity and Accessibility

**The authors did a very clear job of explaining, from start to finish, how to create the necessary Azure resources and why you should have created them in the first place. This was very well done. In just about all sections, the words were supplemented with images and diagrams, making it easier to further understand what was happening in the text. Any links to internet websites were done as short links, making it very easy to copy and navigate to, whether you have a physical copy of the book or a digital copy.**

## Hands-On Exercises and Tutorials

**This book contained valid hands-on exercises and tutorials, allowing you to follow along with the content.**

Sample code and exercise files were also provided publically on GitHub [PacktPublishing/Azure-Architecture-Explained](https://github.com/PacktPublishing/Azure-Architecture-Explained) and [daveRendon/azinsider](https://github.com/daveRendon/azinsider), allowing readers, to easily fork and get a copy of the code required for the relevant exercises, such as creating resources, such as an Azure Virtual Network with Bicep.

## Updates and Relevance

At the time of this review (November 2023), this book (published in September 2023) is still entirely relevant; as mentioned earlier, there have been some renames of products from Microsoft that are a 'gotcha' to know, as part of reading this book, but the theory and implementation steps are entirely relevant.

I came across one link to a website [cafbaseline.com](https://cafbaseline.com/) that was not available at the time of reading, but all other links I used were relevant and working!

**As with all books, if you come across this book 2-3 years down the track *(i.e. 2025/2026)* make sure you check the publishing date and version and make sure there's not a renewer version of this book! This is a book I personally would love to see various revisions and updates to as the world of Microsoft Azure changes!**

## Author's Expertise

I believe the authors have the correct expertise to make this book viable *(and based on my own knowledge, reading this book)* and accurate.

* [David Rendón](https://www.linkedin.com/in/daverndn/) is a Microsoft MVP (Most Valuable Professional) and MCT (Microsoft Certified Trainer); these awards themselves require technical validation, and the display of knowledge to help solve organisation problems, and as an MCT, David, has the experience to explain the concepts, in a way that could be easily understood as a beginner.
* [Brett Hargreaves](https://www.linkedin.com/in/bretthargreaves/) as a current Cloud Practice Lead, with certifications, such as the Azure Solutions Architect Expert and a background in Architect, Brett has the practical know-how to help make this content relevant, to those looking to Architect solutions in Microsoft Azure.

**It is my opinion that this duo is indeed suited to write this type of book, and this can be seen from the actionable and valid output of the book itself.**

## Conclusion

**Azure Architecture Explained is a book containing 409 pages of actionable content.**

The authors draw on their extensive experience and research to provide practical patterns and practices, to help build on the story of starting from scratch, understanding the *big picture* of how complex systems within the Azure ecosystem sit together, with the advice actually to get started and create and modify those resources.

The book is well-structured and full of relevant examples and exercises.

> **I highly recommend this book to anyone interested in architecting solutions across Microsoft Azure, and it was very easy to read and consume the content! I feel smarter, having read it. Thank you to the authors for making the effort to write and release this book. It is a good addition to my library of books that I will be referencing in the future! I read this book on a Cruise while relaxing, and it didn't feel like I was doing work!**
