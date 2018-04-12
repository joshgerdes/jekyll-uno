---
id: 3957
title: Install Visio 2010 Standard instead of Premium
date: 2016-12-28T20:31:10+00:00
author: Luke
layout:
  - ""
guid: https://luke.geek.nz/?p=3957
permalink: /win/install-visio-2010-standard-instead-premium/
sidebar:
  - ""
footer:
  - ""
header_title_bar:
  - ""
header_transparency:
  - ""
post_views_count:
  - "4"
mfn-post-love:
  - "0"
categories:
  - Windows
---
Unfortunately, volume license editions of Visio 2010 install Premium by default – this can then be downgraded to Visio standard by changing the Product key to Standard edition.

However – come annual Microsoft True up you don&#8217;t want any surprises or manual intervention! This is how you can change Visio to be installed by Standard or another SKU automatically without prompting.



  1. Download the latest Visio 2010 ISO from Microsoft Volume Licensing
  2. Extract the ISO using a tool such as 7-Zip
  3. Navigate to the folder containing VisioWW.msi – should be in the x86 or x64 folder depending on architecture.
  4. Right click and select New, Text Document
  5. Rename the newly created text document to: config.xml (you may have to show Extensions to rename the file extension from txt to xml).
  6. Open config.xml
  7. Type in the following and save &#8211; Once saved – install Visio normally and it should install with the correct SKU ie Visio 2010 Standard.

<div class="oembed-gist">
  <noscript>
    View the code on <a href="https://gist.github.com/lukemurraynz/8a1404a51ca472d507622a90ec9a9ec8">Gist</a>.
  </noscript>
</div>

Note: Replace the PIDKey value with any of the Product Keys listed below to change the default install SKU:

<div>
  <table style="border-collapse: collapse" border="0">
    <colgroup> <col style="width: 188px" /> <col style="width: 274px" /></colgroup> <tr style="height: 20px">
      <td style="background: white;padding-left: 7px;padding-right: 7px;border-top: none;border-left: solid black 0.5pt;border-bottom: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt"><strong>Visio Standard 2010</strong></span>
          </li>
        </ul>
      </td>
      
      <td style="padding-left: 7px;padding-right: 7px;border-top: none;border-bottom: solid black 0.5pt;border-right: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt">767HD-QGMWX-8QTDB-9G3R2-KHFGJ</span>
          </li>
        </ul>
      </td>
    </tr>
    
    <tr style="height: 35px">
      <td style="background: white;padding-left: 7px;padding-right: 7px;border-left: solid black 0.5pt;border-bottom: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt"><strong>Visio Professional 2010</strong></span>
          </li>
        </ul>
      </td>
      
      <td style="padding-left: 7px;padding-right: 7px;border-bottom: solid black 0.5pt;border-right: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt">7MCW8-VRQVK-G677T-PDJCM-Q8TCP</span>
          </li>
        </ul>
      </td>
    </tr>
    
    <tr style="height: 18px">
      <td style="background: white;padding-left: 7px;padding-right: 7px;border-top: none;border-left: solid black 0.5pt;border-bottom: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt"><strong>Visio Premium 2010</strong></span>
          </li>
        </ul>
      </td>
      
      <td style="padding-left: 7px;padding-right: 7px;border-top: none;border-bottom: solid black 0.5pt;border-right: solid black 0.5pt">
        <ul>
          <li>
            <span style="color: black;font-family: Verdana;font-size: 8pt">D9DWC-HPYVV-JGF4P-BTWQB-WX8BJ</span>
          </li>
        </ul>
      </td>
    </tr>
  </table>
</div>