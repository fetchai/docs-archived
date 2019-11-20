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
    api = LedgerApi(host="127.0.0.1", port=8100)

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
    api = LedgerApi(host="127.0.0.1", port=8100)

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


## Machine learning on Fetch.ai

...


## Agents



## Next steps

