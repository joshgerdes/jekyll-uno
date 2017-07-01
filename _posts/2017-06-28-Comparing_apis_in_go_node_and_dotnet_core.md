---
title:  "Comparing APIs in go, rust, node and dotnet core"
date:   2017-06-28
excerpt: "Comparing how a basic API in node, go and dotnet might look, and what the experience and performance is like in each."
---

APIs are an important part of modern web applications. They provide a gateway for communication between a back end server and a frontend application. APIs also provide an integration point for other applications. I come from a dotnet background but I am really interested in seeing how APIs work in other languages, so for fun I wrote basic APIs in dotnet core, go and node. 

I built the APIs to cover two different methods

 - GET `/add/x/to/y` which returns a JSON response `{ "sum": <x + y> }`
 - POST `/add` which takes a list of numbers in XML `<numbers><value>x</value>...</numbers>` and returns `<sum>123</sum>`

This gives an idea on how serialisation, routing, verbs and body processing work in each language.

## dotnet

Dotnet core scaffolds a WebApi for you with the `dotnet new webapi` command.

![Project structure]({{site.baseurl}}/images/posts/{{page.date | date: '%Y' }}/dotnet-core-scaffold.png)

I then deleted some of the un-needed bits from the project like logging and config files. This left me with a total of 85 lines of code across 5 files to implement the basic api. This included many of the scaffolded files like the `.csproj` and `Startup.cs`.

### The code
``` csharp
[XmlRoot(ElementName = "numbers")]
public class Numbers
{   
    [XmlElement("value")]     
    public int[] Values { get; set; }
}

public class AddController : Controller
{
    [HttpGet]
    [Route("add/{x}/to/{y}")]
    public IActionResult Get(int x, int y)
    {
        return Ok(x + y);
    }

    [HttpPost]
    [Route("add")]
    public IActionResult Post([FromBody]Numbers numbers)
    {
        return Ok(new { sum = numbers.Values.Sum() });
    }
}
```

In addition I also needed to add `.AddXmlSerializerFormatters()` to the ConfigureServices method in `Startup.cs` to enable XML support


I find this code reasonably simple and easy to read. I like that the route information is inline however I dont find the `IActionResult` return type particularly intuitive. The Serialisation is automatically handled by content type negotiation 

## nodejs

For the node example I started with a blank file and looked at a few tutorials to work out what I needed. The node example is a total of ~~42~~ 38 lines ([thanks tcoats](https://github.com/lukemcgregor/basic-api/pull/1)) over two files (including the `package.json`). I also added content type negotiation to the POST method (`res.format()`) for another 6 lines. This is not strictly necessary for the scenario but I thought it might be nice to compare.

### The code
``` javascript
var app = require('express')()
var xml = require('xml')

var bodyParser = require('body-parser')
require('body-parser-xml')(bodyParser)
app.use(bodyParser.json())
app.use(bodyParser.xml())

app.get('/add/:x/to/:y', (req, res) => {
    res.json({ sum: parseInt(req.params.x) + parseInt(req.params.y) })
})

app.post('/add', (req, res) => {
    var sum = req.body.numbers.value.map(parseInt).reduce((a, b) => a + b)
    res.format({
        xml: () => res.send(xml({sum:sum})),
        json: () => res.json({sum:sum})
    })
})

app.listen(8080)
```

I really liked the experience of writing an API in node, it was super simple and all of the serialisation was very easy. The thing I disliked the most was having to parse the int values out of strings (in both the XML and the querystring). This was annoying, if anyone knows a way to get typed stuff out on first go that would be really interesting.

## Go

I was really excited about doing the Go example as I like quite a lot of the language features. Go came to a total of 48 lines with another 5 if i wanted content type negotiation. I couldnt manage to get the request body to automatically negotiate de-serialisation which was a bit of a shame but I would love to here how to do that if someone knows.

### The code

```go
package main

import (
	"encoding/xml"
	"log"
	"net/http"
	"strconv"

	"github.com/jchannon/negotiator"
	"github.com/julienschmidt/httprouter"
)

type numbers struct {
	Value []int `xml:"value"`
}

type sum struct {
	Sum int64 `xml:",chardata" json:"sum"`
}

func main() {
	router := httprouter.New()
	router.GET("/add/:x/to/:y", func(responseWriter http.ResponseWriter, request *http.Request, params httprouter.Params) {
		x, _ := strconv.ParseInt(params.ByName("x"), 10, 64)
		y, _ := strconv.ParseInt(params.ByName("y"), 10, 64)

		if err := negotiator.Negotiate(responseWriter, request, sum{x + y}); err != nil {
			http.Error(responseWriter, err.Error(), http.StatusInternalServerError)
		}
	})

	router.POST("/add", func(responseWriter http.ResponseWriter, request *http.Request, params httprouter.Params) {
		decoder := xml.NewDecoder(request.Body)
		var payload numbers
		err := decoder.Decode(&payload)
		if err != nil {
			http.Error(responseWriter, err.Error(), http.StatusInternalServerError)
			return
		}
		defer request.Body.Close()
		var total int64

		for val := range payload.Value {
			total += int64(val)
		}

		if err := negotiator.Negotiate(responseWriter, request, sum{total}); err != nil {
			http.Error(responseWriter, err.Error(), http.StatusInternalServerError)
		}
	})

	log.Fatal(http.ListenAndServe(":8080", router))
}

```

I was the least happy with how this code turned out. The serialisation stuff was difficult to do, especially in comparison to node. I also find the code to be much less succinct than either of the other languages. I expect this could be alleviated if I knew a few more libraries to help with these things. Its also important to note that this was my very first go program, whereas I have quite a bit of experience with both c# and client-side javascript.

## Rust (thanks[@Kazetsukai](https://github.com/lukemcgregor/basic-api/pull/2))

I know absolutely nothing about rust (before today), so fun times.

> Rust is a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety. 

The rust example is 42 lines without content type negotiation (including the config files required). 

``` rust
#![feature(plugin)]
#![plugin(rocket_codegen)]

extern crate rocket;
extern crate elementtree;
#[macro_use] extern crate rocket_contrib;

use rocket::data::Data;
use rocket_contrib::{JSON, Value};
use elementtree::Element;

#[get("/add/<x>/to/<y>")]
fn add_json(x: i32, y: i32) -> JSON<Value> {
    JSON(json!({ "sum": (x+y) }))
}

#[post("/add", data = "<numbers>")]
fn add_xml(numbers: Data) -> String {
	let root = Element::from_reader(numbers.open()).unwrap();
	let sum : i32 = root.find_all("value").map(|e| e.text().parse::<i32>().unwrap()).sum();

	let mut result = Element::new("sum");
	result.set_text(sum.to_string());

	return result.to_string().unwrap();
}

fn main() {
    rocket::ignite().mount("/", routes![add_json, add_xml]).launch();
}
```

I find looking a the code the JSON GET example is very elegant and simple, less so the XML POST example. The routing is also super cool, you decorate a function with its route information and then just pass a list of functions to the server. That is super succinct. The performance of the rust service was also amazing being the fastest code example. However the service was not very stable, if I made more concurrent requests than there were cores on the machine the service went into some kind of deadlock, which is pretty poor. Rocket recommends putting the API behind NGINX which would prevent this issue. The tooling support was also much lower than for the other languages. I couldnt get a debugger to work at all, though there are some that are available. This means it wasn't launchable from VS Code. 

## Performance

To get a better idea of the differences between the languages I wrote a load tester which hits each APIs `/add/x/to/y` method with a million requests. Just for fun I wrote this in Go which gave me a bit of a chance to play with the concurrency features such as channels.

||Median| Mean| Max |Total time|
|::|:-:|:-:|:-:|:-:|
|**go**|0.21ms|0.22ms|151.7ms|28.1s|
|**nodejs**|0.80ms|0.97ms|34.34ms|123.3s|
|**dotnet**|0.39ms|0.43ms|1045.2ms|54.5s|
|**rust**|0.20ms|0.21|8.73ms|27.9s|

There are a couple of points of interest in this data

### nodejs total time

Node is inherently single threaded, I was hitting the api with concurrent load which is why the total time was so long. I did some research and there are a few ways to get around this, either run a load balancer across multiple instances (which would make sense if this was a docker process) or run a [node cluster](https://nodejs.org/api/cluster.html) which is essentially a single machine load balancer across processes.

> A single instance of Node.js runs in a single thread. To take advantage of multi-core systems the user will sometimes want to launch a cluster of Node.js processes to handle the load.
>
>The cluster module allows easy creation of child processes that all share server ports.

### dotnet max time

Dotnet processes perform a process called JIT (Just In Time compilation) which lazy loads code components as they are required, theres a great article about how this works [here](http://www.telerik.com/blogs/understanding-net-just-in-time-compilation). This means that on first request the process is loading modules into memory and performing compilation. This affects the first request on dotnet processes. There are ways of getting around this such as heating the process on deploy or using NGen to produce a native binary that doesn't require JIT.

### Conclusions

I ran this test on both my Windows box (i7) and my macbook (i5) both gave similar proportional results, however the timer resolution for go on windows is very low (0.5ms) which didn't give as useful figures. As expected Go and rust were the fastest followed by dotnet and nodejs. 