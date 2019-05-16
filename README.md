# PseudoParser

A parser taking PseudoCode as input and producing a python file as output.

The parser only supports the Syntax used in the "Algorithms and Data structures" lecture at the University of Trier.

## Usage

Place a file called "input_file.txt" in the same directory as pseudo_parser.py. 
It will create a file called "output_file.py".

## Supported Syntax

```
if xxx then
    ...         // if-condition
fi
else if         // else-if-condition
while xxx do    
    ...         // while-loop
od
<-              // assigning a value
A[1...n]        // Initializing a list
A <-> B         // swapping two lists
++              // incrementing a value by 1
--              // decrementing a value by 1
∧               // and
∨               // or
//              // comments
=               // equals
/               // division by whole number
Null            // Null
```

+ Indentation is important
+ If a value is an index for a list, it has to end with "_i" e.g. "x_i <- 1;"

## Todo

```
for             // for-loop
downto          // decrementing for loop
to              // incrementing for loop
A[y...x]        // sliced list
```
+ Add input/output path options via command line tool

## Not Supported

The following things have to be fixed by hand as the output can be different regarding the context
```
FUNCTION()      // either defining or calling a function recursively
A[1...x]        // either a new list with x size or a sliced list
```