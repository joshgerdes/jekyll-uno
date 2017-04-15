---
title:  "MSSQL and large INSERT statements"
date:   2012-08-17
canonical: http://blog.staticvoid.co.nz/2012/8/17/mssql_and_large_insert_statements
redirect_from:
  - 2012/8/17/mssql_and_large_insert_statements
---
When Entity Framework was made open source (which by the way I think is awesome) I posted a possible improvement to the framework which could improve performance especially in scenarios where a set of rows are inserted into a table. There are several different methods of inserting large amounts of data into SQL.<br />
<br />
In this post I'm going to outline each approach to bulk inserts and any issues with the approach and then do a&nbsp;comparison&nbsp;on the actual performance of these different methods.<br />
<br />
<span style="font-size: large;">Appending all of the statements into a single command text</span><br />
<br />
Queries to a SQL server are&nbsp;inherently&nbsp;ordered in nature, we cant insert a new row until the previous one is written as SQL has to lock the table to perform our insert operation. This means that for each row we insert we need to go through a series of steps, each of which takes time.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-HTe0IQ1_vqA/UCyGXMG1EwI/AAAAAAAAARM/jJIhGdvQ2x8/s1600/SQL+Query+Execution.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="48" src="http://2.bp.blogspot.com/-HTe0IQ1_vqA/UCyGXMG1EwI/AAAAAAAAARM/jJIhGdvQ2x8/s640/SQL+Query+Execution.png" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<span style="text-align: left;">The more latency on our network the longer the green blocks become.&nbsp;</span>So if these are the steps which we go through for a single insert, what does it look like for multiple inserts.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-2Da-5Q-F8F0/UCyHhRZqVYI/AAAAAAAAARU/WQRUl45uzaU/s1600/SQL+Query+Execution+-+multiples.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="16" src="http://2.bp.blogspot.com/-2Da-5Q-F8F0/UCyHhRZqVYI/AAAAAAAAARU/WQRUl45uzaU/s640/SQL+Query+Execution+-+multiples.png" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
As you can see we spend a lot of time doing all of the wrapping around the statement and not a lot of time actually inserting rows in SQL.&nbsp;</div>
<br />
By appending all of the statements into a single command text what we are essentially doing is bundling all of the&nbsp;separate&nbsp;actions we need to perform in out insert&nbsp;together. This give us something like the following:<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-3RpUOi5OFnA/UCyKg_TFRTI/AAAAAAAAARs/h8wZJ8jH9G8/s1600/SQL+Query+Execution+-+multiples+batched.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="32" src="http://2.bp.blogspot.com/-3RpUOi5OFnA/UCyKg_TFRTI/AAAAAAAAARs/h8wZJ8jH9G8/s640/SQL+Query+Execution+-+multiples+batched.png" width="640" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
As you can see this theoretically makes the query much more efficient.</div>
<br />
An example of this is if we put the following into a single commandtext<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">INSERT</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: blue;">INTO</span> <span style="color: teal;">[StaticVoid.OrmPerformance.Test]</span><span style="color: grey;">.</span><span style="color: teal;">[dbo]</span><span style="color: grey;">.</span><span style="color: teal;">[TestEntities]</span> <o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: teal; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">[TestString]</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: teal;">[TestDate]</span><span style="color: grey;">,</span> <span style="color: teal;">[TestInt]</span><span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">VALUES </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'some
gumph'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'2012-1-1'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">1<span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">INSERT</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: blue;">INTO</span> <span style="color: teal;">[StaticVoid.OrmPerformance.Test]</span><span style="color: grey;">.</span><span style="color: teal;">[dbo]</span><span style="color: grey;">.</span><span style="color: teal;">[TestEntities]</span> <o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: teal; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">[TestString]</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: teal;">[TestDate]</span><span style="color: grey;">,</span> <span style="color: teal;">[TestInt]</span><span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">VALUES </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'some
gumph 2'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'2012-1-2'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">2<span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">INSERT</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: blue;">INTO</span> <span style="color: teal;">[StaticVoid.OrmPerformance.Test]</span><span style="color: grey;">.</span><span style="color: teal;">[dbo]</span><span style="color: grey;">.</span><span style="color: teal;">[TestEntities]</span> <o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: teal; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">[TestString]</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;"> <span style="color: teal;">[TestDate]</span><span style="color: grey;">,</span> <span style="color: teal;">[TestInt]</span><span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">VALUES </span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'some
gumph 3'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">'2012-1-3'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt; mso-font-kerning: 0pt;">3<span style="color: grey;">)<o:p></o:p></span></span></div>
<br />
<br />
<span style="font-size: large;">Using a multi-row insert statement (Aka Row Constructors)</span><br />
<br />
Like a single command text a multi insert statement has the benefit of reducing the number of round trips to the database. In addition inserting multiple rows with a single statement improves the efficiency of the actual SQL execution as it is executed all in one hit. This means that it only needs to do all the fun stuff that SQL need to do for every query once (like generating query plans, locking tables and other things I&nbsp;don't&nbsp;really understand). This basically gets us back to:<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-HTe0IQ1_vqA/UCyGXMG1EwI/AAAAAAAAARM/jJIhGdvQ2x8/s1600/SQL+Query+Execution.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" height="48" src="http://2.bp.blogspot.com/-HTe0IQ1_vqA/UCyGXMG1EwI/AAAAAAAAARM/jJIhGdvQ2x8/s640/SQL+Query+Execution.png" width="640" /></a></div>
<br />
<br />
An example of a multi-row insert statement is the following<br />
<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt;">INSERT</span><span style="font-family: Consolas; font-size: 9.5pt;">&nbsp;<span style="color: blue;">INTO</span>&nbsp;<span style="color: teal;">[StaticVoid.OrmPerformance.Test]</span><span style="color: grey;">.</span><span style="color: teal;">[dbo]</span><span style="color: grey;">.</span><span style="color: teal;">[TestEntities]</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">(</span><span style="color: teal; font-family: Consolas; font-size: 9.5pt;">[TestString]</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt;">&nbsp;<span style="color: teal;">[TestDate]</span><span style="color: grey;">,</span>&nbsp;<span style="color: teal;">[TestInt]</span><span style="color: grey;">)</span><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt;">VALUES&nbsp;</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'some gumph'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'2012-1-1'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt;">1<span style="color: grey;">)</span></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="color: grey; font-family: Consolas; font-size: 13px;">,</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'some gumph 2'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'2012-1-2'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt;">2<span style="color: grey;">)</span></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="color: grey; font-family: Consolas; font-size: 13px;">,</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">(</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'some gumph 3'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="color: red; font-family: Consolas; font-size: 9.5pt;">'2012-1-3'</span><span style="color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="font-family: Consolas; font-size: 9.5pt;">3<span style="color: grey;">)</span></span></div>
<br />
As you can see this is also a lot less text than the above example so it has an additional benefit of reducing the size of the data which needs to be transmitted (and parsed).<br />
<br />
One of the interesting things about multi-row insert statements is that MSSQL actually appears to have some limits on the query itself.<br />
<br />
<br />
<ul>
<li>A maximum of 1000 rows can be inserted with row constructors. This is a hard limit which means you get an exception when exceeding this limit.</li>
<li>When you exceed 1000 values in your statement SQL shifts its optimisations to reduce the size of its query plans, this means that there is a sharp spike in query execution times when this value is exceeded.&nbsp;</li>
</ul>
<br />
<b>NOTE&nbsp;</b>row constructors are only&nbsp;available&nbsp;in SQL 2008 and above.<br />
<br />
<br />
<span style="font-size: large;">SQL bulk copy</span><br />
<br />
The very best insert performance for inserting large volumes of data can be attained by using SQL Bulk Copy. This method bypasses the SQL query language entirely and streams data directly to SQL.<br />
<br />
While SQL bulk copy is exceptionally fast at inserting large volumes of data there are several dowsides to using this method.<br />
<br />
<ul>
<li>There is no way to get a response back from your write, this means that you cant get back generated IDs for your newly inserted rows.</li>
<li>There is a&nbsp;set up&nbsp;cost incurred with running SQL bulk copy. This means it is not efficient for small datasets.</li>
</ul>
<br />
<span style="font-size: large;">How they compare</span><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-cHlk7bgPY9I/UC37WSnp_xI/AAAAAAAAASE/FsZIGHlmlYs/s1600/Bulk+Insert+Methods.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-cHlk7bgPY9I/UC37WSnp_xI/AAAAAAAAASE/FsZIGHlmlYs/s1600/Bulk+Insert+Methods.png" /></a></div>
<br />
The above graph tells us some interesting things about the way each of these bulk methods work and their individual weaknesses.<br />
<br />
At point <b><span style="color: red;">A</span> </b>we can see a large spike in the execution time for our multi-row insert statement. This occurs at 334 rows inserted. As we discussed earlier SQL changes its&nbsp;behaviour&nbsp;when there are more than 1000 in a single statement. In the above case the SQL statement contained 3 values per row. This means that on the 334th row inserted we have 1002 values in our SQL statement and hence SQL begins to optimise for query plan size. For more info on this particular scenario read <a href="http://stackoverflow.com/a/8640583/1070291">Martin Smiths&nbsp;answer on Stack Overflow</a>&nbsp;(which is a very good read). Its also interesting to note that in my example after this optimisation change we see multi-row inserts become slower than individual SQL insert statements each submitted separately to the database.<br />
<br />
If we look at point <b><span style="color: red;">B</span></b> on the graph we can see a series of sudden drops in execution time which occur every 200 rows beginning on the 400th row. This occurs in correlation with beginning a new batch in our batched approach, ie 401 rows in 3 batches takes less time than 400 rows in 2 batches. This is a very interesting result which I need to do more investigation into (if anyone knows any more about this or has a theory I would love to hear about it). My only hypothesis is that the query plan is calculated on the single row insert and then used for the two larger inserts (which have more variables and are hence harder to parse).<br />
<br />
With our SQL bulk copy line there are a couple of important points to note. Firstly as you can see there appears to be a set up cost associated with the method of around 25ms. Because of this set up cost SQL bulk copy is significantly slower for small numbers of rows. Secondly the point at which SQL bulk copy becomes more efficient in my example is around 150 rows (point<span style="color: red;"> <b>C</b></span> on the graph).<br />
<br />
Detailed times and memory usage results can be found <a href="https://dl.dropbox.com/u/37129059/Performance%20Results%20-%20SQL%20Bulk%20Insert.xlsx">here</a>.<br />
<br />
Thanks to Eli Weinstock Herman (<a href="https://twitter.com/tarwn">t</a> | <a href="http://tiernok.com/">b</a>) for the bulk copy scenario.
