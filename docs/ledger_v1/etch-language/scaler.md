Use a `Scaler` to normalise data.

Declare and initialise a `Scaler`.

``` c++
function main()

	var scaler = Scaler();

endfunction
```

## Min max

The `min_max` flag identifies the scaler which normalises data sets in the range 0-1 based on the maximum and minimum value found in the data set.

Set the `Scaler` type with the `setScale()` function.

``` c++
var scaler = Scaler();
scaler.setScale(data_tensor, "min_max"); 
```

Once the `Scaler` type is set, run the `normalise()` function to scale the data. `deNormalise()` reverses the process. Both functions return a `Tensor`.

``` c++
var norm_data_tensor = scaler.normalise(data_tensor);
var denorm_data_tensor = scaler.deNormalise(norm_data_tensor);
```

## Scaler example

The following code builds a `Tensor` then sets a `Scaler` on it to do min max normalisation.

Two `Tensor` types hold normalised and denormalised data respectfully.

A nested for loop asserts all normalised data points are between 0 and 1, then prints a set of calculations for each data point.

``` c++
function main()

    var height = 20u64;
    var width = 40u64;
    var data_shape = Array<UInt64>(2);
    data_shape[0] = height;
    data_shape[1] = width;

    var data_tensor = Tensor(data_shape);
    data_tensor.fillRandom();

    var scaler = Scaler();
    scaler.setScale(data_tensor, "min_max");

    var norm_data_tensor = scaler.normalise(data_tensor);
    var denorm_data_tensor = scaler.deNormalise(norm_data_tensor);

    for(i in 0u64:height)
        for(j in 0u64:width)

            assert(norm_data_tensor.at(i, j) <= 1.0fp64);
            assert(norm_data_tensor.at(i, j) >= 0.0fp64);

            var diff = abs(data_tensor.at(i, j) - denorm_data_tensor.at(i, j));
            printLn(data_tensor.at(i, j));
            printLn(norm_data_tensor.at(i, j));
            printLn(denorm_data_tensor.at(i, j));
            printLn(diff);
            assert(diff < 0.1fp64);
            
        endfor
    endfor

endfunction
```




<br/>


