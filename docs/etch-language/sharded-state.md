<h1>Sharded States</h1>

A `ShardedState` functions like a `State` type in that data contained within a `ShardedState` will be etched upon the ledger.

The key difference is that a `ShardedState` is a map, containing key/value pairs. 

Behind the scenes, `ShardedState` creates anonymous `State` types for key/value pairs that etch onto the ledger.

Declare a `ShardedState` in the same way you declare a `State`: 

``` c++
function main()

    var state = ShardedState<Int32>("account1");

endfunction
```

The `account1` identifier is the pointer to the place in memory that holds the data. 

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

Let's add some query functions to get the `ShardedState` values. Notice that when you query the data, you can provide default values and you will receive an actual value.

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

 
function query_sales() : Int32
    var state = ShardedState<Int32>("account1");
    return state.get("sales", 0i32);
endfunction

function query_gross_profit() : Int32
    var state = ShardedState<Int32>("account1");
    return state.get("gross_profit", 0i32);
endfunction

function query_net_profit() : Int32
    var state = ShardedState<Int32>("account1");
    return state.get("net_profit", 0i32);
endfunction
```

You can of course create `ShardedState` types using `Address` types.

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

Because `ShardedState` uses anonymous `State` types to write data as soon as it is created, we can access values with keys using any identifier.

This makes the `ShardedState` type much more flexible and powerful than a `State` type.






<br/>


