<h1>States</h1>

Smart contracts store data on the Fetch.AI distributed ledger with `State` and `PersistentMap` data structures. 

A `State` is declared as a `State<ValueType>(name : String, value : ValueType)` like this:

``` c++
	var myState = State<Int32>("balance", 0);
```

In the above `State`, the `Int32` value `0` maps to the key `balance`.

The value set at declaration is the default value. The following snippet prints `0`. 

``` java

function main()
    
  var x : Int32;
  var myState = State<Int32>("balance", x);

  var y = myState.get();
  print(toString(y));

endfunction

```

## State behaviour

`State` behaviour currently has a few surprises. For example, in the code example below we see that we can happily print the value of a state after declaration `// 1. `.

It is possible to change the `State` value within the same method with `set()` and print the change successfully `// 2.`.

However, sending `State` variables to other functions is challenging. In the function `change_state()` we can assign our `State` object to a new name and reset the value and this is the value that `main()` prints in `` 3.``, even though we create a new `State` using the same `"balance"` key and reset the value to `42`. The second statement has no effect on the original `State` object. 

However, in the `query()` function (no connection to `@query`) we call the original `State` in the same way by using the `"balance"` key but without changing the default value from `0`. This time we *do* get access to the original value in `// 4.`.

Interestingly, in `//5.`, if we reset the value with `set()` and return the value with `get()`, the new value is returns by the function. However, there is no change to the `State`.


``` java

function main()
    
  var myState = State<Int32>("balance", 0);
  // 1. print empty state
  print("1: ");
  printLn(toString(myState.get()));

  // 2. change state inside main
  myState.set(33);
  print("2: ");
  printLn(toString(myState.get()));

  change_state(myState);
  // 3. print state after change_state call
  print("3: ");
  printLn(toString(myState.get()));

  var result = query();
  // 4. print state after query call - notice how query function doesn't change state of the original
  print("4: ");
  printLn(toString(result));

  // 5. alter comments in query method to see that state value is not alterable even though
  // accessible from another function
  // print("5: ");
  // printLn(toString(result));
  // printLn(toString(myState.get()));

endfunction



function change_state(state : State<Int32>)

  // you can pass around a State parameter and get access to the original state
  var newState = state;
  newState.set(100);

  // but notice that creating a new local state with the same key string does not change the original
  var anotherState = State<Int32>("balance", 42);

endfunction



function query() : Int32

  // HOWEVER, notice that creating a new state with the original key accesses the original state
  var myState = State<Int32>("balance", 0);
  
  // 4. and returns it, this returns 100!
  return myState.get();

  // 5. 
  // BUT if you set a new variable into the state, it will return the new variable but not 
  // alter the state!!
  // myState.set(55);
  // return myState.get();


endfunction

```

You can add complex types to a `State`:

``` java
function main()

    var myArray = Array<Int32>(5);
    myArray[0] = 23;
    printLn(toString(myArray[0]));

    var myState = State<Array<Int32>>("var", myArray);
    
    // myState.set(myArray[0]=24); // error at '=', expected ')'
    // printLn("My state array index [0] value = " + toString(myState.get(myArray[0]))); // error: unable to find matching function for 'get'

endfunction
```

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

Currently, `State` getters and setters support primitive types only.




