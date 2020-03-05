A `Model` is the simplest way to build, train, and evaluate neural networks in `etch`. The `Model` type takes care of the underlying implementation details for `Graph`, `DataLoader`, and `Optimiser`.

There are three types of `Model`.

* **`Sequential`**: trains a computational graph to predict either continuous variables or classes, and allows more control over the layers of the network.
* **`Regressor`**: trains a computational graph to predict continuous variables. For example, what will be the future price of a particular currency?
* **`Classifier`**: trains a computational graph to predict classes. For example, is this a picture of a cat or a dog?


## Construct a `Model`

Create a `Model` by setting a flag in the constructor.

``` c++
function main()

	var model1 = Model("sequential");
	var model2 = Model("regressor");
	var model3 = Model("classifier");

endfunction
```


## Add

Manually add the layers to a `sequential` `Model`.

The function `add(x, y, z, a)` with four parameters requires you specify a flag type, the dimensions, and the activation type.

The function `add(x, y, z)` with three parameters requires you specify a flag type and the dimensions.

``` c++
function main()

	var model = Model("sequential");
	model.add("dense", 10u64, 10u64, "relu");	      
	model.add("dense", 10u64, 10u64, "relu");      
	model.add("dense", 10u64, 1u64);

endfunction
```


## Compile

Compile the `Model` with the `compile()` function.

The function `compile(loss-function-flag, optimiser-flag)` takes two inputs. In the below example, we compiled with a mean squared error loss function and an Adam `Optimiser`.

``` c++
function main()

	var model = Model("sequential");
	model.add("dense", 10u64, 10u64, "relu");	      
	model.add("dense", 10u64, 10u64, "relu");      
	model.add("dense", 10u64, 1u64);

	model.compile("mse", "adam");

endfunction
```


## Read in input data

The `readCSV(System.Argv(1))` function allows you to read in data from csv files with the `etch` compiler argument commands.

For example, run the below script with the following command. The first if-else block ensure the correct number of arguments with `System.Argc()`.

`./etch -- file1 file2 file3 file4`

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



## Fit

With the `Model` set up as above, you can now add the input data and run the training function `fit(data, labels, batch-size)`.

``` c++
function main()

    var data = readCSV(System.Argv(1));
    var label = readCSV(System.Argv(2));
    var test_data = readCSV(System.Argv(3));
    var test_label = readCSV(System.Argv(4));

    var model = Model("sequential");
    model.add("dense", 13u64, 10u64, "relu");
    model.add("dense", 10u64, 10u64, "relu");
    model.add("dense", 10u64, 1u64);
    model.compile("mse", "adam");

    var batch_size = 10u64;
    model.fit(data, label, batch_size);

endfunction
```


## Evaluate

Evaluate the prediction error with the `evaluate()` function.

``` c++
function main()

    var data = readCSV(System.Argv(1));
    var label = readCSV(System.Argv(2));
    var test_data = readCSV(System.Argv(3));
    var test_label = readCSV(System.Argv(4));

    var model = Model("sequential");
    model.add("dense", 13u64, 10u64, "relu");
    model.add("dense", 10u64, 10u64, "relu");
    model.add("dense", 10u64, 1u64);
    model.compile("mse", "adam");

    var batch_size = 10u64;
    model.fit(data, label, batch_size);

    var loss = model.evaluate();
    printLn(loss);

endfunction
```




## Predict

Finally, make predictions on the data


``` c++
function main()

    var data = readCSV(System.Argv(1));
    var label = readCSV(System.Argv(2));
    var test_data = readCSV(System.Argv(3));
    var test_label = readCSV(System.Argv(4));

    var model = Model("sequential");
    model.add("dense", 13u64, 10u64, "relu");
    model.add("dense", 10u64, 10u64, "relu");
    model.add("dense", 10u64, 1u64);
    model.compile("mse", "adam");

    var batch_size = 10u64;
    model.fit(data, label, batch_size);

    var loss = model.evaluate();
    printLn(loss);

    var predictions = model.predict(test_data);
    print(predictions.at(0u64, 0u64));

endfunction
```

<!--
## Serialise to string

It is possible to store `Model` data in a string. This facilitates smart contract function calls.

Create a string representation of a `Model` with the `serialiseToString()` function. 

Then, serialise the `Model` by setting the string into a `State`.

``` c++
persistent state : String;

function main() 
    
    use state;

    var model = Model("sequential");
    // build out Model here
    // ..

    // create string from Model
    var model_string = model.serializeToString();

    // demo the model string
    printLn(model_string);

    // serialise the Model with its hex string representation
    state.set(model_string);

endfunction
```



## Deserialise from string

Retrieve a `Graph` from the ledger via its string representation with the `deserialiseFromString()` function. 

``` c++
function main() 

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 2u64;
    tensor_shape[1] = 10u64;
    
    var data_tensor = Tensor(tensor_shape);
    var label_tensor = Tensor(tensor_shape);
    
    data_tensor.fill(7.0fp64);
    label_tensor.fill(7.0fp64);
    
    var graph = Graph();
    graph.addPlaceholder("Input");
    graph.addPlaceholder("Label");
    graph.addRelu("Output", "Input");
    graph.addMeanSquareErrorLoss("Error", "Output", "Label");
    graph.setInput("Input", data_tensor);
    graph.setInput("Label", label_tensor);
    
    var graph_string = graph.serializeToString();
    
    // serialise the Graph with its hex string representation
    var state = State<String>("graph_state");
    state.set(graph_string);
    
    graph.evaluate("Error");

    var retrieved_state = State<String>("graph_state");
    var retrieved_graph_string = retrieved_state.get();
    
    // demo the Graph string
    printLn(retrieved_graph_string);
    
    var retrieved_graph = Graph();
    retrieved_graph = retrieved_graph.deserializeFromString(retrieved_graph_string);

endfunction
```
-->


<br />