---
title: Optimal Taleo Settings
permalink: /misc/optimal-taleo-settings/
categories:
  - Misc
  - Windows
---
<p class="Style1">
  Taleo is used for many organisations as its tool for managing job applications. These settings are Internet Explorer recommended settings for displaying Taleo with no problems.
</p>

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Magnification"><span class="toc_number toc_depth_1">1</span> Magnification</a>
    </li>
    <li>
      <a href="#Configuring_Cookie_Policy_for_Internet_Explorer"><span class="toc_number toc_depth_1">2</span> Configuring Cookie Policy for Internet Explorer</a>
    </li>
    <li>
      <a href="#Enabling_JavaScript"><span class="toc_number toc_depth_1">3</span> Enabling JavaScript</a>
    </li>
    <li>
      <a href="#Troubleshooting_JavaScript"><span class="toc_number toc_depth_1">4</span> Troubleshooting JavaScript</a>
    </li>
    <li>
      <a href="#Setting_Browser_to_Cache_Web_Files"><span class="toc_number toc_depth_1">5</span> Setting Browser to Cache Web Files</a>
    </li>
    <li>
      <a href="#Optimizing_Cache_Settings"><span class="toc_number toc_depth_1">6</span> Optimizing Cache Settings</a>
    </li>
    <li>
      <a href="#Configuring_the_Printer"><span class="toc_number toc_depth_1">7</span> Configuring the Printer</a>
    </li>
  </ul>
</div>

#### <span id="Magnification">Magnification</span>

The magnification level of your Internet browser must be set to 100%.
  
Using a setting other than 100% might produce less than optimal results depending on the Taleo product you are
  
using and the action you are performing. For this reason, 100% is the only recommended magnification level.

#### <span id="Configuring_Cookie_Policy_for_Internet_Explorer">Configuring Cookie Policy for Internet Explorer</span>

Prerequisite
  
The default Privacy setting for Internet Explorer is Medium. This setting is normally sufficient to ensure the
  
proper handling of cookies used by Taleo Enterprise.
  
Internet Explorer > Tools > Internet Options > Privacy
  
Steps
  
1. In the Privacy tab, click Advanced.
  
2. In the Advanced Privacy Settings window, clear the Override automatic cookie handling option.
  
3. Click OK.
  
4. In the Privacy tab, click Sites.
  
5. In the Per Site Privacy Actions window, add &#8220;taleo.net&#8221; (without quotes) in the Address of Web site field.
  
6. Click Allow.
  
7. Click Done.

#### <span id="Enabling_JavaScript">Enabling JavaScript</span>

JavaScript is required for the proper function and use of Taleo Enterprise.
  
Prerequisite
  
Internet Explorer > Tools > Internet Options
  
Steps
  
1. In the Security tab, click the Internet icon.
  
2. Click Default Level.
  
3. Click OK.

#### <span id="Troubleshooting_JavaScript">Troubleshooting JavaScript</span>

Allows users to have the application work properly after enabling JavaScript.
  
Prerequisite
  
Enabling JavaScript must have been performed.
  
Internet Explorer > Tools > Internet Options > Security tab
  
Internet and Browser Settings

Steps
  
1. In the Security tab, click the Internet icon.
  
2. Click Custom Level.
  
3. Under Active Scripting, under the Scripting section, click Enable or Prompt.
  
4. Click OK.
  
5. Click Yes.
  
6. Click OK.
  
Result
  
Application should run as expected.

#### <span id="Setting_Browser_to_Cache_Web_Files">Setting Browser to Cache Web Files</span>

Prerequisite
  
Internet Explorer > Tools > Internet Options > Advanced
  
Steps
  
1. Deselect Empty Temporary Internet Files Folder When Browser Is Closed.
  
2. Deselect Do not save encrypted files to disk.
  
3. Click OK.
  
4. Restart browser.

#### <span id="Optimizing_Cache_Settings">Optimizing Cache Settings</span>

Many browsers retain Web site files in the “cache” for a certain period of time. This saves browsing time by
  
accessing the file directly from your computer&#8217;s hard drive rather than gathering it from the Internet, thereby
  
increasing overall performance.
  
Prerequisite
  
Internet Explorer > Tools > Internet Options > General tab
  
Steps
  
1. For Internet Explorer 7 or 8, click Settings under the Browsing History section.
  
2. In the Temporary Internet and History Settings window, select Automatically, for the Check for newer
  
version of stored pages option.
  
3. For the Disk space to use setting, select a value greater than100 MB but less than 500 MB. Setting the
  
cache size higher than 500 MB might actually reduce performance.
  
4. Click OK.
  
5. In the Internet Options window, click OK.

#### <span id="Configuring_the_Printer">Configuring the Printer</span>

Allows users to configure the browser for faster printing results.
  
Prerequisite
  
Internet Explorer > Tools > Internet Options > Advanced
  
Steps
  
1. Scroll down to the Printing settings.
  
2. Select Print background colors and images.
  
3. Click OK.
