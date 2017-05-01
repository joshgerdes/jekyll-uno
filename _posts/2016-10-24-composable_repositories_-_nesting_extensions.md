---
title:  "Composable Repositories - Nesting Extensions"
date:   2016-10-24
excerpt: "A look at several problems with nesting extension methods in LINQ and how to get around these issues with and expression visitor."
redirect_from:
  - 2016/10/24/composable_repositories_-_nesting_extensions
---
In my previous post [Composable Repositories](http://blog.staticvoid.co.nz/2015/9/8/composable_repositories), I introduced using extension methods as the repository in applications. This allows repositories to get much better reuse and be more expressive in their usage. In this post I will look at two issues with extension method based repositories in LINQ and introduce some libraries I built to resolve these issues.

First a refresher, in my previous post I used the following query as an example.

``` csharp
public static IQueryable<Person> InRegion(this IQueryable<Person> people, string region)
{
    return people.Where(p => p.Addresses.Any(a => a.Region == region));
}

public static IOrderedQueryable<Person> OrderByName(this IQueryable<Person> people)
{
    return people.OrderBy(x => x.Name);
}

public static IQueryable<T> Page<T>(this IOrderedQueryable<T> entities, int page, int pageSize = 3)
{
    int skip = Math.Max(0, page - 1) * pageSize;
    return entities.Skip(skip).Take(pageSize);
}

public static IQueryable<PersonModel> ToViewModels(this IQueryable<Person> people)
{
    return people.Select(person => new PersonModel
    {
        Name = person.Name,
        Addresses = person.Addresses.Select(a => a.PostalAddress)
    });
}

//and the query
Context.People
    .InRegion("Shire")
    .OrderByName()
    .Page(1)
    .ToViewModels()
    .ToArray();
```

As you can see this uses chained extension methods to generate the underlying query.

### Issue one: Queryable extensions in the projection

This brings us to the first issue, if you look at the `ToViewModels` projection call you will see the following:

``` csharp
Addresses = person.Addresses.Select(a => a.PostalAddress)
```

Now wouldn’t it be better if we could nest our extension methods here and reuse another projection which relates to addresses? Something like the following:

``` csharp
Addresses = person.Addresses.ToAddressViewModels()
```

Now if you write this and execute it with Entity Framework you will get the following error:

> LINQ to Entities does not recognize the method 'ToAddressViewModels(Address)' method, and this method cannot be translated into a store expression.

This is a bit weird as we seem to be able to use extension methods elsewhere in our queries without issue, why is this instance different? Why can we use `Select` but not our extension which just does a select internally, The problem here comes down to where this occurs in our expression. As you can see in our extension this is not acting on the root queryable directly but instead effecting what essentially amounts to a sub query.

When we were acting directly on the queryable the LINQ method was essentially visiting the expression *returned* by our extension methods, however when we use an extension inside the results nothing has been returned yet so the expression visitor needs to evaluate and translate that method to an expression. The issue is that the visitor at that point doesn't know that the extension you wrote is just another expression (or even that it could possibly be an expression).

### Issue two: Single element projection

Imagine our projection was instead into a singular, for example

``` csharp
Address = person.Address.ToViewModel()
```

This is a very similar problem to that which we are looking at above with one key distinction, we are no longer acting with set based (queryable) logic, instead we are acting on a singular element. At its heart is the same problem as above but it is a little harder to get around.

It would be desirable to solve both of these problems to allow even more expressive queries, especially in relation to projection of entities.

## The solution

To be able to solve these problems we need to get into the depths of LINQ and translate our extension methods for the benefit of the downstream expression visitors. This is possible by writing a new expression visitor which replaces the extension method calls in the expression tree with the actual expressions we wanted to execute. This will let our Entity Framework (or generic LINQ based ORM) expression visitor carry on with its translation to SQL without needing to understand the internals of our extension method.

#### Plugging into the pipeline

The first thing we will need to do is to get our own expression visitor into the mix, we can do this can build a our own [queryable implementation](https://github.com/lukemcgregor/LinqExpander/blob/master/LinqExpander/ExpandableQuery.cs), and a [queryable extension](https://github.com/lukemcgregor/LinqExpander/blob/master/LinqExpander/AsExpandableExtension.cs) to convert to our new queryable implementation. This will let us get amongst with our own [expression visitor](https://github.com/lukemcgregor/LinqExpander/blob/master/LinqExpander/ExpandableVisitor.cs) which is executed as we walk the expression tree.

This means we can do something like this to let our expression visitor participate in translating the LINQ query.

``` csharp
Context.People
    .AsExpandable()
    .InRegion("Shire")
    .OrderByName()
    .Page(1)
    .ToViewModels()
    .ToArray();
```

We are interested especially in the `VisitMethodCall` part of the visitor which will get executed for every extension method. At this point we could intercept and do something with every extension method that gets executed in LINQ but this would mean we would need to manually exclude things which Entity Framework understands (like `Select` and `Where`) and also potentially run into the same problem with things which aren't actually translatable to SQL, so instead we are going to use a marker attribute to tag extension methods we are OK with replacing, `ExpandQueryableAttribute`. Inside the visitor we will then replace any of these queryable replacements with the invoked/expressionised version of the queryable.

This can be used as follows:

``` csharp
[ExpandQueryable]
public static IQueryable<AddressModel> ToViewModels(this IQueryable<Address> addresses)
{
    return addresses.Select(address => new AddressModel
    {
        StreetNumber = address.Number,
        Street = address.Line1
    });
}
```

Voila problem one solved.

The next part will be a little more ninja, to replace the non-queryable parts we don't have anything to invoke and return us an expression. So we are going to need to change the way we write our extension methods to be a little more expression-like. Lets write our singular projection as an expression:

``` csharp
public static Expression<Func<Addresss, AddressModel>> ToViewModelExpression()
{
    return address => new AddressModel
    {
        StreetNumber = address.Number,
        Street = address.Line1
    };
}
```

This isn't really usable in our expression tree yet as we don't have an entry point from our query. Getting an entry point is a little tricky as how do we can't just use an expression on a singular without invoking it (which would get us right back to the original problem. So we are going to use a little bit of a trick, let's create an extension method and use it as a placeholder for the actual expression. We will decorate this with an attribute which points back to the actual expression to execute in its place. When we visit such an extension method in our visitor we will replace it with the expression from the attribute in the expression tree.

``` csharp
[ReplaceInExpressionTree(MethodName = nameof(ToViewModelExpression))]
public static AddressModel ToViewModel(this Address entity)
{
    // We could throw a not implemented exception here as we won't ever
    // execute this unless we use it outside of our visitor. But doing this
    // allows you to use the extension on an in memory object tree without
    // needing our custom visitor to replace it.
    return ToViewModelExpression().Compile()(entity);
}
```

This means we can now use our singular extension methods inside our projections, and both of our original problems are solved.

To save you having to write all of this complex expression magic in you application I have put this library on Nuget and [Github](https://github.com/lukemcgregor/LinqExpander)

<pre class="nuget-button" style="width:100px">Install-Package StaticVoid.Core.IO</pre>

A big thanks to those who helped me learn how expression trees work on StackOverflow in the following questions:

 - [Expression visitor only calling VisitParameter for some lambda expressions](http://stackoverflow.com/q/39864270/1070291)
 - [Projection of single entities in EF with extension methods](http://stackoverflow.com/q/39585427/1070291)

And to [@LordTerabyte](http://stackoverflow.com/a/10726256/1070291)  whose [code](http://pastebin.com/4fMjaCMV) I used as a starting point for these extensions.

## Magic but whats the point?

By enabling nesting in our extension methods we can nest our projections so that we can take our data model and transform it into a more appropriate usage model for use in our applications. We can then reuse these translation extensions so if we want something in the a usage model we always use the same code.

But probably more importantly this allows us to solve an under/over fetch problem. All of the projection code is essentially executed inside of SQL, this means that the full data model is available so we don't need to worry about including the joined tables we require to ensure those navigation properties are not null. We also don't need to worry about including too much information in the result set as we are only going to get the columns which directly map to our projected model. This is a really big benefit in terms of both code complexity and potential performance bottlenecks.

#### A final word of caution

This method allows you to push far more logic into SQL for processing. Be very careful to keep in mind the queries you are generating with nested projection and be sure that the SQL you are generating is kept performant. If you aren't careful about what you write (as with any LINQ based query) you can execute things which are a little crazy when transpiled to SQL.
