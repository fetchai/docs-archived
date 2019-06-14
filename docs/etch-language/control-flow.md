<h1>Control flow</h1>

!!! warning
	Make sure to declare the end of the function and construct.

## if-else

``` c++
function main()

	var x = 2;
	var y = 2;

	if (x == y)
		printLn("they are equal");
	elseif (x > y)
		printLn("x is more than y");
	else if (x > y)
		printLn("x is more than y");
	else
		printLn("y is more than x");
		endif
	endif

endfunction
```

You can also test more complex data types for equality.

``` c++
function main()

	var x = State<Int32>("var", 3);
	var y = State<Int32>("var", 5);

	if (x.get() > y.get())
		printLn("object x is greater than object y");
	else 
		printLn("object x is less than or equal to object y");
	endif

endfunction

```



## while

``` c++
function main()
	
	var i = 0;

	while(i < 10)
	    printLn(toString(i));
	    i += 1;
	endwhile

endfunction
```


## for

!!! warning
	`for` loop range is inclusive.

``` c++
function main()
	
	// ascending
	printLn("Ascending and inclusive for loop");
	for(i in 0:5)
	    printLn(toString(i));
	endfor

	// descending
	printLn("Descending and inclusive for loop");
	for(j in 5:0:-1)
	    printLn(toString(j));
	endfor

	// stepwise ascent
	printLn("Ascending stepwise");
	for(k in 0:10:2)
		printLn(toString(k));
	endfor

	// stepwise descent
	printLn("Descending stepwise");
	for(l in 10:0:-2)
		printLn(toString(l));
	endfor

endfunction
```



## break


``` c++
function main()

	for(i in 0:10)
	    printLn(toString(i));
	    if (i == 5) 
	    	break;
	    endif
	endfor

endfunction
```




## continue

``` c++
function main()
	
	var i = 0;

	while(i < 10)
		i += 1;
	    if (i == 5)
	    	continue;
	    endif
	    printLn(toString(i));
	endwhile

endfunction
```

<br/>
