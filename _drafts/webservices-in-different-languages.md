APIs are an important part of modern web applications. They provide a gateway for communication between a back end server and a frontend application. APIs also provide an integration point for other applications. I come from a dotnet background but I am really interested in seeing how APIs work in other languages, so for fun I wrote basic APIs in dotnet core, go and node. 

I built the APIs to cover two different methods

 - GET `/add/x/to/y` which returns a JSON response `{ "sum": <x + y> }`
 - POST `/add` which takes a list of numbers in XML `<numbers><value>x</value>...</numbers>` and returns `<sum>123</sum>`

This gives an idea on how serialisation, routing, verbs and body processing work in each language.

## dotnet core

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

For the node example I started with a blank file and looked at a few tutorials to work out what I needed. The node example is a total of 42 lines over two files (including the `package.json`). I also added content type negotiation to the POST method (`res.format()`) for another 6 lines. This is not strictly nessacary for the scenario but I thought it might be nice to compare.

### The code
``` javascript
var express     = require('express');
var app         = express();
var bodyParser  = require('body-parser');
var xml         = require('xml');

require('body-parser-xml')(bodyParser);

app.use(bodyParser.json());
app.use(bodyParser.xml());

var port = process.env.PORT || 8080;
var router = express.Router();

router.get('/add/:x/to/:y', function(req, res) {
    res.json({ sum: parseInt(req.params.x) + parseInt(req.params.y) });
});

router.post('/add', function(req, res) {
    var sum = req.body.numbers.value.reduce((a, b) => parseInt(a) + parseInt(b), 0);
    res.format({
        xml: () => {
            res.send(xml({sum:sum}));
        },
        json: () => {
            res.json({sum:sum});
        }
    })
});

app.use('/', router);
app.listen(port);
```

I really liked the experience of writing an API in node, it was super simple and all of the serialisation was very easy. The thing I disliked the most was having to parse the int values out of strings (in both the XML and the querystring). This was annoying, if anyone knows a way to get typed stuff out on first go that would be really interesting.

## Go

I was really excited about doing the Go example as I like quite a lot of the language features. Go came to a total of  48 lines with another 5 if i wanted content type negotiation. I couldnt manage to get the request body to automatically negotiate de-serialisation which was a bit of a shame but I would love to here how to do that if someone knows.

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


## Performance

To get a better idea of the differences between the languages I wrote a load tester which hits each API with a million requests. Just for fun I wrote this in Go which gave me a bit of a chance to play with the concurrency features such as channels.

||Median| Mean| Max |Total time|
|::|:-:|:-:|:-:|:-:|
|**go**|0|0.14ms|8.51ms|17.2s|
|**nodejs**|1ms|0.86ms|57.58ms|107.5s|
|**dotnet**|0|0.22ms|548.29ms|29.0s|



## What do you think?

<a href='https://www.survey-maker.com' poll='1099972xa6B4c554-46' style='width:100%; display:block; text-align:right;'>survey</a>

## Make this better



<script>(function(i,s,o,g,r,a,m){i['QP']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//scripts.poll-maker.com/3012/pollembed.js','qp');</script>