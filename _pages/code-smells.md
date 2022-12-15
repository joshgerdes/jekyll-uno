# Code smells

## Class-level smells

Large class: a class that contains too many types or contains many unrelated methods

Feature envy: a class that uses methods of another class excessively.

Inappropriate intimacy: a class that has dependencies on implementation details of another class

Refused bequest: a class that overrides a method of a base class in such a way that the contract of the base class is not honored by the derived class

Lazy class/freeloader: a class that does too little.

Excessive use of literals: these should be coded as named constants, to improve readability and to avoid programming errors. Additionally, literals can and should be externalized into resource files/scripts, or other data stores such as databases where possible, to facilitate localization of software if it is intended to be deployed in different regions.[8]

Cyclomatic complexity: too many branches or loops; this may indicate a function needs to be broken up into smaller functions, or that it has potential for simplification/refactoring.

Downcasting: a type cast which breaks the abstraction model; the abstraction may have to be refactored or eliminated.[9]

Orphan variable or constant class: a class that typically has a collection of constants which belong elsewhere where those constants should be owned by one of the other member classes.

Data clump: Occurs when a group of variables are passed around together in various parts of the program. In general, this suggests that it would be more appropriate to formally group the different variables together into a single object, and pass around only the new object instead.[10][11]

... in review ...

## library selection bias instead of input for implementation

import in main class library instead of giving required inputs/config

