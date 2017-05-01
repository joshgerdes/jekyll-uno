---
title:  "StaticVoid Repository Pattern - NuGet"
date:   2011-10-13
excerpt: "Repositories are all about decoupling our application from our chosen storage mechanism. This is my take on a Generic Repository with Entity Framework."
redirect_from:
  - 2011/10/13/staticvoid_repository_pattern-nuget
  - 2011/10/staticvoid-repository-pattern-nuget.html
  - 2010/11/my-take-on-repository-pattern.html
---

I recently published a <a href="http://nuget.org/List/Packages/StaticVoid.Core.Repository">NuGet package</a> which contains my version of the repository pattern for EF4.1 so I thought it would be good to write a bit of an explanation of how I use it and what impact this has on the way I access databases within my own applications. My goal is to allow people to use this pattern to reduce the code required to perform the common database tasks while reducing the coupling to the actual underlying database/ORM framework and making the flow of data throughout applications more seamless and hence more elegant.

{% include nuget.html packageId="StaticVoid.Core.Repository" %}

I would also like to outline a few places this method falls down and what the pitfalls are around these specific circumstances.

To use the StaticVoid Repository pattern several things need to be set up.

### Set up the kernel bindings
Kernel bindings tell the dependency injection framework how which concrete implementation to provide to classes when they request them.

Below is an example of the config required to setup Ninject

``` csharp
private static void RegisterServices(IKernel kernel)
{
	//Key components for StaticVoid Repository configuration,
	//this allows injection of IRepository (see GeekLogic)
	//The assumption is that T exists within your EF4.1 entities.
	kernel.Bind<DbContext>().To<GeekContext>().InRequestScope();
	kernel.Bind(typeof(IRepositoryDataSource<>))
		.To(typeof(DbContextRepositoryDataSource<>));
	kernel.Bind(typeof(IRepository<>))
		.To(typeof(SimpleRepository<>));
	kernel.Bind<IGeekLogic>().To<GeekLogic>();
}  
```

Note that we are binding generic implementations of `IRepository<>` and `IRepositoryDataSource<>` to concrete implementations provided by the library.

### Using the repository

Repositories exist against a single entity type within your system. This means that you would consume a repository of a specific type.

Below is an MVC example of consuming a repository of geeks:

```csharp
public class GeekLogic:IGeekLogic
{
	private IRepository<Geek> m_GeekRepository;
	public GeekLogic(IRepository<Geek> geekRepository)
	{
			 m_GeekRepository = geekRepository;
	}
	#region IGeekLogic Members
	public IEnumerable<Geek> OldGeeks(DateTime olderThan)
	{
			 return m_GeekRepository.GetAll().Where(g => g.DateOfBirth < olderThan).ToList().AsEnumerable();
	}
	#endregion
}

public class HomeController : Controller
{
	private IGeekLogic m_GeekLogic;
	public HomeController(IGeekLogic geekLogic)
	{
		m_GeekLogic = geekLogic;
	}
	public ActionResult Index()
	{
		var oldGeeks = m_GeekLogic.OldGeeks(new DateTime(1970, 1, 1));
		return View(new GeekListModel
		{
			Geeks = oldGeeks.Select(g=>new GeekListItemModel{
				Id=g.Id,
				Name = g.Name,
				Age = (int)((new TimeSpan(
						DateTime.Now.Ticks - g.DateOfBirth.Ticks
					).Days) / 365.25) // quick and dirty age
			})
		});
	}
}
```

Note that the underlying data technology and type of repository are irrelevant to the controller accessing the repository.

### Unit testing with repositories

Because the individual technology and data source behind the repository is not implied in the usage of the repository it is really easy to test only the components which are important to the usage.

Below is an example of a unit test of a method which uses a repository:

``` csharp
[TestMethod]
public void OldGeeksTest()
{
	List<Geek> geeks = new List<Geek>
	{
		new Geek{
			Id = 1,
			Name = "Bill Gates",
			DateOfBirth = new DateTime(1955,10,24)
		},
		new Geek{
			Id = 2,
			Name = "Steve Jobs",
			DateOfBirth = new DateTime(1955,2,28)
		},
		new Geek{
			Id = 3,
			Name = "Albert Einstein",
			DateOfBirth = new DateTime(1879,3,14)
		}
	};
	IRepositoryDataSource<Geek> geekDataSource =
		new InMemoryRepositoryDataSource<Geek>(geeks);
	IRepository<Geek> geekRepository =
		new SimpleRepository<Geek>(geekDataSource);
	GeekLogic sut = new GeekLogic(geekRepository);
	var oldGeeks = sut.OldGeeks(new DateTime(1955, 3, 1)).ToList();
	Assert.AreEqual(2,oldGeeks.Count());
	Assert.AreEqual(2, oldGeeks[0].Id);
	Assert.AreEqual(3, oldGeeks[1].Id);
}
```

Note the InMemoryRepositoryDataSource which is used in this example has some differences to the actual EF4.1 data source. One important difference is that when objects are added to an EF data source the foreign keys are populated in both directions whereas with the in memory repository they are only populated in the direction to which you are adding objects.

An example solution is available [here]({{site.baseurl}}/files/posts/{{page.date | date: '%Y' }}/StaticVoid.Repository.Demo.zip) which shows the above examples in a running site.

I hope this post is helpful.
