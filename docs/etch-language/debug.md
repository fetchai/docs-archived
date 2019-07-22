<h1>Debugging tips and tricks</h1>

Use `printLn(toString(...))` to query variables on the command line and in the `etch` playground. 

!!! note
    In a live environment, the `etch` compiler will strip out `printLn()` statements.

## Compiling

[!comment]: <> (Todo: fill out with examples as we go along.)

Our compiler is very strict. It will complain about:

* Unknown and unsupported symbols, operators, and indexes.
* Lack of types for variables and parameters.
* Assigning `null` to primitive types.
* Incorrect, incompatible, and uninferrable types in statements and functions.
* Duplicate variables, parameters, and functions.
* Incomparable types in boolean tests.
* Unmatched and unexpected beginnings, middles, and endings in selections, iterations, statements, and blocks.
* Incorrectly formed statements.
* Incorrect amount, or lack of, operands in boolean tests.
* `break` and `continue` statements outside `while` or `for` loops.
* Non-functions, unmatched functions, and functions that do not return a value.
* Local function definitions.
* Returning `null` or no value from functions.
* Attempts to construct primitives and unmatched constructors.
* Mismatches between type and instance functions.
* Member access support issues with dot operator.
* `while`, `for`, `if`, `var`, `return`, `break`, `continue`, variables, and expressions declared at topmost scope.


## System arguments

`System.Argc()` and `System.Argv()` give access to compiler argument count and values. The following code prints the number of compiler arguments, then lists their values.

``` c++
function main()

  var message : String;

  printLn("System args: " + toString(System.Argc()));

  // print the argument values
  for(i in 0:System.Argc())
    message = toString(i) + " = " + System.Argv(i);
    printLn(message); 
  endfor
  
endfunction
```

Running the code from the command line with zero flags `--` sends arguments to the `etch` executable.  

For example, run the code snippet above with zero flags `--` and an example argument `hello` like this:

`./etch sysargs-examples.etch -- hello`

You should see the following output:

``` c++
 F E ╱     etch v0.1.0-30-g557389e0
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H     

System args: 2
0 = ./etch
1 = hello
```

`etch` features like this are useful for experimentation and debugging in a development environment. For example, the system arguments can load machine learning training data into a script. 

For smart contracts, there are flags, such as `-data`, which do specific things. We explain coding, compiling, contract flags, and all about `etch` smart contracts <a href="../.././smart-contracts/smart-contract-intro/" target=_blank> here</a>.

<br/>