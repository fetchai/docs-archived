<h1>Logical operators</h1>

## Equal to

``` java
function main()

	var x = 12;
	var y = 12;

	if (x == y)
	 	printLn("equal");
	endif

endfunction
```

## Not equal to

``` java
function main()

	var x = 12;
	var y = 11;

	if (x != y)
	 	printLn("not equal");
	endif

endfunction
```

## Less than

``` java
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

``` java
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

``` java
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

``` java
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