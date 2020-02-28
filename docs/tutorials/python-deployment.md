# Deploying an Etch Contract with the Python Ledger API

The following tutorial assumes that you already have a `constellation` instance running on port `8000` and that you have installed the the Python API.

Details for running a node are <a href="/ledger/running-a-constellation/" target=_blank>here</a>.

Details of the Python API are <a href="/ledger/python-ledger-api/python-api-install/" target=_blank>here</a>.

## Requirements

We're going to keep this simple, and refer to FIP-1, our basic token generation contract. 

The FIP-1 contract implements the following functions:

-   `totalSupply() : UInt256` gets the total token supply.
-   `balanceOf(owner: Address): UInt256` gets the balance of an account having address `owner`.
-   `transfer(to: Address, value: UInt256) : Bool` sends `value` amount of tokens to address `to`.

## Deploying the contract:

We're going to create a new script, let's call it deploy.py

### Import 
Let's get the initial things out of the way, let's import:

```python 
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
from contextlib import contextmanager

```

### Connect to network
Then, connect to a local running node:

```python
api = None
if api is None:
    api = LedgerApi(host="127.0.0.1", port=8000)

```

### Setup accounts
Now, we'll read in our etch contract, and create a couple of entities to test with:

```python 

with open ('contract.txt', 'r') as ct:
    contract_text = ct.read()

print (contract_text)

# create our first private key pair
entity1 = Entity()
address1 = Address(entity1)

# create a second private key pair
entity2 = Entity()
address2 = Address(entity2)

```

### Create balance
To test, we need a balance: 
```python 
api.sync(api.tokens.wealth(entity1, 10000))
```
(Note this will functionality will be removed and a faucet will take it's place).


### Create the smart contract object

We create the contract object, and deploy it:
```python 
contract = Contract(contract_text, entity1)
api.sync(contract.create(api, entity1, 4000))
```


### Query the contract
The named argument has to be the exact name of the variable we're accessing in balanceOf
for example, if the state had a named var of "userX" the below code would be:
`print (contract.query(api, 'balanceOf', userX=address1))`
this is an important note for other functions you might create.

```python 
print (contract.query(api, 'totalSupply'))
print (contract.query(api, 'balanceOf', address=address1))
```

### Make a transaction

Using the two entities we created earlier, and their addressed we transact 200 from entity1 to entity2, then check the balance:

```python 
# transfer from one to the other using our newly deployed contract
tok_transfer_amount = 200
fet_tx_fee = 160
api.sync(contract.action(api, 'transfer', fet_tx_fee, [entity1], address1, address2, tok_transfer_amount))


#Query new balance: 
print (contract.query(api, 'balanceOf', address=address1))
```


You can find the source <a href="https://github.com/fetchai/etch-examples/blob/master/Fet-1/submit_contract.py" target=_blank>here</a>.

<br/>
