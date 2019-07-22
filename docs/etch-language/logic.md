<h1>Logical operators</h1>

## Equal to 

``` c++
function main()

	var x = 12;
	var y = 12;

	if (x == y)
	 	printLn("Equal.");
	endif

endfunction
```

## Not equal to 

``` c++
function main()

	var x = 12;
	var y = 11;

	if (x != y)
	 	printLn("Not equal.");
	endif

endfunction
```

## Less than

``` c++
function main()

	var x = 12;
	var y = 11;

	if (y < x)
	 	printLn("Less than.");
	endif

	if (y <= x)
		printLn("Less than or equal to.");
	endif

endfunction
```

## More than 

``` c++
function main()

	var x = 12;
	var y = 11;

	if (x > y)
	 	printLn("More than.");
	endif

	if (x >= y)
		printLn("More than or equal to.");
	endif

endfunction
```

## And 

``` c++
function main()

	var f : Bool = false;
	var t : Bool = true;

	if (f && t)
	 	printLn("True.");
	else
		printLn("False.");
	endif

endfunction
``` 



## Or

``` c++
function main()

	var f : Bool = false;
	var t : Bool = true;

	if (f || t)
	 	printLn("True.");
	else
		printLn("False.");
	endif

endfunction
```


## Xor

!!! note
	Coming soon: support for `xor`.




<br/>