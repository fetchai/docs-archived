# Developing smart contracts

Let's develop a simple `Hello world` contract and submit it to a running local ledger node.

## Hello world with vm-lang

Our demo smart contract has two functions.

The initialisation function etches a `{name}` onto the state database. Then, a query function allows us to query the state database for the `{name}`.

``` python
@init
function createMessage(owner : Address)
  var name : String = "world";
  var state = State< String >("greetings");
  state.set(name);
endfunction

@query
function persistentGreeting() : String
  var state = State< String >("greetings");
  return "Hello, " + state.get() + "!";
endfunction
```
Let's use the `vm-lang` simulator for the development process. 

We need a `main` function that `vm-lang` can invoke:

``` python
@testCase
function main()
  var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
  createMessage(account);
  var greeting = persistentGreeting();

  if(greeting != "Hello, world!")
    panic("Greeting differed from expected message.");
  endif

  printLn(greeting);
endfunction
```

You can test this contract with the `vm-lang` executable. Run the following from your 
build directory:

``` bash
curl https://raw.githubusercontent.com/fetchai/etch-examples/master/01_submitting_contract/hello_world.etch --output hello_world.etch
./apps/vm-lang/vm-lang hello_world.etch
```

This produces an output similar to:
```
 F E ╱     vm-lang v0.4.1-rc3
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H

Hello, world!
```

`vm-lang` executes `main` as the default runner function. When submitting the smart contract to the ledger, we do not need the `main` function as it is inaccessible to the ledger code.


## Submitting the contract to the ledger

To submit the contract to the ledger, we use the Python API. The required imports are as follows:

``` python
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address
```

We first create an identity and corresponding address:
``` python
# Create keypair for the contract owner
entity = Entity()
address = Address(entity)
```

Next, we connect using the API and generate some wealth in order to be able to pay the fees for programming to the ledger:

``` python
# Setting API up
api = LedgerApi('127.0.0.1', 8100)

# Need funds to deploy contract
api.sync(api.tokens.wealth(entity, 100000))
```

Finally, we submit the contract, paying 10000 gas units in fee:
``` python
# Create contract
contract = SmartContract(source)

# Deploy contract
api.sync(api.contracts.create(entity, contract, 10000))
```
After submitting the contract successfully, we can test it with the query function `persistentGreeting`:
``` python
# Printing message
print(contract.query(api, 'persistentGreeting'))    
```
This should produce a `Hello world!` message.

<br/>