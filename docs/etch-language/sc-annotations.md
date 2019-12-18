# Smart contract annotations

Smart contract functions are annotated depending on the activity they perform. These annotations are checked at compile time.

A function definition or prototype can only be annotated once. Attempting to use more than annotation in a function will raise a compile-time error.

## @init

The `@init` function defines a contract constructor that sets the state of the contract prior to any operations performed on it. It is called once and once only on contract initialisation/deployment. The name of the `@init` function can be anything at all.

For example, the following function initialises a contract by creating a `State` type to represent the owner's account which then receives an initial supply of FET tokens.


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

Only one `@init` function per contract is allowed; attempting to define more than one will raise a compile-time error. It must take no arguments or only an `Address`, and its return type must be either `void` or `Int64`.


!!! Remember
    We use `main()` in the examples to allow for testing smart contract code outside of a ledger environment.


## @action

The `@action` annotation signifies a function which performs a transaction. 

A smart contract must have one or more functions annotated with `@action`. In order for a function to be callable from other smart contracts, it must be annotated with `@action`, otherwise it will be effectively considered private.

You cannot run an `etch` smart contract on the <a href="https://github.com/fetchai/ledger-api-py" target=_blank>Python Ledger API</a> without an `@action` function and it is these functions that trigger the charging rules for data persistence fees.

An `@action` return type must be either `void` or `Int64`.

The following function performs a transaction between two parties. In the worst case, this function needs two shards for data storage.

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


## @query

Query functions are read-only functions that allow you to view data residing on the ledger. Their return type can not be `void`.

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
