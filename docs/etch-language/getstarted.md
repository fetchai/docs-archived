#Getting started

## Prerequisites

To build with Etch, you will need a running node. 

### Installation

At the root of your ledger installation directory `cd` into `build` folder.

Run `make etch`.

### Setup

At the root of your ledger installation directory `cd` into `apps/etch`.

Run `./etch` with filename, flags, and arguments: 

`./etch [options] <filename> -- [script args]`.

For example: 

`./etch hello-world.etch -data test.json`. 

This runs a `hello-world.etch` file and produces a `json` file containing info on the data required by the contract.


<!--## Editor plugins

Code editor highlighter plugins are currently available for the following IDEs:

* Sublime
* CLion
* ViM/Vi

You can find the details <a href="https://github.com/uvue-git/fetch-code-highlighter" target=_blank>here</a>.
-->


## Hello world with Etch

Let's use the `etch` simulator for the development process. Unlike Smart Contracts, Etch code needs a main() function as it's entry point. 

``` python
@testCase
function main()
  
    printLn("Hello, world");

endfunction
```

You can test this contract with the `etch` executable. Save this code snippet to `hello_world.etch` Run the following from your 
build directory:

``` bash
./apps/etch/etch hello_world.etch
```

This produces an output similar to:
```
 F E ╱     etch v0.4.1-rc3
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H

Hello, world!
```

`main` is the default runner function in `etch`. When submitting the smart contract to the ledger, we do not need the `main` function as it is inaccessible to the ledger code.



<br/>


### Compile and run two or more `etch` files

It is possible to compile and run two or more `etch` files in one go. 

The files are not order dependent and the single `main()` function can be in any of the files.

For example, run `./etch file-1.etch file-2.etch file-n.etch`.



<br/>



## Etch playground

You can run all the examples in these docs in the <a href="http://build.fetch.ai" target=_blank>`etch` playground here</a> as well as on the command line.

