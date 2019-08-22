<h1>Control flow</h1>

!!! Tip
	Make sure to declare the end of the function and construct.

## if-else

``` c++
function main()

	var x = 2;
	var y = 2;

	if (x == y)
		printLn("They are equal.");
	elseif (x > y)
		printLn("x is more than y.");
	else if (x > y)
		printLn("x is more than y.");
	else
		printLn("y is more than x.");
		endif
	endif

endfunction
```

You can also test the values contained within complex data types for equality.

``` c++
function main()

    var x = State<Int32>("account1");
    var y = State<Int32>("account2");

    x.set(5);
    y.set(8);

    if (x.get() > y.get())
        printLn("Object x is greater than object y.");
    else 
        printLn("Object x is less than or equal to object y.");
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


``` c++
function main()

    // ascending
    printLn("Ascending for loop.");
    for(i in 0:5)
        printLn(toString(i));
    endfor

    // stepwise ascent
    printLn("Ascending stepwise.");
    for(k in 0:10:2)
        printLn(toString(k));
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
