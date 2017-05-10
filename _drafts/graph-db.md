## So whats a graph database

Graph databases are a different way of conceptualizing information to the table structures used by relational databases. At a root conceptual level a relational database is a set lists (tables) whereas a graph database is a set of nodes connected by edges (relationships).

With a relational database relations are created by storing a key to another entity on the related entity (row). When we traverse a relationship we take the key and go to an index on the table to find the linked entity. This traversal has a cost, for example if our index uses a b-tree the lookup time is O(log(n)) where n is the number of rows in the table. Relational databases are strongly typed.

Graph databases are a bit different, instead of storing a key to the other node they use a pointer to that node. This means that traversal of relationships is O(1), making it far more efficient to traverse deeply nested structures. Graph databases are loosely typed.

## Permissions

Permissions systems grant _actors_ access to _actions_ on _resources_. The simplest permissions systems do this with a direct relationship between actors and resources, often only with one implicit action. It doesn't take much before a more complex nested permission structure with groups is required.

When groups are introduced the structure becomes a graph where a permission is defined by the existence of a directional path between an actor and an action on a resource. It doesn't matter how long this path is or if there are multiple paths simply that such a path exists.

## Storing permissions

This structure can be represented in a relational database however it is difficult to follow the structure and difficult to query the structure (especially with a possible infinite level of group nesting).

A graph database can represent this structure in an elegant and intuitive way, and the query language for a graph database is built to traverse such structures and to find the existence of paths through the graph. Neo4j is a graph database with a query language called cypher which will allow us to create and query a permissions graph.
