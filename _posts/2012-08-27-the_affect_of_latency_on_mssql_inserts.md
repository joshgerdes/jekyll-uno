---
title:  "The affect of latency on MSSQL INSERTs"
date:   2012-08-27
excerpt: "SQL is a network application and according to The Fallacies of Distributed Computing tells us that in any network application latency is non-zero. In this article we will explore the effect of latency on SQL insert performance from the scenarios in my last post."
redirect_from:
  - 2012/8/27/the_affect_of_latency_on_mssql_inserts
  - 2012/08/the-affect-of-latency-on-mssql-inserts.html
---
When dealing with any networked system a number of factors become important which do not apply when writing applications which run on a single machine. As a developers its very easy to overlook some of the aspects of developing for networked systems. The [Fallacies of Distributed Computing](http://en.wikipedia.org/wiki/Fallacies_of_Distributed_Computing) remind us not to make assumptions about networks.

The second fallacy of distributed computing is that [latency is zero](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing). In this article we are going to look at the impacts of latency on insert performance and especially how latency affects each of the bulk insert scenarios which were discussed in my previous article [MSSQL and large INSERT statements](http://blog.staticvoid.co.nz/2012/08/mssql-and-large-insert-statements.html).

I have selected several different amounts of latency as below:

 - No added latency, this simulates a typical scenario where your DB server is in the same rack as your client.
 - 5ms, this is a fairly low latency scenario which simulates your DB server being on the same campus/data center as your client but behind a few routers.
 - 10ms, this simulates your DB server being in the same city as your client but not the same campus.
 - 30ms, this simulates a cross country connection where your DB server may be in a different city to your client.
 - 100ms, if you are unfortunate enough to have your DB on the other side of a major ocean you're in big trouble.

### Latency and basic SQL Command inserts

![Latency Impact on Basic SQL Commands]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/latency-impact-on-basic-sql-commands.png)

As we can see from the above graph that latency linearly increases the time taken to insert each row. We can see this as on our log graph the curves appear offset but have no apparent differences in the steepness of the curves. However when we look at the actual time impact that this has it is fairly clear that latency is not our friend here. For example inserting 1000 rows at 5ms latency takes us around 7.5s whereas with 100ms latency those same 1000 rows take 103s (which matches conceptually with a direct linear correlation, 95ms \* 1000 *rows* + 7.5s *5ms baseline* = 102.5s).

### How our scenarios compare with latency

![No added latency]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/no-added-latency.png)

![5ms latency]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/5ms-latency.png)

![10ms latency]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/10ms-latency.png)

![30ms latency]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/30ms-latency.png)

![100ms latency]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/100ms-latency.png)

As you can see as latency increases, a basic SQL command approach performs comparability worse however each of our three alternatives remain comparability similar to each other. This shows that the affect of latency is substantially lower on each of our alternate methods of inserting data.

### What does it mean for developing applications

For developers and admins alike it is particularly important to understand the potential impacts latency can have on SQL performance. What's more these problems are not going to be limited to insert based statements; every call to a database incurs a non-zero latency cost.

With cloud computing and geographically dispersed companies becoming more prevalent data is not always located close to where it is used. While this isn't ideal by paying attention to latency when we construct applications and frameworks makes us far more resilient to higher latency scenarios when they do occur. Remember the [Fallacies of Distributed Computing](http://en.wikipedia.org/wiki/Fallacies_of_Distributed_Computing) and don't assume that latency is insignificant.

With SQL batching multiple statements into a single statement or transmission will save round trips which means they will cope a lot better with latency.

My raw data and graphs can be downloaded [**here**]({{site.baseurl}}/files/posts/{{page.date | date: '%Y' }}/Performance%20results%20-%20latency%20comparisons.xlsx).

**Note**: in this article when discussing latency we are considering **round trip time (RTT)** not one directional latency
