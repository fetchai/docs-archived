# Quickstart!

Fetch.ai is a decentralised platform where autonomous agents can collaborate, using machine learning supported at all levels, from the consensus design to the smart contracts language [Etch](../etch-language/index.md).

This quickstart quide aims to get you moving as quickly as possible, and it will point you at sections where you can learn more. Let's get started!


## Running a node locally

This is a great way to test locally smart contracts developed in the Fetch.ai native language (called [Etch](../etch-language/index.md), and to debug a node's behaviour. You can connect to the testnet or just run as a single node. 

You'll first need to clone the [Fetch.ai ledger repo](https://github.com/fetchai/ledger):

``` bash
cd [working_directory]
git clone https://github.com/fetchai/ledger.git
git checkout release/v0.9.x
```

Update and initialise submodules from the repository root directory:

``` bash
cd ledger
git pull
git submodule update --init --recursive
```

Now let's build the project: 

```bash
./scripts/quickstart.sh
```

And we can now run the ledger locally:

```bash
./build/apps/constellation/constellation -standalone -block-interval 20000
```

This runs a node with a block interval of 2 seconds. Since it is a standalone node, it is not connected to any network. 

For more detailed instructions on how to run a node, please check the following:

* [Running a standalone node or connected to a network](run-a-node.md)
* [`constellation` flags](../ledger/running-a-constellation.md)


## Connecting to the node

If you want to create apps that connect directly to the ledger, or to deploy smart contracts, you can use the Python and Javascript Ledger APIs. In this quickstart guide we will focus on the Python API.

We recommend you install the latest stable version using pip:

```bash
pip install fetchai-ledger-api
```

You can also obtain the latest version of the code from the [GitHub repository](https://github.com/fetchai/ledger-api-py).

Once the API is installed, you need to establish a connection via a new `LedgerApi` object, after which you can generate test tokens for an agent: 

```python

from fetchai.ledger.crypto import Address, Entity
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract

api = None
if api is None:
    api = LedgerApi(host="127.0.0.1", port=8000)

agent1 = Entity()
api.sync(api.tokens.wealth(agent1, 200000000))
```

You can get the public and private keys of the agent with the following:

```python
str(Address(agent1))
agent1.private_key
```


## Deploying a smart contract

In order to deploy the simplest contract, we will elaborate on the previous snippet based on the Python Ledger API:

```python

from fetchai.ledger.crypto import Address, Entity
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract

CONTRACT_TEXT = """
@query
function sayHello() : String
  return "Hello"
endfunction
"""

api = None
if api is None:
    api = LedgerApi(host="127.0.0.1", port=8000)

agent1 = Entity()
api.sync(api.tokens.wealth(agent1, 200000000))

# Create the smart contract
contract = Contract(CONTRACT_TEXT, agent1)
fee = 4000
api.sync(contract.create(api, agent1, fee))

# Query the contract
contract.query(api, 'sayHello')
```

You can check the following for more interesting smart contract examples:

* [Full smart contract example](https://github.com/fetchai/ledger-api-py/blob/master/examples/contracts.py)
* [Synergetic contracts](../smart-contracts/executing-synergetic-code.md), one of our experimental features
* [Non-fungible generation contract example](../tutorials/fet2.md)

We also have an [Etch playground](https://build.fetch.ai) that you can use to learn the Etch language. Please note that we don't recommend it as the environment to develop contracts.


## Using the machine learning library

Let's look at an example of how to use the Fetch.ai machine learning library to train a neural network in a standalone applicatoin. This example will predict house prices for the Boston Housing Dataset, which can be downloaded from [here](http://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html).

The implementation is based on the [Etch language](/etch-language), which is also used to write smart contracts on the Fetch.ai ledger; you saw a very brief example in the previous section. Instructions to set up an Etch development environment can be found [here](/etch-language/getstarted/).

### Loading input data

An Etch program needs a `main()` function as its entry point, and that is where all code in this example will reside.

Since the input is provided via multiple CSV files, the `main()` function firstly has to check the correct number of files is provided, then load the input data from them:

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

* Type: `dense` in this example refers to a fully-connected layer where every neuron in the layer is connected to every input and every output.
* Input size: must match the data for the first layer
* Neurons in layer / output size: must match the label size for the final layer
* Activation type (optional): here we use a rectified linear unit for the first two layers, and no activation for the final layer

Finally, we compile the model using the `mse` (mean squared error) loss function, and the `adam` optimiser.

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


## Agents

Coming soon.


## Next steps

Coming soon.
