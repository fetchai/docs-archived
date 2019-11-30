# AI in Synergetic Contracts

<a href="/machine-learning/smart-contract-example" target=_blank>The previous example</a> demonstrated how to train and execute neural networks in a smart contract. That's useful if you want to set up fully on-chain machine learning, but it also allows you to perform the compute intensive parts of the work off-chain and then load the model directly into smart contract state and use it to make predictions on-chain (trading off a certain amount of model transparency for efficiency/cost).

In this example we'll take this even further with a synergetic contract; this allows off-chain components of work to be specified in the contract. This could be extremely valuable if, for example, you wanted to set up a competition or auction in a contract where miners could take part to do expensive work training a machine learning model in exchange for a chance at winning the rewrad. Then the resulting best model could be uploaded onto the ledger for all to use.

## Simple Synergetic Contract

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>This developer documentation is a work in progress. If you spot any errors please open an issue [here](https://github.com/fetchai/docs).</p>
</div>

``` c++
// set up a problem around training a machine learning model
@problem
function createProblem(data: Tensor, label: Tensor)

  use model_state;
  use data_state;
  use label_state;

  var model = model_state.get(Model("sequential"));
  model.add("dense", 13u64, 10u64, "relu");
  model.add("dense", 10u64, 10u64, "relu");
  model.add("dense", 10u64, 1u64);
  model.compile("mse", "adam");
  model_state.set(model);
endfunction

// evaluates performance as the loss function of the model after training
@objective
function evaluateWork(in_model: String)
  use model_state;
  var model = model_state.get();
  model.fromString(in_model);
  return model.evaluate();
endfunction

// the work of training the model
@objective
function doWork(in_model : String, nonce : UInt256) :  String
  use model_state;
  use data_state;
  use label_state;

  var model = model_state.get();
  model.fromString(in_model);

  // update the learning rate of the local model
  var lr = nonce.toFloat64() % 1.0fp64;
  model.setLearningRate(lr);

  // train the model
  var batch_size = 10u64;
  var data = data_state.get();
  var label = label_state.get();
  model.fit(data, label, batch_size);

  // return the serialised model
  return model.toString();
endfunction

// set the new model to be the specified winner
@clear
function applyWork(in_model: String)
  use model_state;
  var model = model_state.get();
  model.fromString(in_model);
  model_state.set(model);
endfunction

// make a prediction with the model based on input data passed to function
@query
function predict(data: Tensor) : Tensor
  use model_state;
  var model = model_state.get();
  var prediction = model.predict(data);
  return prediction;
endfunction

// query the current model performance
@query
function evaluate() : Tensor
  use model_state;
  var model = model_state.get();
  return model.evaluate();
endfunction

```

A common machine learning task that requires parallelisation is the hyper-parameter search phase. Engineers will perform this when they understand the general architecture/approach that they want to take to produce a machine laerning model, but they don't know the best combination of hyper-parameters (such as learning rate, regularisation settings, dropout rates, etc.). Often the best solution is to simple try out many different combinations of parameters and find out what seems to have worked well; this is called hyper-parameter search.

Above is a trivial example of a synergetic contract for setting up a competition where multiple miners can take part in hyper-parameter search in order to receive rewards for their work. Here we attempt to train the same boston housing regression neural network as in the prior examples but with one key difference: each miner that wishes to take part invokes `doWork` which has the result of using a unique nonce for determining the learning rate at which they train the model.

In a serious implementation we would likely have many hyperparameters to search over and sensible ranges and resolutions for each hyper-parameter. We might also add further sophistication such as building into the contract an algorithm for guiding a random walk through hyper-parameter space across miners. Hopefully, however, this example serves to illustrate what is possible on the fetch ledger with synergetic contracts.

To learn more about synergetic contracts take a look at <a href="/smart-contracts/synergetic" target=_blank>this further documentation</a>.
