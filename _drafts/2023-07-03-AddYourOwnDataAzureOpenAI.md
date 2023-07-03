---
title: Bring your own data into Azure Open AI
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /images/posts/azure-management-group-notloading.png
date: '2023-07-03 00:00:00 +1300'
---

Today, we will be looking at using Azure Open AI, and 'Bring Your Own Data' to allow recent documentation to be referenced.

The example we are going to use today, is the Microsoft Learn documentation.

Our scenario is this:

* We would like to use ChatGPT functionality, to query up-to-date information on Microsoft Azure, in this example, we will look for information on Azure Elastic SAN (which was added in late 2022).

When querying ChatGPT for Azure Elastic SAN, we get:

![ChatGPT - Azure Elastic SAN Query](/images/posts/ChatGPT_Query_AzureElasticSAN.png "ChatGPT - Azure Elastic SAN Query")

Just like the prompt states, ChatGPT only has data up to September 2021, and isn't aware of Elastic SAN *(or any other changes/updates or new (or retired) services after this date)*.

So lets use the Azure Open AI, and Retrieval augment generation (RAG) by bringing in outside data, in this case the Azure document library to overlay on top of the GPT models, giving the illusion the model is aware of the data.

To do this, we will need to provision a few Microsoft Azure services, such as:

1. Azure Storage Account *(this will hold the Azure document library (markdown files) in a blob container)*
1. Cognitive Search *(this search functionality, is the glue that will hold this solution together, by breaking down and indexing the documents in the Azure blob store)*
1. Azure Open AI *(to do this, we will need GPT3.5 turbo or GPT4 models deployed)*
1. Optional - Azure Web App *(this can be created by the Azure Open AI service, to give users access to your custom data)*

We will use the following tools to provision and configure our services:

1. Azure Portal
1. PowerShell (Az Modules)
1. AzCopy

### Download Azure Documents

First up, we will need the Azure documents, to add to our blob storage.

The Microsoft Learn, documentation is open sourced, and constantly kept up to date by using a git repository hosted on GitHub. We will download and extract the document repository, locally *(its roughly about 6 GB in size)*. To do this we will use a PowerShell script:

         $gitRepoUrl = "https://github.com/MicrosoftDocs/azure-docs"
         $localPath = "C:\temp\azuredocs"
         $zipPath = "C:\temp\azurdocs.zip"
         #Download Git repository and extract
         Invoke-WebRequest -Uri "$gitRepoUrl/archive/master.zip" -OutFile $zipPath
         Expand-Archive -Path $zipPath -DestinationPath $localPath

### Create Azure Storage Account

Now that we have a copy of the Azure document repository, its time to create an Azure Storage account to copy the data into. To create this storage account, we will use PowerShell.

         # Login to Azure
         Connect-AzAccount
         # Set variables
         $resourceGroupName = "azuredocs-ai-rg"
         $location = "eastus"
         $uniqueId = [guid]::NewGuid().ToString().Substring(0,4)
         $storageAccountName = "myaistgacc$uniqueId"
         $containerName = "azuredocs"
         # Create a new resource group
         New-AzResourceGroup -Name $resourceGroupName -Location $location
         # Create a new storage account
         New-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccountName -Location $location -SkuName Standard_LRS -AllowBlobPublicAccess $false
         # Create a new blob container
         New-AzStorageContainer -Name $containerName -Context (New-AzStorageContext -StorageAccountName $storageAccountName -StorageAccountKey (Get-AzStorageAccountKey -ResourceGroupName $resourceGroupName -Name $storageAccountName).Value[0])

We have now create our Resource Group, and Storage account to hold our Azure documentation on.

### Upload Microsoft Learn documentation to an Azure blob container

Now that we have the Azure docs repo downloaded and extracted, and an Azure Storage account to hold the documents, its time to use AzCopy to copy the documentation up to the Azure storage account.
To do this, we will use PowerShell to create a SAS token (open for a day), and use that with AzCopy to copy the Azure repo into our newly created container.

         # Set variables
         $resourceGroupName = "azuredocs-ai-rg"
         $storageAccountName = "myaistgacc958b"
         $containerName = "azuredocs"
         $storageAccountKey = (Get-AzStorageAccountKey -ResourceGroupName $resourceGroupName -Name $storageAccountName).Value[0]
         $localPath = "C:\Temp\azuredocs\azure-docs-main"
         $azCopyPath = "C:\tools\azcopy_windows_amd64_10.19.0\AzCopy.exe"
         # Construct SAS URL for destination container
         $sasToken = (New-AzStorageContainerSASToken -Name $containerName -Context (New-AzStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey) -Permission rwdl -ExpiryTime (Get-Date).AddDays(1)).TrimStart("?")
         $destinationUrl = "https://$storageAccountName.blob.core.windows.net/$containerName/?$sasToken"
         # Run AzCopy command as command line
         $command = "& `"$azCopyPath`" copy `"$localPath`" `"$destinationUrl`" --recursive=true"
         Invoke-Expression $command

*Note: It took roughly 6 minutes for me to copy the Azure docs repo, from my local computer (in New Zealand) into a blob storage account in East US, so roughly a gigabyte a minute.*

![Azure Storage Account - Microsoft Learn Docs](/images/posts/AzureStorage_AzureDocs_UploadedAzCopy.png "Azure Storage Account - Microsoft Learn Docs")

### Create Cognitive Search

Now that we have our Azure Blob storage accounts, its time to create our Cognitive Search.
We will need to create a Cognitive Search, with a SKU of Standard, to support the 6GBs of Azure documents that require to be indexed. Please check your costs, this is roughly NZ$377.96 a month to run, you can reduce this cost by limiting the amount of data you need to index (ie only certain documents, not an entire large repository of markdown files). Make sure you refer to the Pricing Calculator.

         # Set variables
         $resourceGroupName = "azuredocs-ai-rg"
         $searchServiceName = "azuredocssearchservice" #Cognitive Service name needs to be lowercase.
         # Create search service
         Install-Module Az.Search
         $searchService = New-AzSearchService -ResourceGroupName $resourceGroupName -Name $searchServiceName -Location "eastus" -Sku Standard

Now that the cognitive search has been created, we now need to create the index, and indexers, which will index our azure documents to be used by Azure Open AI, by creating the index and linking it to the Azuredocs blob container, we created earlier.

*Note: There is no PowerShell cmdlet support for Azure Cognitive Search indexes, you can create using the [RestAPI](https://learn.microsoft.com/azure/search/search-get-started-powershell?WT.mc_id=AZ-MVP-5004796){:target="_blank"} - but we will do this in the Azure Portal as part of the next step.*

### Create Azure Cognitive Search Index

Now, its time to time to create the Cognitive Search Index, and indexer that will index the content.

To do this, we will move away from PowerShell and into the Microsoft Azure Portal.

1. Navigate to the [Microsoft Azure Portal](https://portal.azure.com/#home){:target="_blank"}
1. In the top center search bar type in: Cognitive Search
1. Click on [Cognitive Search](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/AppliedAIHub/~/CognitiveSearch){:target="_blank"}
1. Click on your newly created Cognitive Search
![Azure Portal - Cognitive Search](/images/posts/AzurePortal_CognitiveSearch_Resource.png "Azure Portal - Cognitive Search")
1. Select Import Data
1. Select Azure Blob Storage
![Azure Portal - Cognitive Search - Add Azure Blob Storage](/images/posts/AzurePortal_CognitiveSearch_AddDataStorage.png "Azure Portal - Cognitive Search")
1. Type in your data source name *(ie azuredocs)*
1. For the Connection string, select Choose and existing connection
1. Select your Azure Storage account and container, containing the azure document repository uploaded earlier.
1. Click Select
![Azure Portal - Cognitive Search - Add Azure Blob Storage](/images/posts/AzurePortal_CognitiveSearch_ConnectBlobStorage.png "Azure Portal - Cognitive Search - Add Azure Blob Storage")
1. Click Next: Add cognitive skills (Optional)
1. Here you can Enrich you data, such as enabling OCR (extract text from images automatically) or extracting peoples names, translating text from one lanuage to another, these enrichments are billed seperately, we won't be using any enrichments so we will select Skip to: Customize target index.
1. Here is the index mapping that was done by Cognitive Search automatically, by scanning the schema of the documents. You can bring in additional data about your documents if you want, but I am happy with the defaults, so I click: Next: Create an indexer
![Azure Portal - Cognitive Search - Search Index](/images/posts/AzurePortal_CognitiveSearch_SearchIndex.png "Azure Portal - Cognitive Search - Search Index")
1. The indexer is what is going to create your index, that will be referenced by Azure Open AI later, you can schedule an indexer to run hourly, if new data is being added to the Azure blob container where your source files are sitting, for my purposes I am going leave the Schedule as: Once
1. Uncollapse Advanced Options, and scroll down a bit
1. Here we can select to only index certain files, for our purposes we are going to exclude png files, the Azure document repository contains png images files that aren't able to be indexed (we aren't using OCR), so I am going to optimize the indexing time slightly by excluding them. You can also exclude gif/jpg image files.
![Azure Portal - Cognitive Search - Create Search Indexer](/images/posts/AzurePortal_CognitiveSearch_CreateIndexer.png "Azure Portal - Cognitive Search - Create Search Indexer")
1. Finally, hit Submit to start the indexing process. *This could take a while, depending on the amount of data*
1. You can leave this running in the background, and navigate back to the Cognitive Search resource, Overview pane to see the status.
![Azure Portal - Cognitive Search - Indexer](/images/posts/AzurePortal_CognitiveSearch_OverviewIndexer.png.png "Azure Portal - Cognitive Search - Indexer")

*Note: You can run the Import Data in Azure Open AI Studio as well, which will trigger an index - but you need to keep your browser open and responsive. Depending on the amount of data you are indexing, doing it manually through this process, could be preferred to avoid brower timeout. You also get more options around the index.*

### Create Azure Open AI

Now that we have our base Azure resources, its time to create Azure Open AI.
Make sure your region and subscription, has been approved for Azure Open AI.

Run the following PowerShell cmdlets to create the Azure Open AI service:

To create the Azure Open AI service, we will be using the Azure Portal.

1. Navigate to the [Microsoft Azure Portal](https://portal.azure.com/#home){:target="_blank"}
1. In the top center search bar type in: Azure Open AI
1. 


Now that the Azure Open AI service, has been created you should now have:

* An Azure Open AI service
* A Storage account
* A Cognitive Search service

![Azure Open AI - RAG Deployed Resources](/images/posts/AzurePortal_AzureOpenAI_BYOD_Resources.png "Azure Open AI - RAG Deployed Resources")
