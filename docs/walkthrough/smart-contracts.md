# Deploying and interacting with smart contracts

!!! note "What is a smart contract?"
    A Smart Contract is an agreement with the terms defined as a computer program. The contract exists on a decentralised network, and its execution and transactions can be tracked by anyone and are irreversible. All parties involved can be defined and enforced by the contract and no central authority is required for it to operate.


In this tutorial, we are going to deploy a simple "Hello world" smart contract developed in [Etch](/etch-language/) (the Fetch.ai smart contract language) and interact with it.

``` c++
@query
function sayHello() : String
  return "Hello world"
endfunction
```

This contract has only function annotated as a `@query`. Queries do not alter state, and they return a value to the caller. A contract can contain many of them.

Let's now deploy the contract, assuming it has been saved to a file `hello.etch`. This can be done using the Python Ledger API.

``` python
import sys
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# The contract we are going to load
contract_name = 'hello.etch'

# Connect the API to the testnet
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)

# Load the contract and perform some basic checks on it
try:
	contract_text = open(contract_name, 'r').read()
except IOError as e:
	sys.exit('File not found')

if 0 == len(contract_text):
	print ("Contract is zero length.")
	sys.exit("Invalid contract")

# Private key of the address to deploy from
# WARNING: Unencrypted private keys should not be present in production code
entity = Entity(b'... your private key here ...')
address = Address(entity)

print ("Deploying contract:", contract_name, '\n')
print ("  Owner:", address)
print (" Length:", len(contract_text), "byte(s)")

# Perform the deployment now
try:
	contract = Contract(contract_text, entity)
	gas_fee = 600000
	api.sync(contract.create(api, entity, gas_fee), None, 0)
except Exception as e:
	sys.exit(e);
	
# Deployed, so we can now announce address and owner
print ("\nContract deployed:\n")
print ("Address:", contract.address)
print ("  Owner:", contract.owner)

# Confirm by querying the contract
print (" Output:", contract.query(api, 'sayHello'))
```

If you run the above, having taken these two steps, it will deploy the contract to testnet for you. You'll see something like this:

``` bash
$ python3 deploy.py
Deploying contract: hello.etch

  Owner: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
 Length: 129 byte(s)

Contract deployed:

Address: 2VRHNEDBNfgind7NLmgcGbSvCqc4LX8bMt9Tw9gfyMyk5HXjFS
  Owner: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
 Output: Hello world
```

!!! note
    As with previous examples, everything you see above works on both mainnet and testnet — just change the `api = LedgerApi(network='testnet')` line accordingly.


## Interacting with an already deployed contract

There is a catch with the way we have deployed the contract. Once the program completes, we no longer have a way of interacting with the contract! We need to make some changes to our code to:

1. Serialise the contract as a JSON file when we do the initial deployment
2. Read a contract object from the serialised JSON file and then interact with that

So let's look at how we do this:

``` python
try:
	contract = Contract(contract_text, entity)
	gas_fee = 600000
	api.sync(contract.create(api, entity, gas_fee), None, 0)
	
	with open('hello_contract.json', 'w') as contract_info:
		contract.dump(contract_info)

except Exception as e:
	sys.exit(e);
```

You will see that we have added two extra lines that will save the contract as a JSON file. We can "reconstitute" the contract from this file to allow us to interact with it further. Here is a new Python script which you can save as `interact_with_existing.py`:

``` python
import sys
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# Connect the API to the testnet
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)

# Create a contract from our previously saved one
contract_name = 'hello_contract.json'
try:
	with open(contract_name, 'r') as contract_info:
		contract = Contract.load(contract_info)
except Exception as e:
	sys.exit(e)

# Private key of the address to deploy from
# WARNING: Unencrypted private keys should not be present in production code
entity = Entity(b'... your private key here ...')
address = Address(entity)

# Confirm by querying the contract
print ("Querying existing contract:", contract_name, '\n')
print ("Output:", contract.query(api, 'sayHello'))
```

And when run, the output should look like the following:

``` bash
$ python3 interact_with_existing.py

Querying existing contract: hello_contract.json
Output: Hello world
```
