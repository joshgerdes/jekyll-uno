---
title:  "Making Dapper Faster with Transactions"
date:   2012-04-26
canonical: http://blog.staticvoid.co.nz/2012/4/26/making_dapper_faster_with_transactions
redirect_from:
  - 2012/4/26/making_dapper_faster_with_transactions
---
After posting on the performance of several different ORMs I had a chat to <a href="http://samsaffron.com/">Sam Saffron</a> one of the authors of the Dapper framework around how I could make my Dapper test cases faster. My&nbsp;original&nbsp;test results showed Dapper as being around 55% slower for inserts and 23% slower for updates than Entity Framework.<br />
<br />
What we found was that by default Entity Framework wraps its batches in a transaction but with Dapper you have to perform this manually. With SQL transactions make batch write operations substantially faster. In this post were going to explore how much difference transactions make and look at some of the reasons why they have an impact on performance. For this post I'm using Dapper for simplicity but the same general principles and&nbsp;performance&nbsp;gains apply to other ORMs.<br />
<br />
<span style="font-size: large;">Transaction Performance</span><br />
I have compared below how dapper performs with and without transactions. As you can see they make a pretty big difference to the execution time of database writes, especially as the number of items increases. My&nbsp;original&nbsp;data for these results can be found <a href="http://dl.dropbox.com/u/37129059/Performance%20Results%20-%20Dapper%20Transactions.xlsx">here</a>.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-DrLUnq8zK4Q/T5eJ7bIAScI/AAAAAAAAALY/Qf2l8Ro5h7Q/s1600/Insert+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="379" src="http://3.bp.blogspot.com/-DrLUnq8zK4Q/T5eJ7bIAScI/AAAAAAAAALY/Qf2l8Ro5h7Q/s640/Insert+Comparison.png" width="640" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-HN8WJEXbcjg/T5eJ8fyylGI/AAAAAAAAALc/7iP1Ud5lENc/s1600/Insert+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-HN8WJEXbcjg/T5eJ8fyylGI/AAAAAAAAALc/7iP1Ud5lENc/s1600/Insert+Reletive+Performance.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-G158j1Dcn2M/T5eJ9OMdw7I/AAAAAAAAALk/QGXgwTCgAaY/s1600/Update+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="379" src="http://1.bp.blogspot.com/-G158j1Dcn2M/T5eJ9OMdw7I/AAAAAAAAALk/QGXgwTCgAaY/s640/Update+Comparison.png" width="640" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-2Y6iQ2GoQoI/T5eJ9zfpGiI/AAAAAAAAALs/tyacs0Wrxvg/s1600/Update+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-2Y6iQ2GoQoI/T5eJ9zfpGiI/AAAAAAAAALs/tyacs0Wrxvg/s1600/Update+Reletive+Performance.png" /></a></div>
<br />
<br />
<span style="font-size: large;">Does changing the Isolation Level alter performance?</span><br />
SQL provides several different modes (Isolation Levels) to apply to transactions. These affect how rows which are modified within a transaction are locked and when they can be queried. <a href="http://msdn.microsoft.com/en-us/library/ff647793.aspx#scalenetchapt14 _topic7">MSDN - Improving SQL Server Performance</a> has some great notes on exactly what these lock levels do and what the specific side effects of each method can be. I thought playing with these may affect performance, but I was wrong; <b>Isolation Levels appear to have no affect on single threaded bulk write performance</b>.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-nOvJgk3_Ibk/T5f2uxH7u9I/AAAAAAAAAL8/7kOi5DOFCEg/s1600/Insert+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="400" src="http://2.bp.blogspot.com/-nOvJgk3_Ibk/T5f2uxH7u9I/AAAAAAAAAL8/7kOi5DOFCEg/s640/Insert+Comparison.png" width="640" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-jVkg0z3o6Yo/T5f2vid6F5I/AAAAAAAAAME/KBetckJYspE/s1600/Insert+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-jVkg0z3o6Yo/T5f2vid6F5I/AAAAAAAAAME/KBetckJYspE/s1600/Insert+Reletive+Performance.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-fa5szyoE7s0/T5f2wqp6s6I/AAAAAAAAAMM/S5_Kl2UIatE/s1600/Update+Comparison.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="398" src="http://1.bp.blogspot.com/-fa5szyoE7s0/T5f2wqp6s6I/AAAAAAAAAMM/S5_Kl2UIatE/s640/Update+Comparison.png" width="640" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-kkWekbrSU-I/T5f2xyf9PEI/AAAAAAAAAMQ/1o5SgIrHm0I/s1600/Update+Reletive+Performance.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/-kkWekbrSU-I/T5f2xyf9PEI/AAAAAAAAAMQ/1o5SgIrHm0I/s1600/Update+Reletive+Performance.png" /></a></div>
<br />
<br />
<i>NOTE however that these do have an affect on performance if multiple queries affecting the same tables are being performed as you may need to wait for a previous transaction to complete before you can write with some Isolation Levels.</i><br />
<br />
<span style="font-size: large;">What makes transactions so much faster?</span><br />
So&nbsp;there's&nbsp;a bit of a secret with transactions, under the covers they happen anyway. Whenever you perform a write operation it is implicit that this occurs within a transaction so that it is either&nbsp;completely&nbsp;written or not written at all. What we are really doing when we wrap a query in a transaction is being explicit about when we start and stop the transaction. This means we can perform multiple operations within the same transaction.<br />
<br />
Transactions naturally have an overhead to do with performing lock and unlock operations on data. This means that we really want to have less of them. By wrapping 1000 inserts inside a transaction what we are actually achieving is reducing the number of transactions by 999, which obviously improves performance dramatically.<br />
<br />
See <a href="http://stackoverflow.com/q/5091084/1070291">Stack Overflow - ADO.net SqlTransaction improves performance</a> for a conversation on this topic.<br />
<br />
<span style="font-size: large;">Should I use them everywhere?</span><br />
Transactions are a useful part of SQL and its really important for performance that your operations are correctly encapsulated inside transactions. If you are performing queries which lend themselves to large batches of data its well worth your while reducing the number of transactions which are&nbsp;occurring&nbsp;by being explicit about when transactions start and finish.<br />
<br />
Having said this be aware that if anything inside your transaction fails the entire transaction will be rolled back. This is really important as it means that until you have successfully committed your data, it&nbsp;isn't&nbsp;really saved. This means you need to&nbsp;conciser&nbsp;what other things will be rolled back on failure and make sure that your data is related enough that its OK that the whole transaction is either committed or not committed.<br />
<br />
Another thing to note is that depending on your isolation level you may be blocking other queries to the database for the duration of your transaction. This may have flow on affects on performance to other parts of your system, especially when multiple threads/processes/users are concurrently accessing the database.<br />
<br />
To sum up transactions can be dangerous, make sure you understand whats going on behind the scenes with transactions and spend some time thinking about where you place your transaction&nbsp;boundaries.<br />
<br />
<span style="font-size: large;">Thanks</span><br />
I'm particularly&nbsp;grateful&nbsp;to <a href="http://samsaffron.com/">Sam Saffron</a> for his help identifying transactions as the cause of my dapper performance issues.
