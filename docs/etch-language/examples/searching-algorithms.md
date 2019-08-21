<h1>Creating a search algorithm</h1>

## Linear search

``` java
function main()
  
  var myArray = Array<Int32>(5);
  myArray[0] = 40;
  myArray[1] = 41;
  myArray[2] = 42;
  myArray[3] = 43;
  myArray[4] = 44;

  var search_for = 48;

  var found : Bool;
  found = linear_search(myArray, search_for);
  printLn(toString(search_for) + " is in the list? : " + toString(found));

endfunction


function linear_search(an_array :Array<Int32>, search_for :Int32) : Bool
  
    var found : Bool = false;

    for (i in 0:an_array.count()) 
      if (an_array[i] == search_for)
        found = true;
      endif
    endfor

    return found;

endfunction
```


## Binary search

``` java

function main()

  var myArray = Array<Int32>(5);
  myArray[0] = 40;
  myArray[1] = 41;
  myArray[2] = 42;
  myArray[3] = 43;
  myArray[4] = 44;

  var search_for = 40;

  var found : Bool;
  found = binary_search(myArray, search_for);
  printLn(toString(search_for) + " is in the list? : " + toString(found));

endfunction


function binary_search(an_array :Array<Int32>, search_for :Int32) : Bool

    var start = 0;
    var end = an_array.count(); 
    var found : Bool = false;

    while(start <= end && found == false) 

        var midpoint = (start + end) / 2;

        if (search_for == an_array[midpoint])
            found = true;

          elseif (search_for < an_array[midpoint])
            end = midpoint - 1;
          else
            start = midpoint + 1;

        endif

    endwhile

    return found;

endfunction

```


<br/>