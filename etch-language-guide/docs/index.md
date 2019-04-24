<h1>Welcome to the <code>etch</code> language docs</h1>

<center>
<video controls loop width=100% autoplay style="padding:3px;border:3px;border-style:groove;border-color:#FFFFFF;">
 <source src="movies/hello.mp4" type="video/mp4">
Your browser does not support the video tag.
</video></br>
</center>

For news, tutorials, and the latest, visit <a href="https://community.fetch.ai/" target=_blank>https://community.fetch.ai</a>.

## What's `etch`?

`etch` is a high-level, statically-typed programming language designed for creating smart contracts on the Fetch.AI Constellation ledger. Unlike similar languages, `etch` allows developers to code advanced compute-intensive logic for high performance scenarios such as machine learning and AI.

The Fetch.AI ledger (known as Constellation) runs compiled `etch` bytecode that is extremely robust to ensure maximum hardware-optimised performance.

The `etch` language imposes rigorous compilation restrictions in order to avoid unwelcome and costly runtime errors. 

!!! note "Please note:"
    The `etch` language and the `etch` language guide are work in progress so some areas of the language remain incomplete for now. Please try out as much code as you like and send us your examples. Let us know if you have any problems.


## Getting started

### Prerequisites

Get the Fetch.AI ledger code from Git. 

Full initial installation and build instructions are <a href="https://community.fetch.ai/getting-started/building-fetchai-ledger-node/develop/" target="_blank">here</a>.

### Installation

`cd` into `build` folder.

Run `make -j vm-lang`.

### Setup

`cd` into `apps/vm-lang`.

Run `./vm-lang` with filename, flags, and arguments: 

`./vm-lang [options] <filename> -- [script args]`.

For example: 

`./vm-lang hello-world.etch -data test.json`. 

This runs the `hello-world.etch` file and produces a `json` file containing info on the data required by the contract.

## Etch playground

You can run all the examples in these docs in the <a href="http://etch-tour.economicagents.com/" target=_blank>`etch` playground here</a> as well as on the command line.


<!--## Editor plugins

Code editor highlighter plugins are currently available for the following IDEs:

* Sublime
* CLion
* ViM/Vi

You can find the details <a href="https://github.com/uvue-git/fetch-code-highlighter" target=_blank>here</a>.
-->

## Hello world!

Let’s run our first `etch` program.

Create a new file in the `vm-lang` directory and save it as `hello-world.etch`.

Add the following code:

``` c++
function main()
	printLn("Hello world!");
endfunction
```

Save the file.

Run `./vm-lang hello-world.etch`.

You should see the following output:

``` java
$ ./vm-lang hello-world.etch
 F E ╱     vm-lang v0.1.0-23-gd7622f98
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H     

Hello world!
```




## Debugging tips and tricks

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
* `Break` and `continue` statements outside `while` or `for` loops.
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
