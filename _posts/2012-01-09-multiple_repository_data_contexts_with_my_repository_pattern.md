---
title:  "Multiple Repository Data Contexts with my Repository Pattern"
date:   2012-01-09
excerpt: "I recently needed to have links to multiple different database contexts within an application I was developing using StaticVoid.Core.Repository. I use ninject for all of my dependency injection and I though it might be useful to share how I managed to get the repository binding correctly to different versions of DbContext depending on the type requested."
redirect_from:
  - 2012/1/9/multiple_repository_data_contexts_with_my_repository_pattern
  - 2012/01/multiple-repository-data-contexts-with.html
---
I recently needed to have links to multiple different database contexts within an application I was developing using StaticVoid.Core.Repository. I use ninject for all of my dependency injection and I though it might be useful to share how I managed to get the repository binding correctly to different versions of DbContext depending on the type requested. Below is a little extension method I wrote to deal with this problem:

``` csharp
public static bool IsInjectingToRepositoryDataSourceOfNamespace(
         this IRequest request, string entityNamespace)
{
    if(request.ParentRequest.Service.GetGenericTypeDefinition() ==
         typeof(IRepositoryDataSource<>))
    {
        return request.ParentRequest.Service.GetGenericArguments().First().Namespace
             == entityNamespace;
    }

    return false;
}
```
This can then be used in the following way:

```csharp
Bind<DbContext>().To<Data1Context>().When(t =>
	t.IsInjectingToRepositoryDataSourceOfNamespace("MyApp.Data1"));
Bind<DbContext>().To<Data2Context>().When(t =>
	t.IsInjectingToRepositoryDataSourceOfNamespace("MyApp.Data2"));
```

This makes it quite tidy to link to multiple data contexts and means that anywhere in your app ninject will infer the data context for that type based on the namespace of the type.
