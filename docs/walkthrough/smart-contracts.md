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


## Interacting with an already deployed contract

So, obviously, there is a catch with what we've done. Once the program completes, we no longer have a way of interacting with the contract that we've deployed, so we can't send _more_ tokens to _someone else_ at a later date. Well, actually, we can! And we do it as a two-step process:

1. We serialise out the contract that we create as a JSON file when we do the initial deployment
2. We read a contract object from the serialised JSON file and then interact with that

So let's look at how we do this:

``` python
try:
	contract = Contract(contract_text, entity)
	api.sync(contract.create(api, entity, 600000), None, 0)
	
	with open('contract_data.json', 'w') as contract_info:
		contract.dump(contract_info)

except Exception as e:
	sys.exit(e);
```

This replaces the code which does the contract create at the moment. You'll see that now, we've added two extra lines that will save the contract as a JSON file. We can _reconstitute_ the contract from this file to allow us to interact with it further. Here is a new Python script which you can save as `interact_with_existing.py`:

``` python
import sys
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# this gets us an API connected to the testnet endpoint:
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)

# create a contract from our previously saved one:
try:
	with open('contract_data.json', 'r') as contract_info:
		contract = Contract.load(contract_info)
except Exception as e:
	sys.exit(e)

# us as owner, with private key:	
entity = Entity(b'4\x1f\x00\xf7\x89\x00c\xee\xfd5h\xf2\xf5\xc7\xc3\x10\x80/\xd3+:\x15\xa1\x11\xac\x0f\xbf\xb4\xa6\\\xe0{')
address = Address(entity)

# let's show stats, and then send some more tokens:
print ('\nCurrent token status:\n')
print (" Total supply:", contract.query(api, 'totalSupply'))
print ("Owner balance:", contract.query(api, 'balanceOf', address=address))
print ("Declared name:", contract.query(api, 'getName'))

# Now send someone some tokens:
target_for_tokens = Address('2pMdjmCczv3n1cF7kWSLV4cBSgXt6VmiudzhxGFNnNPJwBUAv9')
print ('\nAttempting to transfer 100 tokens to ', target_for_tokens)
try:
	tx_hash = contract.action(api, 'transfer', 60000, [entity], address, target_for_tokens, 100)
	api.sync(tx_hash)
except Exception as e:
	sys.exit(e);

print ('\nTransfer of tokens complete:\n')
print ('          TX hash:', tx_hash)
print (' Owner balance:', contract.query(api, 'balanceOf', address=address))
print ('Target balance:', contract.query(api, 'balanceOf', address=target_for_tokens))
```

And when run, we now load the previously deployed contract and transfer an additional 100 tokens to the same address as we did in the creation script:

``` bash
$ python3 interact_with_existing.py

Current token status:

 Total supply: 100000
Owner balance: 99900
Declared name: Fet-1 Fungible token

Attempting to transfer 100 tokens to  2pMdjmCczv3n1cF7kWSLV4cBSgXt6VmiudzhxGFNnNPJwBUAv9

Transfer of tokens complete:

          TX hash: f5b2277cf779b6b5a91b48c790f889a0e2599d3b6559933f823f13d227e46fa2
 Owner balance: 99800
Target balance: 200
$
```

Now this is all a "bit manual” at this stage. We don't have command line parameters for interacting sensibly, we have to edit files all the time, and we're storing the private key in the file, but we do have *all the components* in this tutorial to 1) create a contract, 2) interact with it, 3) save it for later interactions and 4) load it for subsequent interactions.

It's pretty straightforward to deploy a token contract using this tutorial, and we recommend that you do. If you mention your token details in the developer Slack, you may find an interest in collecting them for testing purposes!

As with previous examples, everything you see above will work on both main net and testnet — just change the `api = LedgerApi(network='testnet')` line accordingly.

