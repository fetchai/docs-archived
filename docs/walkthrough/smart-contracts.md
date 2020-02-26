# Deploying and interacting with smart contracts

In this tutorial, you'll understand how to deploy a contract and interact with it. You'll be able to see it on the block explorer and view its source. We'll go through this before falling back to talking about encryption and private key management.

!!! note "What is a smart contract?"
    A Smart Contract is an agreement with the terms defined as a computer program. The contract exists on a decentralised network, and its execution and transactions can be tracked by anyone and are irreversible. All parties involved can be defined and enforced by the contract and no central authority is required for it to operate.

In practice, most people's interaction with a smart contract is through those that handle the issuance of tokens, such as the well known Ethereum [ERC20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md). Most token contracts are either:

- Non-fungible tokens (NFT): These are like collectables, as they cannot be split; you can't cut a baseball collector's card and have two that are worth 50% of the original. One of the most well-known of these is [Cryptokitties](https://www.cryptokitties.co/). Most non-fungible tokens are [ERC721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md).
- Fungible tokens (FT): Fungible can be split, and are used for most token issuance. The circulating supply, the issuance foundation and the list of where the tokens are are held and enforced by a smart contract. Most fungible tokens on Ethereum, including non-native FET tokens, are based on [ERC20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md).

## A simple token contract

In today's tutorial, we are going to deploy a simple fungible token contract and make some calls to it. We will then transfer some of our new tokens to some owners.

First things first, let's look at the Etch code for a simple fungible token:

```
//------------------------------------------------------------------------------
//
//   Copyright 2019 Fetch.AI Limited
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
//------------------------------------------------------------------------------

persistent sharded balance_state : UInt64;
persistent supply_state : UInt64;

@init
function init(owner: Address)

    use supply_state;
    use balance_state[owner];

    supply_state.set(100000u64);
    balance_state.set(owner, 100000u64);

endfunction

@query
function getName(): String

	return ("Fet-1 Fungible token");
	
endfunction


@query
function totalSupply(): UInt64

    use supply_state;
    return supply_state.get();

endfunction


@query
function balanceOf(address: Address) : UInt64
    
    use balance_state[address];
    return balance_state.get(address, 0u64);

endfunction

@action
function transfer(from: Address, to: Address, value: UInt64) : Int64

    if(!from.signedTx())
      return 1i64;
    endif

    use balance_state[from, to];
    var from_balance = balance_state.get(from, 0u64);
    var to_balance = balance_state.get(to, 0u64);

    if(from_balance < value)
      return 2i64;
    endif

    var u_from = from_balance - value;
    var u_to = to_balance + value;

    balance_state.set(from, u_from);
    balance_state.set(to, u_to);
    return 0i64;

endfunction
```
This is a relatively straightforward, simplified token. It has several functions that support its operation. They fall into three categories:

1. *Initialisation* (labeled with `@init`). There is one of these, and it is called when the token contract is deployed.
2. *Queries* (labeled with `@query`). There can be many of these. They do not alter state, and they return a value to the caller. In this contract, they are used to return total supply, contract name and get the balance of an address.
3. *Actions* (labeled with `@action`). There can be many of these. They perform actions, can alter state and return a value. Our contract has one of them (`transfer`), and it is for transferring tokens from one address to another. The source of the transfer has to be the caller of the `@action`

You can find the documentation on Etch at https://docs.fetch.ai/etch-language/

## Deploying and interacting with a contract

Let's now deploy our contract. Here's some Python, which we'll break down afterwards:
```
import sys
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# The contract we're going to load:
contract_name = 'Fet1.etch'

# this gets us an API connected to the testnet endpoint:
try:
	api = LedgerApi(network=“testnet")
except Exception as e:
	sys.exit(e)

# load the contract and perform some basic checks on it:
try:
	contract_text = open(contract_name, 'r').read()
except IOError as e:
	sys.exit('File not found')

if 0 == len(contract_text):
	print ("Contract is zero length.")
	sys.exit("Invalid contract")
	
# some simple stats, a bit messy, as the Python API does have this information
# but it isn't yet exposed (January 28th 2020). Future versions will expose actions
# and queries, so non-optimal parsers like the below will absolutely not be 
# necessary!
lines = 0
queries = 0
actions = 0
for line in contract_text.splitlines():
	lines = lines + 1	
	line = line.strip()
	if "@query" == line:
		queries = queries + 1
	elif "@action" == line:
		actions = actions + 1

# private key for deploying from 
# *WARNING* putting an unencrypted private key in a script
# is a terrible idea! Future tutorials will deal with this.
entity = Entity(b'… your private key here …')
address = Address(entity)

# perform the deployment now:
print ("Deploying contract:", contract_name, '\n')
print ("  Owner:", address)
print (" Length:", len(contract_text), "byte(s)")
print ("  Lines:", lines)
print ("Queries:", queries)
print ("Actions:", actions)

try:
	contract = Contract(contract_text, entity)
	api.sync(contract.create(api, entity, 600000), None, 0)
except Exception as e:
	sys.exit(e);
	
# deployed. Announce address and owner:
print ('\nContract deployed:\n')
print ('Address:', contract.address)
print ('  Owner:', contract.owner)

# perform a couple of confirmation queries:
print ('\nFet-1 test calls:\n')
print (" Total supply:", contract.query(api, 'totalSupply'))
print ("Owner balance:", contract.query(api, 'balanceOf', address=address))
print ("Declared name:", contract.query(api, 'getName'))
```
This assumes that you have saved the fungible token as `Fet1.etch`, and that you have added a private key where noted. If you then run the above, having taken these two steps, it will deploy the contract to testnet for you. You'll see something like this:
```
$ python3 deploy.py
Deploying contract: Fet1.etch 

  Owner: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
 Length: 1978 byte(s)
  Lines: 81
Queries: 3
Actions: 1

Contract deployed:

Address: 2VRHNEDBNfgind7NLmgcGbSvCqc4LX8bMt9Tw9gfyMyk5HXjFS
  Owner: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5

Fet-1 test calls:

 Total supply: 100000
Owner balance: 100000
Declared name: Fet-1 Fungible token
$
```
So let's look at some of the key things. You'll recognise much of the code from the examples in [Part 1](LINK), but here's the magic bit that actually deploys the contract to the Fetch ledger:
```
try:
	contract = Contract(contract_text, entity)
	api.sync(contract.create(api, entity, 600000), None, 0)
except Exception as e:
	sys.exit(e);
```
The 600000 value is the gas fee for deployment. It's in 10,000,000's of a FET (canonical FET). The exception handler ensures that you see the error neatly if there are deployment issues.

After we've deployed, we're able to get information about the contract out, such as its address. We use `contract.address` to recall the address on the ledger. This also ensures that we can easily interact with it in the future (although you can track this stuff down on the block explorer!)

We then call all three of the `@query`s in the contract:
```
print (" Total supply:", contract.query(api, 'totalSupply'))
print ("Owner balance:", contract.query(api, 'balanceOf', address=address))
print ("Declared name:", contract.query(api, 'getName'))
```
Note that we're getting the balance of the contract's owner, which will be _all the tokens_, at this stage. If all has worked, you'll see the total supply and balance as the same values. We then call the `@action` to send some tokens to another address:
```
# Now send someone some tokens:
target_for_tokens = Address('2pMdjmCczv3n1cF7kWSLV4cBSgXt6VmiudzhxGFNnNPJwBUAv9')
print ('\nAttempting to transfer 100 tokens to ', target_for_tokens)
try:
	tx_hash = contract.action(api, 'transfer', 60000, [entity], address, target_for_tokens, 100)
	api.sync(tx_hash)
except Exception as e:
	sys.exit(e);

print ('\nTransfer of tokens complete:\n')
print ('       TX hash:', tx_hash)
print (' Owner balance:', contract.query(api, 'balanceOf', address=address))
print ('Target balance:', contract.query(api, 'balanceOf', address=target_for_tokens))
```
So let's unpack what's going on here. Firstly, we're declaring an address that we're going to be sending some tokens to. Then we use `contract.action` to create the transaction to perform the action. The return from this is the *transaction hash*. You can add a `0x` to the front of this and look it up in the appropriate block explorer to see details (https://explore.fetch.ai for mainnet and https://explore-testnet.fetch.ai for testnet). We then use `api.sync` with this transaction hash so that we can wait for it to complete, and therefore show any errors that might occur. Assuming all is good, then we'll show the transaction's hash and then the owner and target balance after the operation. In the above case, we see this:
```
Attempting to transfer 100 tokens to  2pMdjmCczv3n1cF7kWSLV4cBSgXt6VmiudzhxGFNnNPJwBUAv9

Transfer of tokens complete:

       TX hash: 81527b814fe50a1f9c00220813fe2e04570792401e529682a0453a086849a8e3
 Owner balance: 99900
Target balance: 100
$ 
```
Neat, eh? 

## Interacting with an already deployed contract

So, obviously, there is a catch with what we've done. Once the program completes, we no longer have a way of interacting with the contract that we've deployed, so we can't send _more_ tokens to _someone else_ at a later date. Well, actually, we can! And we do it as a two-step process:

1. We serialise out the contract that we create as a JSON file when we do the initial deployment
2. We read a contract object from the serialised JSON file and then interact with that

So let's look at how we do this:
```
try:
	contract = Contract(contract_text, entity)
	api.sync(contract.create(api, entity, 600000), None, 0)
	
	with open('contract_data.json', 'w') as contract_info:
		contract.dump(contract_info)

except Exception as e:
	sys.exit(e);
```
This replaces the code which does the contract create at the moment. You'll see that now, we've added two extra lines that will save the contract as a JSON file. We can _reconstitute_ the contract from this file to allow us to interact with it further. Here is a new Python script which you can save as `interact_with_existing.py`:
```
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
```
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
Now this is all a “bit manual” at this stage. We don't have command line parameters for interacting sensibly, we have to edit files all the time, and we're storing the private key in the file, but we do have *all the components* in this tutorial to 1) create a contract, 2) interact with it, 3) save it for later interactions and 4) load it for subsequent interactions.

It's pretty straightforward to deploy a token contract using this tutorial, and we recommend that you do. If you mention your token details in the developer Slack, you may find an interest in collecting them for testing purposes!

As with previous examples, everything you see above will work on both main net and testnet — just change the `api = LedgerApi(network='testnet')` line accordingly.

