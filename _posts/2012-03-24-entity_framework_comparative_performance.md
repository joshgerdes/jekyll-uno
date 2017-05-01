---
title:  "Entity Framework Comparative Performance"
date:   2012-03-24
excerpt: "I have heard many claims that specific ORMs far outperform others, so I built my own ORM performance testing framework to test some of these results for myself. What I found is there is less difference in performance between ORMs than I expected."
redirect_from:
  - 2012/3/24/entity_framework_comparative_performance
  - 2012/03/entity-framework-comparative.html
---
There are heaps of opinions floating round about which ORM is fastest. I've recently been working on improving the performance of a long running sync of a large data set back ended into SQL. During this process there has been a lot of talk about whether Entity Framework was the correct tool for the job and many sites on the net would imply perhaps it isn't the best tool for batch processing. So I decided to do some tests of my own to find out how much slower Entity Framework actually is.

### Method
During the process of performance tuning on my application and testing out different ORMs I learned a lot about how to get the best performance and when to use specific optimisation. I decided it would also be useful to compare different performance tuning options in my test.

To do this testing I built a test rig to accurately compare the different frameworks and tuning options. The test framework pairs up technology implementations (eg EntityFramework 5.0.0.0 Beta) with performance scenarios (eg bulk insert of random data), I call this a run.

To make the results as fair and unbiased as possible the rig was built with the following principals.

 1. **The test database is rebuilt for each run**, this means that the state of the database is identical for each run.
 2. **The order of technology implementations is random**, this is to avoid specific runs having an advantage because they come first or last within the test execution.
 3. **Runs are repeated**, the results of a scenario should be reproducible.
 4. **The worst instance for each run is discarded** so that external influences on the run are ignored
 5. **Each scenario was run against different numbers of items**, in this post I've used the following *1,10,100,1000,10000* items.
 6. **At the end of each run the database state is asserted** to confirm that the operations expected were performed
 7. **Random data is used** to ensure that there is no data bias between technologies
 8. **The same random data is used for each technology in a specific iteration of a scenario** so that results are based on the same data set.


All code for the tests are published at [https://github.com/lukemcgregor/StaticVoid.OrmPerformance](https://github.com/lukemcgregor/StaticVoid.OrmPerformance) and I would appreciate review of the individual test cases. If you have additional tests, ORMs, or performance improvements I would encourage you to fork the repository and add your tests. That way I can merge them back into the trunk.

### Tests
I decided to test the following database technologies and tuning options:

 1. EntityFramework 4.1
  - Basic Configuration (No optimisations)
  - AutoDetectChanges Disabled
  - My Best effort at making it go fast
 2. EntityFramework 5.0 beta1
  - Basic Configuration (No optimisations)
  - AutoDetectChanges Disabled
  - My Best effort at making it go fast
 3. Dapper 1.8
  - Dapper Rainbow
  - My Best effort at making it go fast
  - **EDIT** Batching inserts/updates using transactions
 4. LINQ to SQL
  - Basic Configuration (No optimisations)
  - Compiled Queries
  - No Object Tracking
  - My Best effort at making it go fast

and the following test scenarios

 - Insert of N rows to the database, each row contains random data.
 - Update of N rows to the database, each original row and each update is random data.
 - Discrete selects of N random rows from the database.
 - Bulk select of N random rows from the database
 - Delete of N random rows from the database

### Results

#### Insert

![Insert Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-insert-comparison.png)

![Insert Relative]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-insert-relative.png)

#### Update


![Update Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-update-comparison.png)

![Update Relative]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-update-relative.png)

#### Bulk Select

![Bulk Select Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-bulk-select-comparison.png)

![Bulk Select Relative]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-bulk-select-relative.png)

#### Discrete Select

![Discrete Select Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-discrete-select-comparison.png)

![Discrete Select Relative]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-discrete-select-relative.png)

#### Delete

![Delete Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-delete-comparison.png)

![Delete Relative]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/performance-delete-relative.png)

I find these results absolutely intriguing, what these show is that it actually isn't very clear which ORM is faster here, its absolutely relative to your target workload, more specifically to the size and type of your operations.

The data which I have used to compile these results can be found in its raw form and with the graphs [here]({{site.baseurl}}/files/posts/{{page.date | date: '%Y' }}/Performance%20Results.xlsx).

### Entity Framework 5 with a Small Number of Items

One of the really interesting points which I've noticed from my results is that over small numbers of items Entity Framework is the fastest in all tests. This is of critical importance when picking an ORM. What this means is that if you have an application such as a website which is performing a bunch of small requests to your database to render your page Entity Framework 5 is going to be really quick (so long as you follow a few pointers on how to set up your context).

### Deleting Data

Dapper and a decent hand crafted query is amazing at deleting data. For this test I used a handcrafted *delete where in* SQL query. The bonus of doing this is that the whole query is executed in a single SQL statement so will run much faster inside SQL. If your application involves a lot of batch deletes you should seriously consider handcrafting your query with something like Dapper.

### Entity Framework 4 vs Entity Framework 5
I find the comparison of the two versions of entity framework very interesting. If you look at the line graphs what you see is that for small numbers of items Entity Framework 5 is a lot quicker, but what I find very interesting is that as the number of items increase the two versions converge on the same amounts of time across the board. This suggests to me that the ADO.Net team has spent a lot of time optimising Entity Framework for small data sets, and have done a great job.

### Bulk Selects with Small Numbers of Items

When doing a *select where* statement with a small number of matches both Entity Framework 5 and Dapper show a very interesting result, it actually takes longer to perform the query for less items. I have done a lot of runs through and this behavior seems to be repeated every time. Its also important to note here that each of these queries are performed on their own database. I have no idea why this is but I would love to know if someone has any insight on this particular behavior.

### Inserts and Updates
~~If your application is mostly performing inserts and updates Entity Framework seems to be quite a bit faster than Dapper. My feeling is that this is probably because Entity Framework performs some optimisation before sending the data to the database. **Perhaps someone better with dapper than I could improve Dapper's performance in this area, however I currently don't have any idea how to do this.**~~
**EDIT:** With the help of [Sam Saffron], one of the authors of Dapper we were able to improve the performance of the dapper Insert and Update test cases to below that of Entity Framework. This was achieved by putting the Dapper commands inside a SQL Transaction (see [here](https://github.com/lukemcgregor/StaticVoid.OrmPerformance/blob/master/Harness.Dapper1-8/DapperBatchConfiguration.cs) for the actual code). I'm intending on following this up with another post soon.

### Selects
If your application is mostly selects Dapper and Linq to SQL are particularly fast for large numbers of items (but again Entity Framework 5 is faster with small numbers of items). My feeling is that this is because Entity framework (even with tracking off) does quite a lot of fiddling with the data after its retrieved from the server.

### General Performance Comparison
~~With the exception of the delete case, even at large numbers the difference in performance between the different ORMs is not (in my opinion) particularly high. In some cases Entity Framework takes half as much time again over Dapper and in some cases this is reversed. Having said that all of the ORMs are performing within the same orders of magnitude (assuming sensible settings). What this means is that you are unlikely to get enormous performance gains from simply switching ORMs.~~
**EDIT:** With the improvement of the Dapper Insert and Update cases Dapper stands out in terms of performance for batch jobs with Entity Framework taking between 126% and 235% of the time that Dapper does. However Entity Framework 5 still appears to be faster in all cases for a small number of items.

### Conclusions/TLDR
If you are picking an ORM to use and want to pick based on performance alone the choice is not entirely simple. For batch based application Dapper is clearly faster. But for user applications which involve a queries involving only a small number of items (ie selects returning under 1000 results) and inserts/updates affecting any number of entities, Entity Framework is clearly faster.

In terms of the batch process I have been writing these results have given me confidence in the performance of Entity Framework and I have no plans to change at this stage. It has shown me that Entity Framework is not significantly slower than other ORMs and in the majority of my application its actually faster (as I am primarily doing updates and inserts).

I would encourage you to download the test framework and look at my test cases, improve them if you can and add your own. I'm really keen to watch this space more and add some more ORMs in the future.

### Other things of note

 - I don't claim to be an expert on the ORMs tested, there may well be additional ways to tweek extra performance out of the specific scenarios. If you know a better way please let me know and I will update my results accordingly.
 - My results are produced from executing these tests against a remote SQL 2008 R2 server running on a VM (but on different physical hardware). This is not a production test and the numbers represented here would be greatly reduced by running this in a faster environment. Having said this the general trends portrayed should be similar regardless of the speed of the individual test environments.
 - .NET 4.5 has been used in these test cases because I wanted to test against the EF 5 beta as it claims to have improved performance. This makes a difference to the overall performance of all the scenarios. If you would like to see the performance using .NET 4 I would encourage you to build the tests using .NET 4 and run them for yourself.
 - These tests take a long time to run (several hours), I would recommend running them overnight.
 - My recommendation is to run the tests in release mode without debugging as this will give you the best results.

### Thanks

I'm very grateful to [Sam Saffron] for his help getting my Dapper test case running faster.

[Sam Saffron]:http://samsaffron.com/
