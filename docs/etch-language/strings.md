<h1>Strings</h1>

`etch` supports ASCII and UTF8 for string representation.




## Concatenation
 
Concatenate strings like this:

``` c++
function main()

    var myString : String = "hello";
    var myInferredString = "hello again";
    var myUtf8String = '人山人海';
    var x: String = null;

    printLn(myString);
    printLn(myInferredString);
    printLn(myInferredString + " " + myString);
    printLn(myUtf8String);
    // printLn(myString + x); // runtime error: line xx: null reference

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



## String functions

You can use the following utility functions for string manipulation:


### Find

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


### Length

The `length()` function returns the number of characters in a string.

* Returns -1 if the string is empty.

``` c++
function main()

	var myString : String = "Hello World";
	printLn(myString.length());
    
endfunction
```


### Reverse

The `reverse()` function reverses the order of characters in a string.

``` c++
function main()

	var myString : String = "xyz";
	myString.reverse();
	printLn(myString);

endfunction
```



### Substring

The `substr()` function extracts a substring from a string, based on specified starting and ending indices (but excluding the final character):

`string.substr(start, end)`

* The `start` character in the string occurs at index 0.
* The `end` character is excluded from the substring.
* Returns an empty string if `start` and `end` indices are equal.
* Returns the whole string if `start` equals 0 and `end` is equal to the length of the string.
* Fails if `start` is greater than `end`.
* Fails if `start` is negative.
* Fails if `end` is greater than the length of the string.

``` c++
function main()

	printLn("Hello World".substr(6, 11));

endfunction
```

### Trim

The `trim()` function removes any whitespace from the start and end of a string.

* Returns an empty string if the original string contains only whitespace.

``` c++
function main()

	var myString : String = "   Hello World  ";
	myString.trim();
	printLn(myString);

endfunction
```


### Split

The `split()` function takes an input string and a character(s) sequence separator to split on and returns an array of strings that does not include the separator. 

* Returns a one element array if there is no separator within it or if the input string is empty.
* Returns an empty string if more than one separator is encountered consecutively.
* Returns an empty string as the first element in the output array if the first element of the input is a separator.
* Returns an empty string as the last element in the output array if the last element of the input is a separator.

The following code takes a string and splits it on the separator ` --` returning an array of strings which it then outputs.

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



<br/>
