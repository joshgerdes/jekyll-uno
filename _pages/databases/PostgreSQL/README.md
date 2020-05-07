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


## Handy queries

### Show tuples per table

```sql
  SELECT schemaname AS schema,
         relname    AS table,
        n_live_tup  AS tuples
    FROM pg_stat_user_tables
ORDER BY schemaname, n_live_tup DESC;
```

### Stats per table

Returns stats of the table, like most common vals, etc

```sql
ANALYZE hazard.footprint;

select * from pg_stats where tablename like 'footprint';
```
