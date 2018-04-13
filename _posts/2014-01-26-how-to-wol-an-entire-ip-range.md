---
title: How to WOL an entire IP range
permalink: /win/how-to-wol-an-entire-ip-range/
categories:
  - Windows
---
WOL (Wake on Lan) functions – can be extremely useful especially in remote management and deployment of resources. I have come across a neat little free utility named: <a href="http://www.softperfect.com/products/networkscanner/" target="_blank">SoftPerfect Network Scanner</a> which although being freeware comes with a manner of useful functionality from small to large WANs so I recommend to anyone having a flick through the utility. 

  1. First download the utility &#8211; <a href="http://www.softperfect.com/products/networkscanner/" target="_blank">SoftPerfect Network Scanner</a> and save to an easily locatable location _– ie Desktop or My Documents/Downloads_. 
  2. Extract the netscan zip file. There are 2 folders – one for 32 or one for 64 bit. 
  3. Open netscan.exe 
  4. In the Range from fields type the IP range you would like to scan – ie 192.168.1.1 to 192.168.1.255 and press Start Scanning to the right. 
  5. Depending on the size of your network – this may take anywhere from a few seconds to minutes. 
  6. Once completed press Ctrl+A to select all devices _(You can also go into View, Quick Filter Hosts & select Shared Folders to help distinguish what machines are actually workstations)._ 
  7. Right click and select Wake-On-LAN, Send Wake-On-LAN signal to send the WOL packet to the workstations in the IP range. 

Note: What I would recommend doing – is doing this process while you know the workstations have been started and instead of sending the Wake-On-LAN signal in Step 8 – select Save MAC to WOL Manager. You can then go to Options on the top menu of the Network Scanner and select Wake-On-LAN Manager – here you can add more workstations – clear the workstations by hostname/mac address and subnet that you do not want to include and specify a delay in sending out the Wake-On-LAN packets between workstations.
