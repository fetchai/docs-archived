# Quickstart!

Fetch.ai is a decentralised platform where autonomous agents can collaborate, enabling machine learning from the consensus design through to applications in Etch.

This quickstart quide aims to get you moving as quickly as possible, and it will point you at sections where you can learn more. Let's get started!


## Running a node locally

This is a great way to test locally smart contracts developed in our native language (called [Etch](../etch-language/index.md), and to debug what a node is doing. You can connect to the testnet or just run as a single node. 

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


## Installing the Python Ledger API

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

## Deploying a contract

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


## Machine learning on Fetch.ai

...


## Agents



## Next steps

