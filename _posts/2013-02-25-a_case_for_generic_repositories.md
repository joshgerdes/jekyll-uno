---
title:  "Generic Repositories"
date:   2013-02-25
excerpt: "I have always liked the abstraction provided by a repository pattern. This article aims to articulate why I use generic repositories and what benefits I feel are most important from this approach. I also examine exactly how I use generic repositories in my applications with some practical examples."
redirect_from:
  - 2013/2/25/a_case_for_generic_repositories
---

**I no longer use generic repositories. I have instead switched to [Composable repositories]({{site.baseurl}}/2015/composable_repositories/) which are well worth a look as they allow for better reuse.** This is really the logical conclusion of extension methods to add functionality. However if you are interested specifically in the generic repository pattern read on :)

---

There are mixed opinions around the usefulness of generic repositories, some call it an anti-pattern. I personally find them useful so in this article I will explore what I like about the Generic Repository abstraction and how I solve some of the common criticisms of the pattern.

### Why are generic repositories controversial?
I have read several articles on generic repositories which prompted this post, probably the most prominent was Greg Young's post [DDD: The Generic Repository](http://codebetter.com/gregyoung/2009/01/16/ddd-the-generic-repository/). In this post Young raises a number of issues with generic repositories. Including the following:

  - What happens if you don't want all CRUD operations available
  - It encourages persistence logic in the domain (you want to be able to unit test without persistence)
  - Specific contracts are an important pointer to specifically what the application requires of the data store.

Young concludes his article by stating that there is a place for generic repositories but they should not be exposed outside of the data tier, that is they should be used to compose other repositories which can be surfaced to the application.

### What is to gain by using a generic repository?

#### A personalized grammar
For me the most important benefit of using repositories is data-tier isolation; that is to provide a clear boundary between your data access layer and your main application. By creating a repository the effect is to constrain the way your application talks about data to a grammar (language) which you define and control. This in turn acts as a barrier to help reduce data concerns leaking into other layers of your application.

#### A centralized contract
By defining a generic repository what you are actually doing is defining a contract for what your application requires from a persistence layer. This gives key insight into what functions our persistence layers must provide. For example if our application uses LINQ to query our data tiers our generic repositories will expose this requirement so that you understand that any alternate persistence layers must also support LINQ. If a persistence layer can provide all of the functions described by our generic repository it could be a suitable alternative to your current persistence technology.

#### An interception point
By having the interception point of a generic repository you can perform what-if scenarios, for example *what if I upgrade to the latest persistence technology?*, or *what if I stored this particular entity in XML on disk instead of a database?*. By having that generic replacement point you can try these scenarios out much more simply than you perhaps could if there were more places accessing the persistence layer.

A Generic Repository is an interception point to your data tier for actions you want to happen globally, caching and auditing are great examples of where this can be a particularly useful.

### When not to use a generic repository
As with any abstraction there are scenarios when your requirements are no longer going to fit and you need to do something a little bit special. Performance is a great example of a reason for which its often necessary to step away from such a pattern.

For example sometimes its necessary to hand-craft the SQL which you are using to access your data. When you get to this point you are diverging from a generic pattern, that logic can only really run on a SQL server. At this point your implementation is very specific and coupled tightly to the technology so a much more specific abstraction is appropriate.

I recommend understanding how your repositories work on the inside. This will help you understand when you need to (or don't need to) depart from this pattern and chose something more specialized. My generic repository implementation is [available on GitHub](https://github.com/lukemcgregor/StaticVoid.Repository) but I would encourage you to read through and understand it and possibly even modify it to make it your own.

### How do they work in practice?

I've spent quite a bit of this article talking through why I like to use generic repositories, perhaps more important is how I use them.

#### Dependency Injection
I use generic repositories in conjunction with dependency injection. This allows implementations of the repository to easily be bound in specific scenarios.

``` csharp
Bind<DbContext>().To<BlogContext>().InRequestScope();
Bind(typeof(IRepositoryDataSource<>)).To(typeof(DbContextRepositoryDataSource<>));
Bind(typeof(IRepository<>)).To(typeof(SimpleRepository<>));
```

What makes this approach so powerful is that when you need more than the stock repository you can flip it out for something a little more specific by binding over the top of the generic binding.

``` csharp
Rebind<IRepository<Data.Post>>().To<CachedPostRepository>();
```

In the above example you bind in a custom repository which is going to cache all our posts in memory so that they are nice and quick when you retrieve them. What is nice about this method is that when you are consuming this in our application it doesn't actually concern us if this information is retrieved from a cache or directly from the database so long as you are able to work with it in an `IRepository<>` way.

#### Extension Methods
With any application you will implement a lot of logic around how you access your applications data. I use extension methods to implement my application specific data logic. This method works really well and I find it keeps application data logic clean and tidy. Its also not limited to to a generic repository scenario, and you can use this style of code in many with many other data access methodologies.

In my blog engine for example the concept of published posts is important and is used everywhere, so I have the following extension method:

``` csharp
public static IQueryable<Post> PublishedPosts(this IRepository<Post> repo)
{
    return repo.GetAll().Where(p => p.Status == PostStatus.Published);
}
```

I often need something more specific than just published posts though, for example if you go to [http://blog.staticvoid.co.nz](http://blog.staticvoid.co.nz) it will forward you to the latest published post, so I have:

``` csharp
public static Post LatestPublishedPost(this IRepository<Post> repo)
{
    return repo.PublishedPosts().OrderByDescending(p=>p.Posted).FirstOrDefault();
}
```

I then use this in my controller to redirect the request to the latest post.

```cs
public ActionResult Index()
{
    var post = _postRepository.LatestPublishedPost();
    if(post== null)
        throw new HttpException((int)HttpStatusCode.NotFound, "No posts have been published");
    return Redirect("/" + post.Path);
}
```

As you can see this lets you chain data logic concepts together into simple readable bites.

Because all of these extension methods are built on top of a generic concept the logic is separated from the specific Entity Framework implementation I use and any implementation which fulfills my `IRepository<>` contract (such as my caching repository) will now work in my application.

#### Unit Testing
Allowing us to switch out that generic implementation becomes even more valuable when you want to test our code. At this point you can switch our actual implementation out for an in memory repository so you don't have to actually query a database and can maintain our state a little more tightly. Below are the tests for post redirection:

```cs
[TestMethod]
[ExpectedException(typeof(HttpException))]
public void RedirectToLatestPostWithNoPostsTest()
{
    IRepository<Post> postRepo = new SimpleRepository<Post>(new InMemoryRepositoryDataSource<Post>());
    PostController sut = new PostController(postRepo);
    try
    {
        sut.Index();
    }
    catch(HttpException ex)
    {
        Assert.AreEqual((int)HttpStatusCode.NotFound, ex.GetHttpCode());
        throw;
    }
}

[TestMethod]
[ExpectedException(typeof(HttpException))]
public void RedirectToLatestPostWithNoPublishedPostsTest()
{
    IRepository<Post> postRepo = new SimpleRepository<Post>(new InMemoryRepositoryDataSource<Post>(
        new List<Post> {
            new Post { Status = PostStatus.Draft},
            new Post { Status = PostStatus.Unpublished}
        }));
    PostController sut = new PostController(postRepo);
    try
    {
        sut.Index();
    }
    catch (HttpException ex)
    {
        Assert.AreEqual((int)HttpStatusCode.NotFound, ex.GetHttpCode());
        throw;
    }
}

[TestMethod]
public void RedirectToLatestPostWithOnePublishedPostsTest()
{
    IRepository<Post> postRepo = new SimpleRepository<Post>(new InMemoryRepositoryDataSource<Post>(
        new List<Post> {
            new Post {
                Status = PostStatus.Published,
                Path ="2013/04/14/some-post",
                Posted = new DateTime(2013,4,14) }
        }));
    PostController sut = new PostController(postRepo);
    var result = sut.Index();
    Assert.AreEqual("/2013/04/14/some-post", ((RedirectResult)result).Url);
}

[TestMethod]
public void RedirectToLatestPostWithMultiplePublishedPostsTest()
{
    IRepository<Post> postRepo = new SimpleRepository<Post>(new InMemoryRepositoryDataSource<Post>(
        new List<Post> {
            new Post {
                Status = PostStatus.Published,
                Path ="2013/04/10/some-other-post",
                Posted = new DateTime(2013,4,10) },
            new Post {
                Status = PostStatus.Published,
                Path ="2013/04/14/some-post",
                Posted = new DateTime(2013,4,14) }
        }));
    PostController sut = new PostController(postRepo);
    var result = sut.Index();
    Assert.AreEqual("/2013/04/14/some-post", ((RedirectResult)result).Url);
}
```

What is great about this is that you can test right to the edges of our system and ensure that you are producing the intended result for this controller, eg that its going to redirect us to the URL of the latest post without the fragility of testing with a database in the mix.

### Summing up
I find generic repositories to be a very useful pattern which allows you to write more change agile code. They provide a key touch point for being able to work with data in different scenarios. While they are not the right abstraction in all scenarios they provide a useful abstraction for a wide range of applications, especially when combined with a dependency injection framework.
