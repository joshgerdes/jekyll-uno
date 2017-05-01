---
title:  "Entity Framework and AsNoTracking"
date:   2012-04-26
excerpt: "Entity Framework change tracking allows the framework to persist only changed data to the database, however this comes at a performance cost. This post discusses the performance impacts of change tracking and when its appropriate to switch it off."
redirect_from:
  - 2012/4/2/entity_framework_and_asnotracking
  - 2012/04/entity-framework-and-asnotracking.html
---
#### TLDR
In a nutshell you should use `.AsNoTracking()` in any Entity Framework query which you intend to use only for reading data. This will ensure minimal memory usage and optimal performance in these cases.

#### What AsNoTracking Does
Entity Framework exposes a number of  performance tuning options to help you optimise the performance of your applications. One of these tuning options is `.AsNoTracking()`. This optimisation allows you to tell Entity Framework not to track the results of a query. This means that Entity Framework performs no additional processing or storage of the entities which are returned by the query. However it also means that you cant update these entities without reattaching them to the tracking graph.

#### AsNoTracking Performance

![Bulk Select (Execution time)]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/asnotracking-bulk-execution-time.png)

![Bulk Select (Execution time)]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/asnotracking-bulk-relative-execution-time.png)

![Bulk Select (Memory usage)]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/asnotracking-bulk-memory-usage.png)

![Bulk Select (Memory usage)]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/asnotracking-bulk-reletive-memory-usage.png)

As you can see AsNoTracking can save both execution time and memory usage. The benefits of AsNoTracking are relative to the number of items which you are retrieving, so applying this option becomes really important when retrieving a large number of items.

One case I have found this particularly valuable is pre-fetching a large table for an in memory cache.

#### How to use AsNoTracking

AsNoTracking is very easy to use in your application, simply do the following:

 - Make sure you are using System.Data.Entity
 ``` csharp
 using System.Data.Entity;
 ```
 - Include AsNoTracking on your query
 ``` csharp
 var items = Context.MyEntityCollection.AsNoTracking().Where(e => e.MyFlag);
 ```

#### When to use AsNoTracking

As you have seen there are significant performance gains to be had by using AsNoTracking, especially when using the Entity Framework Snapshot tracker. If you are using the proxy tracker the performance gains are smaller.

This means you should use this tuning option on all queries for entities you don't want to save back to the database. In a CQRS sense you should probably apply this option globally across your read path to reduce your memory and processing footprint.
It is important however not to use this tuning option when you intend to update the entity as this will mean that Entity Framework has no way of knowing that it needs to save your changes back to the database.

#### Things to Note

 - My results are produced from executing these tests against a remote SQL 2008 R2 server running on a VM (but on different physical hardware). This is not a production test and the numbers represented here would be greatly reduced by running this in a faster environment. Having said this the general trends portrayed should be similar regardless of the speed of the individual test environments.
 - .NET 4.5 has been used in these test cases because I wanted to test against the EF 5 beta as it claims to have improved performance. This makes a difference to the overall performance of all the scenarios. If you would like to see the performance using .NET 4 I would encourage you to build the tests using .NET 4 and run them for yourself.
