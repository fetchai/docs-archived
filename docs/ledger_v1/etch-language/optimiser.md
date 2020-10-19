Use an `Optimiser` to run the machine learning training on a `Graph` and a `DataLoader`.

Declare and initialise an `Optimiser`, giving it the name of the optimisation algorithm you wish to run, the `Graph` and the `DataLoader` objects, and the place-holder nodes for the input data, training data, and error data.


``` c++
var optimiser = Optimiser("sgd", graph, dataloader, {"Input1", "Input2", ...},"Label", "Error");
```

To run the `Optimiser`, call `run()` with a batch size. Batch size sets the number of samples to train on in an epoch.

``` c++
var loss = optimiser.run(batch_size);
```



## Adagrad

`"adagrad"` implements the <a href="http://jmlr.org/papers/volume12/duchi11a/duchi11a.pdf" target=_blank>Adagrad optimiser</a>.

``` c++
function main()

    var data_shape = Array<UInt64>(2);
    data_shape[0] = 20u64;
    data_shape[1] = 4000u64;

    var label_shape = Array<UInt64>(2);
    label_shape[0] = 1u64;
    label_shape[1] = 4000u64;

    var data_tensor = Tensor(data_shape);
    var label_tensor = Tensor(label_shape);

    data_tensor.fillRandom();
    label_tensor.fillRandom();

    var dataloader = DataLoader("tensor");
    dataloader.addData(data_tensor, label_tensor);

    var graph = Graph();
    graph.addPlaceholder("Input");
    graph.addPlaceholder("Label");
    graph.addFullyConnected("Output", "Input", 20, 1);
    graph.addMeanSquareErrorLoss("Error", "Output", "Label");

    var batch_size = 8u64;

    // train the data via an Adagrad Optimiser
    var optimiser = Optimiser("adagrad", graph, dataloader, {"Input"}, "Label", "Error");
    var loss = optimiser.run(batch_size);

endfunction
```


## Adam

`"adam"` implements the <a href="https://arxiv.org/abs/1412.6980" target=_blank>Adam optimiser</a>.

``` c++
	// ...
	// train the data via an Adam Optimiser
    var optimiser = Optimiser("adam", graph, dataloader, {"Input"}, "Label", "Error");
    var loss = optimiser.run(batch_size);
    // ...
```

## Momentum

`"momentum"` implements the <a href="https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum" target=_blank>Momentum optimiser</a>.

``` c++
	// ...
	// train the data via a Momentum Optimiser
    var optimiser = Optimiser("momentum", graph,dataloader,  {"Input"}, "Label", "Error");
    var loss = optimiser.run(batch_size);
    // ...
```

## RMSprop

`"rmsprop"` implements the <a href="http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf" target=_blank>RMSprop optimiser</a>.

``` c++
	// ...
	// train the data via an RMSprop Optimiser
    var optimiser = Optimiser("rmsprop", graph, dataloader, {"Input"}, "Label", "Error");
    var loss = optimiser.run(batch_size);
    // ...
```


## SGD

`"sgd"` implements the <a href="https://en.wikipedia.org/wiki/Stochastic_gradient_descent" target=_blank>SGD optimiser</a>.

``` c++
	// ...
	// train the data via an SGD Optimiser
    var optimiser = Optimiser("sgd", graph, dataloader, {"Input"}, "Label", "Error");
    var loss = optimiser.run(batch_size);
    // ...
```


## Full optimisation example

Run the collection of `Optimiser` consecutively and check that error reduction is consistent.

``` c++
function main()

    var data_shape = Array<UInt64>(2);
    data_shape[0] = 20u64;
    data_shape[1] = 4000u64;

    var label_shape = Array<UInt64>(2);
    label_shape[0] = 1u64;
    label_shape[1] = 4000u64;

    var data_tensor = Tensor(data_shape);
    var label_tensor = Tensor(label_shape);

    data_tensor.fillRandom();
    label_tensor.fillRandom();

    var dataloader = DataLoader("tensor");
    dataloader.addData(data_tensor, label_tensor);

    var graph = Graph();
    graph.addPlaceholder("Input");
    graph.addPlaceholder("Label");
    graph.addFullyConnected("Output", "Input", 20, 1);
    graph.addMeanSquareErrorLoss("Error", "Output", "Label");

    var batch_size = 8u64;

    // test that every optimiser can be constructed and that running reduces loss

    var optimiser1 = Optimiser("adagrad", graph, dataloader, {"Input"}, "Label", "Error");
    var loss = optimiser1.run(batch_size);

    var optimiser2 = Optimiser("adam", graph, dataloader, {"Input"}, "Label", "Error");
    var loss2 = optimiser2.run(batch_size);
    assert(loss2 < loss);

    var optimiser3 = Optimiser("momentum", graph, dataloader, {"Input"}, "Label", "Error");
    loss = optimiser3.run(batch_size);
    assert(loss < loss2);

    var optimiser4 = Optimiser("rmsprop", graph, dataloader, {"Input"},"Label", "Error");
    loss2 = optimiser4.run(batch_size);
    assert(loss2 < loss);

    var optimiser5 = Optimiser("sgd", graph, dataloader, {"Input"}, "Label", "Error");
    loss = optimiser5.run(batch_size);
    assert(loss < loss2);

    loss2 = optimiser1.run(batch_size);
    assert(loss2 < loss);

endfunction
```



## Reset Graph or DataLoader

Reset the `Graph` or `DataLoader` into the `Optimiser` with the `setGraph()` and `setDataLoader()` functions.


``` c++ 
function main()

    var data_shape = Array<UInt64>(2);
    data_shape[0] = 20u64;
    data_shape[1] = 4000u64;

    var label_shape = Array<UInt64>(2);
    label_shape[0] = 1u64;
    label_shape[1] = 4000u64;

    var data_tensor = Tensor(data_shape);
    var label_tensor = Tensor(label_shape);

    data_tensor.fillRandom();
    label_tensor.fillRandom();

    var dataloader = DataLoader("tensor");
    dataloader.addData(data_tensor, label_tensor);

    var graph = Graph();
    graph.addPlaceholder("Input");
    graph.addPlaceholder("Label");
    graph.addFullyConnected("Output", "Input", 20, 1);
    graph.addMeanSquareErrorLoss("Error", "Output", "Label");

    var batch_size = 8u64;

    // test that every optimiser can be constructed and that running reduces loss

    var optimiser = Optimiser("adagrad", graph, dataloader, {"Input"}, "Label", "Error");
    var loss1 = optimiser.run(batch_size);

    // build new Graph and DataLoader
    var graph2 = Graph();
    graph2.addPlaceholder("Input");
    graph2.addPlaceholder("Label");
    graph2.addFullyConnected("Output", "Input", 20, 1);
    graph2.addMeanSquareErrorLoss("Error", "Output", "Label");
    var dataloader2 = DataLoader("tensor");

    data_tensor.fillRandom();
    label_tensor.fillRandom();
    dataloader2.addData(data_tensor, label_tensor);

    // set new Graph and DataLoader into the Optimiser
    optimiser.setGraph(graph2);
    optimiser.setDataloader(dataloader2);
    var loss2 = optimiser.run(batch_size);
    
    // assert(loss2 < loss1);

endfunction
```



</br>