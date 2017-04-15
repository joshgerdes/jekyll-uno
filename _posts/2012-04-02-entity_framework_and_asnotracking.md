---
title:  "Entity Framework and AsNoTracking"
date:   2012-04-26
canonical: http://blog.staticvoid.co.nz/2012/4/2/entity_framework_and_asnotracking
redirect_from:
  - 2012/4/2/entity_framework_and_asnotracking
---
<span style="font-size: large;">TLDR</span><br />
In a nutshell you should use .AsNoTracking() in any Entity Framework query which you intend to use only for reading data. This will ensure minimal memory usage and optimal performance in these cases.<br />
<br />
<span style="font-size: large;">What AsNoTracking Does</span><br />
Entity Framework exposes a number of &nbsp;performance tuning options to help you optimise the&nbsp;performance&nbsp;of your applications. One of these tuning options is .AsNoTracking(). This optimisation allows you to tell Entity Framework not to track the results of a query. This means that Entity Framework performs no additional processing or storage of the entities which are returned by the query. However it also means that you cant update these entities without reattaching them to the tracking graph.<br />
<br />
<span style="font-size: large;">AsNoTracking Performance</span><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-W9P-nNJSSwQ/T3mH3RsqZ2I/AAAAAAAAAJo/zOvRyOKfYys/s1600/AsNoTracking+-+Execution+Time.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="351" src="http://4.bp.blogspot.com/-W9P-nNJSSwQ/T3mH3RsqZ2I/AAAAAAAAAJo/zOvRyOKfYys/s640/AsNoTracking+-+Execution+Time.png" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-4ZnsgOffppc/T3mH4uotdyI/AAAAAAAAAJ4/LG3dCelK8rc/s1600/AsNoTracking+-+Reletive+Execution+Time.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-4ZnsgOffppc/T3mH4uotdyI/AAAAAAAAAJ4/LG3dCelK8rc/s1600/AsNoTracking+-+Reletive+Execution+Time.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-QmMNZ6wPg7o/T3mH3--4k9I/AAAAAAAAAJs/ODDP4Z9VAR0/s1600/AsNoTracking+-+Memory+Usage.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="351" src="http://3.bp.blogspot.com/-QmMNZ6wPg7o/T3mH3--4k9I/AAAAAAAAAJs/ODDP4Z9VAR0/s640/AsNoTracking+-+Memory+Usage.png" width="640" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-cROuRsD5GhE/T3mH5p2tZtI/AAAAAAAAAJ8/_oU6x-6uQzs/s1600/AsNoTracking+-+Reletive+Memory+Usage.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-cROuRsD5GhE/T3mH5p2tZtI/AAAAAAAAAJ8/_oU6x-6uQzs/s1600/AsNoTracking+-+Reletive+Memory+Usage.png" /></a></div>
<br />
As you can see AsNoTracking can save both execution time and memory usage. The benefits of AsNoTracking are relative to the number of items which you are retrieving, so applying this option becomes really important when retrieving a large number of items.<br />
<br />
One case I have found this particularly valuable is pre-fetching a large table for an in memory cache.<br />
<br />
<span style="font-size: large;">How to use AsNoTracking</span><br />
AsNoTracking is very easy to use in your application, simply do the following:<br />
<ul>
<li>Make sure you are using System.Data.Entity<br /><div class="MsoNormal" style="background-attachment: initial; background-clip: initial; background-color: white; background-image: initial; background-origin: initial; background-position: initial initial; background-repeat: initial initial; margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas;">using</span><span style="font-family: Consolas;">&nbsp;System.Data.Entity;<br /><br /><span style="font-size: x-small;"><o:p></o:p></span></span></div>
</li>
<li>Include .AsNoTracking() on your query<br /><span style="color: blue; font-family: Consolas; line-height: 115%;">var</span><span style="font-family: Consolas; line-height: 115%;">&nbsp;items&nbsp;=&nbsp;Context.MyEntityCollection.AsNoTracking().Where(e&nbsp;=&gt;&nbsp;e.MyFlag);</span></li>
</ul>
<br />
<span style="font-size: large;">When to use AsNoTracking</span><br />
As you have seen there are significant performance gains to be had by using AsNoTracking, especially when using the Entity Framework Snapshot tracker. If you are using the proxy tracker the performance gains are smaller.<br />
This means you should use this tuning option on all queries for entities you&nbsp;don't&nbsp;want to save back to the database. In a CQRS sense you should probably apply this option globally across your read path to reduce your memory and processing footprint.<br />
It is important however not to use this tuning option when you intend to update the entity as this will mean that Entity Framework has no way of knowing that it needs to save your changes back to the database.<br />
<br />
<span style="font-size: large;">Things to Note</span><br />
<ul>
<li>My results are produced from executing these tests against a remote SQL 2008 R2 server running on a VM (but on different physical hardware). This is not a production test and the numbers represented here would be greatly reduced by running this in a faster environment. Having said this the general trends portrayed should be similar regardless of the speed of the individual test environments.</li>
<li>.NET 4.5 has been used in these test cases because I wanted to test against the EF 5 beta as it claims to have improved performance. This makes a difference to the overall performance of all the scenarios. If you would like to see the performance using .NET 4 I would encourage you to build the tests using .NET 4 and run them for yourself.</li>
</ul>
<br />
