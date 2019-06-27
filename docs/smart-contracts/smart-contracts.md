<h1>Smart contracts</h1>

Smart contract code runs on the `etch` VM. 

All ledger nodes maintain `etch` VM and smart contract code.

The identity  of a smart contract is calculated by performing a `SHA256` hash of the contract code as an initial step. Next, a further `SHA256` hash is calculated from the previous result concatenated with a public key `Address`.

On the ledger, the `etch` VM stores the contract name, the contract source code, and the data resources that are mapped by a `data.json` file.

Taking this contract identity data, the `etch` VM performs a modulo 16 calculation from which it decides how to store the data on the ledger, i.e. onto which shard.

!!! note
	Coming soon: details on how developers may dictate the sharding storage design for a smart contract.



## Basic Smart contract

Smart contract functions are annotated depending on the activity they perform.

<H3>@init</H3>	

The `@init` function defines a contract constructor that sets the state of the contract prior to any operations performed on it. It is called once and once only on contract initialisation/deployment.

The name of the `@init` function can be anything you like.

For example, the following function initialises a contract by creating a `State` type that represents the owner's account which sets an initial supply of FET tokens. 


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

You cannot create a contract in `etch` without an `@action` function and it is these functions that trigger the charging rules for data persistence fees.

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

In the worst case, the above function needs two shards for data.


<h3>@query</h3>

Query functions are read-only functions that allow you to view data on the ledger. 

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
	var x = balance(owner);
	printLn(x);

endfunction
```

## Data confirmation

If you run an `etch` contract in the simulator containing one or more `State` types and flag the compiler with `-data` and a filename, it will create a `json` file containing data details.

`./vm-lang *filename* -data data.json`

If we run one of the above code examples in this way, `data.json` may contain the following:

``` json
{"2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9": "8403000000000000"}
```

## Utility functions

```getBlockNumber()``` : returns the number of the current block in `UInt64`.


<br/>
