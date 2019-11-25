# AI in Etch

Let's look at an example of training a fully connected neural network to predict house prices for the Boston Housing Dataset, which can be downloaded from [here](http://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html).

This example will be implemented in Etch, the language used for executing applications in the Fetch.ai Virtual Machine, and to write smart contracts on the Fetch.ai ledger. Instructions to set up an Etch development environment can be found [here](/etch-language/getstarted/).

### Loading input data

An Etch program needs a `main()` function as its entry point, and that is where all code in this example will reside.

Since the input is provided via multiple CSV files, the the `main()` function firstly has to check the correct number of files is provided, then load the input data from them:

``` c++
function main()

    if (System.Argc() != 5)
      print("Usage: SCRIPT_FILE -- PATH/TO/BOSTON_TRAIN_DATA.CSV PATH/TO/BOSTON_TRAIN_LABELS.CSV PATH/TO/BOSTON_TEST_DATA.CSV PATH/TO/BOSTON_TEST_LABELS.CSV ");
      return;
    endif

    var data = readCSV(System.Argv(1));
    var label = readCSV(System.Argv(2));
    var test_data = readCSV(System.Argv(3));
    var test_label = readCSV(System.Argv(4));

endfunction
```

### Setting up the model

We then create a `Model` type and set a flag on it that describes what kind of `Model` we want. A `sequential` model allows us to manually add layers specifying:

* Type: `dense` in this example
* Input size: must match the data for the first layer
* Neurons in layer / output size: must match the label size for the final layer
* Activation type (optional): here we use a rectified linear unit for the first two layers, and no activation for the final layer

Finally, we compile the model using the `mean squared error` loss function, and the `adam` optimiser.

``` c++
var model = Model("sequential");
model.add("dense", 13u64, 10u64, "relu");
model.add("dense", 10u64, 10u64, "relu");
model.add("dense", 10u64, 1u64);
model.compile("mse", "adam");
```

### Training and evaluating the model

Training the model once set up is easy: we just call `fit` with the data, labels, and chosen batch size.

``` c++
var batch_size = 10u64;
model.fit(data, label, batch_size);
```

Evaluating the model will return the training loss by default, but other metrics may be specified.

``` c++
var loss = model.evaluate();
```

### Making predictions on the model

Finally, we make house price predictions by passing in the test data. Since `test_data` contains input data for multiple houses, the output tensor contains multiple predictions.

``` c++
var predictions = model.predict(test_data);
```

### Running the script

The script can be run from the root of the ledger folder, passing the input files as arguments with the following:

``` c++
./etch boston-training.etch -- 1st-file 2nd-file 3rd-file 4th-file
```


<br />
