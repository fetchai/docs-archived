The `etch` language provides a number of object types and functions designed specifically with smart contract development in mind. 

We detail these in the <a href="../../etch-language/states" target=_blank>`etch` language guide</a> but here's an overview.


## State

A `State` provides persistent storage for smart contracts. The data referenced by a `State` type resides on the ledger. 

`State` values are available for use in smart contract functions.


## Sharded State

A `ShardedState` is like a `State` type in that data contained within a `ShardedState` also resides on the ledger and is available for use in smart contract functions.

However, `ShardedState` is a map of key/value pairs so can wrap significantly more data under one reference. 

Moreover, `ShardedState` manages the sharded structure of ledger memory more efficiently than a `State` type.


## Address

The `Address` data structure formats multiple cryptographic public key types and includes a number of useful functions such as `verify()` and `existed()`.



## Cryptographic functions

Currently, we support the <a href="../../etch-language/crypto" target=_blank>`SHA256()`</a>function.


<br/>
