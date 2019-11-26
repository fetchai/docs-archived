#Quickstart!
Fetch.ai is a platform for decentralised autonomous agents to work, it's a platform that enables machine learning from the consensus design through to applications in Etch. 

This quickstart quide is to get you moving as quickly as possible. Let's get started, anything we miss will be highlighted for you to deep dive on later.

###Running a node locally:

This is a great way to test Etch code locally and view what a node is doing; you can connect to the testnet or just run as a single node. 

Let's do that. You're going to need to clone the fetch.ai ledger repo:
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

###Building and running the ledger:
Now let's build the project: 

```bash
./scripts/quickstart.sh
```

we can now run the leder locally: 
```bash
./build/apps/constellation/constellation -standalone -block-interval 20000
```

The node is running, it's not connected to the network and a block interval of 2 seconds. 

For more detailed instructions, including helpful tips if you're running into errors head here. 


##Install the Python Ledger API

If you want to develop Smart Contracts and deploy them, or create apps to connect directly to the ledger, the Python Ledger API is currently one of two ways to do so. 

You can see the source <a href="https://github.com/fetchai/ledger-api-py">here</a>, or just install with pip:
```bash
pip install fetchai-ledger-api
```
Keep close attention to build versions, if your ledger is at latest, grab latest, else, stick with a latest labeled version.

With this installed, get started quickly with: 

```python

from fetchai.ledger.crypto import Address, Entity
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import Contract

api = None
if api is None:
    api = LedgerApi(host="127.0.0.1", port=8100)

agent1 = Entity()
api.sync(api.tokens.wealth(agent1, 200000000))
```

With this, you've got test tokens and you're connected to the ledger. 

You can get public, and private key of the agent by:

```python
str(Address(agent1))
agent1.private_key
```

##Deploying a contract

Let's create another Python Script for this.

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
    api = LedgerApi(host="127.0.0.1", port=8100)

agent1 = Entity()
api.sync(api.tokens.wealth(agent1, 200000000))

# create the smart contract
contract = Contract(CONTRACT_TEXT, agent1)
fee = 4000
api.sync(contract.create(api, entity1, fee))

#Query the contract
contract.query(api, 'sayHello')

```

This is intentionally very simple; to see a full example go <a href="https://github.com/fetchai/ledger-api-py/blob/master/examples/contracts.py">here</a>. If you'd like to see much more, such as <a href="http://etch-docs.fetch.ai/smart-contracts/executing-synergetic-code/">experimental features</a> or <a href="http://etch-docs.fetch.ai/tutorials/fet2/">non-fungible generation contract example</a> click those links, or check out our <a href="/tutorial/">tutorials</a>.

We also have <a href="https://build.fetch.ai/">Etch playground</a>, while not the best way to develop contracts it's a great way to <a href="https://build.fetch.ai/">learn Etch.</a>


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


##Agents

...

##Next steps
