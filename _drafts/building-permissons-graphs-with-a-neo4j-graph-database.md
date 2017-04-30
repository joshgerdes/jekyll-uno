---
title:  "Building permissions graphs with a neo4j graph database"
excerpt: "There are many different data storage technologies around and each has specific strengths. This post looks at a permissions system and how this application is especially suited to graph based representations."
---

## So whats a graph database

Graph databases are a different way of conceptualizing information to the table structures used by relational databases. At a root conceptual level a relational database is a set lists (tables) whereas a graph database is a set of nodes connected by edges (relationships).

With a relational database relations are created by storing a key to another entity on the related entity (row). When we traverse a relationship we take the key and go to an index on the table to find the linked entity. This traversal has a cost, for example if our index uses a b-tree the lookup time is O(log(n)) where n is the number of rows in the table. Relational databases are strongly typed.

Graph databases are a bit different, instead of storing a key to the other node they use a pointer to that node. This means that traversal of relationships is O(1), making it far more efficient to traverse deeply nested structures. Graph databases are loosely typed.
