<h1>Debugging tips and tricks</h1>

Use `printLn(toString(...))` to query variables on the command line and in the `etch` playground. 

!!! note
    In a live environment, the `etch` compiler will strip out `printLn()` statements.

<H3>Compiling</H3>

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
* Mismatches between type and instance functions - *awaiting clarification*.
* Member access support issues with dot operator - *awaiting clarification*.
* `while`, `for`, `if`, `var`, `return`, `break`, `continue`, variables, and expressions declared at topmost scope.


<H3>System arguments</H3> 

`System.Argc()` and `System.Argv()` give us access to compiler argument count and values. In the following code, first we print the number of compiler arguments, then we list them.

``` c++
function main()
  var message : String;
  
  printLn("System args: " + toString(System.Argc()));

  // print the argument values
  for(i in 0:System.Argc() - 1)
    message = toString(i) + " = " + System.Argv(i);
    printLn(message); 
  endfor
endfunction
```

Running the code from the command line with zero flags `--` sends arguments to the `vm-lang` executable. 

For example, run the code snippet above with zero flags `--` and an example argument `hello` like this:

`./vm-lang sysargs-examples.etch -- hello`

You should see the following output:

``` c++
 F E ╱     vm-lang v0.1.0-30-g557389e0
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H     

System args: 2
0 = ./vm-lang
1 = hello
```

`etch` features like this are useful for playing around with and for debugging in a dev environment. They should not be included in smart contract code. 

For smart contracts, there are more flags, such as `-data`, which do specific things. We explain coding, compiling, contract flags, and all about `etch` smart contracts [here](smart-contracts.md).