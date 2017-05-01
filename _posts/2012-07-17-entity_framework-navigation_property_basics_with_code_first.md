---
title:  "Entity Framework - Navigation Property Basics with Code First"
date:   2012-08-01
excerpt: "Navigation properties are Entity Frameworks way of representing Foreign Key relationships in databases as C# object references. In this post I explore the basics of how to use Navigation Properties with C# and how they work."
redirect_from:
  - 2012/7/17/entity_framework-navigation_property_basics_with_code_first
  - 2012/07/entity-framework-navigation-property.html
---
### What is a navigation property?

Navigation properties are Entity Frameworks way of representing Foreign Key relationships inside the database. Navigation properties allow you to define relationships between entities (rows in your database) in a way that makes sense in an object oriented language. Consider the following database:

![User-Post relationship]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/user-post-relationship.png)


As you can see a post has an author and that is relationaly linked inside our database. So how would we represent this same structure inside of an application (if we ignore the way this is implemented in a relational database)? It seems sensible that we would model this same structure with something like the following:

``` csharp
public class User
{
	public string Name { get; set; }
}

public class Post
{
	public User Author { get; set; }
}
```


Which means we can use it in code like this:

``` csharp
String.Format("{0} wrote this post", post.Author.Name);
```

What Entity Framework navigation proprieties do is to allow us to do just this with our database models. For example the above database structure could be represented as:

``` csharp
public class User
{
	public int Id { get; set; }
	public string Name { get; set; }
}

public class Post
{
	public int Id { get; set; }
	public User Author { get; set; }
}
```

### How do Navigation Properties work?

When you are using navigation properties in your code you are asking Entity Framework to automatically perform a SQL join between your two tables. For example:

``` csharp
context.Posts.Where(p => p.Author.Name == "Luke");
```

will be translated into the following SQL*:

``` sql
SELECT
	 p.Id,
	 p.Author_Id
   FROM  Posts AS p
	 INNER JOIN Users AS u ON p.Author_Id = u.Id
   WHERE u.Name = N'Luke'
```

As you can see our relationship in c# has been converted into the equivalent SQL join.

### How do I load my properties (Why is my navigation property null)?

Navigation properties are not loaded by default, so its important to know how and when you need to load navigation properties. So lets look at some scenarios and see what entity framework will give us. These scenarios are based off the following data:

#### User

|Id|Name|
|::|:-:|
|1|Luke|
|2|Bob|

#### Post

|Id|Author_Id|
|:-:|:-:|
|1|1|
|2|2|



#### Case 1 :

``` csharp
context.Posts.ToArray();
```

When we make this request we get the following:

``` json
{
	"posts": [
		{
			"id": 1,
			"author": null
		},
		{
			"id": 2,
			"author": null
		}
	]
}
```

As you can see we have retrieved all the posts but haven't received any of the linked authors.

#### Case 2:


```csharp
context.Posts.Where(p => p.Author.Name == "Luke").ToArray();
```

When we make this request we get the following:


``` json
{
	"posts": [
		{
			"id": 1,
			"author": null
		}
	]
}
```

In this case the `where` clause successfully interacts with the author to filter by name, however when the results are returned the author is still not linked.

#### Case 3:

```csharp
using System.Data.Entity; //this is required for .Include
...
context.Posts.Include(p => p.Author).ToArray();
```

When we make this request we get the following:

``` json
{
	"posts": [
		{
			"id": 1,
			"author": {
				"id":1,
				"name": "Luke"
			}
		},
		{
			"id": 2,
			"author":  {
				"id":2,
				"name": "Bob"
			}
		}
	]
}
```

As you can see by adding a `.Include` statement we are able to fetch the linked authors.

#### A note on lazy loading

Lazy loading is also an alternative to using the .Include syntax, however I recommend against using it in almost all cases as it makes it very easy to introduce subtle performance issues into your application. in addition using the include syntax makes it much more obvious what queries your code performs so increases readability.

### How does Entity Framework detect Navigation Properties

When entity framework examines a class which is attached to the context it finds other complex type properties on the class and assumes that they are a foreign key to that table. Entity framework then creates a foreign key with the name `[PropertyName]_[PropertyIdName]` for example in the case of the post class the `Author` is `[PropertyName]` and in the user table `Id` is the Id. This means `Author_Id` is generated as the foreign key name.

The rules around navigation properties what's acceptable and how they are generated are defined by a set of conventions. I'm not going to go into any more detail on how these work but for more information you can take a look at the following pages:

 - [EF Feature CTP5: Pluggable Conventions](http://blogs.msdn.com/b/adonet/archive/2011/01/10/ef-feature-ctp5-pluggable-conventions.aspx)
 - [MSDN - System.Data.Entity.ModelConfiguration.Conventions Namespace]
 - [Entity Framework Navigation Property generation rules](http://stackoverflow.com/a/11081568/1070291)


### More than the defaults with the Model Builder

Entity framework provides a mechanism to configure additional information about navigation properties. This additional configuration can be done using the Model Builder. The model builder allows control over how Entity Framework represents the database, one of the features of the model builder allows for control over how foreign keys in the database are translated to Navigation Properties in the Entity Framework Model.

To get access to the model builder you will need to override the `OnModelCreating` method on your `DbContext`. You can then use the `modelBuilder` argument to structure your Entity Framework Model.

```csharp
public class MyContext : DbContext
{
	protected override void OnModelCreating(DbModelBuilder modelBuilder)
	{
	}   
}
```

The Model Builder uses a two part fluent expression to define navigation properties within the model. The first part of the expression defines the navigation property on the current entity, the second part of the expression defines the reverse navigation property. Navigation properties properties can be either **Optional** (ie *0..1 to x*), **Required** (ie *1 to x*) or **Many** (ie ** to x*). So lets take a look at some examples:

#### Optional relationship

If you have the following classes:

``` csharp
public class Entity1
{
    public int Id { get; set; }
}

public class Entity2
{
    public int Id { get; set; }
    public Entity1 Entity1 { get; set; }
}
```

Using the following model builder statement

```csharp
protected override void OnModelCreating(DbModelBuilder modelBuilder)
{
    modelBuilder.Entity<Entity2>().HasOptional(e => e.Entity1).WithMany();
}  
```

Will create the following relationship

![Optional relationship]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/optional-relationship.png)

**Note** the two parts of the query the first to define `Entity1` navigation property, the first part defines an optional relationship (ie a nullable foreign key) and the second part `.WithMany()` defines the remote entity's (`Entity1`) multiplicity. Using `.WithMany()` with no argument tells Entity Framework that the relationship does not have a remote navigation property.

#### Required Relationship

If you have the following classes:

```csharp
public class Entity1
{
   public int Id { get; set; }
   public List<Entity2> Entity2s { get; set; }
}

public class Entity2
{
   public int Id { get; set; }
   public Entity1 Entity1 { get; set; }
}
```

Using the following model builder statement

```csharp
protected override void OnModelCreating(DbModelBuilder modelBuilder)
{
	modelBuilder.Entity<Entity2>()
		.HasRequired(e => e.Entity1)
		.WithMany(e => e.Entity2s);
}   
```

Will create the following relationship

![Required relationship]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/required-relationship.png)

**Note** that in this example we have specified a remote collection for the relationship. This means that you can use the `Entity2s` property to find all linked entities.

#### Many Relationship

If you have the following classes:

```csharp
public class Entity1
{
	public int Id { get; set; }
	public List<Entity2> Entity2s { get; set; }
}

public class Entity2
{
	public int Id { get; set; }
	public List<Entity1> Entity1s { get; set; }
}
```

Using the following model builder statement

```csharp
protected override void OnModelCreating(DbModelBuilder modelBuilder)
{
	modelBuilder.Entity<Entity2>()
		.HasMany(e => e.Entity1s)
		.WithMany(e => e.Entity2s);
}
```

Will produce the following relationship

![Many relationship]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/many-relationship.png)

With the following database tables
![Many database relationship]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/many-database-relationship.png)

**Note** that here we have chained two `.Many` statements to produce a many to many relationship. As you can see the Entity Framework has created a link table in the database but the actual link in the model is created as two collections (without a link table) which makes more sense in c#.

### Wrapping up

In this post we have looked in detail at navigation properties, what they are, how they are detected and how they are configured. As with many ORMs Entity Framework provides an abstraction over database Foreign Keys. As with any abstraction its really important to understand its limitations. I hope this post helps you better understand how Navigation Properties work and enables you to make good decisions when dealing with Entity Framework.


[MSDN - System.Data.Entity.ModelConfiguration.Conventions Namespace]: http://msdn.microsoft.com/en-us/library/system.data.entity.modelconfiguration.conventions(v=vs.103).aspx
