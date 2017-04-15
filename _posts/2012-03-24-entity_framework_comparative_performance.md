---
title:  "Entity Framework Comparative Performance"
date:   2012-03-24
canonical: http://blog.staticvoid.co.nz/2012/3/24/entity_framework_comparative_performance
redirect_from:
  - 2012/3/24/entity_framework_comparative_performance
---
<br />
<span style="font-size: large;">Introduction</span><br />
There are heaps of opinions floating round about which ORM is fastest.&nbsp;I've&nbsp;recently been working on improving the performance of a long running sync of a large&nbsp;data set&nbsp;back ended&nbsp;into SQL. During this process there has been a lot of talk about&nbsp;whether&nbsp;Entity Framework was the correct tool for the job and many sites on the net would imply&nbsp;perhaps&nbsp;it&nbsp;isn't&nbsp;the best tool for batch processing. So I decided to do some tests of my own to find out how much slower Entity Framework&nbsp;actually is.<br />
<br />
<span style="font-size: large;">Method</span><br />
During the process of performance tuning on my application and testing out different ORMs I learned a lot about how to get the best performance and when to use specific optimisation. I decided it would also be useful to compare different performance tuning options in my test.<br />
<br />
To do this testing I built a test rig to&nbsp;accurately&nbsp;compare the different frameworks and tuning options. The test framework pairs up technology implementations (eg EntityFramework 5.0.0.0 Beta) with performance scenarios (eg bulk insert of random data), I call this a run.<br />
<br />
To make the results as fair and unbiased as possible the rig was built with the following principals.<br />
<ol>
<li><b>The test database is rebuilt for each run</b>, this means that the state of the database is identical for each run.</li>
<li><b>The order of technology implementations is random</b>, this is to avoid specific runs having an advantage because they come first or last within the test execution.</li>
<li><b>Runs are repeated</b>, the results of a scenario should be&nbsp;reproducible.</li>
<li><b>The worst instance for each run is discarded</b> so that external influences on the run are ignored</li>
<li><b>Each scenario was run against different numbers of items, </b>in this post I've used the following<i> 1,10,100,1000,10000 </i>items.</li>
<li><b>At the end of each run the database state is asserted</b> to confirm that the operations expected were performed</li>
<li><b>Random data is used</b> to ensure that there is no data bias between technologies</li>
<li><b>The same random data is used for each technology in a specific iteration of a scenario</b> so that results are based on the same&nbsp;data set.</li>
</ol>
<div>
All code for the tests are published at&nbsp;<a href="https://github.com/lukemcgregor/StaticVoid.OrmPerformance">https://github.com/lukemcgregor/StaticVoid.OrmPerformance</a>&nbsp;and I would appreciate review of the individual test cases. If you have additional tests, ORMs, or performance improvements I would encourage you to fork the repository and add your tests. That way I can merge them back into the trunk.<br />
<br />
<span style="font-size: large;">Tests</span><br />
I decided to test the following database technologies and tuning options:<br />
<ul>
<li>EntityFramework 4.1</li>
<ul>
<li>Basic Configuration (No optimisations)</li>
<li>AutoDetectChanges Disabled</li>
<li>My Best effort at making it go fast</li>
</ul>
<li>EntityFramework 5.0 beta1</li>
<ul>
<li>Basic Configuration (No optimisations)</li>
<li>AutoDetectChanges Disabled</li>
<li>My Best effort at making it go fast</li>
</ul>
<li>Dapper 1.8</li>
<ul>
<li>Dapper Rainbow&nbsp;</li>
<li>My Best effort at making it go fast</li>
<li><b>EDIT </b>Batching inserts/updates using transactions</li>
</ul>
<li>LINQ to SQL</li>
<ul>
<li>Basic Configuration (No optimisations)</li>
<li>Compiled Queries</li>
<li>No Object Tracking</li>
<li>My Best effort at making it go fast&nbsp;</li>
</ul>
</ul>
<div>
and the following test scenarios</div>
</div>
<div>
<ul>
<li>Insert of N rows to the database, each row contains random data.</li>
<li>Update of N rows to the database, each&nbsp;original&nbsp;row and each update is random data.</li>
<li>Discrete selects of N random rows from the database.</li>
<li>Bulk select of N random rows from the database</li>
<li>Delete of N random rows from the database</li>
</ul>
</div>
<div>
<br />
<span style="font-size: large;">Results</span><br />
<br />
<b>Insert</b><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-PMP0l3LH2nQ/T4lILTFqnbI/AAAAAAAAAKw/W1l_YCap45w/s1600/Insert+Comparison.png" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="400" src="http://1.bp.blogspot.com/-PMP0l3LH2nQ/T4lILTFqnbI/AAAAAAAAAKw/W1l_YCap45w/s640/Insert+Comparison.png" width="640" /></a><a href="http://2.bp.blogspot.com/-9OmRrHE01k0/T4lIL1joA1I/AAAAAAAAAK4/OE1DH5QIe2U/s1600/Insert+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-9OmRrHE01k0/T4lIL1joA1I/AAAAAAAAAK4/OE1DH5QIe2U/s1600/Insert+Reletive+Performance.png" /></a></div>
<br />
<b>Update</b><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-jWRbWk0fB48/T4lIMpFzmkI/AAAAAAAAALA/_VPIboI8P_g/s1600/Update+Comparison.png" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="399" src="http://4.bp.blogspot.com/-jWRbWk0fB48/T4lIMpFzmkI/AAAAAAAAALA/_VPIboI8P_g/s640/Update+Comparison.png" width="640" /></a><a href="http://3.bp.blogspot.com/-8UvvTgwxrBA/T4lINcRoPhI/AAAAAAAAALI/oAfwRguv-zE/s1600/Update+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-8UvvTgwxrBA/T4lINcRoPhI/AAAAAAAAALI/oAfwRguv-zE/s1600/Update+Reletive+Performance.png" /></a></div>
<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
</div>
<b>Bulk Select</b><br />
<a href="http://2.bp.blogspot.com/-wtb2je2NPOQ/T4lIHF_xZlI/AAAAAAAAAKI/vilKlC0ac2U/s1600/Bulk+Select+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="395" src="http://2.bp.blogspot.com/-wtb2je2NPOQ/T4lIHF_xZlI/AAAAAAAAAKI/vilKlC0ac2U/s640/Bulk+Select+Comparison.png" width="640" /></a><br />
<div class="separator" style="clear: both; text-align: center;">
</div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-WEnAV0uf2Wo/T4lIH3-C4DI/AAAAAAAAAKM/-Gi88DsXuUM/s1600/Bulk+Select+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" src="http://3.bp.blogspot.com/-WEnAV0uf2Wo/T4lIH3-C4DI/AAAAAAAAAKM/-Gi88DsXuUM/s1600/Bulk+Select+Reletive+Performance.png" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<b>Discrete Select</b></div>
<div class="separator" style="clear: both; text-align: left;">
<a href="http://4.bp.blogspot.com/-txnAaDhM_e8/T4lIJ-UYVCI/AAAAAAAAAKk/seRef8UNFXI/s1600/Discrete+Select+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="398" src="http://4.bp.blogspot.com/-txnAaDhM_e8/T4lIJ-UYVCI/AAAAAAAAAKk/seRef8UNFXI/s640/Discrete+Select+Comparison.png" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-9uQzOkKwsgc/T4lIKuGoigI/AAAAAAAAAKs/V1EvE3Z7pWA/s1600/Discrete+Select+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-9uQzOkKwsgc/T4lIKuGoigI/AAAAAAAAAKs/V1EvE3Z7pWA/s1600/Discrete+Select+Reletive+Performance.png" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<b>Delete</b></div>
<div class="separator" style="clear: both; text-align: center;">
</div>
<a href="http://3.bp.blogspot.com/-K-7Ou7AO0RI/T4lIIfuPpwI/AAAAAAAAAKU/nj6WyHxHcww/s1600/Delete+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="398" src="http://3.bp.blogspot.com/-K-7Ou7AO0RI/T4lIIfuPpwI/AAAAAAAAAKU/nj6WyHxHcww/s640/Delete+Comparison.png" width="640" /></a><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-JP6grmegMNQ/T4lIJCYZ5RI/AAAAAAAAAKc/56ILfJKrSOU/s1600/Delete+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" src="http://2.bp.blogspot.com/-JP6grmegMNQ/T4lIJCYZ5RI/AAAAAAAAAKc/56ILfJKrSOU/s1600/Delete+Reletive+Performance.png" /></a></div>
I find these results&nbsp;absolutely&nbsp;intriguing, what these show is that it actually isn't very clear which ORM is faster here, its&nbsp;absolutely&nbsp;relative to your target workload, more specifically to the size and type of your operations.<br />
<br />
The data which i have used to compile these results can be found in its raw form&nbsp;and with the graphs <a href="http://dl.dropbox.com/u/37129059/Performance%20Results.xlsx">here</a>.<br />
<br />
<b>Entity Framework 5 with a Small Number of Items</b><br />
One of the really interesting points which I've noticed from my results is that over small numbers of items Entity Framework is the fastest in all tests. This is of critical importance when picking an ORM. What this means is that if you have an application such as a website which is performing a bunch of small requests to your database to render your page Entity Framework 5 is going to be really quick (so long as you follow a few pointers on how to set up your context).<br />
<br />
<b>Deleting Data</b><br />
Dapper and a decent hand crafted query is amazing at deleting data. For this test I used a handcrafted <i>delete where in</i> SQL query. The bonus of doing this is that the whole query is executed in a single SQL statement so will run much faster inside SQL. If your application involves a lot of batch deletes you should seriously&nbsp;conciser&nbsp;handcrafting your query with something like Dapper.<br />
<br />
<b>Entity Framework 4 vs Entity Framework 5</b><br />
I find the comparison of the two versions of entity framework very interesting. If you look at the line graphs what you see is that for small numbers of items Entity Framework 5 is a lot quicker, but what I find very interesting is that as the number of items increase the two versions converge on the same&nbsp;amounts&nbsp;of time across the board. This&nbsp;suggests&nbsp;to me that the ADO.Net team has spent a lot of time optimising Entity Framework for small data sets, and have done a great job.<br />
<br />
<b>Bulk Selects with Small Numbers of Items</b><br />
When doing a <i>select where</i> statement with a small number of matches both Entity Framework 5 and Dapper show a very interesting result, it actually takes longer to perform the query for less items. I have done a lot of runs through and this behavior seems to be repeated every time. Its also important to note here that each of these queries are performed on their own database. I have no idea why this is but I would love to know if someone has any insight on this particular behavior.<br />
<br />
<b>Inserts and Updates</b><br />
<strike>If your application is mostly performing inserts and updates Entity Framework seems to be quite a bit faster than Dapper. My feeling is that this is probably because Entity Framework performs some optimisation before sending the data to the database.</strike>&nbsp;<strike><b>Perhaps&nbsp;someone better with dapper than I could improve Dapper's performance in this area, however I currently&nbsp;don't&nbsp;have any idea how to do this.</b></strike><br />
<b>EDIT:</b> With the help of<a href="http://samsaffron.com/"> Sam Saffron</a>, one of the authors of Dapper we were able to improve the performance of the dapper Insert and Update test cases to below that of Entity Framework. This was achieved by putting the Dapper commands inside a SQL Transaction (see <a href="https://github.com/lukemcgregor/StaticVoid.OrmPerformance/blob/master/Harness.Dapper1-8/DapperBatchConfiguration.cs">here</a> for the actual code). I'm intending on following this up with another post soon.<br />
<br />
<b>Selects</b><br />
If your application is mostly selects Dapper and Linq to SQL are particularly fast for large numbers of items (but again Entity Framework 5 is faster with small numbers of items). My feeling is that this is because Entity framework (even with tracking off) does quite a lot of fiddling with the data after its retrieved from the server.<br />
<br />
<b>General Performance Comparison</b><br />
<strike>With the exception of the delete case, even at large numbers the difference in performance between the different ORMs is not (in my&nbsp;opinion) particularly high. In some cases Entity Framework takes half as much time again over Dapper and in some cases this is reversed. Having said that all of the ORMs are performing within the same orders of magnitude (assuming sensible settings). What this means is that you are unlikely to get&nbsp;enormous performance gains from simply switching ORMs.</strike><br />
<b>EDIT:</b> With the improvement of the Dapper Insert and Update cases Dapper stands out in terms of performance for batch jobs with Entity Framework taking between 126% and 235% of the time that Dapper does. However Entity Framework 5 still appears to be faster in all cases for a small number of items.<br />
<br />
<span style="font-size: large;">Conclusions/TLDR</span><br />
If you are picking an ORM to use and want to pick based on performance alone the choice is not entirely simple.&nbsp;For batch based application Dapper is clearly faster. But for user applications which involve a queries involving only a small number of items (ie selects returning under 1000 results) and inserts/updates affecting any number of entities, Entity Framework is clearly faster.<br />
<br />
In terms of the batch process I have been writing these results have given me confidence in the performance of Entity Framework and I have no plans to change at this stage. It has shown me that Entity Framework is not significantly slower than other ORMs and in the majority of my application its actually faster (as I am&nbsp;primarily&nbsp;doing updates and inserts).<br />
<br />
I would encourage you to download the test framework and look at my test cases, improve them if you can and add your own. I'm really keen to watch this space more and add some more ORMs in the future.<br />
<br />
<span style="font-size: large;">Other things of note</span><br />
<ul>
<li>I don't claim to be an expert on the ORMs tested, there may well be additional ways to tweek extra performance out of the specific scenarios. If you know a better way please let me know and I will update my results accordingly.</li>
<li>My results are produced from executing these tests against a remote SQL 2008 R2 server running on a VM (but on different physical hardware). This is not a production test and the numbers represented here would be greatly reduced by running this in a faster environment. Having said this the general trends&nbsp;portrayed&nbsp;should be similar regardless of the speed of the individual test environments.</li>
<li>.NET 4.5 has been used in these test cases because I wanted to test against the EF 5 beta as it claims to have improved performance. This makes a difference to the overall performance of all the scenarios. If you would like to see the performance using .NET 4 I would encourage you to build the tests using .NET 4 and run them for yourself.</li>
<li>These tests take a long time to run (several hours), I would recommend running them overnight.</li>
<li>My recommendation is to run the tests in release mode without debugging as this will give you the best results.&nbsp;</li>
</ul>
<div>
<span style="font-size: large;">Thanks</span></div>
</div>
<div>
I'm&nbsp;very&nbsp;grateful&nbsp;to <a href="http://samsaffron.com/">Sam Saffron</a> for his help getting my Dapper test case running faster.</div>
