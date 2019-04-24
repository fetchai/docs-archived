<h1>Functions</h1>

## Writing a function

Coding a function in `etch` is straightforward. 

All `etch` programs run from a `main()` function.

In the example below, we declare a function `myFunction()` and call it from `main()`.

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

The function will return an `Int32` and declares this with `: Int32`.

``` java
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


``` java
function fibonacci(n: Int32) : Int32
  	
  	if(n <= 1)
    	return n;
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


``` java
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

However, this is not the case with object types such as `State`.

``` java
function main() 

	var myState = State<Int32>("balance", 10);
	printLn(myState.get());

	change_value(myState);
	printLn(myState.get());

endfunction


function change_value(state :State<Int32>)
  	
  	state.set(30);

endfunction

```

And `Array`.

``` java
function main() 

	var myArray = Array<Int32>(5);
    myArray[0] = 40;
    myArray[1] = 41;
    myArray[2] = 42;
    myArray[3] = 43;
    myArray[4] = 44;

    printLn(toString(myArray[2]));
	change_value(myArray);
	printLn(toString(myArray[2]));

endfunction


function change_value(myArray :Array<Int32>)
  	
  	myArray[2] = 100;
  	
endfunction
```

Reassigning a primitive type to a new variable does not affect the original.

``` java
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
However, reassigning an object and changing any of its values does affect the original.

``` java
function main() 

	var myArray = Array<String>(2);
	myArray[0] = "hello";
	printLn(myArray[0]);

	change_value(myArray);
	printLn(myArray[0]);

endfunction


function change_value(myArray :Array<String>)
  	
  	var newArray = Array<String>(2);

  	newArray = myArray;
  	newArray[0] = "goodbye";

endfunction
```



## Utility functions

<H3>Random</H3>

You can currently generate non-deterministic, random, signed and unsigned integers and floats.

There is one restriction: the beginning value of the range *must* be less than the end value.

``` java
function main()

    // var randUInt8 = Rand(0u8, 1000u8); // error: unable to find matching function for 'Rand'
    // printLn(toString(randUInt8));

    // unpermitted range
    // var rand_test = Rand(100u16, 0u16); // runtime error: Invalid argument: Rand(a, b) must satisfy a < b

    var randUInt16 = Rand(0u16, 1000u16);
    // printLn(toString(randUInt16));

    var randUInt32 = Rand(0u32, 1000u32);
    printLn(toString(randUInt32));

    var randUInt64 = Rand(0u64, 1000u64);
    printLn(toString(randUInt64));

    // var randInt8 = Rand(0u8, 1000u8);
    // printLn(toString(randInt8));

    var randInt16 = Rand(0i16, 1000i16);
    // printLn(toString(randInt16));

    var randInt32 = Rand(0i32, 1000i32);
    printLn(toString(randInt32));

    var randInt64 = Rand(0i64, 1000i64);
    printLn(toString(randInt64));

    var randFloat32 = Rand(0.0f, 1000.0f);
    printLn(toString(randFloat32));

    var randFloat64 = Rand(0.0, 1000.0);
    printLn(toString(randFloat64));

endfunction
```

<H3>Print</H3> 

`printLn()` is available for printing variables to the console.

`print()` is available without a line break.

If the variable is a string, you don't have to cast it before printing, otherwise you should cast it with `toString()`.

!!! note
	`etch` strips out all `printLn()` statements in a release environment. This means that logs and other miscellaneous debug code never finds its way onto ledger shards. 


<H3>Sysargs</H3>

The following `System` functions `Argc()` and `Argv()` return the number of arguments to `vm-lang` and their value.

* `System.Argc()`
* `System.Argv()`

!!! note 
	Coming soon: common utility maths functions such as `pow()`, `exp()`, `Abs()`, `Sine()`, `Cosine()`, etc.



## Type casting functions

* `toInt8()`
* `toInt16()`
* `toInt64()`
* `toByte()`
* `toUInt16()`
* `toUInt32()`
* `toUInt64()`
* `toFloat32()`
* `toFloat64()`
* `toString()`

For example:

``` c++
function main()

	var x = 10;
	var y = toByte(x);
	var z = toInt8(x);
	var a = toInt16(x);
	var b = toInt32(x);
	var c = toInt64(x);
	var d = toUInt16(x);
	var e = toUInt32(x);
	var f = toUInt64(x);
	var g = toFloat32(x);
	var h = toFloat64(x);
	// var i = toFixed32(x); // error: unknown symbol 'toFixed32'
	// var j = toFixed64(x); // error: unknown symbol 'toFixed64'

endfunction
```

## Annotations

`etch` smart contract code includes annotated functions:

* `@init` is a constructor method that initialises the contract.

* `@action` is a function which defines transactions on the ledger that change state.

* `@query` is a function that allows you to query data residing on the ledger.


## Getters and setters

Getters and setters are available for `State` types.

[comment]: <> (Any other types have get and set?)

* `set()`
* `get()`



