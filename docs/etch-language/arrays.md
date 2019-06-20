<h1>Arrays</h1>


!!! warning
    Array ranges are wholly inclusive in `etch`.


## One dimensional arrays

Declare, access by index, and iterate over an array like this:

``` c++
function main()

    // var mySizelessArray = Array<String>(); // error: unable to find matching constructor for type/function 'Array<String>'
    // Failed to compile.

    var myArray = Array<Int32>(5);
    myArray[0] = 40;
    myArray[1] = 41;
    myArray[2] = 42;
    myArray[3] = 43;
    myArray[4] = 44;

    // print the array
    printLn(myArray);

    // print one element of the array
    printLn(toString(myArray[3]));

    // print ascending
    for (i in 0:4)
        printLn(toString(myArray[i]));
    endfor

    // print descending
    for (j in 4:0:-1)
        printLn(toString(myArray[j]));
    endfor

endfunction
```

## Two dimensional arrays

Declare a 4x4 2d array like this:

``` c++
function main()

    // build a 4x4 grid
    var grid = Array< Array<Int32> >(4);
    for (row in 0:3)
      grid[row] = Array<Int32>(4);
    endfor

    // initialise row and column values
    var count = 1;
    for(row in 0:3)
        for(column in 0:3)
            grid[row][column] = count;
            count += 1;
        endfor
        printLn(grid[row]);
    endfor
    
endfunction
```

## Utility functions

You can use the following utility functions to manipulate arrays:

* [append()](arrays.md#append)
* [extend()](arrays.md#extend)
* [count()](arrays.md#count)
* [popBack() and popFront()](arrays.md#pop)
* [reverse()](arrays.md#reverse)

<h3 id="append">Append</h3>

The `append()` function adds a new type safe item to the end of a one dimensional array.

``` c++
function main()

    var myArray = Array<UInt32>(2);
    myArray[0] = 1u32;
    myArray[1] = 2u32;
    myArray.append(42u32);
    // type safety
    // myArray.append("hello"); // error: unable to find matching function for 'append'
    printLn(myArray);

endfunction
```
Or an array to the end of a two dimensional array.

``` c++
function main()

    var my2dArray = Array<Array<Int32>>(3);
    var count = 1;
    for (i in 0:2)
        my2dArray[i] = Array<Int32>(3);
        for (j in 0:2)
            my2dArray[i][j] = count;
            count += 1;
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

<h3 id="extend">Extend</h3>

Use `extend()` to append the contents of one array to another. Array types must be the same.

``` c++
function main()
    
    var data1 = Array<Int32>(3);
    data1[0] = 1;
    data1[1] = 2;
    data1[2] = 3;
    printLn(data1);
    
    var data2 = Array<Int32>(2);
    data2[0] = 5;
    data2[1] = 4;
    data1.extend(data2);
    printLn(data1);

endfunction

```



<h3 id="count">Count</h3>

The `count()` function returns the number of items in a one dimensional array, or the number of arrays in a two dimensional array.

* Returns 0 if the array is empty.

``` c++
function main()

	var myArray = Array<Int32>(2);
    myArray[0] = 40;
    myArray[1] = 41;
    printLn(myArray.count());
	myArray.append(42);
	printLn(myArray.count());

endfunction
```

``` c++
function main()

	printLn(Array<Array<UInt32>>(10).count());

endfunction
```

<h3 id="pop">Pop back and pop front</h3>

The `popBack()` function removes and returns the last item from a one dimensional array, or the last array from a two dimensional array. 

The `popFront()` function removes and returns the first item or array.

* Fails if the array is empty.
  
``` c++
function main()

    var myArray = Array<Int32>(3);
    myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;

    printLn(myArray);
    
    var backItem = myArray.popBack();
    var frontItem = myArray.popFront();
    printLn((toString(backItem)) + " removed from the end of myArray");
    printLn((toString(frontItem)) + " removed from the start of myArray");
    printLn(myArray);

endfunction
```

``` c++
function main()

    //create a 3 by 3 array
    var my2dArray = Array<Array<Int32>>(3);
    var count = 1;
    for (i in 0:2)
        my2dArray[i] = Array<Int32>(3);
        for (j in 0:2)
            my2dArray[i][j] = count;
            count += 1;
        endfor
        printLn(my2dArray[i]);
    endfor

    printLn("Remove back and front arrays");
    var backArray = my2dArray.popBack();
    printLn(backArray);
    var frontArray = my2dArray.popFront();
    printLn(frontArray);
    
    printLn("Left with");
    for (row in 0:my2dArray.count()-1)
        printLn(my2dArray[row]);
    endfor

endfunction
```

Use `popBack(n)` to remove the last `n` items from a one dimensional array, or the last `n` arrays from a two dimensional array, and return them as an array(s). Use `popFront(n)` to remove and return the first `n` items or arrays. 

* `n` must be a positive, whole number.
* Returns an array.
* Fails if `n` is negative or `n` is greater than the number of items or arrays.
* Returns an empty array if `n` equals 0, leaving the original array unchanged.

``` c++
function main()
    
    var myArray = Array<Int32>(5);
    myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;
    myArray[3] = 40;
    myArray[4] = 50;

    printLn(myArray);

    var backItems = myArray.popBack(2);
    var frontItems = myArray.popFront(1);
    printLn("Items removed from end: ");
    printLn(backItems);
    printLn("Items removed from start: ");
    printLn(frontItems);
    printLn("Remaining array: ");
    printLn(myArray);

endfunction
```

``` c++
function main()
    
    var my2dArray = Array<Array<Int32>>(5);
    var count = 11;
    for (i in 0:4)
        my2dArray[i] = Array<Int32>(5);
        for (j in 0:4)
            my2dArray[i][j] = count;
            count += 1;
        endfor
        printLn(my2dArray[i]);
    endfor

    var backArray = my2dArray.popBack(2);
    var frontArray = my2dArray.popFront(2);
    printLn("Removed back arrays: ");
    for (k in 0:1)
        printLn(backArray[k]);
    endfor
    printLn("Removed front arrays: ");
    for (l in 0:1)
        printLn(frontArray[l]);
    endfor

    printLn("Remaining array(s): ");
    for (m in 0:0)
        printLn(my2dArray[m]);
    endfor
    
endfunction
```
<h3 id="reverse">Reverse</h3>
The reverse() function reverses the order of items in a one dimensional array, or the order of arrays in a two dimensional array.

``` c++
function main()

    var myArray = Array<Int32>(3);
    myArray[0] = 10;
    myArray[1] = 20;
    myArray[2] = 30;

    printLn(myArray);
    myArray.reverse();
    printLn(myArray);

endfunction
```

``` c++
function main()

    var my2dArray = Array<Array<Int32>>(5);
    var count = 101;
    for (i in 0:4)
        my2dArray[i] = Array<Int32>(5);
        for (j in 0:4)
            my2dArray[i][j] = count;
            count += 1;
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


<br/>
