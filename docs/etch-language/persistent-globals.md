For enhanced developer experience, we have introduced more succinct and ledger efficient persistent variable types for storing data on the Fetch.AI Ledger. These types are equivalent to `State` and `ShardedState` objects.

Five new keywords identify these types: `persistent`, `sharded`, `use`, `as`, and `any`.

As `etch` evolves along with the Fetch.AI Ledger, persistent globals will help ensure maximum ledger storage efficiency and we recommend their use over `State` and `ShardedState`.



## Syntax

Declare all persistent variables the smart contract may use at the top of the file before any function declarations.



### `persistent`

Use the `persistent` keyword to reference global persistent `State` types available to the contract. 

``` c++
persistent total : UInt32;
// more persistent globals

// smart contract functions...
function main()
// do stuff
endfunction
```

The above syntax references a `State` variable that previously could only be constructed as follows.


``` c++
function main()
	
	var total_state = State<UInt32>("str_ref");
    
    var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
    var account_state = State<UInt256>(account);

endfunction
```

Using the persistent global syntax, there is no way to reference the `String` or `Address` constructor parameter references as before.

!!!	Note
	It is still possible to construct `State` types without persistent global declarations.



### `sharded`

Use the `persistent sharded` keyword pair to declare global persistent `ShardedState` types available to the contract.


``` c++
persistent sharded balances : UInt64;
// more persistent globals

// smart contract functions...
function main()
// do stuff
endfunction
```

The above syntax references a `ShardedState` variable that previously could only be constructed as follows.


``` c++
function main()
	
	var balances_sharded_state = ShardedState<UInt64>("balances");

endfunction
```

This means you cannot build a `ShardedState` referenced by a single `String` or `Address` as before. However, this limitation should promote a more economical use of the ledger.

!!! Note
    It is still possible to construct `ShardedState` types without persistent global declarations.


### `use`

Import the global persistent variables into smart contract functions with the `use` keyword. 

#### `State`

For `State` types, call `get()` and `set()` on the variable name as before.

``` c++
persistent total : UInt32;

function main()

    // import a State type
    use total;

    // call functions on the Fetch ledger types as before
    total.set(10u32);
    printLn(total.get());

endfunction
```

#### `ShardedState`

For `ShardedState` types, call `get()` and `set()` as before.

``` c++
persistent sharded balances : UInt64;

function main()

    // import a ShardedState type with one key
    use balances["balance1", "balance2", "balance3"];

    // set a value on the keys
    balances.set("balance1", 10u64);
    balances.set("balance2", 20u64);
    balances.set("balance3", 30u64);

    // print a value
    printLn(toString(balances.get("balance2")));

endfunction
```

However, note that setting keys on the `ShardedState` type happens at import time and there is no limit to the number of keys. 

Set and use keys on a persistent global `ShardedState` in a flexible manner as demonstrated by the following example.

``` c++
persistent sharded balances : UInt64;


function main()

    use balances;

    add_one_key();
    add_two_more_keys();

    printLn(balances.get("key_3"));

endfunction


function add_one_key()

    use balances["key_1"];

    balances.set("key_1", 10u64);

endfunction


function add_two_more_keys()

    use balances["key_2", "key_3"];

    balances.set("key_2", 20u64);
    balances.set("key_3", 30u64);

endfunction
```

!!! Warning
    If you don't use a declared persistent global variable you have imported, `etch` generates a compilation error. This ensures maximum ledger efficiency (i.e. not paying for unused objects).




### `as`

Alias the persistent global variable name to avoid confusion in large smart contract scripts.

``` c++
persistent total : UInt32;


function main()

    use total as first_total;

    first_total.set(0u32);

    second();

endfunction


function second()

    use total as second_total;

    second_total.set(20u32);
    
endfunction
```



### `any`

!!! Warning
    Use `any` with great care. `any` does not require use of the variable within the function and it therefore has no safety mechanism for avoiding additional charges.

Import all the declared persistent global variables with the wildcard keyword `any`.

``` c++
persistent total : UInt64;
persistent sharded balances : UInt64;

function main()

    use any;

    total.set(100u64);
    balances.set("balance_1", 100u64);

endfunction
```


<!--
## Function call limitations
means you can't pass these variables around
-->


## Benefits

Using persistent global syntax means that only one variable identifier can point to a single `State` or `ShardedState` object.

The following unusual situation is not possible with persistent globals.

``` c++
function main()

    var a = State<Int32>("account1");
    var b = State<Int32>("account1");
    a.set(100);
    b.set(-10);
    printLn("My state value = " + toString(a.get()));
    // My state value = 100

    var x = ShardedState<Int32>("account2");
    var y = ShardedState<Int32>("account2");
    x.set("balance", 100);
    y.set("balance", -10);
    printLn("My sharded state value = " + toString(x.get("balance")));
    // My state value = -10

endfunction
```


<br/>
