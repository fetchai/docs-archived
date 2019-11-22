# AI in Etch

The `etch` language is used for executing applications in the Fetch VM, which is required for writing smart contracts on the Fetch Ledger.
Writing machine learning applications in the `etch` language should be familiar for developers with machine learning experience in other frameworks. Let's look at an example of training a fully connected neural net to predict house prices for the boston housing dataset.

## Boston Housing Price Prediction
``` c++
function main()

    // read in training and test data
    if (System.Argc() != 5)
      print("Usage: SCRIPT_FILE -- PATH/TO/BOSTON_TRAIN_DATA.CSV PATH/TO/BOSTON_TRAIN_LABELS.CSV PATH/TO/BOSTON_TEST_DATA.CSV PATH/TO/BOSTON_TEST_LABELS.CSV ");
      return;
    endif

    var data = readCSV(System.Argv(1));
    var label = readCSV(System.Argv(2));
    var test_data = readCSV(System.Argv(3));
    var test_label = readCSV(System.Argv(4));

    // set up a model architecture
    var model = Model("sequential");
    model.add("dense", 13u64, 10u64, "relu");
    model.add("dense", 10u64, 10u64, "relu");
    model.add("dense", 10u64, 1u64);
    model.compile("mse", "adam");

    // train the model
    var batch_size = 10u64;
    model.fit(data, label, batch_size);

    // evaluate performance
    var loss = model.evaluate();

    // make predictions on all test data
    var predictions = model.predict(test_data);

endfunction
```

Above is code example for an etch script that trains a fully connected model on csv's read in from the command line.

We can break it down into the following steps:

1. Load in some data files. In this case we use the <a href="https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html" target=_blank>Boston Housing Dataset</a>.
2. Define a sequential model with three fully connected layers.
3. Compile the model, specifying the loss function and optimiser.
4. Train the model by fitting it to the training data.
5. Evaluate performance on the model
6. Make a prediction on the test data

Let's take a closer look.

### Setup the `etch` vm

If you haven't yet run an `etch` script, make sure you can do so from the console. 

Instructions are <a href="../getstarted/" target=_blank>here</a>.



### Input file check

First, the code checks for the correct the number of input files.

``` c++
if (System.Argc() != 5)
  
  print("Usage: SCRIPT_FILE -- PATH/TO/BOSTON_TRAIN_DATA.CSV PATH/TO/BOSTON_TRAIN_LABELS.CSV PATH/TO/BOSTON_TEST_DATA.CSV PATH/TO/BOSTON_TEST_LABELS.CSV ");
  return;

endif
```


### Load the input data

Next, we load the input data from the files.

``` c++
var data = readCSV(System.Argv(1));
var label = readCSV(System.Argv(2));
var test_data = readCSV(System.Argv(3));
var test_label = readCSV(System.Argv(4));
```


### Set up the model

First, we create a `Model` type and set a flag on it that describes what kind of `Model` we want. The `sequential` model allows us to manually add the layers.

We then `add` our layers to the model specifying the layer type ('dense'), input size (must match the data for the first layer), neurons in layer / output size (must match the label size for the final layer), and lastly an optional activation type (here we use a rectified linear unit for the first two layers, and no activation for the final layer).

Finally, we compile the model using the 'mean squared error' loss function, and the 'adam' optimiser.

``` c++
var model = Model("sequential");
model.add("dense", 13u64, 10u64, "relu");
model.add("dense", 10u64, 10u64, "relu");
model.add("dense", 10u64, 1u64);
model.compile("mse", "adam");
```


### Train the model

Training the model once set up is easy; we just call `fit` with the data, labels, and chosen batch size.

``` c++
var batch_size = 10u64;
model.fit(data, label, batch_size);
```

### Evaluate the model

Evaluating the model will, by default, return the training loss; but other metrics may be specified.
``` c++
var loss = model.evaluate();
```


### Make predictions on the model

Finally we make house price predictions by passing in the test data. Since the test_data contains input
data for multiple houses, the output tensor contains multiple predictions.
``` c++
var predictions = model.predict(test_data);
```



### Run the script

Run the script from the ledger repo adding the input files as input arguments with the following.

``` c++
./etch boston-training.etch -- 1st-file 2nd-file 3rd-file 4th-file
```


<br />
