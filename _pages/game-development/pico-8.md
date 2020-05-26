---
---


## PICO-8 Cheatsheet

### Commandline
HELP
SAVE GAME.P8
LOAD GAME.P8
RUN
SPLORE

### Variables & Types

A=nil
X=23
local S="TEXT"
T={name="Joe", age="32"}

### Operators

```lua
+ - * / ^ %
< > <= >= ~= ==
#list  "A".."B"
and or not
Functions
FUNCTION ADD(a,b)
 RETURN A+B
END
If-Statement
IF (X  < 33) THEN
 PRINT("HALLO")
else
 print("hey")
END
```

### Loops

```lua
--UP
FOR I = 1,10 DO
 PRINT(I)
END

--DOWN
FOR A=10,0,-2 DO
 PRINT(A)
END

--ARRAY
FOR S IN ALL(SHIPS) DO
 PRINT(S.NAME)
END

--Table
FOR K,V IN PAIRS(M) DO
 PRINT("K:"..K..",V:"..V)
END
```

### Tables

```lua
t={a="x",b=1}
add(t, v)
del(t, v)
t={1,2,3,4}
print(t[1]) --1-based!! 
```
