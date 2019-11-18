
# Create an FET-1 contract

The following tutorial assumes that you already have a `constellation` instance running on port `8100` and that you have installed the the Python API.

Details for running a node are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.

Details of the Python API are <a href="../../getting-started/python-api-install/" target=_blank>here</a>.


## Requirements

The FET-1 contract implements following functions:

- `totalSupply() : UInt256` gets the total token supply.
- `balanceOf(owner: Address): UInt256` gets the balance of an account having address `owner`.
- `transfer(to: Address, value: UInt256) : Bool` sends `value` amount of tokens to address `to`.
- `transferFrom(from: Address, to: Address, value: UInt256): Bool` sends `value` amount of tokens from address `from` to address `to`.
- `approve(spender: Address, value: UInt256) : Bool` allows `spender` to withdraw from your account, multiple times, up to the `value` amount. If this function is called again it overwrites the current allowance with `value`.
- `allowance(owner: Address, spender: Address)` returns the amount which `spender` is still allowed to withdraw from `owner`.

We now go ahead and implement most of these functions. 

!!! Note
    As Fetch.ai smart contracts do not have implicit addresses, as in Ethereum, the function signatures are slightly different, as  will see below, but the overall functionality remains the same.


## Initialisation function

We first define the contract constructor function which is annotated with the `@init` keyword. The `@init` annotation tells the ledger that the function should be invoked upon initial deployment of the contract:

``` c++
@init
function createSupply(owner: Address, supply: UInt256)

    var supply_state = State< UInt256 >("total_supply");  
    supply_state.set(supply);

    var balance_state = State< UInt256 >(owner);
    balance_state.set( supply );

endfunction
```

The transaction that submits the contract to the ledger is responsible for providing the constructor arguments. 

The above `@init` function creates a state for the `owner` issuing `supply` tokens. 

Furthermore, for this specific contract we have made the total supply programmable so that the contract can be reused and to facilitate testing.


## Queries

The FET-1 contract has three query functions: 

* `totalSupply(): UInt256`.
* `balanceOf(owner: Address) : UInt256`.
* `allowance(owner: Address, spender: Address) : UInt256`.

We will define `totalSupply` and `balanceOf` in this section and discuss `allowance` later on.

Both `totalSupply` and `balanceOf` are straightforward to implement. `totalSupply` queries the `State` variable `total_supply` and returns it as a result:

``` c++
@query
function totalSupply(): UInt256

    var supply_state = State< UInt256 >("total_supply"); 
    return supply_state.get(0u64); 

endfunction
```

`balanceOf`, on the other hand, does a dynamic look up based on the address of `owner`:

``` c++
@query
function balanceOf(owner: Address) : UInt256
  
    var balance_state = State< UInt256 >(owner);

    if(!balance_state.existed())
      return UInt256(0u64);
    endif

    return balance_state.get(UInt256(0u64));

endfunction
```

These two query mechanisms demonstrate two different ways of handling undefined states. 

In the first query, we request the `total_supply` by calling `get` on the state variable and supplying a default value if the state does not exist. 

In the second query, we manually check whether the variable existed at the beginning of the contract call and if not, we return `0`. 

Both are valid ways to manage a state existence.



## Actions

The FET-1 contract defines three functions annotated with `@action`:

* `transfer(from: Address, to: Address, value: UInt256) : Bool`. 
* `transferFrom(from: Address, to: Address, value: UInt256): Bool`.
* `approve(spender: Address, value: UInt256) : Bool`. 

We will discuss `approve` in the next section. 

In `etch`, `transfer` and `transferFrom` are one and the same function as `etch` does not have an implicitly provided sender. Rather `from` and `to` are explicit function arguments and whether these addresses signed the transaction is checked within the `@action` function.

``` c++
@action
function transfer(from: Address, to: Address, value: UInt256) : Bool

    if(!from.signedTx())
      return false;
    endif

    var from_state = State< UInt256 >(from);
    var from_balance = from_state.get( UInt256(0u64) );
    if(from_balance < value)
      return false;
    endif

    var to_state = State< UInt256 >(to);
    var to_balance = to_state.get( UInt256(0u64) );

    // TODO: Polyfilling due to missing UInt256 functionality
    var u_from = toUInt64(from_balance);  
    var u_to = toUInt64(to_balance);
    var u_amount = toUInt64(value);
    u_from -= u_amount;
    u_to += u_amount;
    from_balance = UInt256(u_from);
    to_balance = UInt256(u_to);  

    from_state.set(from_balance);
    to_state.set(to_balance);
    return true;

endfunction
```

The above demonstrates one of the simplest possible token contracts keeping a balance associated with each address and allowing transfers from one address to the other if the address holds sufficient tokens.


## Implementing allowance

So far, the functions we've seen constitute a basic token contract that allows creation of tokens and transfer between participants. A more interesting functionality is the `allowance` mechanism in the FET-1 contract that gives one address the possibility of spending some amount based on the allowance details. 

To create this functionality we could use the normal `State` object by simply defining the object identifiers. However, a more appropriate mechanism for this purpose is the `ShardedState` which ensures that the payload is assigned to an appropriate shard within the system. 

Implementing the `approve` mechanism using the `ShardedState` is relatively easy as it provides dictionary-like functionality:

``` c++
@action
function approve(owner: Address, spender: Address, value: UInt256) : Bool

    var state = ShardedState< UInt256 >(spender);
    state.set(owner, value); 
    return true;

endfunction
```

The above builds object addresses by concatenating the `spender` address with the `owner` address. However, unlike a normal dictionary, `ShardedState` does not keep a record of which entries exist or not. Such functionality could be added by simply adding another state variable keeping track of owners. We will see an example on a similar type of functionality in the next part of this guide.

Finally, implementing a query mechanism is equally straight forward:

``` c++
@query
function allowance(owner: Address, spender: Address) : UInt256

    var state = ShardedState< UInt256 >(spender);
    return state.get(owner, UInt256(0u64));

endfunction
```

The contract provided here obviously still need additional functionality for `allowance` to be truly useful as we have not implemented any method to actually spend the allowance. 

You can find the full contract <a href="https://github.com/fetchai/etch-examples/blob/master/02_erc20/contract.etch" target=_blank>here</a>.

<br/>