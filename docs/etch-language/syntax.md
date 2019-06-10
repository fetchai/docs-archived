<h1>Syntax</h1>

The `etch` language was initially integrated with the Fetch.AI C++ ledger project. It is designed to run on a number of platforms. 

`etch` is inspired by Rust, C++, and Python, but it also has some idiosyncrasies. 

The `etch` language is extremely restrictive to avoid costly errors on the ledger. See [Smart Contract](smart-contract-intro.md) section for more information. 

`etch` is a statically typed language and static typing is enforced by the compiler. 

!!! note
	Blocks of code require no delimiters. White space is ignored. Indentation is recommended.

You can extend and customise `etch` in C++. We show you how to do that [here](extending-etch.md).

Let's take a closer look at `etch`.


## Declarations

Explicitly declare the type:

``` c++
function main()

	var myvariable : String;

endfunction
```

In some cases, type can be inferred:

``` c++
function main()

    var myvariable = "hello";

endfunction
```

Assign a value like this:

``` c++
function main()

	var myvariable : String = "hello";

endfunction
```


For multivariate types, all the types must be declared:

``` c++

    var multitype-variable-name : Type<Type<Type>>();

```

Not declaring the variable type and inferrable value results in a compilation error:

``` c++
function main()

    var myVariable;

endfunction 

Failed to compile.
line 3: error at ';', expected ':' or '='
Failed to compile.
```

[!comment]: (All variables in `etch` receive a default value at compile time.)

## Main

Initially, all our code snippets execute inside the `main` function:

``` java
function main()

	// stuff

endfunction
```

## Keywords

Here is a current list of `etch` keywords:


<table align="center" style="font-family: monospace;">
    <tr>
        <td align="center">var</td>
        <td align="center">if</td>
        <td align="center">endif</td>
        <td align="center">else</td>
    </tr>
    <tr>
        <td align="center">for</td>
        <td align="center">endfor</td>
        <td align="center">while</td>
        <td align="center">endwhile</td>
    </tr>
    <tr>
        <td align="center">function</td>
        <td align="center">endfunction</td>
        <td align="center">break</td>
        <td align="center">continue</td>
    </tr>
    <tr>
        <td align="center">return</td>
        <td align="center"></td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
</table>


## Comments

Both line and block comments are possible:  

``` c++
// a single comment inside a function

/* 
   ..lines of commented out stuff inside and outside functions
*/
```


## Annotations

`etch` code for smart contracts includes annotated functions. These are more like `Java` method annotations and not at all like `Python` decorators:

* `@init` is a constructor method that initialises the contract.

* `@action` is a function which defines transactions on the ledger that change state.

* `@query` is a function that allows you to query data residing on the ledger.



We tell you all about these functions in the section on [smart contracts](smart-contract-intro.md).

