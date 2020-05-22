---
title: Python - Performance tuning
date: 2020-05-22 09:50:26
category: programming-languages
tags: [python performance-tunin]

layout: page
---

## [memory-profiler](https://pypi.org/project/memory-profiler/)

This is a python module for monitoring memory consumption of a process as well as line-by-line analysis of memory consumption for python programs. It is a pure python module which depends on the psutil module.

## Installation

Install via pip:

```
$ pip install -U memory_profiler
```

The package is also available on conda-forge.

To install from source, download the package, extract and type:

```
$ python setup.py install
```

## MPROF

In order to analize memory consumption by the scripts and make optimizations you can use mprof to evaluate consumtion of memory over time and mprof plot to check the evolution over time of each file extraction

```
mprof run --python script.py
```

```
pip3 install matplotlib
mprof plot
```

