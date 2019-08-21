A `DataLoader` loads two `Tensor` data nodes to form a set of `TrainingPair` data point objects for machine learning operations.

A `DataLoader` is used in conjunction with an `Optimiser`.

Declare and initialise a `DataLoader` giving a string parameter which define the type of input data. The common generic `DataLoader` takes `Tensor` objects. 

``` c++
function main()

    var dataLoader = DataLoader("tensor");

endfunction
```

There are currently three flavours of `DataLoader` in `etch`. 

Fetch.AI developers have built specific `DataLoader` types for research and example purposes that take `MNIST` files, and `csv` files for a commodity application.


## `Tensor` data loader

Use the `addData()` function for loading `Tensor` objects.

``` c++
var dataloader = DataLoader("tensor");
dataloader.addData(data_tensor, label_tensor);
```

The following code builds two `Tensor` objects containing data and label values respectively. 

These are then loaded into a `DataLoader()` with the `addData()` function.

``` c++
function main()

    var data_shape = Array<UInt64>(2);
    data_shape[0] = 2u64;
    data_shape[1] = 4u64;

    var label_shape = Array<UInt64>(2);
    label_shape[0] = 2u64;
    label_shape[1] = 4u64;

    var data_tensor = Tensor(data_shape);
    var label_tensor = Tensor(label_shape);

    var dataloader = DataLoader("tensor");
    dataloader.addData(data_tensor, label_tensor);

endfunction
```

## `isDone()` and `getNext()`

`DataLoader` function `isDone()` returns a boolean if a read has reached the end of a training epoch.

The `getNext()` function iterates through the `TrainingPair` types contained within a `DataLoader`.

Typically, use `isDone()` and `getNext()` together.

``` c++
function main()

    var data_shape = Array<UInt64>(2);
    data_shape[0] = 2u64;
    data_shape[1] = 4u64;

    var label_shape = Array<UInt64>(2);
    label_shape[0] = 2u64;
    label_shape[1] = 4u64;

    var data_tensor = Tensor(data_shape);
    var label_tensor = Tensor(label_shape);

    var dataloader = DataLoader("tensor");
    dataloader.addData(data_tensor, label_tensor);

    while (!dataloader.isDone())
      dataloader.getNext();
      // do stuff here
    endwhile

endfunction
```


<!--
## MNIST data loader

To add <a href="https://en.wikipedia.org/wiki/MNIST_database" target=_blank>MNIST</a> data to a `DataLoader` use `etch` system function `System.Argv()` that has access to command line arguments.


``` c++
var data_loader = DataLoader("mnist");
data_loader.addData(System.Argv(1), System.Argv(2));
```

The following code takes test MNIST image and label files downloaded from <a href="http://yann.lecun.com/exdb/mnist/" target=_blank>here</a>. It then builds a `DataLoader()` object and calls the `addData()` function to load the files into the `DataLoader`.

``` c++
function main()

    printLn(System.Argv(1));
    printLn(System.Argv(2));

    var data_loader = DataLoader("mnist");
    data_loader.addData(System.Argv(1), System.Argv(2));

endfunction
```
To send the files to `main()` use the following format on the command line.

```./etch ./tests/test.etch -- ~/Downloads/t10k-images-idx3-ubyte ~/Downloads/t10k-labels-idx1-ubyte```


## Commodity data loader

The commodity `DataLoader` is for a specific Fetch internal example. It is for testing purposes only and we do not recommend its use.

Use the `commodity` flag on the `addData()` function to load commodity example data contained in `.csv` files.

``` c++
var data_loader = DataLoader("commodity");
data_loader.addData(System.Argv(1), System.Argv(2));
```

The following code loads a pair of example `csv` files containing commodity data into a `DataLoader`.

``` c++
function main()

    // debug checks
    printLn(System.Argv(1));
    printLn(System.Argv(2));

    var data_loader = DataLoader("commodity");
    data_loader.addData(System.Argv(1), System.Argv(2));

endfunction
```
To send the files to `main()` use the following format.

`./etch ./tests/test.etch -- ~/Downloads/best_models/keras_aluminium_px_last_us_x_test.csv ~/Downloads/best_models/keras_aluminium_px_last_us_y_pred_test.csv`.


-->



<br/>

