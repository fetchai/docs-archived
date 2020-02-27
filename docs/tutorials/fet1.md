# Create a token smart contract

Most people interact with smart contracts that handle the issuance of tokens, such as the well known Ethereum [ERC20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md). Most token contracts are either:

- Non-fungible tokens (NFT): These are like collectables, as they cannot be split; you can't cut a baseball collector's card and have two that are worth 50% of the original. One of the most well-known of these is [Cryptokitties](https://www.cryptokitties.co/). Most non-fungible tokens are [ERC721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md).
- Fungible tokens (FT): Fungible can be split, and are used for most token issuance. The circulating supply, the issuance foundation and the list of where the tokens are are held and enforced by a smart contract. Most fungible tokens on Ethereum, including non-native FET tokens, are based on [ERC20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md).

In this tutorial, we are going to deploy a simple fungible token contract and make some calls to it. We will then transfer some of our new tokens to some owners.

!!! note
    As Fetch.ai smart contracts do not have implicit addresses (as in Ethereum), the function signatures are slightly different, but the overall functionality remains the same.


## Initialisation function

We first define the contract constructor function which is annotated with the `@init` keyword. The `@init` annotation tells the ledger that the function should be invoked upon initial deployment of the contract:

``` java
persistent sharded balance_state : UInt64;
persistent supply_state : UInt64;

@init
function init(owner: Address)

    use supply_state;
    use balance_state[owner];

    supply_state.set(100000u64);
    balance_state.set(owner, 100000u64);

endfunction
```

The transaction that submits the contract to the ledger is responsible for providing the constructor arguments.

The above `@init` function creates a state for the `owner` issuing `supply` tokens.

Furthermore, for this specific contract we have made the total supply programmable so that the contract can be reused and to facilitate testing.


## Queries

Functions labeled with `@query` do not alter state, and they return a value to the caller. There can be many of these in a single contract. In this contract, they are used to return the contract name, total supply, and get the balance of an address.

`getName` simply returns the contract name without further calculations:

``` java
@query
function getName(): String

    return "FIP-1 fungible token";

endfunction
```

The other two query mechanisms demonstrate two different ways of handling undefined states.

`totalSupply` queries the state variable `total_supply` and returns it as a result:

``` java
@query
function totalSupply(): UInt64

    use supply_state;
    return supply_state.get();

endfunction
```

On the other hand, `balanceOf` uses the sharded state of `balance_state` and does a dynamic look up based on an `address`. If the variable does not exist, it returns `0`.

``` java
@query
function balanceOf(address: Address) : UInt64
    
    use balance_state[address];
    return balance_state.get(address, 0u64);

endfunction
```


## Actions

The FIP-1 contract defines one function annotated with `@action`. Actions can alter state and return a value. Like with queries, a contract can contain many of these.

The only action in this contract transfers an amount between two different addresses. The source of the transfer has to be the caller of the `@action`, and the function is responsible for checking that the source address has signed the transaction.

``` java
@action
function transfer(from: Address, to: Address, value: UInt64) : Bool

    if(!from.signedTx())
      return false;
    endif

    if(from == to)
      return false;
    endif

    use balance_state[from, to];
    var from_balance = balance_state.get(from, 0u64);
    var to_balance = balance_state.get(to, 0u64);

    if(from_balance < value)
      return false;
    endif

    var u_from = from_balance - value;
    var u_to = to_balance + value;

    balance_state.set(from, u_from);
    balance_state.set(to, u_to);
    return true;

endfunction
```

The above demonstrates one of the simplest possible token contracts, keeping a balance associated with each address and allowing transfers from one address to another as long as the source address holds sufficient tokens.


## Implementing allowance

So far, the functions we've seen constitute a basic token contract that allows creation of tokens and transfer between participants. A more interesting functionality is the `allowance` mechanism in the FIP-1 contract that gives one address the possibility of spending some amount based on the allowance details.

To create this functionality we could use the normal `State` object by simply defining the object identifiers. However, a more appropriate mechanism for this purpose is the `ShardedState` which ensures that the payload is assigned to an appropriate shard within the system.

Implementing the `approve` mechanism using the `ShardedState` is relatively easy as it provides dictionary-like functionality:

``` java
@action
function approve(owner: Address, spender: Address, value: UInt256) : Bool

    var state = ShardedState< UInt256 >(spender);
    state.set(owner, value);
    return true;

endfunction
```

The above builds object addresses by concatenating the `spender` address with the `owner` address. However, unlike a normal dictionary, `ShardedState` does not keep a record of which entries exist or not. Such functionality could be added by simply adding another state variable keeping track of owners. We will see an example on a similar type of functionality in the next part of this guide.

Finally, implementing a query mechanism is equally straight forward:

``` java
@query
function allowance(owner: Address, spender: Address) : UInt256

    var state = ShardedState< UInt256 >(spender);
    return state.get(owner, UInt256(0u64));

endfunction
```

The contract provided here obviously still need additional functionality for `allowance` to be truly useful as we have not implemented any method to actually spend the allowance.

You can find the full contract within <a href="https://github.com/fetchai/etch-examples/blob/master/Fet-1/contract.etch" target=_blank>here</a>.

<br/>
