---
title:  "Making Dapper Faster with Transactions"
date:   2012-04-26
excerpt: "Transactions are an often neglected component of how we access databases. They are important when we are writing to databases as they affect how and how often tables are locked. In this post we will examine what kind of difference transactions make in practice."
redirect_from:
  - 2012/4/26/making_dapper_faster_with_transactions
  - 2012/04/making-dapper-faster-with-transactions.html
---
After posting on the performance of several different ORMs I had a chat to [Sam Saffron] one of the authors of the Dapper framework around how I could make my Dapper test cases faster. My original test results showed Dapper as being around 55% slower for inserts and 23% slower for updates than Entity Framework.

What we found was that by default Entity Framework wraps its batches in a transaction but with Dapper you have to perform this manually. With SQL transactions make batch write operations substantially faster. In this post were going to explore how much difference transactions make and look at some of the reasons why they have an impact on performance. For this post I'm using Dapper for simplicity but the same general principles and performance gains apply to other ORMs.

### Transaction Performance

I have compared below how dapper performs with and without transactions. As you can see they make a pretty big difference to the execution time of database writes, especially as the number of items increases. My original data for these results can be found [here]({{site.baseurl}}/files/posts/{{page.date | date: '%Y' }}/Performance%20Results%20-%20Dapper%20Transactions.xlsx).

![Insert Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-insert-comparison.png)

![Insert Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-insert-relative-performance.png)

![Update Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-update-comparison.png)

![Update Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-update-relative-performance.png)


### Does changing the Isolation Level alter performance?
SQL provides several different modes (Isolation Levels) to apply to transactions. These affect how rows which are modified within a transaction are locked and when they can be queried. [MSDN - Improving SQL Server Performance](http://msdn.microsoft.com/en-us/library/ff647793.aspx#scalenetchapt14 _topic7) has some great notes on exactly what these lock levels do and what the specific side effects of each method can be. I thought playing with these may affect performance, but I was wrong; **Isolation Levels appear to have no affect on single threaded bulk write performance**.


![Transactions Insert Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-transactions-insert-comparison.png)

![Transactions Insert Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-transaction-insert-relative-performance.png)

![Transactions Update Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-transactions-update-comparison.png)

![Transactions Update Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dapper-transactions-update-relative-performance.png)

***NOTE*** *however that these do have an affect on performance if multiple queries affecting the same tables are being performed as you may need to wait for a previous transaction to complete before you can write with some Isolation Levels.*

### What makes transactions so much faster?

So there's a bit of a secret with transactions, under the covers they happen anyway. Whenever you perform a write operation it is implicit that this occurs within a transaction so that it is either completely written or not written at all. What we are really doing when we wrap a query in a transaction is being explicit about when we start and stop the transaction. This means we can perform multiple operations within the same transaction.

Transactions naturally have an overhead to do with performing lock and unlock operations on data. This means that we really want to have less of them. By wrapping 1000 inserts inside a transaction what we are actually achieving is reducing the number of transactions by 999, which obviously improves performance dramatically.

See [Stack Overflow - ADO.net SqlTransaction improves performance](http://stackoverflow.com/q/5091084/1070291) for a conversation on this topic.

### Should I use them everywhere?

Transactions are a useful part of SQL and its really important for performance that your operations are correctly encapsulated inside transactions. If you are performing queries which lend themselves to large batches of data its well worth your while reducing the number of transactions which are occurring by being explicit about when transactions start and finish.

Having said this be aware that if anything inside your transaction fails the entire transaction will be rolled back. This is really important as it means that until you have successfully committed your data, it isn't really saved. This means you need to conciser what other things will be rolled back on failure and make sure that your data is related enough that its OK that the whole transaction is either committed or not committed.

Another thing to note is that depending on your isolation level you may be blocking other queries to the database for the duration of your transaction. This may have flow on affects on performance to other parts of your system, especially when multiple threads/processes/users are concurrently accessing the database.

To sum up transactions can be dangerous, make sure you understand whats going on behind the scenes with transactions and spend some time thinking about where you place your transaction boundaries.

### Thanks

I'm particularly grateful to [Sam Saffron] for his help identifying transactions as the cause of my dapper performance issues.

[Sam Saffron]:http://samsaffron.com/
