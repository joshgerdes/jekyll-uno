---
title: Upgrade MDT 2013 to MDT Current Branch
tags:
  - Windows
date: 2016-12-13 00:00:00 +1300
---
Upgrading MDT _(Microsoft Deployment Toolkit)_ is generally not an issue – the main points are:

  * Upgrade the Windows ADK before upgrading MDT.
  * Make sure you have a backup _(or can restore to a pre-upgraded MDT)_ of the Deployment Share – the Upgrade will upgrade the schema of the MDT database – including allowing new ADK features for your Deployment Share.

Now that we have a backup it is now time to go through the Windows ADK _(Windows Assessment and Deployment Kit)_ upgrade on the MDT server and MDT current branch update. Follow the guide below to complete.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Upgrade_Windows_ADK"><span class="toc_number toc_depth_1">1</span> Upgrade Windows ADK</a>
    </li>
    <li>
      <a href="#Upgrade_MDT"><span class="toc_number toc_depth_1">2</span> Upgrade MDT</a>
    </li>
  </ul>
</div>

## <span id="Upgrade_Windows_ADK">Upgrade Windows ADK</span>

I will be using Windows ADK for Windows 10, version 1607 in my example.

  1. Download the latest Windows ADK – <a href="https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit" target="_blank">https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit</a> and save the setup file to your MDT server.

<img class="alignnone" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT21.png?resize=624%2C333" alt="Windows ADK" width="624" height="333" data-recalc-dims="1" />

  1. If you try to install the ADK without upgrading, you will get the following error:

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT22.png?w=1500" alt="" data-recalc-dims="1" />

  1. So open Program and Features and select Windows Assessment and Deployment Kit – Windows 10 and select Uninstall to uninstall the old ADK (in this example I am uninstalling the v1511 Windows 10 ADK).

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT23.png?w=1500" alt="" data-recalc-dims="1" />

  1. Select Yes to uninstall the Windows ADK and Close when the uninstall has been completed

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT24.png?w=1500" alt="" data-recalc-dims="1" />

  1. Now that the old Windows ADK has been uninstalled you can now launch the new Windows ADK downloaded in Step 1 and make sure Install the Windows Assessment and Deployment Kit – Windows 10 to this computer is selected and the install path is correct and click Next

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT25.png?w=1500" alt="" data-recalc-dims="1" />

6. You can either select Yes or No to allow Microsoft to collect usage data – I am just going to select No and click Next to proceed with the install

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT26.png?w=1500" alt="" data-recalc-dims="1" />

7. Click Accept on the license agreement

8. You will now get greeted by a dialog for installing the features of the Windows ADK – you need: Deployment Tools, Windows Preinstallation Environment (Windows PE) and User State Migration Tool (USMT) and select Install

<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT27.png?resize=690%2C508" alt="Windows ADK" width="690" height="508" data-recalc-dims="1" />

9. Once the Windows Assessment and Deployment Kit installation has been completed, restart your MDT server (this is not required – but I prefer to do it to make sure any registered DLLs or registry changes have taken affect and it is in a clean state).

## <span id="Upgrade_MDT">Upgrade MDT</span>

1. Now that the Windows ADK has been updated – it is time to download the Microsoft Deployment Toolkit &#8211; <a href="https://www.microsoft.com/en-us/download/details.aspx?id=54259" target="_blank">https://www.microsoft.com/en-us/download/details.aspx?id=54259</a> by selecting Download

<img class="alignnone" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT28.png?resize=639%2C525" alt="MDT Download" width="639" height="525" data-recalc-dims="1" />

2. We are upgrading the x64 version so select this and click Next _(same process for x32 – just download that instead)_.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT29.png?w=1500" alt="" data-recalc-dims="1" />12. Select Run to start the install

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT210.png?w=1500" alt="" data-recalc-dims="1" />

3. You will now have the Install Microsoft Deployment Toolkit Setup wizard – select Next to start the install

<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT211.png?resize=508%2C396" alt="MDT install" width="508" height="396" data-recalc-dims="1" />

4. Accept the License Agreement and select Next

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT212.png?w=1500" alt="" data-recalc-dims="1" />

5. Make sure that Microsoft Deployment Toolkit – Documents and Tools and Templates are select and the install path is correct (matches your current MDT install) and click Next

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT213.png?w=1500" alt="" data-recalc-dims="1" />

6. Select Yes or No to joining the Customer Experience Improvement Program and select Next

7. Finally – click Install to start the MDT install

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT214.png?w=1500" alt="" data-recalc-dims="1" />

8. Once installed click Finish

9. Open the Deployment Workbench

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT215.png?w=1500" alt="" data-recalc-dims="1" />

10. It should automatically have your Deployment Share listed under Deployment Shares – if you will need to click File, Add Deployment Share to add your deployment share. Right click your deployment share and select Upgrade Deployment Share

<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT216.png?resize=476%2C240" alt="Upgrade Deployment Share" width="476" height="240" data-recalc-dims="1" />

11. Verify that the information is correct and click Next to start the Upgrade

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT217.png?w=1500" alt="" data-recalc-dims="1" />

12. This will start the upgrade of the Deployment Share

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT218.png?w=1500" alt="" data-recalc-dims="1" />

13. Once the Upgrade of the Deployment Share has been completed – it is time to upgrade the Boot Image

14. Right click your Deployment Share again – and instead of Upgrade, there will be Update. Select Update Deployment Share

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT219.png?w=1500" alt="" data-recalc-dims="1" />

15. You will be greeted by the Update Deployment Share Wizard – select completely regenerate the boot images and click Next

<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT220.png?resize=653%2C542" alt="Update Boot Image" width="653" height="542" data-recalc-dims="1" />

16. You will then be forwarded to a review page, verify the permissions are correct and click Next to start regenerating the boot images.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT221.png?w=1500" alt="" data-recalc-dims="1" />

17. Once completed you are finished. You have now hopefully successfully upgraded the ADK, MDT and Boot Images.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/121316_0538_UpgradeMDT222.png?w=1500" alt="" data-recalc-dims="1" />
