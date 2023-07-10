---
title: Azure OpenAI error log summarization with completion 
author: Luke
categories:
  - Azure
toc: false
header:
  teaser: /images/posts/AzureOpenAI_Completion_ErrorLog.png
date: '2023-07-10 00:00:00 +1300'
---
I was assisting a user on [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/?WT.mc_id=AZ-MVP-5004796){:target="_blank"} with an issue, that involved looking over some event logs.

The issue itself was related to the Nested Virtualization, with the user unable to install Hyper-V or WSL (Windows Subsystem for Linux), it turned out to be [incompatilibies with the SKU size and Secure boot](https://learn.microsoft.com/azure/virtual-machines/trusted-launch?WT.c_id=AZ-MVP-5004796#unsupported-features){:target="_blank"}.

But as part of troubleshooting this issue, I recreated the Azure compute environment, this user had and started to delve into the Windows logs.

However, in this case I did something a bit difference, I exported the logs as text file and opened up [Azure OpenAI](https://learn.microsoft.com/azure/cognitive-services/openai/overview?WT.mc_id=AZ-MVP-5004796){:target="_blank"}, then navigated to Azure OpenAI Studio, clicked on Completion and used the summarization powers of the GPT 3.5 Large lanuage model, to delve into the logs for me:

![Azure OpenAI - Summarize Error Log](/images/posts/AzureOpenAI_Completion_ErrorLog.png "Azure OpenAI - Summarize Error Log")

Copying, the Log into the Completion pane of Azure OpenA

And using sing the Prompt of:

    ----
    Summarize all the errors and warnings from above and sort by potential cause of the issues, with the most likely cause first. Format as a table.

Azure OpenAI was able to use the reasoning ability of the GPT 3.5 LLM (Large Lanuage Model) to sort through 115 lines of Logs, and work out the probability of what could be causing the root cause of the issue.

As you can see, Azure OpenAI and the LLMs can not just be used as an assistant in writing, studying it can be learned to assist in Incident and root-cause resolution.
