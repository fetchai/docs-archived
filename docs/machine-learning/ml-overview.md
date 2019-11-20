Writing machine learning applications in the `etch` language should be familiar for developers already experience in writing with other machine learning frameworks. Let's look at an example of training a fully connected neural net to solve the regression problem of predicting house prices for the boston housing dataset.

### Boston Housing Example

Below is code for an etch script that trains a fully connected model on csv's read in from the command line. Naturally a different approach has to be taken in a smart contract, but for now we'll work locally just to see how machine learning works in etch.

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
    print(loss);

    // make predictions on all test data
    var predictions = model.predict(test_data);
    print(predictions.at(0u64, 0u64));

endfunction
```

At the core of this example is setting up a sequential model that lets you specify what each layer of the graph should be. In this case we specify a three-layer dense network. Then we compile the model, specifying the loss function to be mean squared error, and the optimiser to be adam.

With the model set up we fit the data to the labels, and specify the batch size for training.

The demo does four things.

1. Builds a neural network with the <a href="https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html" target=_blank>Boston Housing Dataset</a>.
2. Trains the model.
3. Evaluates the model accuracy.
4. Makes predictions on the model.

Let's take a closer look.



## Setup the `etch` vm

If you haven't yet run an `etch` script, make sure you can do so from the console. 

Instructions are <a href="../getstarted/" target=_blank>here</a>.



## Input file check

First, the code checks for the correct the number of input files.

``` c++
if (System.Argc() != 5)
  
  print("Usage: SCRIPT_FILE -- PATH/TO/BOSTON_TRAIN_DATA.CSV PATH/TO/BOSTON_TRAIN_LABELS.CSV PATH/TO/BOSTON_TEST_DATA.CSV PATH/TO/BOSTON_TEST_LABELS.CSV ");
  return;

endif
```


## Load the input data

Next, we load the input data from the files.

``` c++
var data = readCSV(System.Argv(1));
var label = readCSV(System.Argv(2));
var test_data = readCSV(System.Argv(3));
var test_label = readCSV(System.Argv(4));
```


## Set up the model

First, we create a `Model` type and set a flag on it that describes what kind of `Model` we want. The `sequential` model allows us to manually add the layers.

We then `add` our layers to the model with a given flag, width, and activation type.

Finally, we compile the model with a specific loss function and optimiser.

``` c++
var model = Model("sequential");
model.add("dense", 13u64, 10u64, "relu");
model.add("dense", 10u64, 10u64, "relu");
model.add("dense", 10u64, 1u64);
model.compile("mse", "adam");
```


## Train the model

Training the model once set up is super easy.

``` c++
var batch_size = 10u64;
model.fit(data, label, batch_size);
```

## Evaluate the model

``` c++
var loss = model.evaluate();
print(loss);
```


## Make predictions on the model

``` c++
var predictions = model.predict(test_data);
print(predictions.at(0u64, 0u64));
```




## Run the script

Run the script from the ledger repo adding the input files as input arguments with the following.

``` c++
./etch boston-training.etch -- 1st-file 2nd-file 3rd-file 4th-file
```


<br />
