<h1>Designing a sorting algorithm</h1>

## Bubble sort

``` c++
function main()
  
  var myArray = Array<Int32>(5);
  myArray[0] = 41;
  myArray[1] = 40;
  myArray[2] = 43;
  myArray[3] = 44;
  myArray[4] = 42;

  
  print("Unsorted:");
  for (i in 0:myArray.count())
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

  bubble_sort(myArray);

  print("Sorted:");
  for (i in 0:myArray.count())
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

endfunction


function bubble_sort(an_array :Array<Int32>)

    var more_swaps : Bool = true;
  
    while(more_swaps == true)

      more_swaps = false;

      for (i in 0:an_array.count()-1) 
          
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

``` c++
function main()
  
  var myArray = Array<Int32>(5);
  myArray[0] = 41;
  myArray[1] = 40;
  myArray[2] = 43;
  myArray[3] = 44;
  myArray[4] = 42;

  
  print("Unsorted:");
  for (i in 0:myArray.count())
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

  insertion_sort(myArray);

  print("Sorted:");
  for (i in 0:myArray.count())
    print(toString(myArray[i]) + " ");
  endfor
  printLn("");

endfunction


function insertion_sort(an_array :Array<Int32>)


    for(index in 1:an_array.count()) 

      var currentvalue = an_array[index];
      var position = index;

      while ((position >= 1) && (an_array[position - 1] > currentvalue))
         
          an_array[position] = an_array[position - 1];
          position = position - 1;

      endwhile

      an_array[position] = currentvalue;

    endfor
    

endfunction
```


## Merge sort

``` c++
function main()

  // needs to be an even number length
    var a_list = Array<UInt32>(15);

    for (i in 0:a_list.count())
        a_list[i] = rand(0u32, 1000u32);
    endfor

    printLn(a_list);
    merge(a_list);
    printLn(a_list);

endfunction


function merge(a_list : Array<UInt32>)

    // print("Splitting "); printLn(a_list);

    if (a_list.count() > 1)

        var mid = a_list.count() / 2;

        var left_half = Array<UInt32>(mid);
        var right_half = Array<UInt32>(mid);

        if (a_list.count() % 2 != 0)
          right_half = Array<UInt32>(mid+1);
        endif

        for (x in 0:mid)
            left_half[x] = a_list[x];
        endfor

        var count = 0;
        for (y in mid:a_list.count())
            right_half[count] = a_list[y];
            count += 1;
        endfor

        // print("Left half "); printLn(left_half);
        // print("Right half "); printLn(right_half);

        merge(left_half);
        merge(right_half);


        var i = 0;
        var j = 0;
        var k = 0;


        while (i < left_half.count() && j < right_half.count())
            if (left_half[i] < right_half[j])
                a_list[k] = left_half[i];
                i += 1;
            else
                a_list[k] = right_half[j];
                j += 1;
            endif

            k=k+1;
        endwhile


        while (i < left_half.count())
            a_list[k] = left_half[i];
            i += 1;
            k += 1;
        endwhile


        while (j < right_half.count())
            a_list[k] = right_half[j];
            j += 1;
            k += 1;
        endwhile      

    endif 

    //print("Merging "); printLn(a_list);

endfunction 
```


## Quick sort

``` c++
function main()

    var a_list = Array<Int32>(15);

    for (i in 0:a_list.count())
      a_list[i] = rand(0, 1000);
    endfor

    var n = a_list.count(); 

    printLn(a_list); 
    quick_sort(a_list, 0, n-1);
    printLn(a_list);

endfunction


function quick_sort(a_list : Array<Int32>, low : Int32, high : Int32) 

    var pi = 0;

    if (low < high)

        // get the partition index
        pi = partition(a_list, low, high);

        quick_sort(a_list, low, pi-1);
        quick_sort(a_list, pi+1, high);

    endif

endfunction


function partition (a_list : Array<Int32>, low : Int32, high : Int32) : Int32

    var pivot = rand(low, high);
    
    // swap random pivot with high
    var temp = a_list[high];
    a_list[high] = a_list[pivot];
    a_list[pivot] = temp;
    
    // track next pivot index
    var new_pivot_index = low - 1;

    for (index in low:high)

        if (a_list[index] < a_list[high])

            new_pivot_index = new_pivot_index + 1;
            temp = a_list[new_pivot_index];
            a_list[new_pivot_index] = a_list[index];
            a_list[index] = temp;

        endif

    endfor

    // swap pivot to new spot
    temp = a_list[new_pivot_index + 1];
    a_list[new_pivot_index + 1] = a_list[high];
    a_list[high] = temp;
    
    return new_pivot_index + 1;

   
endfunction
```


<br/>