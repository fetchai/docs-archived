# Making an ERC20 contract
The following tutorial assumes that you already have a `constellation` instance running on port `8100` and that you have installed the the Python API.

## Requirements
The ERC20 contract implements following functions:

- `totalSupply() : UInt256` -- Get the total token supply.
- `balanceOf(owner: Address): UInt256` -- Get the account balance of another account with address `owner`.
- `transfer(to: Address, value: UInt256) : Bool` -- Send `value` amount of tokens to address `to`.
- `transferFrom(from: Address, to: Address, value: UInt256): Bool` -- Send `value` amount of tokens from address `from` to address `to`.
- `approve(spender: Address, value: UInt256) : Bool` -- Allow `spender` to withdraw from your account, multiple times, up to the `value` amount. If this function is called again it overwrites the current allowance with `value`.
- `allowance(owner: Address, spender: Address)` -- Returns the amount which `spender` is still allowed to withdraw from `owner`.

We will in the following implement most of these functions. As the Fetch.AI smart contracts do not have implicit addresses as in Ethereum, the function signatures are will be slightly different as will be seen below, but the overall functionality remains the same.


## Initialisation function
We first define the contract constructor function which is annotated with the `@init` keyword. This tells the ledger that this function should be invoked upon instating the contract:
```
@init
function createSupply(owner: Address, supply: UInt256)
  var supply_state = State< UInt256 >("total_supply");  
  supply_state.set(supply);

  var balance_state = State< UInt256 >(owner);
  balance_state.set( supply );
endfunction
```
The transaction that submits the contract to the ledger is responsible for providing the constructor arguments. The above init function creates a state for the `owner` issuing `supply` tokens. Furthermore, for this specific contract we have made the total supply programmable such that the contract can be reused as well as to make it easy to write tests for the contract.

## Queries
The ERC20 contract provides three query functions: `totalSupply`, `balanceOf` and `allowance`. We will define `totalSupply` and `balanceOf` in this section and dicuss `allowance` in a section later on.

Both `totalSupply` and `balanceOf` are straightforward to implement. Total supply queries the `State` variable `total_supply` and returns it as a result:
```
@query
function totalSupply(): UInt256
  var supply_state = State< UInt256 >("total_supply"); 
  return supply_state.get(0u64); 
endfunction
```
`balanceOf`, on the other hand, makes a dynamic look up based on the address of `owner`:
```
@qeury
function balanceOf(owner: Address) : UInt256
  var balance_state = State< UInt256 >(owner);

  if(!balance_state.existed())
    return UInt256(0u64);
  endif

  return balance_state.get(UInt256(0u64));
endfunction
```
These two query mechanisms demonstrate two different ways of handling undefined states. In the first query, we request the `total_supply` by calling `get` on the state variable and supplying a default value if the state does not exist. In the second query, we manually check whether the variable existed at the beginning of the contract call and if not, we return `0`. Both are valid ways to manage a state existance.

## Actions
The ERC20 contract defines three queries: `transfer`, `transferFrom` and `approve`. We will discuss `approve` in the next section. In Etch, `transfer` and `transferFrom` are one and the same function as Etch does not have an implicitly provided sender. Rather `from` and `to` are explicit function arguments and whether these addresses signed the transaction needs to be checked within the `@action`:
```
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
The above demonstrates one of the simplest possible token contracts that can be implemented: It merely keeps a balance associated with each address and allows transfers from one address to the other if the address holds sufficient tokens.

## Implementing allowance
The functions up until now constitute a basic token contract that allows creation of tokens and transfer between participants. The more interesting functionality is the `allowance` mechanism in the ERC20 contract that gives one address the possibility of spending some amount based on the allowance details. 

To create this functionality we could use the normal `State` object by simply definining the object identifiers. However, a more appropriate mechanism for this purpose is the `ShardedState` which ensures that the payload is assigned to an appropiate shard within the system. Implementing the `approve` mechanism using the `ShardedState` is relatively easy as it provides dictionary-like functionality:
```
@action
function approve(owner: Address, spender: Address, value: UInt256) : Bool
  var state = ShardedState< UInt256 >(spender);
  state.set(owner, value);
  return true;
endfunction
```
The above constructs object addresses by concatenating the `spender` address with the `owner` address. However, unlike a normal dictionary, the `StateShard` does not keep a record of which entries exists and which not. Such functionality could be added by simply adding another state variable keeping track of owners. We will see an example on a similar type of functionality in the next part of this guide.

Finally, implementing a query mechanism is equally straight foward:
```
@query
function allowance(owner: Address, spender: Address) : UInt256
  var state = ShardedState< UInt256 >(spender);
  return state.get(owner, UInt256(0u64));
endfunction
```
The contract provided here obviously still need additional functionality for `allowance` to be truly useful as we have not implemented any method to actually spend the allowance. 

You can find the full contract <a href="https://github.com/fetchai/etch-examples/blob/master/02_erc20/contract.etch" target=_blank>here</a>.

<br/>