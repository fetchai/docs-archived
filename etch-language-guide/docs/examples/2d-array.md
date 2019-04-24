<h1>Creating a 2D array</h1>

``` java

// create a 2dArray
function create_2dArray(i: Int32, j: Int32) : Array< Array<Int32> >
    
    var x = Array< Array<Int32> >(i);

     for (k in 0:i-1)
       x[k] = Array<Int32>(j);
     endfor
    
     return x;

endfunction

// call and build the create_2dArray function from main
function main()

    var x : Array< Array<Int32> > = create_2dArray(10, 15);

    for (i in 0:9)
      for (j in 0:14)
        x[i][j] = toInt32(i) * toInt32(j);
      endfor
    endfor
    
    for (i in 0:9)
      for (j in 0:14)
        printLn(toString(x[i][j]));
      endfor
    endfor

endfunction

```