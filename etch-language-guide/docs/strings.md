# Strings

`etch` supports ASCII and UTF-8 for string representation.

!!! note
	Coming soon: length attribute, string indexing, and common string functions.



## Concatenation
 
Concatenate strings like this:

``` c++
function main()

	var myString : String = "hello";
	var myInferredString = "hello again";
	var myChineseUTFString : String = "提供"; // prints on console, not in playground
	var x: String = null;

	printLn(myString);
	printLn(myInferredString);
	printLn(myInferredString + " " + myString);
	printLn(myChineseUTFString);
	// printLn(toString(x)); // error: unable to find matching function for 'toString'

    // myString2[0]; // error: operand does not support index operator

endfunction
```



## Equality

You can test strings for equality.

``` c++
function main()

	var myString1 : String = "hello";
	var myString2 : String = "again";

	if (myString1 == myString2)
		printLn("They are equal.");
	else
		printLn("They are not equal.");
	endif

endfunction
```

And inequality.

``` c++
function main()

	var myString1 : String = "hello";
	var myString2 : String = "again";

	if (myString1 != myString2)
		printLn("They are not equal.");
	else
		printLn("They are equal.");
	endif

endfunction
```


You can do a `less than` comparison on equal and unequal length strings.

``` c++
function main()

	// with regards to character
	var myString1 : String = "a";
	var myString2 : String = "b";

	// with regards to length of string
	// var myString1 : String = "aa";
	// var myString2 : String = "a";

	if (myString1 < myString2)
		printLn("myString1 is less than myString2.");
	else
		printLn("myString1 is not less than myString2.");
	endif

endfunction
```


And a `less than or equal to` comparison on equal and unequal length strings.

``` c++
function main()

	// with regards to character
	var myString1 : String = "a";
	var myString2 : String = "b";

	// with regards to length of string
	// var myString1 : String = "aa";
	// var myString2 : String = "a";

	if (myString1 <= myString2)
        printLn("myString1 is less than or equal to myString2.");
	else
        printLn("myString1 is not less or equal to than myString2.");
	endif

endfunction
```

You can calculate `greater than` between two equal or unequal length strings.

``` c++
function main()

	// with regards to character
	var myString1 : String = "a";
	var myString2 : String = "b";

	// with regards to length of string
	// var myString1 : String = "aa";
	// var myString2 : String = "a";

	if (myString1 >= myString2)
        printLn("myString1 is greater than or equal to myString2.");
	else
        printLn("myString1 is not greater than or equal to myString2.");
	endif

endfunction
```


And `greater than or equal to` also.

``` c++
function main()

	var myString1 : String = "a";
	var myString2 : String = "a";

	if (myString1 >= myString2)
		printLn("myString1 is greater than or equal to myString2.");
	else
		printLn("myString1 is not greater than or equal to myString2.");
	endif

endfunction
```


## Indexing

!!! note 
	Coming soon.



## Common functions

!!! note 
	Coming soon.




## Formatting

!!! note 
	Coming soon.


