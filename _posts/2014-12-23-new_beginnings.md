---
title:  "New beginnings"
date:   2014-12-23
excerpt: "Today I started a new job and a new project. I'm going to be blogging much more about this over the coming months."
redirect_from:
  - 2014/12/23/new_beginnings
---
For a long time I have wanted to do my own project. I have had plenty of ideas which I would love to build but I've never had the time to commit to a serious effort completing any of them, especially after becoming a dad. So I decided to take a year off to try an idea out for myself. I'm really excited about taking this chance so over the next few months I'm going to be posting more information about what I'm doing and how the project is going.

Today is my first day on my new project. Its a little weird to think I wont be going back to the office for the rest of the year but its also pretty exciting.

My project is going to be a website and SEO is going to be one important aspect of the site. Before starting I have though a lot about what tech stack I wanted to use for the project. As a significant proportion of the project is likely to be in javascript I decided to use the [ASP.NET 5 (vNext)](http://www.asp.net/vnext/overview/aspnet-vnext/aspnet-5-overview) which has much better support for stuff like NPM and grunt (and I'm a sucker for bleeding edge pain and suffering). I also decided to use [ReactJS.NET](http://reactjs.net/) as it supports server side rendering of react components which will allow me to give the site a single-page-app feel while still allowing search engines to index the site without JS.

Enter my first problem, there's not really any support yet for ReactJS.NET and vNext. Fortunately its all open source and hopefully shouldn't be too hard to add that support in but I suppose this is the price to pay for going bleeding edge.

By the end of the day however I have made some progress. I have a basic site in source control and deployed on Azure, I have learnt a lot about the new vNext project structure and especially about the relationship between old and new .NET. I have also learnt quite a bit about different module systems (other than AMD which I am familiar with), and hacked around with React.NET.
