<h1>Etch smart contracts</h1>

!!! quote

    A smart contract is a computer protocol intended to digitally facilitate, verify, or enforce the negotiation or performance of a contract. Smart contracts allow the performance of credible transactions without third parties. These transactions are trackable and irreversible. Source: <a href="https://en.wikipedia.org/wiki/Smart_contract" target=_blank>Wikipedia</a>.

Smart contract code runs on the `etch` virtual machine. 

All ledger nodes maintain the `etch` VM and smart contract code.

The identity  of a smart contract is calculated by performing a `SHA256` hash on the contract code string as an initial step. Next, a further `SHA256` hash is calculated from the previous result concatenated with a public key `Address` which represents the contract owner.

On the ledger, the `etch` VM stores the contract identity, the contract source code, and the data resources that are mapped by a `data.json` file.

With this information, the `etch` VM performs a modulo 16 calculation to decide where to store the data on the ledger, i.e. onto which shard.

!!! note
	Coming soon: details on how developers may dictate the sharding storage design for a smart contract.



## Smart contract structure

Smart contract functions are annotated depending on the activity they perform.

<H3>@init</H3>	

The `@init` function defines a contract constructor that sets the state of the contract prior to any operations performed on it. It is called once and once only on contract initialisation/deployment.

The name of the `@init` function can be anything you like.

For example, the following function initialises a contract by creating a `State` type to represent the owner's account which then receives an initial supply of FET tokens. 

This happens once and once only at contract deployment.


``` c++
@init
function initialise(owner: Address)

    var INITIAL_SUPPLY = 100000000000u64;
    var account = State<UInt64>("owner");
    account.set(INITIAL_SUPPLY);

endfunction

function main()

	var owner = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
	initialise(owner);

endfunction
```


<H3>@action</H3>

The `@action` annotation signifies a function which performs a transaction. 

You cannot create a smart contract in `etch` without an `@action` function and it is these functions that trigger the charging rules for data persistence fees.

The following function performs a transaction between two parties.

``` c++
@action
function transfer(from: Address, to: Address, amount: UInt64)
    
    var from_balance = State<UInt64>(from); 
    from_balance.set(1000u64);
    var to_balance = State<UInt64>(to);
    to_balance.set(0u64);

    // check if all the conditions are valid
    if (from_balance.get() <= amount)
    	panic("Argh!");
    endif

    from_balance.set(from_balance.get() - amount);
    to_balance.set(to_balance.get() + amount);
    
endfunction

function main()

	var owner = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
	var user = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
	transfer(owner, user, 100u64);

endfunction
```

In the worst case, the above function needs two shards for data storage.


<h3>@query</h3>

Query functions are read-only functions that allow you to view data residing on the ledger. 

The following function queries the balance of an `Address`.

``` c++
@query
function balance(address : Address) : UInt64

    var account = State<UInt64>(address);
    account.set(100u64);
    return account.get();

endfunction

function main()
	
	var owner = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
	var owner_balance = balance(owner);
	printLn(owner_balance);

endfunction
```


## Smart contract addresses

`etch` smart contracts have a unique identification protocol for addressing on the Fetch Ledger.

`etch` smart contract identifiers are a SHA256 hash of the contract source code which is then Base64 encoded and finally concatenated with the Base64 encoded owner's public key.

Using this identifier, smart contract functions are accessible with a subsequent `.` plus function name.



## Data confirmation

If you run an `etch` contract in the simulator containing one or more `State` types and flag the compiler with `-data` and a filename, it will create a `json` file containing the details of the data that will be stored on the ledger.

`./etch *filename* -data data.json`

If we run one of the above code examples in this way, `data.json` may contain the following:

``` json
{"2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9": "8403000000000000"}
```

## Utility functions

`getBlockNumber()` : returns the number of the current block in `UInt64`. 

See an example of running `getBlockNumber()` on a running node <a href="../../tutorials/block-number" target=_blank>here</a>.

You need a node running to test this. As well as that, you can only get a result when the function is embedded within smart contract code in Python.

Details for running a node are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.


<br/>
