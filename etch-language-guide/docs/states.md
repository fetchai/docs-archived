<h1>States</h1>

Smart contracts store data on the Fetch.AI distributed ledger with `State` and `PersistentState` data structures. 

A `State` is declared as a `State<ValueType>(name : String, value : ValueType)` like this:

``` c++
	var myState = State<Int32>("balance", 0);
```

In the above `State`, the `Int32` value `0` maps to the key `balance`.

The value `0` set at declaration is the default value. A `State` will not compile without a default value.

A common use for the `State` type is to represent account owner `Address` types with their respective balances. To this end, you can declare a `State` where the first parameter is an `Address` type.

In the code below we first create an `Address` type. We can then define the transaction sender account wrapped in a `State` type where the first parameter `from` is the `Address` we just created and the second parameter is the account balance in `UInt64`:

``` c++
function main()

 	var from = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+Pw==");
	var from_account = State<UInt64>(from, 0u64);

endfunction
```

!!! note 
	Coming soon: support for including a `Map` in a `State`.

	``` java

	// var myMapState = State<Map<String, Int32>>(myMap, null); // error: unable to find matching constructor for type/function 'State<Map<String, Int32>>'
	```



## Getters and setters

Getters and setters are available for `State` types.

``` c++
function main()

	var myAccount = State<Int32>("balance", 0);
	printLn("My balance = " + toString(myAccount.get()));
	myAccount.set(10);
	printLn("My balance = " + toString(myAccount.get()));

endfunction
```

Currently, `State` supports primitive types only.




