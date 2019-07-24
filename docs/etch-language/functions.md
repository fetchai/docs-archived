<h1>Functions</h1>

## Writing a function

Coding a function in `etch` is straightforward. 

All `etch` programs run in the simulator are triggered by a `main()` function. This is for development purposes only. Smart contracts do not require a `main()` function.

In the example below, a function `myFunction()` is called from `main()`.

``` c++
function main()

  myFunction();

endfunction

// declare the function called from main()
function myFunction()

  printLn("hello");

endfunction
```




## Parameter and return types

The iterative `fibonacci` function below takes a parameter `n: Int32` which is a 32 bit integer type named `n`. 

The function returns an `Int32` and declares this after the function name and parameter list as `: Int32`.

``` c++
function fibonacci(n: Int32) : Int32

    var a = 0;
    var b = 1;
    var temp = 0;

    for(i in 0:n)
      temp = a;
        a = b;
        b = temp + b;
        printLn(toString(a));
    endfor

    return a;

endfunction

// call fibonacci from main()
function main()

  fibonacci(10);

endfunction

```




## Recursion

Below is an example of the fibonacci function implemented with recursion.

!!! warning
    Take care with recursion in smart contract code.


``` c++
function fibonacci(n: Int32) : Int32

    if(n == 1 || n == 0)
      return 1;
    else
      return (fibonacci(n-1) + fibonacci(n-2));
    endif

endfunction


function main()

   var nterms = 10;

   for (i in 0:nterms)
      printLn(toString(fibonacci(i)));
   endfor

endfunction
```


## Pass by reference

All variables in `etch` are passed by reference. 

Attempting to reassign the value of a primitive variable passed to another function will cause a compilation error.


``` c++
function main() 

  var original_value = 10;
  printLn(original_value);

  change_value(original_value);
  printLn(original_value);

endfunction

function change_value(value :Int32)
    
    // value = 20; // error: assignment operand is not writeable. Failed to compile.

endfunction

```

The same is true of complex types.

``` c++
function main() 

    var myArray = Array<Int32>(5);
    change_value(myArray);

endfunction

function change_value(value :Array<Int32>)

    // value = Array<Int32>(3); // error: assignment operand is not writeable. Failed to compile.

endfunction

```

However, this is not the case with athe internal state of object types such as `Array`.


``` c++
function main() 

    var myArray = Array<Int32>(5);
    myArray[0] = 40;
    myArray[1] = 41;
    myArray[2] = 42;
    myArray[3] = 43;
    myArray[4] = 44;

    printLn(myArray);
    change_value(myArray);
    printLn(myArray);

endfunction

function change_value(myArray :Array<Int32>)

    myArray[2] = 100;

endfunction
```

Reassigning a primitive type to a new variable does not affect the original.

``` c++
function main() 

  var x = 10;
  printLn(x);

  change_value(x);
  printLn(x);

endfunction

function change_value(value :Int32)
    
    var y = 20;
    y = value;
    printLn(y);
    y = 20;

endfunction

```
However, reassigning an object and changing any of its internal values does affect the original.

``` c++
function main() 

  var myArray = Array<String>(2);
  myArray[0] = "hello";
  printLn(myArray[0]);

  change_value(myArray);
  printLn(myArray[0]);

endfunction

function change_value(myArray :Array<String>)
    
    myArray[0] = "goodbye";

endfunction
```



## Utility functions



### Print 

`printLn()` is available for printing variables to the console with a line break.

`print()` is available without a line break.

!!! note
    `etch` strips out all `printLn()` statements in a release environment. This means that logs and other miscellaneous debug code never finds its way onto ledger shards. 


### Sysargs

The following `System` functions `Argc()` and `Argv()` return the number of arguments to `etch` and their value. These functions are only useful on the `etch` simulator outside of smart contract development.

* `System.Argc()`
* `System.Argv()`



### Type casting

* `toInt8()`
* `toInt16()`
* `toInt64()`
* `toUInt8()`
* `toUInt16()`
* `toUInt32()`
* `toUInt64()`
<!-- `toUInt256()` -->
* `toFloat32()`
* `toFloat64()`
* `toFixed32()`
* `toFixed64()`
* `toString()`

For example:

``` c++
function main()

    var x = 10;
    printLn(x);
    var y = toInt8(x);
    printLn(y);
    var z = toInt16(x);
    printLn(z);
    var a = toInt32(x);
    printLn(a);
    var b = toInt64(x);
    printLn(b);
    var c = toUInt8(x);
    printLn(c);
    var d = toUInt16(x);
    printLn(d);
    var e = toUInt32(x);
    printLn(e);
    var f = toUInt64(x);
    printLn(f);
    var g = toFloat32(x);
    printLn(g);
    var h = toFloat64(x);
    printLn(h);
    var i = toFixed32(x); 
    printLn(i);
    var j = toFixed64(x); 
    printLn(j);

endfunction
```

## Annotations

`etch` smart contract code includes annotated functions:

* `@init` is a constructor method that initialises the contract.

* `@action` is a function which defines transactions on the ledger that change state.

* `@query` is a function that allows you to query data residing on the ledger.

There are more annotations for synergetic contracts.


## Getters and setters

Getters and setters are available for `State` and `ShardedState` types.

[comment]: <> (Any other types have get and set?)

* `set()`
* `get()`


<br/>
