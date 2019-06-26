<h1>Strings</h1>

`etch` supports ASCII for string representation.




## Concatenation
 
Concatenate strings like this:

``` c++
function main()

    var myString : String = "hello";
    var myInferredString = "hello again";
    var x: String = null;

    printLn(myString);
    printLn(myInferredString);
    printLn(myInferredString + " " + myString);
    // printLn(toString(x)); // error: unable to find matching function for 'toString'

    // var y = myString[0]; // error: unable to find matching index operator for type 'String'

endfunction
```



## Equality

You can test strings for equality.

``` c++
function main()

	var myString1 : String = "hello";
	var myString2 : String = "hello";

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

	if (myString1 > myString2)
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



## Utility functions

You can use the following utility functions for string manipulation:

* [find()](strings.md#find)
* [length()](strings.md#length)
* [reverse()](strings.md#reverse)
* [substr()](strings.md#substr)
* [trim()](strings.md#trim)
* [split()](strings.md#split)

<h3 id="find">Find</h3>

The `find()` function searches a string for the first occurrence of a specified substring. 

* The search is case sensitive.
* The first character in the string occurs at index 0.
* Returns the index of the first occurrence of the substring.
* Returns -1 if the substring is not found.
* Returns -1 if either the string or the substring are empty.

``` c++
function main()

	var myString : String = "Hello World";
	printLn(myString.find("o"));

endfunction
```

<h3 id="length">Length</h3>

The `length()` function returns the number of characters in a string.

* Returns -1 if the string is empty.

``` c++
function main()

	var myString : String = "Hello World";
	printLn(myString.length());
    
endfunction
```

<h3 id="reverse">Reverse</h3>

The `reverse()` function reverses the order of characters in a string.

``` c++
function main()

	var myString : String = "xyz";
	myString.reverse();
	printLn(myString);

endfunction
```

<h3 id="substr">Substr</h3>

The `substr()` function extracts a substring from a string, based on specified starting and ending indexes (but excluding the final character):

`string.substr(start, end)`

* The `start` character in the string occurs at index 0.
* The `end` character is excluded from the substring.
* Returns an empty string if `start` and `end` indexes are equal.
* Returns the whole string if `start` equals 0 and `end` is equal to the length of the string.
* Fails if `start` is greater than `end`.
* Fails if `start` is negative.
* Fails if `end` is greater than the length of the string.

``` c++
function main()

	printLn("Hello World".substr(6, 11));

endfunction
```

<h3 id="trim">Trim</h3>

The `trim()` function removes any whitespace from the start and end of a string.

* Returns an empty string if the original string contains only whitespace.

``` c++
function main()

	var myString : String = "   Hello World  ";
	myString.trim();
	printLn(myString);

endfunction
```


<h3 id="substr">Split</h3>

The `split()` function takes an input string and a character(s) sequence to split on and returns an array of strings that does not include the split character(s). 

* Returns a one element array if there is no tokenizer within it or if the input string is empty.
* Returns an empty string if more than one tokenizer is encountered consecutively.
* Returns an empty string as the first element in the output array if the first element of the input is a tokenizer.
* Returns an empty string as the last element in the output array if the last element of the input is a tokenizer.

The following code takes a string and splits it on the tokenizer ` --` returning an array of strings which it then outputs.

``` c++
function main()

	var text = 'xxx --yyy --zzz';
	printLn(text);
    var output = text.split(' --');
    printLn(output[0]);
    printLn(output[1]);
    printLn(output[2]);

endfunction
```

[!comment]: <> (More examples when there is more time.)

<br/>
