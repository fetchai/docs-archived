# Developing smart contracts
We will discuss smart contracts in more details in one of the later tutorials, 
but before we dive into the examples, we will explore the Python API for the 
ledger and discuss the contract simulator tool `vm-lang`. We will be develop a
very simple `Hello world` contract and submit it to local ledger node to 
familiarize ourselves with the development process.

## Developing contracts with vm-lang
In this section we will develop a `Hello world` contract. When the contract
is submitted, the contract initialisation function 
engraves a name into the state database and then a single query function 
that provides the greeting sentence `Hello {name}!` where `{name}` is the name 
in the state database.

The contract itself is short and simple, providing the two above described functions:
```
@init
function createMessage()
  var name = "world";
  var state = State< String >("greetings");
  state.set(name);
endfunction

@query
function persistentGreeting() : String
  var state = State< String >("greetings");
  return "Hello, " + state.get() + "!";
endfunction
```
When developing a contract, it is often useful to use `vm-lang` for the development process. To this end, we also provide a `main` function that is invoked by `vm-lang`:
```
@testCase
function main()
  createMessage("world");
  var greeting = persistentGreeting();

  if(greeting != "Hello, world!")
    panic("Greeting differed from expected message.");
  endif

  printLn(greeting);
endfunction
```
You can test this contract by using the `vm-lang` executable. To test the script by running following from your 
build directory:
```
curl https://raw.githubusercontent.com/fetchai/etch-examples/master/01_submitting_contract/hello_world.etch --output hello_world.etch
./apps/vm-lang/vm-lang hello_world.etch
```
This produce an output similar to:
```
 F E ╱     vm-lang v0.4.1-rc3
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H

Hello, world!
```
We note that `vm-lang` executes `main` as the default function. When submitting the script to the ledger, we can leave `main` as it will not be accessible since it is not annotated as being invokable by the ledger code.

## Submitting the contract to the ledger
To submit the contract to the ledger, we use the Python API. The components needed are
```
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address
```
We first create an identity and corresponding address:
```
# Create keypair for the contract owner
entity = Entity()
address = Address(entity)
```
Next, we connect using the API and generate some wealth in order to be able to pay the fees for programming the ledger:
```
# Setting API up
api = LedgerApi('127.0.0.1', 8100)

# Need funds to deploy contract
api.sync(api.tokens.wealth(entity, 100000))
```
Finally, we submit the contract, paying 10000 gas units in fee:
```
# Create contract
contract = SmartContract(source)

# Deploy contract
api.sync(api.contracts.create(entity, contract, 10000))
```
After the contract has been successfully added, we can test it by using the query `persistentGreeting`:
```
# Printing message
print(contract.query(api, 'persistentGreeting'))    
```
This should produce a `Hello world!` message.