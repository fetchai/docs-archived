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

## Utility functions

You can use the following utility functions to manipulate arrays:

* [append()](arrays.md#append)
* [count()](arrays.md#count)
* [popBack() and popFront()](arrays.md#pop)
* [reverse()](arrays.md#reverse)

<h3 id="append">Append</h3>

The `append()` function adds one new item to the end of a one dimensional array, or an array to the end of a two dimensional array.

* Statically type safe.

``` java
function main()

	var myArray = Array<UInt32>(2);
    myArray[0] = 1u32;
    myArray[1] = 2u32;
	myArray.append(42u32);
	printLn(myArray);

endfunction
```

``` java
function main()

	var my2dArray = Array<Array<Int32>>(3);
	for (i in 0:2)
    	my2dArray[i] = Array<Int32>(3);
        for (j in 0:2)
        	my2dArray[i][j] = toInt32(i) * toInt32(j);
        endfor
        printLn(my2dArray[i]);
    endfor

    printLn(" ");

 	my2dArray.append(Array<Int32>(8));
	my2dArray[1].append(42);
 
 	for (k in 0:3)
    	printLn(my2dArray[k]);
    endfor

endfunction
```

<h3 id="count">Count</h3>

The `count()` function returns the number of items in a one dimensional array, or the number of arrays in a two dimensional array.

* Returns 0 if the array is empty.

``` java
function main()

	var myArray = Array<Int32>(2);
    myArray[0] = 40;
    myArray[1] = 41;
    printLn(myArray.count());
	myArray.append(42);
	printLn(myArray.count());

endfunction
```

``` java
function main()

	printLn(Array<Array<UInt32>>(10).count());

endfunction
```

<h3 id="pop">Popback and popfront</h3>

The `pop_back()` function removes and returns the last item from a one dimensional array, or the last array from a two dimensional array. The `pop_front` function removes and returns the first item or array.

* Fails if the array is empty.
  
``` java
function main()

	var myArray = Array<Int32>(3);
	myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;

    var backItem = myArray.popBack();
	var frontItem = myArray.popFront();
    printLn((toString(backItem)) + " removed from the end of myArray");
	printLn((toString(frontItem)) + " removed from the start of myArray");
    printLn(myArray);

endfunction
```

``` java
function main()

	//create a 3 by 3 array
	var my2dArray = Array<Array<Int32>>(3);
	for (i in 0:2)
		my2dArray[i] = Array<Int32>(3);
		for (j in 0:2)
        	my2dArray[i][j] = toInt32(i) * toInt32(j);
        endfor
    	printLn(my2dArray[i]);
    endfor
    
    var backArray = my2dArray.pop_back();
	var frontArray = my2dArray.pop_front();
    printLn("Removed back and front arrays: ");
    printLn(backArray);
	printLn(frontArray);

endfunction
```

Use `pop_back(n)` to remove the last `n` items from a one dimensional array, or the last `n` arrays from a two dimensional array, and return them as an array. Use `pop-front(n)` to remove and return the first `n` items or arrays. 

* n must be a positive, whole number.
* Returns an array.
* Fails if n is negative or n is greater than the number of items or arrays.
* Returns an empty array if n equals 0, leaving the original array unchanged.

``` java
function main()
	
	var myArray = Array<Int32>(5);
	myArray[0] = 10;
	myArray[1] = 20;
	myArray[2] = 30;
	myArray[3] = 40;
	myArray[4] = 50;

    var backItems = myArray.pop_back(2);
	var frontItems = myArray.pop_front(1);
	printLn("Items removed from end: ");
    printLn(backItems);
	printLn("Items removed from start: ");
    printLn(frontItems);

endfunction
```

``` java
function main()
	
    var my2dArray = Array<Array<Int32>>(10);
    for (i in 0:9)
        my2dArray[i] = Array<Int32>(5);
        for (j in 0:4)
            my2dArray[i][j] = toInt32(i) * toInt32(j);
        endfor
        printLn(my2dArray[i]);
    endfor

    var backArray = my2dArray.pop_back(3);
    var frontArray = my2dArray.pop_front(5);
    printLn("Removed back arrays: ");
    for (k in 0:2)
    	printLn(backArray[k]);
    endfor
    printLn("Removed front arrays: ");
    for (l in 0:4)
    	printLn(frontArray[l]);
    endfor
    
endfunction
```
<h3 id="reverse">Reverse</h3>
The reverse() function reverses the order of items in a one dimensional array, or the order of arrays in a two dimensional array.

``` java
function main()
	
	var myArray = Array<Int32>(3);
	myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;
	
	myArray.reverse();
    printLn(myArray);

endfunction
```

``` java
function main()

    var my2dArray = Array<Array<Int32>>(5);
    for (i in 0:4)
        my2dArray[i] = Array<Int32>(5);
        for (j in 0:4)
            my2dArray[i][j] = toInt32(i) * toInt32(j);
        endfor
        printLn(my2dArray[i]);
    endfor
    
    my2dArray.reverse();
    
    printLn("Reversed: ");
    for (k in 0:4)
    printLn(my2dArray[k]);
    endfor

endfunction
```

[comment]: <> (<a href="https://github.com/uvue-git/fetch-ledger/issues/812" target=_blank>https://github.com/uvue-git/fetch-ledger/issues/812</a>)
