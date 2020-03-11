---
title: Request id tracing
date: 2016-01-08 15:04:23
categories: [monitoring]
tags: [tracing logger security monitoring]

layout: page
---

## What is distributed tracing?

Modern applications and sites increasingly use many interconnected services. An application architecture that relies on many services or microservices is often referred to as a distributed system.

**Distributed tracing** is the process of tracking the activity resulting from a request to an application. With this feature, you can:
* Trace the path of a request as it travels across a complex system
* Discover the latency of the components along that path
* Know which component in the path is creating a bottleneck

AKA as CorrelationId

Commonly used as:

- Http request/response as a headers

## Javascript/NodeJS

### [Continuation Local Storage](https://github.com/othiym23/node-continuation-local-storage)

Continuation-local storage works like thread-local storage in threaded programming, but is based on chains of Node-style callbacks instead of threads. The standard Node convention of functions calling functions is very similar to something called "continuation-passing style" in functional programming, and the name comes from the way this module allows you to set and get values that are scoped to the lifetime of these chains of function calls.

## Cloud native approach

### AWS X-Ray – Distributed Tracing System

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components. You can use X-Ray to analyze both applications in development and in production, from simple three-tier applications to complex microservices applications consisting of thousands of services.

#### Benefits

Review request behavior, Discover application issues

#### Observations

Only available for AWS services

## References

[W3C Recommendation 06 February 2020: Trace Context standard](https://www.w3.org/TR/trace-context/)

Initiative in W3C to standarize the practice
