---
title:  "EntityFramework Performance and AutoDetectChanges"
date:   2012-05-07
excerpt: "Entity Framework change tracking performs well when using small sets of data however as the number of changes grows it becomes inefficient. In this post we look at what causes this degradation and how we can tune EF to perform better with large data sets."
redirect_from:
  - 2012/5/7/entityframework_performance_and_autodetectchanges
  - 2012/05/entityframework-performance-and.html
---

### What is Auto Detect Changes?
Entity framework has two methods of change detection built into the framework, Instant Notification and Snapshot. Most people seem to use the Snapshot mechanism as it is the easiest to configure and most well known. I will cover the Instant Notification (Proxy Entities) Mechanism in a later post.

Detect Changes has two purposes:

 1. Snapshot change detection takes a copy of every entity in the system when they are added to the Entity Framework tracking graph. Then as entities change each entity is compared to its snapshot to see any changes. This occurs by calling the `DetectChanges` method. What's important to know about `DetectChanges` is that it has to go through all of your tracked entities each time its called, so the more stuff you have in your context the longer it takes to traverse.
 2. To run 'Fixups' across the context so that navigation properties are updated throughout the context.

For more details on Detect Changes [Arthur Vickers](http://blog.oneunicorn.com/) from the Entity Framework team has an awesome [blog series on how DetectChanges works](http://blog.oneunicorn.com/2012/03/10/secrets-of-detectchanges-part-1-what-does-detectchanges-do/) in much greater detail.

What Auto Detect Changes does is plugs into events which happen on the context and calls detect changes as they occur.

### Auto Detect Changes Performance

![Insert Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/insert-comparison.png)

![Insert Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/insert-reletive-performance.png)

![Update Comparison]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/update-comparison.png)

![Update Relative Performance]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/update-reletive-performance.png)

So wow, lets take a look at those results a little more closely.

From the graphs above you can see that with Auto Detect Changes **off** the relationship between *time* and *number of items* is approximately linear ie O(N), and with Auto Detect Changes **on** the relationship is quadratic O(N<sup>2</sup>), see [here](http://math.stackexchange.com/a/138301/30204). That means the more items that we modify to our context in Entity Framework the longer it takes to perform each modification.

### Why is Auto Detect Changes so slow with many items?

As we have touched on earlier whenever we make a change to the context DetectChanges gets called. Detect changes enumerates all attached items

This means that if we are adding 1000 items the first item we add enumerates no items, the second enumerates 1 item and so on. So if we do the math for this we get:

$$1 + 2 + 3 + ... + 999 + 1000$$

or:

$$\sum_{i=0}^N(N-i)=\sum_{i=0}^Ni=\frac{N(N+1)}2\;$$

where in this case N is 1000. This function is of the class O(N<sup>2</sup>) which explains why it takes so long to add a large number of items.<

### How do I turn it off?

Fortunately its really easy to turn Auto Detect Changes on and off. Simply use:

```csharp
context.Configuration.AutoDetectChangesEnabled = false;
```

But be careful while you have Auto Detect Changes off Entity Framework will not be tracking the changes you have made or fixing up navigation properties. MSDN says this may mean that turning off Auto Detect Changes *"can potentially introduce subtle bugs into your application if not used correctly."*([MSDN][1])

Once your done with your bulk changes its worth while manually calling DetectChanges so that you leave the context in an aware state. You can do this as follows:

```csharp
context.ChangeTracker.DetectChanges();
```

### Why would I leave it on?

Detect changes is actually really useful in most cases. As you can see from my results when you are dealing with less than 100 items in the context the performance impact is negligible. In most cases its much simpler to leave Auto Detect Changes on. As Arthur Vickers aptly puts it *"change tracking and the DetectChanges method are a part of the stack where there is a tension between ease-of-use and performance"* ([Secrets of DetectChanges](http://blog.oneunicorn.com/2012/03/10/secrets-of-detectchanges-part-1-what-does-detectchanges-do/)).

My general feeling is that if you are doing batch modifications to the database you should be turning Auto Detect Changes off, otherwise it adds complexity for very little gain.

### Well worth reading

Change tracking is the central and most complex component of Entity Framework, so if you use EF its well worth while to understand some of how it works. Here's some resources that go into a little more detail:

 - [Secrets of DetectChanges Series](http://blog.oneunicorn.com/2012/03/10/secrets-of-detectchanges-part-1-what-does-detectchanges-do/) - Arthur Vickers
 - [Change Tracking][2] - MSDN


[1]:http://msdn.microsoft.com/en-us/library/gg696177(v=vs.103).aspx
[2]:http://msdn.microsoft.com/en-us/library/gg696177(v=vs.103).aspx

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" async>
