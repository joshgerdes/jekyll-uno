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

Github Codespaces, went into [general availability](https://azure.microsoft.com/updates/general-availability-github-codespaces/?WT.mc_id=AZ-MVP-5004796) on August 2021 and is built ontop of the [devcontainers](https://containers.dev/) schema.

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

If you leave your Codespace running without interaction, or if you exit your codespace without explicitly stopping it, the codespace will timeout after a period of inactivity and stop running. You can [adjust the timeout](https://docs.github.com/en/codespaces/customizing-your-codespace/setting-your-timeout-period-for-github-codespaces) of your codespace to a maximum of 240 minutes (4 hours) for new Codespaces, but keep in mind ou will be charged, unless the Codespace is stopped. If the Codespace remains inactive for a period of time, it could be deleted. You should get an email notification before this happens, but I suggust keeping an eye on your Codespace and make sure its only running when you need it.

> Warning: Codespaces compute usage is billed for the duration for which a codespace is active. If you're not using a codespace but it remains running, and hasn't yet timed out, you are billed for the total time that the codespace was active, irrespective of whether you were using it. For more information, see "[About billing for GitHub Codespaces](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#codespaces-pricing)."

As with any Visual Studio Code instance, you can also login to your Github account, to pull your settings and extensions, but to keep things clean, distraction free, you can customize your Codespace instead, for only what you or others working in the same repository need.

#### Customizing Your Codespace

You can customize your Codespace, to suit the project you are working on, some examples I use personally are:

* Markdown editing _(for example, my website is hosted on Github Pages, and the formatting is done using Markdown, so I have a devcontainer preconfigured to run Markdown Visual Studio Code extensions and linting, so as soon as I open it - its good to go!)_
* Infrastructure as Code development _(I have preconfigured devcontainer, running on a container, that has the latest version of PowerShell, Terraform, Bicep installed and relevant Visual Studio extensions)_

I am someone who use to install everything locally, to the point when I would be reinstalling Windows every few months. to keep my device clean, I had moved to an Azure Virtual Desktop host as my development environment, but Codespaces now give me the flexibility to install what I need (when I need it) within an Linux environment, and I know when I rebuild the Codespace, I will have the latest libraries.

There are a lot of customisation you can do, we won't be able to cover all possible customisations tn this article, but I aim to cover the basics to get you up and running!

##### Setting Sync

Before, delving into some of the more customistion of the devcontainer configuration itself, lets not forget the Visual Studio Code settings sync.

If your someone who works on the same products and services and has invested time in configuring Visual Studio profiles, theres nothing indicating that you can't use this in a Github Codespace, especially if its a trusted repository.

You will already be logged into Visual Studio Code, with your Github account, you can turn on Setting Sync, to have your Visual Studio code settings and profiles sync straight into your devcontainer.

![Github Codespaces - Setting Sync](/images/posts/VisualStudioCode_Codespace_TurnonSettingSync.gif)

One of the downsides of this method, is the container can get bloated with extensions and configuration you don't need, and you will have turn on Setting Sync, each time a Codespace is launched.

[Setting Sync](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account#turning-on-settings-sync-in-a-codespace) is an easy way to import your configuration from your Desktop into the Cloudspace.

##### Codespace templates

Instead of spending the time, developing your own template, you may find a devcontainer template already exists for your use case, some examples consist of:

* Ruby on Rails
* React
* Juypter Notebooks and more.

These [Codespace Templates](https://github.com/codespaces/templates), can easily be launched from the web browser and are a great resource to test the power of Codespace, and refer to when customisting your own devcontainer.

 See [devcontainers/template-starter](https://github.com/devcontainers/template-starter) and [devcontainers/feature-starter](https://github.com/devcontainers/feature-starter) for information on creating your own!

##### Devcontainers

Within each customised Codespace, is a "[devcontainer.json](https://containers.dev/implementors/json_reference/)" json file, and some containers will have a [dockerfile](https://code.visualstudio.com/docs/devcontainers/create-dev-container#_dockerfile).

These files will sit inside a /.devcontainer/ folder at the root of your git repository. Its worth noting that you can have multiple devcontainer files within a single repository, you will be prompted which one to be used when you start the Codespace up.

These files are key to customising your own devcontainer.

Although they serve different purpose they can work standalone or together to create a consistent and reproducible development environment for your project.

|File | Purpose  |
|---|---|
|devcontainer.json|  The devcontainer.json file is used to configure how your development environment is set up within the Docker container when using the Remote - Containers extension. |
|dockerfile| The dockerfile to define the environment you need for your project. When you create a Codespace, GitHub will use the specified Dockerfile to build a container image that includes all the tools, libraries, and configurations required to work on your project.   |

When you open your project in a GitHub Codespace that uses a devcontainer.json file, Visual Studio Code will automatically detect the configuration and set up your development environment according to the specified settings.

You can use a dockerfile to define the environment you need for your project. When you create a Codespace, GitHub will use the specified Dockerfile to build a container image that includes all the tools, libraries, and configurations required to work on your project.

Even without using a dockerfile, you can install any dependant libraries onto your codespace, but they be lost when the container gets rebuilt, there are certain approved features you can add to your devcontainer file, that will be installed when a container is launched, which is great when making sure you are working on with the latest component.

The idea with both these files, is to _keep them lean_ and make sure that you are running the components you only need, to keep launch time and performance as quick as possible, it is possible to '[prebuild](https://docs.github.com/en/codespaces/prebuilding-your-codespaces/about-github-codespaces-prebuilds)' your image if it is largely complex, but we don't be covering that here.

###### devcontainer.json

Lets take a look at the 'devcontainer.json' file. As Codespaces uses the [devcontainer](https://containers.dev/implementors/spec/) schema, all the customisations offered such as:

* entrypoint
* onCreateCommand
* customizations
* features
  
Can be used, offering a vast range of customisation opportunities to suit your needs.

For most purposes, you may be able to find you can get away with a devcontainer.json file without having to delve into building your own dockerfile.

Lets look into the devcontainer.json file, I am using for this blog article:

```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/markdown
{
	"name": "Markdown Editing",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/base:bullseye",

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Configure tool-specific properties.
	"customizations": {
		// Configure properties specific to VS Code.
		"vscode": {			
			// Add the IDs of extensions you want installed when the container is created.
			"extensions": [
				"yzhang.markdown-all-in-one",
				"streetsidesoftware.code-spell-checker",
				"DavidAnson.vscode-markdownlint",
				"shd101wyy.markdown-preview-enhanced",
				"bierner.github-markdown-preview"
			]
		}
	}

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "uname -a",

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}

```

This was from an already existing template, that had everything I needed from: [devcontainers/templates](https://github.com/devcontainers/templates/tree/main/src).

A few things stand out:

* image
* customizations
* features

1. The image is the docker image, that this Codespace is running.
1. Customizations is my application specific customisations, in my example vscode, and the extensions that are automatically provisioned for me when I started this codespace.
1. Features, which is currently blank, but will allow us to run scripts to install any relevant dependences when the container is started.

This json file is a great reference point, as we go into creating our own. You can create your own devcontainer.json file - or we can do it within the devcontainer itself using the Codespaces extension, preinstalled into your new Codespace.

In our newly created Codespace from the Setting up Codespace step earlier, its time to create our own devcontainer. The project we will be working on will be Terraform development, so we want to customise our own codespace for Infrastructure as Code development.

1. Press **Ctrl+Shift+P** (or click View, Command Palette)
2. Type in: **Codespaces** _(with the codespaces commands you can rebuild your container, resize and modify your codespace)_
3. Select **Add Dev Container Configuration Files**
4. Select **Create a new Configuration**
5. Type in **Ubuntu**
6. Select the latest version (or default)
7. In the **[features](https://github.com/devcontainers/features)** list we have the option to install third party tools and dependencies that will be installed when we launch our Codespace, search for **Terraform**
8. Select **Terraform, tflint, and TFGrunt**
9. Click **Ok**
10. Select **Configure Options**
11. Check the **installTFsec** and **instalLTerraformDocs**
12. Click **Ok**
13. Select the **latest** Terraform version
14. Select the latest **Tflint** version

This will now create a devcontainer json file, using a base Ubuntu image, with the latest version of Terraform, tflint and Terragrunt installed!

![Github Codespaces - Create](/images/posts/VisualStudioCode_Codespace_CreateTerraform.gif)

**Make sure you save and commit the devcontainer.json file to the repository! You have now created your first custom codespace**.

You can now rebuild your container, to run inside your Terraform container:

1. Press **Ctrl+Shift+P** (or click View, Command Palette)
2. Type in: **Codespaces**
3. Select **Full Rebuild Container**
4. Accept the prompt. that it will be rebuild with the devcontainer configuration.
5. GitHub Codespaces will then grab the Ubuntu image, and the Terraform feature and run.

> Note: If the build fails, at the time of writing, there looked to be an issue with the latest version of [terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/supported-terraform-versions/), I pined it to this specific version: 0.48.0, and it fixed it. So edit the JSON file and update latest to the version. Feel free to review my example codespace here: [lukemurraynz/codespaces](https://github.com/lukemurraynz/codespaces/tree/main).

1. Once loaded, I can immediately run 'terraform init'

![Github Codespaces - Terraform init](/images/posts/VisualStudioCode_Codespace_Terraforminit.gif)

Now that we have Terraform installed, the Azure Terraform and HashiCorp extension - we may want the [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) extension, to help with working with other developers, so lets add this!

1. Navigate to the **Extensions**
2. Search for **GitLens**
3. **Right** click the **extension** button and select '**Add to devcontainer.json**'
4. Then commit your save, you have now added the GitLens extension into your devcontainer, this will automatically be installed on your next rebuild.

![Github Codespaces - Install Extension](/images/posts/VisualStudioCode_Codespace_AddGitLens.gif)

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
