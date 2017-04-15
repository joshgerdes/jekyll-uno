---
title:  "The affect of latency on MSSQL INSERTs"
date:   2012-08-27
canonical: http://blog.staticvoid.co.nz/2012/8/27/the_affect_of_latency_on_mssql_inserts
redirect_from:
  - 2012/8/27/the_affect_of_latency_on_mssql_inserts
---
<div class="separator" style="clear: both; text-align: left;">
When dealing with any networked system a number of factors become important which do not apply when writing applications which run on a single machine. As a developers its very easy to overlook some of the aspects of developing for networked systems. The <a href="http://en.wikipedia.org/wiki/Fallacies_of_Distributed_Computing">Fallacies of Distributed Computing</a> remind us not to make assumptions about networks.</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
The second fallacy of distributed computing is that <i>latency is zero</i>. In this article we are going to look at the impacts of latency on insert&nbsp;performance&nbsp;and especially how latency affects each of the bulk insert scenarios which were discussed in my previous article&nbsp;<a href="http://blog.staticvoid.co.nz/2012/08/mssql-and-large-insert-statements.html">MSSQL and large INSERT statements</a>.</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
I have selected several different amounts of latency as below:</div>
<div class="separator" style="clear: both; text-align: left;">
</div>
<ul>
<li>No added latency, this simulates a typical scenario where your DB server is in the same rack as your client.</li>
<li>5ms, this is a fairly low latency scenario which simulates your DB server being on the same campus/data center&nbsp;as your client but behind a few routers.</li>
<li>10ms, this simulates your DB server being in the same city as your client but not the same campus.</li>
<li>30ms, this simulates a cross country connection where your DB server may be in a different city to your client.</li>
<li>100ms, if you are unfortunate enough to have your DB on the other side of a major ocean&nbsp;you're&nbsp;in big trouble.</li>
</ul>
<br />
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
<span style="font-size: large;">Latency and basic SQL Command inserts</span></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-QwrXRtk7OPY/UDmsBqZCKKI/AAAAAAAAASc/cwU0bihpF38/s1600/Latency+Impact+on+Basic+SQL+Commands.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-QwrXRtk7OPY/UDmsBqZCKKI/AAAAAAAAASc/cwU0bihpF38/s1600/Latency+Impact+on+Basic+SQL+Commands.png" /></a></div>
<br />
As we can see from the above graph that latency linearly increases the time taken to insert each row. We can see this as on our log graph the curves appear offset but have no apparent&nbsp;differences&nbsp;in the steepness of the curves. However when we look at the actual time impact that this has it is fairly clear that latency is not our friend here. For example inserting 1000 rows at 5ms latency takes us around 7.5s whereas with 100ms latency those same 1000 rows take 103s (which matches conceptually with a direct linear correlation, 95ms * 1000 <i>rows </i>+ 7.5s&nbsp;<i>5ms baseline</i> = 102.5s).<br />
<br />
<span style="font-size: large;">How our scenarios compare with latency</span><br />
<span style="font-size: large;"><br /></span>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-0NnvucejGU8/UDsZgh-1JkI/AAAAAAAAATQ/UoMevogpcpI/s1600/No+added+Latency.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-0NnvucejGU8/UDsZgh-1JkI/AAAAAAAAATQ/UoMevogpcpI/s1600/No+added+Latency.png" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-JEmJ33Rg8Yo/UDsZfcuhN3I/AAAAAAAAATM/IaF9Y3jbLeA/s1600/5ms+Latency.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-JEmJ33Rg8Yo/UDsZfcuhN3I/AAAAAAAAATM/IaF9Y3jbLeA/s1600/5ms+Latency.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-I_DXj2xWcUM/UDsZdjVd0cI/AAAAAAAAAS8/H7nN-w0WpOE/s1600/10ms+Latency.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-I_DXj2xWcUM/UDsZdjVd0cI/AAAAAAAAAS8/H7nN-w0WpOE/s1600/10ms+Latency.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-vBnLx9hPP1M/UDsZel6mc1I/AAAAAAAAATA/ov7aRb4ymnI/s1600/30ms+Latency.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-vBnLx9hPP1M/UDsZel6mc1I/AAAAAAAAATA/ov7aRb4ymnI/s1600/30ms+Latency.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-GfPfHh9qQVo/UDsZchY8waI/AAAAAAAAAS0/VCHbx-MH_Mo/s1600/100ms+Latency.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-GfPfHh9qQVo/UDsZchY8waI/AAAAAAAAAS0/VCHbx-MH_Mo/s1600/100ms+Latency.png" /></a></div>
<br />
As you can see as latency increases, a basic SQL command approach performs&nbsp;comparability&nbsp;worse however each of our three alternatives remain&nbsp;comparability&nbsp;similar to each other. This shows that the affect of latency is substantially lower on each of our alternate methods of inserting data.<br />
<br />
<span style="font-size: large;">What does it mean for developing applications</span><br />
<br />
For developers and admins alike it is particularly important to understand the potential impacts latency can have on SQL performance. Whats more these problems are not going to be limited to insert based statements; every&nbsp;call to a database incurs a non-zero latency cost.<br />
<br />
With cloud computing and geographically&nbsp;dispersed&nbsp;companies&nbsp;becoming&nbsp;more&nbsp;prevalent&nbsp;data is not always located close to where it is used. While this isn't ideal by paying attention to latency when we construct applications and&nbsp;frameworks&nbsp;makes us far more&nbsp;resilient&nbsp;to higher latency scenarios when they do occur. Remember the&nbsp;<a href="http://en.wikipedia.org/wiki/Fallacies_of_Distributed_Computing">Fallacies of Distributed Computing</a>&nbsp;and&nbsp;don't&nbsp;assume that latency is insignificant.<br />
<br />
With SQL batching multiple statements into a single statement or transmission will save round trips which means they will cope a lot better with latency.<br />
<br />
My raw data and graphs can be downloaded <b><a href="https://dl.dropbox.com/u/37129059/Performance%20results%20-%20latency%20comparisons.xlsx">here</a></b>.<br />
<br />
<b>Note</b>: in this article when discussing latency we are&nbsp;considering&nbsp;<b>round trip time (RTT)&nbsp;</b>not one directional latency
