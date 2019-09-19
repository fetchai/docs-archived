A `Tensor` is a vector or matrix type having multiple dimensions. 

In `etch` it is the n-dimensional matrix type used by the mathematics and machine learning libraries.


## Declare and initialise

Declare and initialise a `Tensor` by first defining the size of its dimensions. 

We do that with a one dimensional array of 64 bit unsigned integers: `Array<UInt64>`. 

!!! Note
    There is conceptually no limit to how many dimensions a `Tensor` object can have, although there are practical limitations set by the `etch` implementation which the documentation highlights.

The following code sets up a two dimensional `Tensor` object's shape by declaring an array with length equal to two. 

We give the first dimension three elements and the second dimension four.

Finally, the code takes the array, builds the `Tensor`, and prints the default `Fixed64` values contained within.

``` c++
function main()

	var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 4u64;

    var tensor = Tensor(tensor_shape);
    printLn(tensor.toString());

endfunction
```

## toString

Print a `Tensor` object with no more than two dimensions with the `toString()` function.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();
    printLn(tensor.toString());

endfunction
```


## Size

Get the size of a `Tensor` object with the `size()` function. It returns the total number of elements in the `Tensor`.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 12u64;
    tensor_shape[1] = 12u64;

    var tensor = Tensor(tensor_shape);
    printLn(tensor.size());

endfunction
```



## fromString

Use the `fromString()` function to insert a comma separated string of values into each element of the `Tensor`. 

``` c++
function main() 

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 4u64;
    tensor_shape[1] = 1u64;
    
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();
    printLn(tensor.toString());
    
    var string_vals = "1.0, 1.0, 1.0, 1.0";
    tensor.fromString(string_vals);
    printLn(tensor.toString());

endfunction
```


## Fill

Use the `fill()` function to insert a specific `Fixed64` value into each element of the `Tensor`. 

The following two dimensional `Tensor` contains nine elements all set to `7.0`.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fill(7.0fp64);

    printLn(tensor.toString());

endfunction
```


## Fill Random

The function `fillRandom()` inserts random `Fixed64` values between 0 and 1 into the `Tensor`.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    printLn(tensor.toString());

endfunction
```

## Setters

Use `setAt()` to insert a `Fixed64` value at a specific index.

### 1D

The following code creates a one dimensional `Tensor` object. The dimension has three elements.

The code sets specific values at each element with the function `setAt(index_u64, value_fp64)`.


``` c++
function main()

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.setAt(0u64, 33.0fp64);
    tensor.setAt(1u64, 34.0fp64);
    tensor.setAt(2u64, 35.0fp64);

    printLn(tensor.toString());

endfunction
```


### 2D

The following code creates a two dimensional `Tensor` object. Each dimension has three elements.

The code sets specific values at each element with the function `setAt(index1_u64, index2_u64, value_fp64)`.


``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;

    var tensor = Tensor(tensor_shape);

    tensor.setAt(0u64, 0u64, 33.0fp64);
    tensor.setAt(1u64, 1u64, 34.0fp64);
    tensor.setAt(2u64, 2u64, 35.0fp64);

    printLn(tensor.toString());

endfunction
```

### 3D

The following code creates a three dimensional `Tensor` object. Each dimension has three elements.

The code sets specific values at each element with the function `setAt(index1_u64, index2_u64, index3_u64, value_fp64)`.


``` c++
function main()

    var tensor_shape = Array<UInt64>(3);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    tensor_shape[2] = 3u64;

    var tensor = Tensor(tensor_shape);

    tensor.setAt(0u64, 0u64, 0u64, 33.0fp64);
    tensor.setAt(1u64, 1u64, 1u64, 34.0fp64);
    tensor.setAt(2u64, 2u64, 2u64, 35.0fp64);

endfunction
```

### 4D

The following code creates a four dimensional `Tensor` object. Each dimension has three elements.

The code sets specific values at each element with the function `setAt(index1_u64, index2_u64, index3_u64, index4_u64, value_fp64)`.


``` c++
function main()

    var tensor_shape = Array<UInt64>(4);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    tensor_shape[2] = 3u64;
    tensor_shape[3] = 3u64;

    var tensor = Tensor(tensor_shape);

    tensor.setAt(0u64, 0u64, 0u64, 0u64, 33.0fp64);
    tensor.setAt(1u64, 1u64, 1u64, 1u64, 34.0fp64);
    tensor.setAt(2u64, 2u64, 2u64, 2u64, 35.0fp64);
    tensor.setAt(3u64, 3u64, 3u64, 3u64, 36.0fp64);

endfunction
```


## Getters

The getter function `at()` is available for one, two, and three dimension `Tensor` objects. It returns the value of the element at the given dimension.

### 1D

``` c++
function main()

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.setAt(0u64, 33.0fp64);
    tensor.setAt(1u64, 34.0fp64);
    tensor.setAt(2u64, 35.0fp64);

    printLn(tensor.at(1u64));

endfunction
```
### 2D

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    printLn(tensor.at(1u64, 1u64));

endfunction
```

### 3D

``` c++
function main()

    var tensor_shape = Array<UInt64>(3);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    tensor_shape[2] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    printLn(tensor.at(1u64, 1u64, 1u64));

endfunction
```

### 4D

``` c++
function main()

    var tensor_shape = Array<UInt64>(4);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    tensor_shape[2] = 3u64;
    tensor_shape[3] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    printLn(tensor.at(1u64, 1u64, 1u64, 1u64));

endfunction
```



## Reshape

The function `reshape()` allows you to reshape an already existing `Tensor` into a new dimensional shape. 

!!! Note
    The `reshape()` function is destructive and the previous `Tensor` data is not preserved.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    var new_shape = Array<UInt64>(10);
    tensor.reshape(new_shape);

endfunction
```


## Squeeze

The function `squeeze()` returns a copy of the `Tensor` removing any dimension with size 1.

Currently, `squeeze()` throws an error if there are no dimensions in the `Tensor` of size 1.

``` c++
function main() 

    var tensor_shape = Array<UInt64>(3);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 1u64;
    tensor_shape[2] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fill(7.0fp64);

    // reassign tensor
    tensor = tensor.squeeze();
    printLn("Squeezed!");

    printLn(tensor.toString());

endfunction
```



## Serialisation

A `Tensor` is serialisable and deserialisable.

The following code stores a `Tensor` in a `State` object. It then retrieves the `State` object, gets and prints the `Tensor`.

``` c++
function main()

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 12u64;
    tensor_shape[1] = 12u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();
    
    var serialised_tensor = State<Tensor>("tensor"); 
    serialised_tensor.set(tensor); 
    
    var retrieved_tensor = Tensor(tensor_shape);
    retrieved_tensor = serialised_tensor.get();

    printLn(retrieved_tensor.toString());

endfunction
```






<br/>