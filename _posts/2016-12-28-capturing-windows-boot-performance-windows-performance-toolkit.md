---
title: Capturing Windows boot performance with the Windows Performance Toolkit
permalink: /win/capturing-windows-boot-performance-windows-performance-toolkit/
image: /wp-content/uploads/2016/12/122816_0751_Howtocaptur5.png
categories:
  - Windows
---
The Windows Performance Toolkit, developed by Microsoft has 3 separate tools and are key to solving a lot of boot and general performance issues:

•    Windows Performance Recorder

•    Windows Performance Analyzer

•    Xperf

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Download_Windows_Performance_Toolkit"><span class="toc_number toc_depth_1">1</span> Download Windows Performance Toolkit</a>
    </li>
    <li>
      <a href="#Run_Windows_Performance_Recorder"><span class="toc_number toc_depth_1">2</span> Run Windows Performance Recorder</a>
    </li>
    <li>
      <a href="#Run_Windows_Performance_Analyzer"><span class="toc_number toc_depth_1">3</span> Run Windows Performance Analyzer</a>
    </li>
    <li>
      <a href="#Useful_resources"><span class="toc_number toc_depth_1">4</span> Useful resources</a>
    </li>
  </ul>
</div>

### <span id="Download_Windows_Performance_Toolkit">Download Windows Performance Toolkit</span>

This can be downloaded by going to the Microsoft website and looking for the latest Windows Assessment and Deployment Toolkit for the operating system you want to analyze – for example: Windows 10

<a href="https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit" target="_blank">https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit</a>

Download and run, we only need the Windows Performance Toolkit portion of the ADK:

<img class="alignnone" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0751_Howtocaptur1.png?resize=697%2C404&#038;ssl=1" alt="Windows Performance Toolkit" width="697" height="404" data-recalc-dims="1" />

Once installed navigate to: C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit

_Tip: You can copy the Redistributables folder if you need to install the Windows Performance Toolkit only on another computer.
  
_ 

### <span id="Run_Windows_Performance_Recorder">Run Windows Performance Recorder</span>

We only need too: WPRUI.EXE – Windows Performance Recorder & WPA.EXE – Windows Performance Analyzer.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0751_Howtocaptur2.png?w=1500&#038;ssl=1" alt="" data-recalc-dims="1" />

Run WPRUI to launch Windows Performance Recorder

Change the Performance Scenario to Boot, and File

Select Resource Analysis and click CPU usage

_Tip: You can add more: File I/O, Networking I/O, GPU usage etc if you know what in particular may be causing your boot slowness, the more you add the more data and complexity is added. I would recommend to only add additional resource analytics when required._

<img class="alignnone" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0751_Howtocaptur3.png?resize=659%2C518&#038;ssl=1" alt="Windows Performance Recorder" width="659" height="518" data-recalc-dims="1" />

Click Start to select where your boot traces will go and click Ok to start your boot traces, this will restart your computer 3 times.

_Tip: If you need to login, please make sure you login quickly during each trace as the longer you leave it unattended the more data and delay it will collect.
  
_ 

### <span id="Run_Windows_Performance_Analyzer">Run Windows Performance Analyzer</span>

Once the computer has been restarted 3 times and your traces have been complete navigate back to: C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit and click on WPR.EXE to open the Windows Performance Analyzer or click Open in WPA from the Windows Performance Recorder dialog.

The Windows Performance Analyzer will be our canvas in analyzing issues, you can expand areas like System Activity to dig into Processes, Services. Just drag the data onto the Analysis screen to go through it

<img src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0751_Howtocaptur4.png?w=1500&#038;ssl=1" alt="" data-recalc-dims="1" />

From here you can drill down into the data to find the cause or improvements for your login time, from here I can see one of the delays of my system is the CortanaUI.

I am running this on a 16GB i7 4GHZ machine running on an SSD so it isn&#8217;t really a good example, but have used this in the past to work out that my login was slow because Lync had logging turned on.

<img src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0751_Howtocaptur5.png?w=1500&#038;ssl=1" alt="" data-recalc-dims="1" />

Hopefully this gets you through the first steps in diagnosis and resolving your performance issues.

### <span id="Useful_resources">Useful resources</span>

Troubleshooting Windows Internals when unexpected events happen &#8211; <a href="https://channel9.msdn.com/events/Ignite/New-Zealand-2016/M405" target="_blank">https://channel9.msdn.com/events/Ignite/New-Zealand-2016/M405</a>

Investigating website performance with Windows Performance Toolkit &#8211; <a href="https://github.com/MicrosoftEdge/MicrosoftEdge-Documentation/tree/master/performance-analysis/windows-performance-toolkit" target="_blank">https://github.com/MicrosoftEdge/MicrosoftEdge-Documentation/tree/master/performance-analysis/windows-performance-toolkit</a>

Slow Boot Slow Logon (SBSL), A Tool Called XPerf and Links You Need To Read &#8211; <a href="https://blogs.technet.microsoft.com/askpfeplat/2012/06/09/slow-boot-slow-logon-sbsl-a-tool-called-xperf-and-links-you-need-to-read/" target="_blank">https://blogs.technet.microsoft.com/askpfeplat/2012/06/09/slow-boot-slow-logon-sbsl-a-tool-called-xperf-and-links-you-need-to-read/</a>
