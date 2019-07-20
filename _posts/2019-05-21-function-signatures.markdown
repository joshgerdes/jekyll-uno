---
title:  "We can't even make function signatures consistent"
date:   2019-05-21 12:00:00
categories: [just-saying]
tags: [serverless]
---

Not even simplest things in IT can be simple and efficient, everybody wants their own way to define a computing function.

![wtf](https://media.giphy.com/media/G6sJqVpD1U4jC/giphy-downsized.gif "wtf")

## AWS Lambda

```javascript
'use strict'

exports.handler = function(event, context, callback) {
  callback(null, { test: 1234 })
}
```

## Azure Functions

```javascript
// You must include a context, but other arguments are optional
module.exports = function(context) {
    // Additional inputs can be accessed by the arguments property
    if(arguments.length === 4) {
        context.log('This function has 4 inputs');
    }
};

// or you can include additional inputs in your arguments
module.exports = function(context, myTrigger, myInput, myOtherInput) {
    // function logic goes here :)
};
```

## Google Cloud Functions

```javascript
/**
 * HTTP Cloud Function.
 *
 * @param {Object} req Cloud Function request context.
 * @param {Object} res Cloud Function response context.
 */
exports.helloGET = (req, res) => {
  res.send('Hello World!');
};
```

## OpenFaaS

```javascript
module.exports = (callback, context) => {
    callback(null, { test: 1234 })
}
```

## OpenWhisk

```javascript
function main(args) {
    return { payload: { test: 1234 } };
}
```
