# Developing smart contracts

Let's develop a simple `Hello world` contract and submit it to a running local ledger node.

You can find the code for this tutorial <a href="https://github.com/fetchai/etch-examples" target=_blank>here</a>.

To run the code in this demo, you will need a running node. Details are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.

## Hello world with etch

Our demo smart contract has two functions.

The `@init` function etches the variable `name` onto the state database. 

Next, a `@query` function queries the state database for `name`.

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
Let's use the `etch` simulator for the development process. Details on setting up the `etch` simulator are <a href="../../etch-language/getstarted/" target=_blank>here</a>.

We need a `main` function that `etch` can invoke:

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

You can test this contract with the `etch` executable. Run the following from your 
build directory:

``` bash
curl https://raw.githubusercontent.com/fetchai/etch-examples/master/01_submitting_contract/hello_world.etch --output hello_world.etch
./apps/etch/etch hello_world.etch
```

This produces an output similar to:
```
 F E ╱     etch v0.4.1-rc3
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H

Hello, world!
```

`main` is the default runner function in `etch`. When submitting the smart contract to the ledger, we do not need the `main` function as it is inaccessible to the ledger code.


## Submitting the contract to the ledger

To submit the contract to the ledger, we use the Python API. 

Details for building and installing the Python API are <a href="../../getting-started/python-api-install/" target=_blank>here</a>.

The required imports are as follows:

``` python
from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address
```

Next, we embed the smart contract code into the Python script as a string:

``` python
CONTRACT_TEXT = """
@init
function setup(owner : Address)
  var owner_balance = State<UInt64>(owner, 0u64);
  owner_balance.set(1000000u64);
endfunction

@action
function transfer(from: Address, to: Address, amount: UInt64)

  // define the accounts
  var from_account = State<UInt64>(from, 0u64);
  var to_account = State<UInt64>(to, 0u64); // if new sets to 0u

  // Check if the sender has enough balance to proceed
  if (from_account.get() >= amount)
  
    // update the account balances
    from_account.set(from_account.get() - amount);
    to_account.set(to_account.get() + amount);
  endif

endfunction

@query
function balance(address: Address) : UInt64
    var account = State<UInt64>(address, 0u64);
    return account.get();
endfunction

"""
```

We first create an identity and corresponding address:
``` python
# Create keypair for the contract owner
entity = Entity()
address = Address(entity)
```

Next, we connect to the running node and generate some wealth in order to be able to pay the fees for programming to the ledger:

``` python
# Setting API up
api = LedgerApi('127.0.0.1', 8100)

# Need funds to deploy contract
api.sync(api.tokens.wealth(entity, 100000))
```

Finally, we create and submit the contract, paying 10000 gas units in fee:
``` python
# Create contract
contract = SmartContract(CONTRACT_TEXT)

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