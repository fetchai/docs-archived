## Version 0.4.x

Significant changes in this version of the `etch` virtual machine include the following:

* `Byte` type deprecated in favour of `UInt8` - *breaking change*.
* `ByteArray` type now available.
* New unsigned integer 256 byte type available `UInt256`.
* Null pointer included for uninitialised `String` types.
* `panic` support for possible runtime errors included.
* `extend()` function included in array functions.
* Updated `Map` implementation.
* Updated `State` type implementation - *breaking change*.
* New complex map type for ledger memory manipulation, `ShardedState`. This deprecates previous implementation, `PersistentMap`.
* Updated implementation for `Address` types as `Base58` encoded 64 byte ECDSA public key - *breaking change*.
* Updated implementation for `Address` verification `signedTx()` - *breaking change*.
* Cryptographic function `SHA256()` is now available.
* The machine learning libraries now include support for graph and tensor types and mean squared error and cross entropy functions.


<br/>
