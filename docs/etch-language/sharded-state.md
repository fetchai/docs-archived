<h1>Sharded States</h1>

A `ShardedState` is like a `State` type in that data contained within a `ShardedState` will be etched upon the ledger.

The key difference is that a `ShardedState` is a map, containing key/value pairs. 

A key must be a `String` or `Address` type.

Behind the scenes, `ShardedState` creates anonymous `State` types for key/value pairs that etch onto the ledger.

## Declaration

Declare a `ShardedState` in the same way you declare a `State`: 

``` c++
function main()

    var state = ShardedState<Int32>("account1");

endfunction
```

The `account1` identifier is the pointer to the place in memory that holds the data. 


## Add key/value pairs

Add key/value pairs to the `ShardedState` like this:

``` c++
function main()

    var myShardedState = ShardedState<Int32>("account1");
    myShardedState.set("sales", 0i32);
    myShardedState.set("gross_profit", 0i32);
    myShardedState.set("net_profit", 0i32);
    
    set_values_on_state();

endfunction

function set_values_on_state()
      
    var state = ShardedState<Int32>("account1");
    state.set("sales", 2000000);
    state.set("gross_profit", 1800000);
    state.set("net_profit", 1300000);

endfunction
```

## Querying with default values

Let's add some query functions to get the `ShardedState` values. Notice that when you query the data, you provide default values and receive the actual value.

!!! Note
    The annotation `@query` is used in smart contract code and unnecessary for testing with the `etch` VM.

``` c++
function main()

    var myShardedState = ShardedState<Int32>("account1");
    myShardedState.set("sales", 0i32);
    myShardedState.set("gross_profit", 0i32);
    myShardedState.set("net_profit", 0i32);

    set_values_on_state();
    printLn(query_sales());
    printLn(query_gross_profit());
    printLn(query_net_profit());

endfunction

function set_values_on_state()

    var state = ShardedState<Int32>("account1");
    state.set("sales", 2000000);
    state.set("gross_profit", 1800000);
    state.set("net_profit", 1300000);

endfunction

@query
function query_sales() : Int32

    var state = ShardedState<Int32>("account1");
    return state.get("sales", 0i32);

endfunction

@query
function query_gross_profit() : Int32

    var state = ShardedState<Int32>("account1");
    return state.get("gross_profit", 0i32);

endfunction

@query
function query_net_profit() : Int32

    var state = ShardedState<Int32>("account1");
    return state.get("net_profit", 0i32);
    
endfunction
```

## `ShardedState` types with `Address` references

You can create `ShardedState` types using `Address` types as the reference.

``` c++
function main()

    var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
    var myState = ShardedState<Int32>(account);
    myState.set("balance", 100);
    myState.set("transx1", -10);
    myState.set("transx2", 30);
    printLn("My account balance = " + toString(myState.get("balance")));

endfunction
```

## Writing `ShardedState` data to the ledger

Any number of `var` identifiers can point to the same `ShardedState` object.

``` c++
function main()

    var x = ShardedState<Int32>("account1");
    var y = ShardedState<Int32>("account1");
    x.set("balance", 100);
    y.set("balance", -10);
    printLn("My state value = " + toString(x.get("balance")));

endfunction
```




<br/>


