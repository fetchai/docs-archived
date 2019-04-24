<h1>Arrays</h1>

## One dimensional arrays

Declare and iterate over an array like this:

``` java
function main()

	// var mySizelessArray = Array<String>(); // error: unable to find matching constructor for type/function 'Array<String>'
	// Failed to compile.

	var myArray = Array<Int32>(5);
	myArray[0] = 40;
	myArray[1] = 41;
	myArray[2] = 42;
	myArray[3] = 43;
	myArray[4] = 44;

	printLn(toString(myArray[3]));

	// ascending
	for (i in 0:4)
		printLn(toString(myArray[i]));
	endfor

	// descending
	for (j in 4:0:-1)
		printLn(toString(myArray[j]));
	endfor

endfunction
```

## Two dimensional arrays

``` java
function main()

    var x = Array< Array<Int32>>(1);
    x[0] = Array<Int32>(1);
    x[0][0] = 13;

    // printLn(toString(x[0])); // error: unable to find matching function for 'toString'
    printLn(toString(x[0][0])); 

endfunction
```


## Array functions

!!! note 
	Coming soon.

[comment]: <> (<a href="https://github.com/uvue-git/fetch-ledger/issues/812" target=_blank>https://github.com/uvue-git/fetch-ledger/issues/812</a>)