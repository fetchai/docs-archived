Declare and initialise a `Graph`.

``` c++
function main()

    var graph = Graph();

endfunction
```

A `Graph` is a directed acyclic computational graph used to process data through a sequence of operations. 

The current primary use case for these is the instantiation of neural networks. Each node in the `Graph` maintains responsibility for either a single operation or a layer of operations.

The preferred method for training a `Graph` is to use a `DataLoader` and `Optimiser`. We describe these two objects in a later section. 



## Placeholders

Placeholder nodes store data on the `Graph`. Use them to set the input for computing a forward pass of a neural network.

Create a placeholder node with `addPlaceholder()`.

``` c++
function main()

    var graph = Graph();
    graph.addPlaceholder("my_tensor");

endfunction
```






## Operations



### Fully connected

Add a fully connected layer to a `Graph` with the function `addFullyConnected()`.

It takes four input parameters specifying the name of the fully connected node, the name of a previously defined node, input size, and output size.


``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(2);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    graph.addPlaceholder("my_tensor");
    graph.setInput("my_tensor", tensor);

    graph.addFullyConnected("connected", "my_tensor", 3*3, 4);

endfunction
```


### 1D convolution

The `addConv1D()` training node operation of a `Graph` convolves the input layer in one dimension.

It takes six parameters specifying the name of the node, the name of a previously defined node (to feed input), the number of filters, number of input channels, kernel size, and stride size respectively.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(3);
    tensor_shape[0] = 3u64;
    tensor_shape[1] = 3u64;
    tensor_shape[2] = 3u64;

    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    graph.addPlaceholder("my_tensor");
    graph.setInput("my_tensor", tensor);

    graph.addConv1D("conv", "my_tensor", 3, 3, 3, 2);

endfunction
```

## Activations

### ReLU

The `addRelu()` function of a `Graph` adds a node which contains the rectified linear unit (ReLU) activation function. Its behaviour can be characterised as returning `x` if `x > 0`, or `0` otherwise.

It takes two parameters specifying the node name and the name of a node which feeds input to the ReLU.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    graph.addPlaceholder("my_tensor");
    graph.setInput("my_tensor", tensor);

    graph.addRelu("relu", "my_tensor");

endfunction
```

### Softmax

The `addSoftmax()` function of a `Graph` adds a node to the `Graph` that applies the `softmax` activation function to the input `Tensor`.

It takes two parameters specifying the name of the node and the name of an existing node that feeds input data.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    graph.addPlaceholder("my_tensor");
    graph.setInput("my_tensor", tensor);

    graph.addSoftmax("softmax", "my_tensor");

endfunction
```


### Dropout

The `addDropout()` function of a `Graph` adds a node that applies the `dropout` activation function to the input `Tensor`.

It takes three parameters specifying the name of the node, the name of an existing node that feeds input data, and a `Fixed64` type with a value between 0 and 1 specifying the dropout randomisation value.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    graph.addPlaceholder("my_tensor");
    graph.setInput("my_tensor", tensor);

    graph.addDropout("dropout", "my_tensor", 0.5fp64);

endfunction
```


## Loss functions

### Cross entropy loss

The `addCrossEntropyLoss()` function of a `Graph` is a loss function measuring the performance of a classification model. 

It takes three parameters specifying the name of the node, the name of the input data node, and the name of the label data node.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    input_tensor.fillRandom();

    var label_tensor = Tensor(tensor_shape);
    label_tensor.fillRandom();

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);

    graph.addCrossEntropyLoss("cross_entropy_loss", "input", "label");

endfunction
```



### Mean square error loss

The `addMeanSquareErrorLoss()` function of a `Graph` is a loss function measuring the average of the square of errors.

It takes three parameters specifying the name of the node, the name of the input data node, and the name of the label data node.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    input_tensor.fillRandom();

    var label_tensor = Tensor(tensor_shape);
    label_tensor.fillRandom();

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);

    graph.addMeanSquareErrorLoss("mean_square_error_loss", "input", "label");

endfunction
```

<!--
## State dicts 

A `StateDict` extracts the weights from a `Graph` and passes them to another. It only saves the weights in a layer and discards all meta data.

Create a `StateDict` type.

``` c++
function main()

    var state_dict = StateDict();

endfunction
```

Set weights on it with a `Tensor`.

``` c++
function main()

    var state_dict = StateDict();

    var graph = Graph();
    graph.addPlaceholder("my_tensor");

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var tensor = Tensor(tensor_shape);
    tensor.fillRandom();

    // state_dict.setWeights("my_tensor", tensor);
    // Segmentation fault: 11

endfunction
```

Load it into a `Graph`.

``` c++
function main()

    var state_dict = StateDict();
    var graph = Graph();
    graph.loadStateDict(state_dict);

endfunction
```
-->

## Serialisation

A `Graph` is serialisable and deserialisable.

The following code stores a `Graph` in a `State` object. It then creates a new `Graph` object and retrieves the `Graph` from the `State`.

``` c++
function main()

    var graph = Graph();

    var graph_state = State<Graph>("graph");
    graph_state.set(graph);

    var retrieved_graph = Graph();
    retrieved_graph = graph_state.get();

endfunction
```


## Build a `Graph` example

The example below builds a `Graph` object by first adding two placeholder nodes which will contain the input and label data. 

Next, a fully connected layer is set up, `FC_1`, containing 128 neurons and taking input data of size `28x28`. The output will feed into a ReLU activation, `Relu_1`.

These two steps are repeated with new fully connected layer `FC_2` taking `Relu_1` as input and consequently lowering the input dimension and output neurons. The output of this, `FC_2`, is fed into another ReLU activation, `Relu_2`.

Finally, after running a final fully connected layer, we will calculate a soft max activation before applying the cross entropy loss function against the `Label` data to evaluate the accuracy of the model.

The code does not show steps for loading the data or training the `Graph`.


``` c++
function main()

    // define the neural network
    var g = Graph();

    // placeholders to map input data
    g.addPlaceholder("Input");
    g.addPlaceholder("Label");

    // fully connected layers with ReLU
    g.addFullyConnected("FC_1", "Input", 28*28, 128);
    g.addRelu("Relu_1", "FC_1");
    g.addFullyConnected("FC_2", "Relu_1", 128, 64);
    g.addRelu("Relu_2", "FC_2");

    // fully connected layer with soft max
    g.addFullyConnected("FC_3", "Relu_2", 64, 10);
    g.addSoftmax("Softmax", "FC_3");

    // loss function
    g.addCrossEntropyLoss("Error", "Softmax", "Label");

    // load data here
    // run operations here

endfunction
```


## Training a `Graph` example

Manually train a neural network on a graph by repeatedly processing the following 4 steps:

1. Set input data to `Graph` placeholders.
2. Evaluate a forward pass on the `Graph`.
3. Back propagate through the `Graph` (to compute gradients).
4. Apply gradients to the weights calculated at the back propagation.

Steps 1-3 may be processed multiple times prior to processing step 4 (the gradients will accumulate).

In `etch`, these functions are taken care of by the more efficient `DataLoader` and `Optimiser` objects which we will see in a later section.




### 1. Set input

Add `Tensor` input or training data to a `Graph` with the `setInput()` function which takes a previously set placeholder string.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    var label_tensor = Tensor(tensor_shape);

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.addFullyConnected("fc1", "input", 1, 3);
    graph.addMeanSquareErrorLoss("error", "fc1", "label");

    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);   

endfunction
```

### 2. Evaluate

The `evaluate()` method performs a forward pass on the `Graph`, computing the output of all operations/layers as required and leading to the specified output node.

The return parameter is the `Tensor` computed at the output of the specified node.


``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    var label_tensor = Tensor(tensor_shape);

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.addFullyConnected("fc1", "input", 1, 3);
    graph.addMeanSquareErrorLoss("error", "fc1", "label");

    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);
    
    // perform a forward pass
    var loss = graph.evaluate("error");   

endfunction
```

### 3. Back propagate

Perform back propagation with the `backPropagate()` function. The function back propagates from the specified node through all ops leading to it.

Having already made a prediction via the forward pass through the `Graph`, `backPropagate()` computes the error gradient with respect to the weights in every node.


``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    var label_tensor = Tensor(tensor_shape);

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.addFullyConnected("fc1", "input", 1, 3);
    graph.addMeanSquareErrorLoss("error", "fc1", "label");

    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);
    
    // perform a forward pass
    var loss = graph.evaluate("error"); 

    // run back propagation
    graph.backPropagate("error");  

endfunction
```

### 4. Step

Run the `step()` function on a `Graph`  to generate the results. The function applies the SGD function to weights calculated by the previous training cycles.

The `Fixed64` parameter value the function takes is the learning rate.

``` c++
function main()

    var graph = Graph();

    var tensor_shape = Array<UInt64>(1);
    tensor_shape[0] = 3u64;
    var input_tensor = Tensor(tensor_shape);
    var label_tensor = Tensor(tensor_shape);

    graph.addPlaceholder("input");
    graph.addPlaceholder("label");
    graph.addFullyConnected("fc1", "input", 1, 3);
    graph.addMeanSquareErrorLoss("error", "fc1", "label");

    graph.setInput("input", input_tensor);
    graph.setInput("label", label_tensor);
    
    // perform a forward pass
    var loss = graph.evaluate("error"); 

    // run back propagation
    graph.backPropagate("error");  

    // call step
    graph.step(0.1fp64); 

endfunction
```

!!! Note
    `step()` will be deprecated in favour of `applyGradients()`.



<br/>



