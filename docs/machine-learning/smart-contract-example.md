
# AI in Smart Contracts

<a href="../getting-started/quickstart#training-a-neural-network" target=_blank>The quickstart example</a> demonstrates how to train and execute neural networks in the Etch language locally. This example focuses on reworking that example as a smart contract that can be executed entirely on-chain.

``` c++
// initial set up creates the model and persistent data
@init
function setup(owner : Address)
  use model_state;
  var model = model_state.get(Model("sequential"));
  model.add("dense", 13u64, 10u64, "relu");
  model.add("dense", 10u64, 10u64, "relu");
  model.add("dense", 10u64, 1u64);
  model.compile("mse", "adam");
  model_state.set(model);
endfunction

// pass in some data, train the model with it, save the updated model to state
@action
function train(data: Tensor, label: Tensor)
  use model_state;
  var model = model_state.get();

  var batch_size = 10u64;
  model.fit(data, label, batch_size);
  model_state.set(model);
endfunction

// get the current training loss of the model
@query
function evaluate() : Tensor
  use model_state;
  var model = model_state.get();
  var loss = model.evaluate();
  return loss;
endfunction

// make a prediction with the model based on input data passed to function
@query
function predict(data: Tensor) : Tensor
  use model_state;
  var model = model_state.get();
  var prediction = model.predict(data);
  return prediction;
endfunction

```

Above is a simple smart contract for setting up the same neural network as before to make predictions on the boston housing data set.
The main differences from the previous etch example are:

1. persistent storage
2. seperately callable functions
3. function decorators

### Persistent storage

The ledger maintains a state database for smart contracts to store objects. In this example we indicate our intention to access the model in the state database with `use model_state`, we store our model in the state database using `set()`, and we recover it for use with `get()`. It's important to consider carefully what make sense to store in the state database, and what should be managed locally.

A full explanation of persistent storage is given <a href="../etch-language/persistent-globals" target=_blank>here</a>.

### Separately callable functions

In this example the `train`, `evaluate`, and `predict` functions are all separately callable. This allows users to contribute to training the model, or utilise the model for prediction independently.

### Function decorators

Finally, this example utilises the function decorators `@init`, `@action`, and `@query`. `@init` specifies the function to execute when the contract is first registered, this ensures that the model is created upon construction. After this subsequent `@action` and `@query` functions may be invoked, the former of which are permitted to read and write to the state database, whereas the latter may only read from it; this is useful because it allows model predictions to be made 'between blocks', whereas training and updating the model would need to be written to the state database and would hence occur only when each new block is added.

## Advanced customisation

With these new tools we can rewrite this smart contract to be more efficient, depending on what we wish to accomplish. For example, if we expect various agents to occassionally provide new data, but we want to train the model asynchronously with these data dumps, we might want to store that data in a state, and define a separate function for training the model that reads the previously stored data from state; e.g.

``` c++
// set input data
@action
function setData(in_data: String)
  use data_state;
  var data = data_state.get();
  data.fromString(in_data);
endfunction

// set label
@action
function setLabel(in_label: String)
  use label_state;
  var label = label_state.get();
  label.fromString(in_label);
endfunction

// load data and label from state and train the model with it
@action
function train()
  use model_state;
  use data_state;
  use label_state;

  var model = model_state.get();
  var data = data_state.get();
  var label = label_state.get();

  var batch_size = 10u64;
  model.fit(data, label, batch_size);
  model_state.set(model);
endfunction
```

Similarly, it may be too expensive to train the model on-chain, and we may instead wish to simply over-write the model with one we have trained off-chain. This is also easily accomplishable:

``` c++
// set input data
@action
function setModel(in_model: String)
  use model_state;
  var model = model_state.get();
  model = model.deserializeFromString(in_model);
  model_state.set(model);
endfunction
```

To take this idea further, we may wish to perform most of the expensive work off-chain but automate/manage it on-chain. This would be an ideal application for a <a href="../machine-learning/synergetic-contract-example" target=_blank>synergetic contract</a>.

<br />
