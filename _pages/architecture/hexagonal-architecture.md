---
title: Hexagonal architecture (software)
date: 2021-03-23 11:49:00
category: architecture
tags: [architecture]
layout: page
---

From Wikipedia, the free encyclopedia

The hexagonal architecture, or ports and adapters architecture, is an architectural pattern used in software design. It aims at creating loosely coupled application components that can be easily connected to their software environment by means of ports and adapters. This makes components exchangeable at any level and facilitates test automation.[1]

## Origin
The hexagonal architecture was invented by Alistair Cockburn in an attempt to avoid known structural pitfalls in object-oriented software design, such as undesired dependencies between layers and contamination of user interface code with business logic, and published in 2005.[2]

The term "hexagonal" comes from the graphical conventions that shows the application component like a hexagonal cell. The purpose was not to suggest that there would be six borders/ports, but to leave enough space to represent the different interfaces needed between the component and the external world.[1]

## Principle
Example of hexagonal architecture with an inner hexagon representing the application core, and an outer hexagon for the adapters, the border between the two being the ports
Example of hexagonal architecture
The hexagonal architecture divides a system into several loosely-coupled interchangeable components, such as the application core, the database, the user interface, test scripts and interfaces with other systems. This approach is an alternative to the traditional layered architecture.

Each component is connected to the others through a number of exposed "ports". Communication through these ports follow a given protocol depending on their purpose. Ports and protocols define an abstract API that can be implemented by any suitable technical means (e.g. method invocation in an object-oriented language, remote procedure calls, or Web services).

The granularity of the ports and their number is not constrained:

a single port could in some case be sufficient (e.g. in the case of a simple service consumer) ;
typically, there are ports for event sources (user interface, automatic feeding), notifications (outgoing notifications), database (in order to interface the component with any suitable DBMS), and administration (for controlling the component);
in an extreme case, there could be a different port for every use case, if needed.
Adapters are the glue between components and the outside world. They tailor the exchanges between the external world and the ports that represent the requirements of the inside of the application component. There can be several adapters for one port, for example, data can be provided by a user through a GUI or a command-line interface, by an automated data source, or by test scripts.

## Criticism
The term "hexagonal" implies that there are 6 parts to the concept, whereas there are only 4 key areas. The term’s usage comes from the graphical conventions that shows the application component like a hexagonal cell. The purpose was not to suggest that there would be six borders/ports, but to leave enough space to represent the different interfaces needed between the component and the external world.[3]

According to Martin Fowler, the hexagonal architecture has the benefit of using similarities between presentation layer and data source layer to create symmetric components made of a core surrounded by interfaces, but with the drawback of hiding the inherent asymmetry between a service provider and a service consumer that would better be represented as layers.[4]

## Evolution
According to some authors, the hexagonal architecture is at the origin of the microservices architecture.[5]

## Variants
The onion architecture proposed by Jeffrey Palermo in 2008 is similar to the hexagonal architecture: it also externalizes the infrastructure with proper interfaces to ensure loose coupling between the application and the database.[6] It decomposes further the application core into several concentric rings using inversion of control.[7]

The clean architecture proposed by Robert C. Martin in 2012 combines the principles of the hexagonal architecture, the onion architecture and several other variants; It provides additional levels of detail of the component, which are presented as concentric rings. It isolates adapters and interfaces (user interface, databases, external systems, devices) in the outer rings of the architecture and leaves the inner rings for use cases and entities[8],.[9] The clean architecture uses the principle of dependency inversion with the strict rule that dependencies shall only exist between an outer ring to an inner ring and never the contrary.

## References
[Hexagonal Architecture: three principles and an implementation example](https://blog.octo.com/en/hexagonal-architecture-three-principles-and-an-implementation-example/)
