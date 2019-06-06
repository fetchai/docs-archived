<h1>Getting started</h1>

### Prerequisites

Get the Fetch.AI ledger code from Git. 

Full initial installation and build instructions are <a href="https://community.fetch.ai/getting-started/building-fetchai-ledger-node/develop/" target="_blank">here</a>.

### Installation

`cd` into `build` folder.

Run `make -j 4 vm-lang`.

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

