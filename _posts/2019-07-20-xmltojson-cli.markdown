---
title: "xmltojson-cli"
date:   2019-07-20 12:00:00
categories: [javascript]
tags: [xmltojson-cli]
---

Still working on the essential tolling for my personal projects I came with the idea of building a wrapper for xml to json transformation using a command that supports pipes

version v0.0.1 is already solving my problem, no need for future releases in the short term

Example:

```bash
echo '<doc p="test"><a>HelloWorld</a></doc>' | xmltojson
{
  "doc": {
    "_attributes": {
      "p": "test"
    },
    "a": {
      "_text": "HelloWorld"
    }
  }
}
```

We could combine with `jq .` and get a clean approach to extract data from xml:

```bash
echo '<doc p="test"><a>HelloWorld</a></doc>' | xmltojson | jq .doc.a._text
"HelloWorld"
```

Personal note: Duncker's candle problem applied to build tools focus in getting one thing done, no more, no less.

[xmltojson-cli]: https://www.npmjs.com/package/@gbalbuena/xmltojson-cli
