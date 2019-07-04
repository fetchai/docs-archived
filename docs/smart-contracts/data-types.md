The `etch` language provides a number of object types and functions designed specifically with smart contract development in mind. 

We detail these in the <a href="../../etch-language/states" target=_blank>`etch` language guide</a> but here's an overview.


## State

A `State` provides persistent storage for smart contracts. 

It’s like a global variable whose value is always available when any function of your contract runs.


## ShardedState

A `ShardedState` is like a State type in that data contained within a ShardedState is etched upon the ledger and is available to smart contract functions.

`ShardedState` is a map type so can wrap significantly more information under one reference. 


## Address

The `Address` data structure formats multiple cryptographic public key types and included a number of useful functions such as `verify()` and `existed()`.



## Cryptographic functions

Currently, we support the `SHA256()` function.


<br/>
