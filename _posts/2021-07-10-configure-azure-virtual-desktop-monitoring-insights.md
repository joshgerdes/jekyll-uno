---
date: '2021-07-10 00:00:00 +1200'
title: Configure Azure Virtual Desktop Monitoring Insights
author: Luke
categories:
  - Azure
toc: true
header:
  teaser: /uploads/azportal_azurevirtualdesktopinsights.png
_template: new_post
---

Microsoft has now added a built-in Monitoring workbook for Azure Virtual Desktop performance monitoring; this monitoring includes dashboards related _(but not limited to)_:

* Session host diagnostics
* Connection performance
* Host performance
* User login events
* Remote Desktop client versions

To configure, we first need to create a Log Analytics workspace that both the Host Pool and Workspace will connect to.

### Create a Log Analytics workspace

You can use a Log Analytics workspace if it already exists; if not, we will have to create one.

 1. Log in to the **Azure Portal**
 2. Click on + **Create a Resource**
 3. Search for: **Log Analytics workspace**
 4. Click **Create**
 5. ![Azure Portal - Log Analytics Marketplace](/uploads/azportal_loganalyticsworkspace.png "Azure Portal - Log Analytics Marketplace")
 6. Here we can **select** the **Resource Group**, **Name** and **Location** of the Log Analytics workspace we will create.
 7. I am going to **create** a new **Resource Group** called: aad_mgmt
 8. I click Create New and **enter** in the **name** of the **Resource Group**
 9. Under Instance Details, make sure you select a name that adheres to your naming governance.
10. _Note: the name of your Log Analytics workspace is now scoped to the Resource Group, so you can have Log Analytics workspaces with the same name, as long as they are indifferent resource groups._
11. ![Azure Portal - Create Log Analytics](/uploads/azportal_createloganalyticsworkspace.png "Azure Portal - Create Log Analytics")
12. Click on: **Next: Pricing Tier**
13. **Select** the applicable **pricing tier**, I only have Pay-as-you-go (Per GB 2018), so I will select that.
14. _Note: You can view the Pricing for Log Analytics on the_ [_Pricing Calculator_](https://azure.microsoft.com/en-us/pricing/details/monitor/?WT.mc_id=AZ-MVP-5004796, "Azure Pricing Calculator - Azure Monitor"){:target="_blank"}_:  look at the Pay-As-You rates._
15. ![Azure Portal - Create Log Analytics](/uploads/azportal_createloganalyticsworkspacepricing.png "Azure Portal - Create Log Analytics")
16. Click **Next: Tags**
17. **Enter** in any **applicable tags**, such as Creator, Who it may get billed to, Project ID etc. that’s relevant and select **Review + Create**
18. **Review** the **configuration** and click **Create** to create your Log Analytics workspace! _(It should take less than a minute._)

### Configure Azure Virtual Desktop Insights

 1. Log in to the **Azure Portal**
 2. **Search** for: **Azure Virtual Desktop**
 3. Click on [**Insights**](https://portal.azure.com/#blade/Microsoft_Azure_WVD/WvdManagerMenuBlade/insights "Azure Virtual Desktop - Insights"){:target="_blank"}
 4. A Workbook blade should now greet you
 5. This is where we will **configure** the Azure Virtual Desktop **Insights**. You can see on the lower right-hand side that we will be deploying Azure Monitor for 'Windows Virtual Desktop v1.0.4' _(however, this will be managed by Microsoft, but it is handy to know the version in case of support later on)._
 6. ![Azure Virtual Desktop - Insights](/uploads/azportal_azurevirtualdesktop_insights.png "Azure Virtual Desktop - Insights")
 7. Click on **Open Configuration Workbook**
 8. Here, **select** the Log Analytics **workspace** you created earlier _(or want to use)_
 9. Select **Configure host pool**
10. ![Azure Virtual Desktop - Insights](/uploads/azportal_azurevirtualdesktopcheckconfiguration.png "Azure Virtual Desktop - Insights")
11. Click on **Deploy** _(make sure all your Session Hosta are started so that Azure can deploy and configure the Log Analytics agent on the Virtual Machines)_
12. You can select View Template and Parameters if you want to confirm the host pool and workspace configured.
13. ![Azure Virtual Desktop - Insights](/uploads/azportal_azurevirtualdesktophostpooldeploy.png "Azure Virtual Desktop - Insights")
14. While the Diagnostic host pool settings are being configured, click on **Configure workspace.**
15. Click on: **Deploy**
16. Once the Workspace and Host Pool deployments are done, click on **Refresh.**
17. ![Azure Virtual Desktop - Insights](/uploads/azportal_azurevirtualdesktopcheckconfigrefresh.png "Azure Virtual Desktop - Insights")
18. **Confirm** that **Enabled** is: True
19. ![Azure Virtual Desktop](/uploads/azportal_azurevirtualdesktopcheckconfig.png)
20. The journey is not over yet; now that the Host Pool and Workspace have been configured, we need to **add** the **Session Hosts** and configure the **performance counters** to the same workspace!
21. Click on: **Session host data settings.**
22. **Select** your Log Analytics **workspace**
23. Select **Add hosts to workspace**
24. ![Azure Virtual Desktop](/uploads/azportal_sessionhostdatasettings.png)
25. Confirm the Deployment and click **Deploy**
26. **Wait until** the **deployment** has **succeeded,** or you may get API errors, then select:
27. Navigate down and click **Configure performance counters**
28. ![Azure Virtual Desktop](/uploads/azportal_performancecounterssettings.png)
29. Click on **Apply** config.
30. **Wait until** the **deployment** has **succeeded,** or you may get API errors, then select:
31. Navigate down and click on **Configure events**
32. ![Azure Virtual Desktop](/uploads/azportal_eventlogssettings.png)
33. Click on **Deploy**

    Now click on: **Refresh**, and you should see 'No missing performance counters', 'No missing events found'.
34. ![Azure Virtual Desktop](/uploads/azportal_performancecountersreview.png)
35. **You have now configured Azure Virtual Desktop Insights!**

    _It may take a few minutes to an hour to populate and collect the data for some of the events and counters._
36. ![Azure Virtual Desktop](/uploads/azportal_azurevirtualdesktopinsights.png)

    _On the plus side, all the data is also in Log Analytics so that it can be queried, and you can set up Alert rules against it and get more visibility into your Azure Virtual Desktop environment and use._

    ![Azure Virtual Desktop](/uploads/azportal_azurevirtualdesktoploganalytiicsquery.png)
    
