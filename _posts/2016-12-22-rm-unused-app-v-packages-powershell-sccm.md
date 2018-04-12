---
title: Remove unused App-V packages automatically using PowerShell and Configuration Manager
permalink: /win/rm-unused-app-v-packages-powershell-sccm/
categories:
  - Windows
---
<section class="av\_textblock\_section " itemscope="itemscope" itemtype="https://schema.org/BlogPosting" itemprop="blogPost" >

<div class='avia_textblock  '   itemprop="text" >
  <p style="text-align: justify;">
    I had an issue with unused/old App-V packages getting left in the App-V package store, the Help Desk would RDP onto a workstation, causing their Applications to download. This was causing issues with Reporting and overall cleanliness of the environment.
  </p>
  
  <p>
    <span style="color: black;">Using Configuration Manager and PowerShell I was able to create a Configuration Baseline for cleaning up the App-V client cache of unused packages from workstations.<br /> </span>
  </p>
  
  <p>
    <span style="color: black;">The script/baseline follows the logic diagrammed below:<br /> </span>
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse1.jpg?w=1500" alt="" data-recalc-dims="1" /><span style="color: black;"><br /> </span>
  </p>
  
  <h3>
    How to create and deploy the Configuration Baseline?
  </h3>
  
  <p>
    To create a Configuration Baseline which is deployed to a Collection, we first need to create a Configuration Item – to do this follow the guide below:
  </p>
  
  <p>
    Open Configuration Manager
  </p>
  
  <p>
    Navigate to the Assets and Compliance work-space
  </p>
  
  <p>
    Click on Compliance Settings
  </p>
  
  <p>
    Right click on Configuration Items and select Create Configuration Item
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse2.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    Select a name for your Configuration Item such as: App-V Clean-up and fill out the rest of the details and click Next
  </p>
  
  <p>
    <img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse3.png?resize=575%2C396" alt="App-V Cleanup" width="575" height="396" data-recalc-dims="1" />
  </p>
  
  <p>
    Select the Operating Systems that will support this Configuration Item, depending on your environment it may be cleaner to make sure that it only works on certain Windows Desktop operating systems – in my case I will be controlling everything through the deployment Collection and may extend to Windows Servers in a VDI environment in the future so I will be leaving the defaults and click Next
  </p>
  
  <p>
    <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse4.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    &#8220;Specify Settings for this Operating System&#8221; is where you set the grunt work for the Configuration Item. Select New..
  </p>
  
  <p>
    Give the Item a name such as: Remove App-V Packages, for the Setting Type change it to Script and then change the Data type to: String.
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse5.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    For the Discovery Script – select Add Script..
  </p>
  
  <p>
    Change the Script Language to Windows PowerShell and copy in the Discovery Script from below.
  </p>
  
  <p>
    Once, completed click Ok
  </p>
  
  <p>
    Now we need to do the same for Remediation Script which will be the script that will be doing the clean-up, click on Add Script&#8230; And change the Script Language to Windows PowerShell, then copy the Remediation Script from below into it.<strong><br /> </strong>
  </p>
  
  <div class="oembed-gist">
    <noscript>
      View the code on <a href="https://gist.github.com/lukemurraynz/4bb2b67bae79372bb785850106945ef6">Gist</a>.
    </noscript>
  </div>
  
  <div class="oembed-gist">
    <noscript>
      View the code on <a href="https://gist.github.com/lukemurraynz/4bb2b67bae79372bb785850106945ef6">Gist</a>.
    </noscript>
  </div>
  
  <p>
    Once, completed click Ok and then select the Compliance Rules tab
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse6.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    This is where we set the Configuration Item compliance rule so the item knows when something is marked as Non-Compliant and how Configuration Manager will deal with it. Click on New…
  </p>
  
  <p>
    Because we specified String earlier, and the PowerShell discovery script is outputting Compliant, Non-Compliant we will be using the following logic:
  </p>
  
  <p>
    If the value returned by the specified script: Equals, Compliant then run the remediation script if Compliant is not found. Fill in the details like the screen capture below and click Ok
  </p>
  
  <p>
    <img class="alignnone" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse7.png?resize=591%2C551" alt="Configuration Baseline" width="591" height="551" data-recalc-dims="1" />
  </p>
  
  <p>
    Note: Just because these are set, does not mean when you deploy it – it will remediate, as part of the deployment you can set it to Monitor or Remediate <em>(in other words, mark as Compliant or Non-Compliant without doing anything or actually remediate it), </em>we are just setting the base up so the Configuration Item knows how to handle both.
  </p>
  
  <p>
    Verify the information is correct and click Ok then Next and Next again to finish creating your Configuration Item.
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse8.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    Once the Configuration Baseline is completed navigate to Configuration Baselines
  </p>
  
  <p>
    Right click Configuration Baseline and select Create Configuration Baseline
  </p>
  
  <p>
    <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse9.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    Give your Configuration Baseline a name, for example: Remove App-V Client Package
  </p>
  
  <p>
    Under Configuration Data, select Add and click on Configuration Item and add the App-V package clean-up Configuration Item you created earlier and select Ok to create your Configuration Baseline.
  </p>
  
  <p>
    <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse10.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    Now that your Configuration Item and Configuration Baseline has been created, you can now Deploy it to a collection by right clicking the Configuration Baseline and select Deploy
  </p>
  
  <p>
    <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse11.png?w=1500" alt="" data-recalc-dims="1" />
  </p>
  
  <p>
    This is where you can specify to just monitor or remediate. I recommend selecting a small group of computers first for Testing and monitoring to verify that Configuration Manager isn&#8217;t getting any errors back and it appears to be working. Once you are ready you can go back into the Deployments tab at the bottom of the Configuration Baseline and change the properties to Remediate NonCompliant Rules when Supported and click Ok
  </p>
  
  <p>
    <img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse12.png?resize=624%2C602" alt="Configuration Baseline" width="624" height="602" data-recalc-dims="1" />
  </p>
  
  <p>
    You have now successfully created a Configuration Item with a Discovery and Remediation script for cleaning up App-V packages, it may need to be tweaked for your environment and just change the number from 30 to something like 60 or 90 if that better matches your environment in both the Discovery and Remediation script.
  </p>
  
  <p>
    If you get errors about PowerShell signing, you will have to create a Custom Client under Administration, Client Settings, Computer Agent setting which sets the PowerShell execution policy to Bypass for your computers
  </p>
  
  <p>
    <img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122216_0752_Removeunuse13.png?resize=334%2C28" alt="PowerShell execution policy" width="334" height="28" data-recalc-dims="1" />
  </p>
  
  <p>
    Note: This setting does not set the global scope for PowerShell to Unrestricted/Bypass it is only controlling the execution policy of PowerShell scripts delivered through Configuration Manager, whether it is a PowerShell package or Baseline.
  </p>
</div></section>
