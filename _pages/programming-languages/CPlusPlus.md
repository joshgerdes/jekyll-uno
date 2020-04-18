---
title: C Plus Plus
date: 2016-01-08 15:04:23
category: programming-languages
tags: []
layout: page
---

Make sure you have installed [Xcode command line tools](http://sourabhbajaj.com/mac-setup/Xcode/). Check the C++ version to make sure it is Clang 4.0+.

```bash
$ c++ --version
Apple LLVM version 5.1 (clang-503.0.38) (based on LLVM 3.4svn)
Target: x86_64-apple-darwin13.1.0
Thread model: posix
```

## Compilation

To be able to compile files from your terminal you can add the following alias in your `env.sh` file.

```bash
alias cppcompile='c++ -std=c++11 -stdlib=libc++'
```

Then you can run all cpp file directly using `cppcompile main.cpp` and it will use C++11 so no errors in the case of using vectors, auto, sets etc.

A common practice is to use a `Makefile` to simplify and declare how to compile build and run the code
