## Bubble sort

``` java
function main()
  
  var myArray = Array<Int32>(5);
  myArray[0] = 41;
  myArray[1] = 40;
  myArray[2] = 43;
  myArray[3] = 44;
  myArray[4] = 42;

  
  print("Unsorted:");
  for (i in 0:myArray.count()-1)
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

  bubble_sort(myArray);

  print("Sorted:");
  for (i in 0:myArray.count()-1)
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

endfunction


function bubble_sort(an_array :Array<Int32>)

    var more_swaps : Bool = true;
  
    while(more_swaps == true)

      more_swaps = false;

      for (i in 0:an_array.count()-2) 
          
          if (an_array[i] > an_array[i + 1])

              more_swaps = true;

              var temp = an_array[i];
              an_array[i] = an_array[i + 1];
              an_array[i + 1] = temp;

          endif
      endfor

    endwhile

endfunction

```


## Insertion sort

``` java
function main()

  var myArray = Array<Int32>(5);
  myArray[0] = 41;
  myArray[1] = 40;
  myArray[2] = 43;
  myArray[3] = 44;
  myArray[4] = 42;


  print("Unsorted:");
  for (i in 0:myArray.count()-1)
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

  insertion_sort(myArray);

  print("Sorted:");
  for (i in 0:myArray.count()-1)
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

endfunction


function insertion_sort(an_array :Array<Int32>)


    for(index in 1:an_array.count()-1) 

      var currentvalue = an_array[index];
      var position = index;

      while ((position > 1) && (an_array[position - 1] > currentvalue)) // this should be position > 0 in first operand

          an_array[position] = an_array[position - 1];
          position = position - 1;

      endwhile

      an_array[position] = currentvalue;

    endfor

endfunction
```


## Merge sort

!!! note 
	Coming soon. 


## Quick sort

!!! note 
	Coming soon.