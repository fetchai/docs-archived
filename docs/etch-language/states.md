<h1>States</h1>

## Introduction to `State` variables

A `State` provides persistent storage for smart contracts. It’s like a global variable that is always there when any function of your contract runs. 

A smart contract might use a `State` to store the total supply or use multiple `State` variables to keep a track of who has what, for example. It can also let a contract track whether some events have occurred before it releases tokens.

Declare a `State` like this:

``` c++
var myState1 = State<Int32>("simple_state_declaration");
```

Or even this:

``` c++
var myState2 = State<Array<Array<Array<String>>>>("nested_array_state_declaration");
```

A `State` is not like a normal variable, you have to create a *reference* to it. For example:

``` c++
function main()

    var supply = UInt256(1000u64);
    var contract_amount_state = State<UInt256>("contract_amount");  
    contract_amount_state.set(supply);

endfunction
```

The above code creates a variable name `contract_amount_state` and assigns it to a `State<Int32>` with a reference `contract_amount`. It then sets a value on the `State`. 

`State` references can be `Address` types.

``` c++
function main()

    var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
    var supply = UInt256(1000u64);
    var myState = State<UInt256>(account);
    myState.set(supply);

endfunction
```
`State` references can also be strings and you can get and set values on a `State` object.

``` c++
function main()

    var contract_amount_state = State<UInt256>("contract_amount");
    var supply = UInt256(1000u64);
    contract_amount_state.set(supply);
    var contract_amount = contract_amount_state.get();
    printLn("My state value = " + toString(contract_amount_state.get()));

endfunction
```

## Default values

If a value has not yet been set on the `State` object and the `State` does not already exist on the ledger, a run-time error is thrown on calling `get()`. 

To avoid this, use **with care** `get(<default value>)` with a default value. For example, the following code prints zero if the state doesn't exist and the value that was originally set on it if it does exist.

``` c++
function main()

    var contract_amount_state = State<Int32>("contract_amount");  
    var contract_amount = contract_amount_state.get(0); 
    printLn(toString(contract_amount));

endfunction
```

## Test a `State` exists

You can test if a state already exists with `existed()`.

``` c++
function main()

    var contract_amount_state = State<Int32>("contract_amount");   

    if (contract_amount_state.existed())
      printLn("Yes, it existed");
    endif

endfunction
```

This test is useful for scenarios in which you use states to see who has what, as you might do in a token contract where you need to keep track of who has the tokens.


## State references and scope

In the example below, `ownerState` and `contractState` point to the same `State` object on the ledger.

``` c++
function main()

    var owner = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
    var ownerState = State<Int32>(owner);
    ownerState.set(333);
    printLn("My state value = " + toString(ownerState.get()));
    var contractState = State<Int32>(owner);
    // printLn("My state value = " + toString(contractState.get())); 
    // runtime error: line 7: The state does not represent any value. 
    // The value has not been assigned and/or it does not exist in data storage.

endfunction
```

Assuming the referenced `State` object does not exist on the ledger, attempting to print the value of the second declaration of `State` generates an error - even though a value was set on it previously. 

This is because the data set in `ownerState` has not yet been written to the intermediate cache or ledger storage, so when `contractState` tries to access it, it finds no value and this generates a runtime error.




## Writing `State` data to the ledger

The following is true for `State` variables declared with a `var` identifier.

Currently, `State` data is written to smart contract intermediate cache only after control has passed out of function scope.

While identifiable `State` variables remain inside function scope, data is written to an intermediate object cache mechanism at construction time. 

Within the same scope, such data is inaccessible to new `State` identifiers (which have not explicitly called `set()` on the `State`).

You cannot access a value set on a `State` if the function scope in which it was created is still open.

``` c++
function main()

    var state = State<Int32>("value");
    state.set(11);  
    printLn(state.get()); 

    var value1 = value();     
    printLn(toString(value1));
    // scope not yet closed therefore runtime error: 
    // The state does not represent any value. 
    // The value has not been assigned and/or it does not exist in data storage.

endfunction    

function value() : Int32      
    
    var state = State<Int32>("value");
    return state.get();
 
endfunction
```

Once control reaches the end of the function, the data is written to an intermediate ledger cache mechanism and is available throughout the contract.

Once control has reached the end of the contract, and no errors have arisen, the data is etched upon the ledger.

<center>

![How smart contracts manage State and ShardedState memory allocation](img/memory-caching.png)

</center>


## Anonymous `State` types

Declaring an anonymous `State` type without a `var` name performs an immediate data write.

``` c++
function main()
  
    State<String>("account1").set("owner1_name");

    var account1 = State<String>("account1");
    printLn(account1.get());

endfunction
```

This is useful for `ShardedState` types which build up with immediate write anonymous `State` types behind the scenes.



## Passing States around

The following code shows the behaviour of `State` types as they are passed around functions.

`State` values are available to `get()` if the function scope they were created in originally has closed.


``` c++
function main()

    var myState = State<Int32>("contract_owner_balance");
    myState.set(33);
    printLn(toString(myState.get()));
    // PRINTS 33

    change_state(myState);
    printLn(toString(myState.get()));
    // PRINTS 44

    var result = query();
    printLn(toString(result));
    // PRINTS 55

endfunction

function change_state(state : State<Int32>)

    // you can pass around a State parameter and get access to the original state
    var newState = state;
    newState.set(44);

    // a new state with pointer = "balance"
    var anotherState = State<Int32>("balance");
    anotherState.set(55);
    // all states from this function are written now

endfunction

function query() : Int32

    // accessing the State at pointer = "balance", a value out of scope 
    var myState = State<Int32>("balance");
    // returns the 55 set in change_state()
    return myState.get();

endfunction
```



## Verify an Address

Often, a contract needs to confirm whether an `@action` or `@query` comes from a specific address. This can be done with the `signedTx()` function of the `Address` type. 

In the example below, an `@action` establishes if the the signer of the calling transaction is a specific authorised address.

``` c++
@action 
function doSomething(signer : Address)

  if (!signer.signedTx())
      panic("This address doesn't verify, stopping here.");    
    endif

    // Get the authorised address from the ledger
    var authorised_state = State<Address>("owner");
    var authorised_address = authorised_state.get();

    if (authorised_address != signer)
        panic("Incorrect address used to trigger");
    endif
        // ... we're good to go, the signer of the TX is the stored authorised address...

endfunction

function main()

    var owner = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
    var authorised = State<Address>("owner");
    authorised.set(owner);
    doSomething(owner);

endfunction
```

<br/>


