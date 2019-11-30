Smart contract functions are annotated depending on the activity they perform.

## @init	

The `@init` function defines a contract constructor that sets the state of the contract prior to any operations performed on it. It is called once and once only on contract initialisation/deployment.

The name of the `@init` function can be anything at all.

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

!!! Remember
    We use `main()` in the examples to allow for testing smart contract code outside of a ledger environment.


## @action

The `@action` annotation signifies a function which performs a transaction. 

A smart contract must have one or more functions annotated with `@action`.

You cannot run an `etch` smart contract on the <a href="https://github.com/fetchai/ledger-api-py" target=_blank>Python Ledger API</a> without an `@action` function and it is these functions that trigger the charging rules for data persistence fees.

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


## @query

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

<br />
