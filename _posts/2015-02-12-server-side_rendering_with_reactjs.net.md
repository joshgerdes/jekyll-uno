---
title:  "Server-side rendering a single page app with ReactJS.NET"
date:   2015-02-12
excerpt: "In the last few years web applications have been increasingly built in JavaScript.This provides rich interactive UI's but introduces problems with non-js search crawlers and initial page load performance. In this post I will look at server-side rendering of a JS application to mitigate these problems."
redirect_from:
  - 2015/2/12/server-side_rendering_with_reactjs.net
---
In the last few years we have seen a shift in the way web applications are built from JavaScript being a complementary tool to augment in functionality toward it being the main language in which an autonomous client side application is developed. Browsers have also helped the single page application paradigm with the introduction of the [history API](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Manipulating_the_browser_history) in HTML5. This means many recent web applications have been developed to only make a single page request and then subsequently make ajax calls back to the server to update the application. This gives users a much more responsive experience using web applications.

### Problems with single page applications
Building applications which render content from JavaScript introduces some interesting problems.

#### Initial load flickering
Traditionally when we browse web pages we get most of the content on the page immediately (with the notable exception of images). This is because a full HTML document complete with all of the content has been sent down from the server. Single page applications tend to send down a skeleton document on initial load and then pull in the correct bits for the actual page via JavaScript. This introduces a lot of movement on the page during initial load while the DOM changes structure as different parts are loaded. This can produce a disconcerting experience for a user watching this happen. There are of course many techniques which can be used to mitigate this effect.

#### SEO and search engines
While in recent years developers have been building JavaScript heavy applications, many search engine [webcrawlers do not execute javascript when indexing](https://developers.google.com/webmasters/ajax-crawling/docs/learn-more) sites. This is a bit of a problem if you have a single page application and want the content to be indexed by Google.

### Server-side rendering
As I posted last week I have just started on [my own project](/2014/12/23/new_beginnings) which I will be working on for the next year. My site is going to be heavily reliant on SEO but I don't want to constrain the user experience because search engines wont execute JavaScript. Enter server-side rendering (SSR).

The principal behind SSR is to take a JavaScript enabled page and optimistically execute the JavaScript required to reach the initial page state and then send down that generated DOM to the client rather than our skeleton page. This is actually pretty similar to what web technologies have been doing for years with server code generating the DOM and sending that down to users, but our language isn't ASP.Net, Rails or PHP its JavaScript that would normally execute in the browser.

The net effect of this optimistic generation of the DOM is that the page that has been sent to the client doesn't need to change at until user performs some actions. This means that it will render quickly in the browser rather than needing to wait for JS or possibly AJAX to complete. As a result search crawlers without JS will see complete content. Once that initial DOM is rendered in the browser our single page application can take over and register all the necessary JS events required.

#### [ReactJS.NET](http://reactjs.net/)
While I'm sure there are several tools which will enable you to do SSR, I love [React](http://facebook.github.io/react/) (made by Facebook) as a front-end rendering technology and Daniel Lo Nigro ([@daniel15](https://twitter.com/daniel15) who also works at Facebook) has done a great job building a server side rendering engine for React in .NET. This takes your react components and allows you to render them onto the page with some props passed in via c#.

    @Html.React("CommentsBox", new { initialComments = Model.Comments })

That's pretty tidy! What this will do is to generate the react DOM for this control and props and insert it into the page. You can then point react at that piece of DOM on the client-side and it will detect its already rendered, not modify the DOM and attach any additional JS bits it needs. I'm not going to go into any more detail about the actual server-side rendering code as there are plenty of details on the ReactJS.NET site.

### Using SSR to build a single page app
That's all great and useful functionality and allows you to render your react controls onto a single page but it isn't really a single page app just yet. For that to happen we need to have a couple of pages rigged to a router. In my example we will build a little application which has a list and a separate page for the detail of each list item.

Our app will have:

 - a mini router
 - a list view
 - a detail view
 - a controller

 When we load the page in our server side view we will use the ReactJS.NET helper to render out our react view.

 For our detail page we will make the router pass enough information from the list to display the detail page, so there's no need to ajax back to the server, however when we use the router to go back to our list page we wont pass in enough details to render the page instead we will go back to the server.

The net effect of this will be that we will have a single page app feel where we click an item in the list and immediately have our data available. All we need to do is re-render client side the specific section of the page that's relevant. This happens really fast. When we go back to the list page we show a loading message while the page goes back and retrieves data from the server. We still don't need to wait for very much here, only a small section of DOM being rendered and an ajax request, this is faster than doing a whole page request back to the server and re-rendering the entire DOM to the browser.

#### [The app](http://seofriendlysinglepageapp.azurewebsites.net/)

Have a play with the sample app with JS on and off, and check out the net tab to see requests going back to the server. (note: the back button isn't implemented properly and just forces a page refresh. In a real app you would use a proper router to help here)

#### [The source](https://github.com/lukemcgregor/SeoFriendlySinglePageApp)

As you can see this is pretty easy to do and gives a great result with JS on or off so its good for search engines too.

#### gotchas
There are a few things to note when doing SSR with a router:

 - ReactJS.NET wont do ajax requests or provide access to any browser variables so your initial page state cant call anything like window.
 - You need to have routing on both the server and client, the server must respond to all URLs the browser router creates.
 - If the user middle clicks a link, bypass the router completely as you want them to open the link in a new tab.

This tech is pretty cool, its great that we can build applications that get the best of both worlds when it comes to server vs client side rendering. Keep an eye on my blog over the next few weeks to hear more about my project.
