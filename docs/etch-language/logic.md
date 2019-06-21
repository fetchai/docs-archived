<h1>Logical operators</h1>

## Equal to 

``` c++
function main()

	var x = 12;
	var y = 12;

	if (x == y)
	 	printLn("equal");
	endif

endfunction
```

## Not equal to 

``` c++
function main()

	var x = 12;
	var y = 11;

	if (x != y)
	 	printLn("not equal");
	endif

endfunction
```

## Less than

``` c++
function main()

	var x = 12;
	var y = 11;

	if (y < x)
	 	printLn("less than");
	endif

	if (y <= x)
		printLn("less than or equal to");
	endif

endfunction
```

## More than 

``` c++
function main()

	var x = 12;
	var y = 11;

	if (x > y)
	 	printLn("more than");
	endif

	if (x >= y)
		printLn("more than or equal to");
	endif

endfunction
```

## And 

``` c++
function main()

	var f : Bool = false;
	var t : Bool = true;

	if (f && t)
	 	printLn("true");
	else
		printLn("false");
	endif

endfunction
``` 



## Or

``` c++
function main()

	var f : Bool = false;
	var t : Bool = true;

	if (f || t)
	 	printLn("true");
	else
		printLn("false");
	endif

endfunction
```


## Xor

!!! note
	Coming soon: support for `xor`.


## Short circuiting

Currently, we don't short circuit. This may cause unexpected results.

``` c++
function foo() : Bool
  Print('1');
  return true;
endfunction

function bar() : Bool
  Print('2');
  return false;
endfunction

function main()
    if (foo() || bar())
       Print('3');
    endif
endfunction
```

<br/>