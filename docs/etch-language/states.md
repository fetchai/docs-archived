<h1>States</h1>

Smart contracts store data on the Fetch.AI distributed ledger using `State`.

A `State` is declared as a `State<ValueType>(name : String, value : ValueType)` like this:

``` c++
	var myState = State<Int32>("balance", 0);
```

In the above `State`, the key on the left maps to the `Int32` value on the right. 

The key can be a `String` or an `Address`. Wherever referenced, the key gives access to the `State`, regardless of whether or not the variable name pointing to the `State` has changed.

The value set at declaration is the default value. The following snippet prints `0`. 

``` c++

function main()
    
  var x : Int32;
  var myState = State<Int32>("balance", x);

  var y = myState.get();
  print(toString(y));

endfunction

```

You can only update the default value using a `set()` function.

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



## State behaviour

Currently `State` behaviour is fairly trivial. The code below gives a number of examples.

First, we see that we can happily print the value of a state after declaration `// 1. `.

In `// 2.` it is possible to change the `State` value within the same method with `set()`.

In the function `change_state()` we can assign our `State` object to a new name and reset the value to `100` which `main()` prints at `` // 3.``, even though we also create a new `State` using the same `"balance"` key and reset the value to `42`. The second statement has no effect on the original `State` object. 

The `query()` function (no connection to `@query`) also references the original `State` by using the `"balance"` key and declares the default value as `0`. However, this time we *do* get access to the original `State` and the value returned is `100` again.

There is an option in `//5.` to uncomment and test the `set()` function.


``` c++

function main()

  var myState = State<Int32>("contract_owner_balance", 0);
  // 1. print empty state
  print("1: ");
  printLn(toString(myState.get()));
  // PRINTS 0

  // 2. change state inside main
  myState.set(33);
  print("2: ");
  printLn(toString(myState.get()));
  // PRINTS 33

  change_state(myState);
  // 3. print state after change_state call
  print("3: ");
  printLn(toString(myState.get()));
  // PRINTS 100

  var result = query();
  // 4. print state after query call - notice how query function doesn't change state of the original
  print("4: ");
  printLn(toString(result));
  // PRINTS 100

  // 5. alter comments in query method to see that state value is not alterable even though
  // accessible from another function
  // print("5: ");
  // printLn(toString(result));
  // printLn(toString(myState.get()));
  // PRINTS 55

endfunction



function change_state(state : State<Int32>)

  // you can pass around a State parameter and get access to the original state
  var newState = state;
  newState.set(100);

  // this has no effect on the original State
  var anotherState = State<Int32>("balance", 42);

endfunction


function query() : Int32

  // this gives a default value
  var myState = State<Int32>("balance", 0);

  // 4. this returns 100
  return myState.get();

  // 5. 
  // If you set a new variable into the state, it will return the new variable 
  // myState.set(55);
  // return myState.get();

endfunction


```

## Non-primitive types

A common use for the `State` type is to represent account owner `Address` types with their respective balances. To this end, you can declare a `State` where the first parameter is an `Address` type.

In the code below we first create an `Address` type. We can then define the transaction sender account wrapped in a `State` type where the first parameter `from` is the `Address` we just created and the second parameter is the account balance in `UInt64`:

``` c++
function main()

  var from = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
  var from_account = State<UInt64>(from, 0u64);

endfunction
```


<br/>


