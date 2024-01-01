---
title: Database error when making changes to DHCP reservations
tags:
  - Windows
date: 2016-12-28 00:00:00 +1300
---
'An error occurred while accessing the DHCP database.'
  
<img class="alignnone" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/12/122816_0625_Databaseerr1.png?resize=515%2C179&#038;ssl=1" alt="an error occurred while accessing the DHCP database" width="515" height="179" data-recalc-dims="1" />

One of the issues I have ran into since an upgrade to Windows Server 2012 R2 DHCP servers – was due to multiple processes access the DHCP database when I was attempting to Create or Modify a DHCP v4 reservation.

  1. Adding an exclusion to DHCP.MDB file for Real Time scanning on my antivirus product.
  2. Disabling the Windows indexing service from indexing the DHCP folder.

To disable the Windows indexing service from indexing the DHCP server follow the quick steps below:

  1. Open Windows Explorer – or Computer: on the DHCP server
  2. Navigate to: c:\Windows\System32\DHCP
  3. Click on the General Tab up the top and click Advanced
  4. Uncheck &#8216;For Fast Searching, Allow Indexing Service to Index this Folder.&#8217;
  5. Click Ok

Useful Resources:

Microsoft Anti-Virus Exclusion List &#8211; <a href="https://social.technet.microsoft.com/wiki/contents/articles/953.microsoft-anti-virus-exclusion-list.aspx?WT.mc_id=AZ-MVP-5004796" target="_blank">https://social.technet.microsoft.com/wiki/contents/articles/953.microsoft-anti-virus-exclusion-list.aspx</a>
