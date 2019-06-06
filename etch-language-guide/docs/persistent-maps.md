<h1>PersistentMaps</h1>
<h2>Deprecating in favour of ShardedStates</h2>

A `PersistentMap` is a data structure like `State` but is more flexible. 

`PersistentMap` can contain multiple data entries and therefore is a more economical use of the ledger.

Declare a `PersistentMap` with `PersistentMap<K, V>` where `K` is a unique key and `V` is the value associated with the key. 


``` java
function main()

	// create a PersistentMap
	// var pm : PersistentMap<String, String>(myPm : String); // error at '<', expected '=' or ';'
	// create a value
	// var val : String = "hello";
	// add the value to the PersistentMap at a specific key name
	// pm["0"] = val;

endfunction
```

To add a `State` to a `PersistentMap`, do the following:

!!! note 
	Coming soon: support for `PersistentMap`.

``` java
function main()
	
    // declare a State and set a value on it
    var myState = State<Int32>("xyz.balance", 0);
    myState.set(100);
    // declare a PersistentMap with the same name as the State
    // var myPm = PersistentMap<String, Int32>("xyz"); // error at ',', expected ';'
    // Failed to compile.
    // access a variable in the State using a handle to the PeristentMap
    // printLn(myPm["balance"]);

endfunction
```

In a `PersistentMap` the key must be a `String` or an `Address` type.


A `PersistentMap` can wrap around `State` types. For example, a common requirement for smart contracts is to facilitate transfers. Below, the `from` and `to` variables are `Address` types representing the two parties to a transaction along with their balances.

``` java
	var from_address = State<UInt64>(from, 0u64);
	var to_address = State<UInt64>(to, 0u64);
```

This is better represented by a `PersistentMap` where `from_address` and `to_address` represent keys, the values of which are set prior to building the data structure.

``` java
function main()

	// var transactPm : PersistentMap<Address, String>(tx : Int32); // error at '<', expected '=' or ';'
    // create transaction account details
    // var from_address = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7DF8+Pw==");
    // var to_address = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+Pw==");
    // create values representing the balances of the accounts
    // var from_balance : String = 1000u64;
    // var to_balance : String = 0u64;
    // add the value to the PersistentMap at a specific key name
    // transactPm[from_address] = from_balance;
    // transactPm[to_address] = to_balance;

endfunction
```

A duplicate key overwrites the previously defined entry.


[!comment]: <> (To clarify: In the other direction, a `State` can wrap around a `PersistentMap`. After declaring a `PersistentMap`, you can add it to a `State` which gives you access to the data, getters, and setters. For example: var myState : State<Type>(transactPm.from_address) var getAddress = myState.get())
