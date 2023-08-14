---
title: Coding on the Cloud: Getting Started with GitHub Codespaces
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/Header_Getting_Started_with_GitHub_Codespace.gif
date: '2023-08-13 00:00:00 +1300'
---

[Github Codespaces](https://github.com/features/codespaces) gives you the full capability of your favourite IDE (Integrated Development Environment) like Visual Studio Code, Jupyter, or JetBrains and extension, to your web browser, and with it you can develop your applications without needing any dependant service or tool installed or configured locally, giving developers a standard way of working on applications and scripts.

![Github Codespaces - Getting Started](/images/posts/Header_Getting_Started_with_GitHub_Codespace.gif)

Github Codespaces does this, by leveraging the power of the Cloud and GitHub, to run containers, that you can personalize to run your IDE, extensions, and any dependencies that you may need, whether you are a developer needing python, apache, react or a devops engineer requiring Bicep and Terraform support, Codespaces is an ideal enabler for our toolkit, in fact this article was written in a Github Codespace, using Visual Studio Code and Markdown extensions.

> A codespace is a development environment that's hosted in the cloud. You can customize your project for GitHub Codespaces by configuring dev container files to your repository (often known as Configuration-as-Code), which creates a repeatable codespace configuration for all users of your project.
> GitHub Codespaces run on a variety of VM-based compute options hosted by GitHub.com, which you can configure from 2 core machines up to 32 core machines. You can connect to your codespaces from the browser or locally using an IDE like Visual Studio Code or IntelliJ.

Let's delve into [Github Codespaces](https://github.com/features/codespaces) a bit more!

#### Introduction

GitHub Codespaces is a cloud-based development environment provided by GitHub, designed to enhance the coding experience and streamline collaboration for developers. It allows you to create, manage, and access your development environments directly from your web browser. With GitHub Codespaces, you can code, build, test, and debug your projects without the need to set up complex local development environments on your machine.

![Github Codespaces](/images/posts/github_codespaces.png)

Key features and benefits of GitHub Codespaces include:

* Access Anywhere: You can access your coding environment from anywhere with an internet connection. This is particularly useful for remote work, collaboration, and coding on the go.
* Consistency: Codespaces ensures consistency across development environments, which can help avoid the "it works on my machine" issue often encountered in software development.
* Collaboration: Multiple developers can collaborate on the same Codespace simultaneously, making it easier to pair program, review code, and troubleshoot together in real time.
* Isolation: Each project or repository can have its own isolated Codespace, preventing conflicts between dependencies and configurations.
* Quick Setup: Setting up a development environment is quick and easy. You don't need to spend time installing and configuring software locally.
* Configurability: Codespaces can be customized with extensions, tools, and settings to match your preferred development environment.
* Scalability: GitHub Codespaces can scale according to your needs, making it suitable for both individual developers and larger teams.
* Version Control Integration: Codespaces is tightly integrated with GitHub repositories, making it seamless to switch between your code and the development environment.
* Security: Codespaces offer a secure environment for development, as it doesn't store any sensitive data and is protected by GitHub's security measures.
* Project Setup: Codespaces can be configured to automatically set up a project with required dependencies and tools, reducing the time needed to get started.

Github Codespaces, went into [general availability](https://azure.microsoft.com/updates/general-availability-github-codespaces/?WT.mc_id=AZ-MVP-5004796) on August 2021.

#### Prerequisites

To use Github Codespaces, you need a [Github](https://github.com/) account.

GitHub Codespaces is available for developers in every organization, however organizations can choose whether codespaces created from their repositories will be user-owned or organization-owned.. All personal GitHub.com accounts include a monthly quota of free usage each month.

GitHub will provide **users in the Free plan 120 core hours, or 60 hours of run time on a 2 core codespace, plus 15 GB of storage each month**.

For further information on pricing, make sure you review:

* [About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)
* [Pricing calculator](https://github.com/pricing/calculator)

> Pricing, features and offerings could change at any time. For the most up to date information make sure you review the documentation on github.com.

To use Github Codespaces, you need an active repository, by default Github Codespaces is configured for the repository you set.

You will also need a [supported browser](https://docs.github.com/en/get-started/using-github/supported-browsers) (the latest versions of Chrome, Edge, Firefox, or Safari are recommended) view your IDE, in this article, we will be using Visual Studio Code.

#### Setting Up GitHub Codespaces

Github Codespaces, can be accessed directly from the GitHub interface.

1. **Navigate** to a new **repository**
2. Click **Code**
3. Click **+** in the Codespaces tab to open a new **Codespace** on your repo, by default a Visual Studio Code instance will open in your browser, note the 'funky' name and URL thats create to give you a unique container.

_Note: Don't worry, nothing is saved to your repository unless you want to commit any changes._

Your Codespace is now started, and running in a default GitHub supplied development container.

> A development container is a running Docker container with a well-defined tool/runtime stack and its prerequisites.

![Github Codespaces - Run](/images/posts/OpenCodespace.gif)

#### Exploring the Interface

Once you have your Codespace running, you have access to most native [Visual Studio Code](https://code.visualstudio.com/) capability's and all the files in your repository.

![Github Codespaces - Overview](/images/posts/Codespaces_VSCode_Overview.png)

We now have our workspace, consisting of Visual Studio code, running in your own docker container! The Host field _(lower left)_ indicates that you are running in a Codespace.

Out of the box, Visual Studio code has git integration, so you can easily commit any changes to the repository as you would, if you were working from your local development workstation - this is critical to remember, when making a change to your devcontainer configuration - you have to commit it, before you can rebuild or you will lose your configuration (we will get to this further in the article).

As its running in a hosted container, you can switch easily between computers and browsers, by opening the Codespace (the same way you created your Codespace, but instead selecting an already running instance), or copy the URL of your Codespace, and log back into Github on another computer to go directly to the container instance:

![Github Codespaces - Run](/images/posts/Github_Codespaces_OpenRunning.png)

If you leave your Codespace running without interaction, or if you exit your codespace without explicitly stopping it, the codespace will timeout after a period of inactivity and stop running. You can [adjust the timeout](https://docs.github.com/en/codespaces/customizing-your-codespace/setting-your-timeout-period-for-github-codespaces) of your codespace to a maximum of 240 minutes (4 hours) for new Codespaces, but keep in mind ou will be charged, unless the Codespace is stopped.

> Warning: Codespaces compute usage is billed for the duration for which a codespace is active. If you're not using a codespace but it remains running, and hasn't yet timed out, you are billed for the total time that the codespace was active, irrespective of whether you were using it. For more information, see "[About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing)."

As with any Visual Studio Code instance, you can also login to your Github account, to pull your settings and extensions, but to keep things clean, distraction free, you can customize your Codespace instead, for only what you or others working in the same repository need.

#### Customizing Your Codespace

You can customize your Codespace, to suit the project you are working on, some examples I use personally are:

* Markdown editing _(for example, my website is hosted on Github Pages, and the formatting is done using Markdown, so I have a devcontainer preconfigured to run Markdown Visual Studio Code extensions and linting, so as soon as I open it - its good to go!)_
* Infrastructure as Code development _(I have preconfigured devcontainer, running on a container, that has the latest version of PowerShell, Terraform, Bicep installed and relevant Visual Studio extensions)_

I am someone who use to install everything locally, to the point when I would be reinstalling Windows every few months. to keep my device clean, I had moved to an Azure Virtual Desktop host as my development environment, but Codespaces now give me the flexibility to install what I need (when I need it) within an Linux environment, and I know when I rebuild the Codespace, I will have the latest libraries.

There are a lot of customisation you can do, we won't be able to cover all possible customisations tn this article, but I aim to cover the basics to get you up and running!

##### DevContainers

sd

Explain how to personalize the Codespace environment:
Describe how to add extensions for enhanced functionality.
Show how to modify settings to align with individual preferences.
Working with Files and Code:

#### Detail common tasks within Codespaces

Cover opening, editing, creating, and deleting files.
Provide tips on utilizing shortcuts and editor features.

#### Integrating Version Control

Emphasize the integration with Git and version control:
Guide readers on how to commit, push, and pull changes within Codespaces.
Explain how to switch branches and handle merge conflicts.

#### Collaboration and Real-time Editing

Illustrate how Codespaces facilitates collaboration:
Explain the process of inviting collaborators to your Codespace.
Show how simultaneous real-time editing works.

#### Building and Running Code

Walk users through building and executing code within Codespaces:
Explain how to use the integrated terminal to run commands and scripts.
Provide guidance on debugging and error handling.

#### Data Persistence and Storage

Discuss how data is persisted in Codespaces:
Clarify whether data is retained between sessions.
Explain how to manage data storage and potential limitations.

#### Tips for Efficient Usage

Offer practical tips to optimize the Codespaces experience:
Suggest keyboard shortcuts for common actions.
Provide insights on managing multiple Codespaces.
.Codespaces

#### Ending and Additional Resources

Recap the main points covered in the article.
Offer links to official documentation, tutorials, and community resources.
Encourage readers to experiment, explore further, and provide feedback.

#### Troubleshooting and FAQs (Optional)

Include a section addressing common issues or questions readers might encounter.
Provide solutions or links to resources for resolving problems.

#### Conclusion

Summarize the key takeaways from the article.
Highlight the convenience and benefits of using GitHub Codespaces for development
