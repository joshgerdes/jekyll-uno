---
title: 'Windows Antivirus – Installation &amp; Scanning Guide'
permalink: /win/windows-antivirus-installation-scanning-guide/
categories:
  - Windows
---
<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">The following procedures will outline the installation instructions of third party Antivirus and Anti-malware tools that do include Rootkit scanning and removal. The Trend Micro utilities should be run first and if possible a virus sample collected and sent to Trend Micro. The following utilities are included in this: AVG Antivirus Free, CCleaner, ClamWin Antivirus, CWShredder, HijackThis, Malwarebytes Anti-malware, Microsoft Security Essentials, Rootkit Revealer, Spybot Search & Destroy.<br /> </span>
</p>

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti1.png?w=1500" alt="" data-recalc-dims="1" />

<!--more-->

Offline Updates to these products are found at the following locations (that should be downloaded and copied to the USB flash drive to allow offline updating at time of incident) and ran after the anti-malware or antivirus utility has been installed.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti2.png?w=1500" alt="" data-recalc-dims="1" />AVG Antivirus &#8211; <http://free.avg.com/au-en/download-update>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti3.png?w=1500" alt="" data-recalc-dims="1" />ClamWin Antivirus &#8211; <http://www.clamwin.com/content/view/58/27/>

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti4.png?w=1500" alt="" data-recalc-dims="1" />**
  
** Malwarebytes Anti-Malware &#8211; <http://data-cdn.mbamupdates.com/tools/mbam-rules.exe>

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti5.png?w=1500" alt="" data-recalc-dims="1" />**
  
** Search & Destroy &#8211; ht[tp://www.majorgeeks.com/files/details/spybot\_search\_and\_destroy\_update.html
  
](//www.majorgeeks.com/files/details/spybot_search_and_destroy_update.html) 

Note: In order to fully utilize these utilities, the user must have local administration rights to PC to install the software.

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Collect_Suspicious_Files_and_System_Information_with_Trend_Micro"><span class="toc_number toc_depth_1">1</span> Collect Suspicious Files and System Information with Trend Micro</a>
    </li>
    <li>
      <a href="#Trend_Micro_Anti-Threat_Toolkit"><span class="toc_number toc_depth_1">2</span> Trend Micro Anti-Threat Toolkit:</a>
    </li>
    <li>
      <a href="#Trend_Micro_Rootkit_Buster"><span class="toc_number toc_depth_1">3</span> Trend Micro Rootkit Buster</a>
    </li>
    <li>
      <a href="#Trend_Micro_Rescue_Disk"><span class="toc_number toc_depth_1">4</span> Trend Micro Rescue Disk</a>
    </li>
    <li>
      <a href="#AVG_Antivirus"><span class="toc_number toc_depth_1">5</span> AVG Antivirus</a>
    </li>
    <li>
      <a href="#ClamWin_Antivirus"><span class="toc_number toc_depth_1">6</span> ClamWin Antivirus</a>
    </li>
    <li>
      <a href="#RootkitRevealer"><span class="toc_number toc_depth_1">7</span> RootkitRevealer</a>
    </li>
    <li>
      <a href="#Trend_Micro_CWShredder"><span class="toc_number toc_depth_1">8</span> Trend Micro CWShredder</a>
    </li>
    <li>
      <a href="#Malwarebytes_Anti-Malware"><span class="toc_number toc_depth_1">9</span> Malwarebytes Anti-Malware</a>
    </li>
    <li>
      <a href="#Spybot_Search_Destroy"><span class="toc_number toc_depth_1">10</span> Spybot Search & Destroy</a>
    </li>
    <li>
      <a href="#Misc"><span class="toc_number toc_depth_1">11</span> Misc</a>
    </li>
  </ul>
</div>

# <span id="Collect_Suspicious_Files_and_System_Information_with_Trend_Micro">Collect Suspicious Files and System Information with Trend Micro</span>

  1. Download the Anti-Threat Toolkit by clicking your operating system version below:

<a href="https://spnsupport.trendmicro.com/attk/5238c65d-d7d9-4e8d-a695-c82c49d162cf" target="_blank">32-bit</a>

<a href="https://spnsupport.trendmicro.com/attk64/73340FDF-9E0C-4d96-9137-F91EACD45392" target="_blank">64-bit</a>

  1. Read the Trend Micro License Agreement. Once you click I Accept, the download will start.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti6.jpg?w=1500" alt="" data-recalc-dims="1" />

  1. Choose the preferred directory where the tool will be stored then click Save.
  2. Log on to the computer that is possibly infected by a malware. Copy the Anti-Threat Toolkit into the infected computer.
  3. After copying the Anti-Threat Toolkit, right-click the tool and then click Run as administrator.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti7.png?w=1500" alt="" data-recalc-dims="1" />

  1. Click Yes when the User Account Control window appears.
  
    A Command Prompt window will appear to show the system forensic analysis progress.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti8.jpg?w=1500" alt="" data-recalc-dims="1" />

A browser window will appear after the analysis finishes.

  1. Click Proceed to send the information the tool collected to Trend Micro Technical Support. You will receive a temporary ID number that you can use when you contact Trend Micro Technical Support.

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti9.jpg?w=1500" alt="" data-recalc-dims="1" />

  1. The Trend Micro Anti-Threat Toolkit folder will appear on the same folder where you ran the tool.

Go to Trend Micro Anti-Threat Toolkit folder > Output.
  
You will find a .ZIP file with the filename containing the timestamp and GUID.

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti10.jpg?w=1500" alt="" data-recalc-dims="1" />

Do either of the following:

If you have an existing case, send a copy of the .ZIP file together with the temporary ID number to the engineer who is handling your case.

# <span id="Trend_Micro_Anti-Threat_Toolkit">Trend Micro Anti-Threat Toolkit:</span>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">For computers with internet connection<br /> </span>
</p>

<p style="text-align: justify;">
  <a href="https://spnsupport.trendmicro.com/attk/4F52A9E7-5683-4F01-ADDF-2D993326168F" target="_blank"><span style="font-family: Arial; font-size: 10pt;">Online Scan / Clean Tool (32-bit)</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <a href="https://spnsupport.trendmicro.com/attk64/4b815388-ec34-0d78-aa83-b019227a057c" target="_blank"><span style="font-family: Arial; font-size: 10pt;">Online Scan / Clean Tool (64-bit)</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">For computers without internet connection<br /> </span>
</p>

<p style="text-align: justify;">
  <a href="https://spnsupport.trendmicro.com/attk/6CB39656-5F38-4541-BB23-7810C8F78112" target="_blank"><span style="font-family: Arial; font-size: 10pt;">Offline Scan / Clean Tool (32-bit)</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <a href="https://spnsupport.trendmicro.com/attk64/0c4b4ca2-f686-6b3c-50a6-f9e28f6e4722" target="_blank"><span style="font-family: Arial; font-size: 10pt;">Offline Scan / Clean Tool (64-bit)</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Read the Trend Micro License Agreement, then click I Accept to agree with the EULA and download the tool.<br /> </span>
    </div>

  2. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click Save when the File Download window appears.<br /> </span>
    </div>

  3. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Select Desktop as the download location, then click Save.<br /> </span>
    </div>

  4. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Log on to the computer that is possibly infected by a malware. Copy the Anti-Threat Toolkit into the infected computer.<br /> </span>
    </div>

  5. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">After copying the Anti-Threat Toolkit, right-click the tool and then click Run as administrator.<br /> </span>
    </div>

  6. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click Yes when the User Account Control window appears.<br /> </span>
    </div>

  7. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click Scan Now when the Trend Micro Anti-Threat Toolkit window appears.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti11.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">The scan may take some time. The tool will scan your computer and list the threats it finds.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti12.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">The tool will show a summary of the scan. Click Fix Now to clean your computer<br /> </span>
    </div>

# <span id="Trend_Micro_Rootkit_Buster">Trend Micro Rootkit Buster</span>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">To use the Rootkit Buster:<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">Download the Rootkit Buster file that corresponds to your system type and save the file on your desktop. You may <a href="http://esupport.trendmicro.com/solution/en-us/1038680.aspx" target="_blank">check first your version of Windows operating system</a> when you are not sure with your system type.<br /> </span>
</p>

<p style="text-align: justify;">
  <a href="http://files.trendmicro.com/products/rootkitbuster/RootkitBusterV5.0-1180.exe" target="_blank"><span style="font-family: Arial; font-size: 10pt;">32-bit</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <a href="http://files.trendmicro.com/products/rootkitbuster/RootkitBusterV5.0-1180x64.exe" target="_blank"><span style="font-family: Arial; font-size: 10pt;">64-bit</span></a><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">Do either of the following:<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">For Windows XP: Double-click RootkitBuster.exe to run the file.<br /> </span>
</p>

<p style="text-align: justify;">
  <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti13.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">For Windows Vista, 7 and 8: Right-click RootkitBuster.exe, then select Run as administrator. The following error message appears when you do not run the installer with administrator privileges:<br /> </span>
</p>

<p style="text-align: justify;">
  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti14.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Read the license agreement.<br /> </span>
    </div>

  2. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Select I accept the terms of the license agreement, then click Next.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti15.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click Scan Now.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti16.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Wait for the program to finish scanning your computer until you see the result of the scan.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti17.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Tick the detected threats, then click Fix Now.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti18.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Wait for the Trend Micro Rootkit Buster to fix the threats.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti19.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click Restart Now to finish the cleanup.<br /> </span>
    </div>

<p style="text-align: justify;">
  <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti20.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><br /> </span>
</p>

# <span id="Trend_Micro_Rescue_Disk">Trend Micro Rescue Disk</span>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Click <a href="http://free.antivirus.com/us/rescue-disk/index.html">Download</a> to begin.<br /> </span>
    </div>

  2. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">If prompted, click Save or Save As, and save the file on your computer&#8217;s desktop.<br /> </span>
    </div>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">While the installer downloads, prepare one of the following:<br /> </span>
</p>

  * <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Blank CD or DVD (do not use a rewritable disc)<br /> </span>
    </div>

  * <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">Empty USB Drive (128MB or larger)<br /> NOTE: The drive will be reformatted before creating Rescue Disk, and anything already on the USB drive will be lost. Please back up any important files before using a USB drive for Trend Micro Rescue Disk.<br /> </span>
    </div>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;">When you have finished downloading the file, double-click the Trend Micro Rescue Disk icon to start the installer.<br /> </span>
    </div>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">To launch your computer from a CD or DVD, you must set the BIOS to boot from a different device. While the exact procedure differs from computer to computer, the overall process is usually like this:<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">Insert the disc or USB drive into the computer.<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">Restart the computer.<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">When the computer powers up again, look for a BIOS setup message, which often looks like &#8220;Press [KEY] to run Setup&#8221; where [KEY] might be Delete, ESC, or one of the F1–F12 keys.<br /> </span>
</p>

<p style="text-align: justify;">
  <span style="color: black; font-family: Arial; font-size: 10pt;">Once the BIOS Setup Utility has opened, look for a tab labeled Boot, Boot Order, or Boot Options.<br /> </span>
</p>

# <span id="AVG_Antivirus">AVG Antivirus</span>

  1. **Run &#8220;avg\_free\_x64\_all\_2015_*.exe&#8221;**
  
    <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti21.png?w=1500" alt="" data-recalc-dims="1" /> **and select Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti22.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Click on Accept
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti23.png?w=1500" alt="" data-recalc-dims="1" />

  1. **The license number will automatically get generated as part of the Free version of AVG. Make sure there is a license number applied then click Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti24.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Select Standard Install and click Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti25.png?w=1500" alt="" data-recalc-dims="1" />

  1. **This will now start the AVG installation (wait for this process to complete)
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti26.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Once completed. Uncheck &#8220;I want to help AVG improve its products by sending anonymous usage data as part of AVG&#8217;s&#8221; and select Finish
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti27.png?w=1500" alt="" align="left" data-recalc-dims="1" />**
  
** 

  1. **Once installed you will be greeted with the AVG splash screen. Press Scan Now
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti28.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Click Scan Whole Computer to start the AVG scan
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti29.png?w=1500" alt="" data-recalc-dims="1" />

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti30.png?w=1500" alt="" data-recalc-dims="1" />

# <span id="ClamWin_Antivirus">ClamWin Antivirus</span>

  1. **Run &#8220;clamwin-*-setup.exe&#8221;  <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti31.png?w=1500" alt="" data-recalc-dims="1" />and select Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti32.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Accept the License Agreement and select Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti33.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select Anyone who uses this computer (all users) and select Next
  
** 

**
  
<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti34.png?w=1500" alt="" data-recalc-dims="1" />
  
** 

  1. **Verify installation path is set: c:\Program Files (x86)\ClamWin as default and select Next
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti35.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click on Custom Installation and make sure that &#8220;ClamAV Files & ClamWin Files&#8221; are the only objects selected and click Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti36.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti37.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **If you are connected to the Internet – select &#8220;Download Virus Database Files&#8221; if you are not unselect the checkbox.
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti38.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select Install
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti39.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **ClamWin Antivirus will now install
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti40.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select Finish to complete the installation
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti41.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Open ClamWin Antivirus and select the drive mapping you would like to scan (for example to scan the Operating System select (C:) and select Scan
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti42.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **ClamWin Antivirus will now scan the computer for viruses.
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti43.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

# <span id="RootkitRevealer">RootkitRevealer</span>

  1. **Extract RootkitRevealer.zip and run RootKitRevealer.exe <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti44.png?w=1500" alt="" data-recalc-dims="1" />
  
** 
  2. **Click Agree
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti45.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

<p style="margin-left: 18pt;">
  <strong>3. Click Scan<br /> </strong>
</p>

# <span id="Trend_Micro_CWShredder">Trend Micro CWShredder</span>

  1. <div style="text-align: justify;">
      <span style="color: black; font-family: Arial; font-size: 10pt;"><strong>Run cwshredder.exe <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti46.png?w=1500" alt="" data-recalc-dims="1" /> and click &#8220;I Agree&#8221; on the license agreement<br /> </strong></span>
    </div>

<p style="text-align: justify;">
  <img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti47.png?w=1500" alt="" data-recalc-dims="1" /><span style="color: black; font-family: Arial; font-size: 10pt;"><strong><br /> </strong></span>
</p>

  1. **Select Scan Only to scan the computer for any CoolWebSearch malware that may exist on the computer.
  
** 
  2. **If it detects any select Fix.
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti48.png?w=1500" alt="" data-recalc-dims="1" />

# <span id="Malwarebytes_Anti-Malware">Malwarebytes Anti-Malware</span>

  1. **Run mbam-setup-*.exe  <img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti49.png?w=1500" alt="" data-recalc-dims="1" />and select Ok
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti50.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click on Next to start the Malwareytes installation
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti51.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click on &#8220;I accept the agreement&#8221; to accept the agreement and click on Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti52.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select Next to continue installation
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti53.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Verify installation path is: C:\Program Files (x86)\Malwarebytes Anti-Malware and select Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti54.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Verify the below information and click Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti55.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Make Click Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti56.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Verify the installation information is correct and press Install
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti57.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Uncheck &#8220;Enable Free Trial of Malwares Anti-Malware Premium&#8221; and if you have access to the Internet select &#8220;Launch Malwarebytes Anti-Malware&#8221; if you don&#8217;t uncheck this and select Finish
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti58.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Once Malwares Anti-Malware is loaded you will be greeted with the following screen press Scan Now to start the scan
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti59.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Malwarebytes Anti-Malware will than scan the computer for any malware this detects.
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti60.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

# <span id="Spybot_Search_Destroy">Spybot Search & Destroy</span>

  1. **Run &#8220;spybot-*.exe&#8221;**
  
    <img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti61.png?w=1500" alt="" data-recalc-dims="1" /> **and accept lanuage.
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti62.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click Next to start the Spybot installation
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti63.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select &#8220;… installing Spybot for personal use, and will decide later.&#8221; And click Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti64.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select &#8220;I want more control, more feedback and more responsibility&#8221;
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti65.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Click I accept the agreement and select Next
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti66.png?w=1500" alt="" data-recalc-dims="1" />

  1. **Verify the installation path is: C:\Program Files (x86)\Spybot – Search & Destroy 2 and click Next
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti67.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Select Full Installation and click Next
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti68.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Unselect all checkboxes and select Next
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti69.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Verify installation information is correct and click Install
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti70.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Spybot Search and Destroy is now installing
  
** 

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti71.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **If you are connected to the Internet, click on Start a System Scan to download the latest definitions and run a scan if you are not uncheck all and click Finish.
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti72.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Open Spybot and click Cancel on creating the Whitelist.
  
** 

<img src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti73.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

  1. **Click on System Scan and Start a Scan to start a scan of the system for malware.
  
** 

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2015/10/103015_0604_WindowsAnti74.png?w=1500" alt="" data-recalc-dims="1" />**
  
** 

# <span id="Misc">Misc</span>

The Trend Micro support page is a relevant resource: <http://esupport.trendmicro.com/en-us/default.aspx>
