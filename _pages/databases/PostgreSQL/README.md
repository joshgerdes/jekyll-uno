---
title: PostgreSQL
date: 2016-01-08 15:04:23
category: databases
tags: []
layout: page
---

## Install using Brew

To install run:

```
$ brew update
$ brew install postgresql
```

`brew` will initialize the database as part of the installation scripts and creates a default login with your username

### Usage

To have launchd start postgresql now and restart at login:

```
$ brew services start postgresql
```

Or, if you don't want/need a background service you can just run:

```
$ pg_ctl -D /usr/local/var/postgres start
```

## GUI Tools

### pgAdmin 4 \(free\)

```
$ brew cask install pgadmin4
```



