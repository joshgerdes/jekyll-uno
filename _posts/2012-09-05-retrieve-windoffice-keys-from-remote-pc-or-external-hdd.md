---
id: 1613
title: Retrieve Windows/Office Keys from Remote PC or External HDD
date: 2012-09-05T11:00:38+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1613
permalink: /win/retrieve-windoffice-keys-from-remote-pc-or-external-hdd/
dsq_thread_id:
  - "5090972682"
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "21"
categories:
  - Windows
---
Using a Windows utility called ProduKey you can retrieve the product keys for Microsoft Windows and Office.

<ol start="1">
  <li>
    First click “<a title="Produ Key" href="http://www.nirsoft.net/utils/product_cd_key_viewer.html" target="_blank">here</a>” to <strong>download</strong> (the link is down the bottom, you want the ZIP file)
  </li>
  <li>
    Open the saved file and <strong>extract</strong> <strong>to</strong> a <strong>folder</strong> that is easily accessible
  </li>
  <li>
    <strong>Open</strong> <strong>ProduKey</strong>.exe and it will automatically retrieve the product keys for the local machine.
  </li>
  <li>
    To <strong>recover</strong> the keys <strong>for</strong> another <strong>Windows</strong> installation, <strong>click</strong> <strong>File</strong>, Select <strong>Source</strong>
  </li>
  <li>
    Select <strong>Load</strong> the Product Keys from <strong>External</strong> <strong>Windows</strong> <strong>Directory</strong> and <strong>click</strong> <strong>Browse</strong> to <strong>locate</strong> the <strong>Windows</strong> directory you want to <strong>retrieve</strong> the <strong>keys</strong> for.
  </li>
</ol>

Note: Using this utility you can also recover the keys using a software hive and remote computers on the network _(you have admin access to)._

Note: Below are the command prompts commands to run the tool from the windows Command Prompt.

_produkey.exe /remote Server01_

_produkey.exe /remotefile &#8220;c:tempcomputers.txt&#8221;_

_produkey.exe /regfile &#8220;F:WINNTsystem32configsoftware&#8221;_

_produkey.exe /windir &#8220;c:winnt&#8221; /shtml &#8220;c:temppk.html&#8221;_

_produkey.exe /remoteall_

_produkey.exe /remotealldomain MyDomain_

_produkey.exe /iprange 192.168.1.10 192.168.1.50_

_produkey.exe /stab &#8220;&#8221; >> c:tempprd.txt_

_produkey.exe /OfficeKeys 0 /WindowsKeys 1 /shtml f:tempkeys.html_

&nbsp;