---
title: Install Visio 2010 Standard instead of Premium
author: Luke
lpermalink: /win/install-visio-2010-standard-instead-premium/
categories:
  - Windows
---
Unfortunately, volume license editions of Visio 2010 install Premium by default – this can then be downgraded to Visio standard by changing the Product key to Standard edition.

However – come annual Microsoft True up you don't want any surprises or manual intervention! This is how you can change Visio to be installed by Standard or another SKU automatically without prompting.



  1. Download the latest Visio 2010 ISO from Microsoft Volume Licensing
  2. Extract the ISO using a tool such as 7-Zip
  3. Navigate to the folder containing VisioWW.msi – should be in the x86 or x64 folder depending on architecture.
  4. Right click and select New, Text Document
  5. Rename the newly created text document to: config.xml (you may have to show Extensions to rename the file extension from txt to xml).
  6. Open config.xml
  7. Type in the following and save, Once saved – install Visio normally and it should install with the correct SKU ie Visio 2010 Standard.


{% gist 8a1404a51ca472d507622a90ec9a9ec8 %}


Note: Replace the PIDKey value with any of the Product Keys listed below to change the default install SKU:

Visio Professional 2010 - 7MCW8-VRQVK-G677T-PDJCM-Q8TCP

Visio Premium 2010 - D9DWC-HPYVV-JGF4P-BTWQB-WX8BJ
