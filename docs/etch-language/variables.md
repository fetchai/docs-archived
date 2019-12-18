<h1>Variables</h1>

`etch` is a statically-typed programming language.

The behaviour of value and reference types (primitives and non-primitives in Java) is the same as in other high level languages such as C++, Java, .Net, and Python.

Declare a variable with the keyword `var`.

Declare numeric values with literals where possible.

[!comment]: <> (## Assignments TODO:)

## Naming

Variable naming follows the same rules as C++.

```c++
function main()

    var ABC = 0;
    var abc = 1;
    var _abc = 2;
    // var *abc = 3; // error at '*', expected variable name
    // var 123 = 4; // error at '123', expected variable name
    var a123 = 5;
    var a_123 = 6;

endfunction
```

## Integers

Integers can be signed or unsigned and are _currently_ restricted to the width range 8-256 bits (1 to 32 bytes).

They are declared as signed `Int8`, `Int16`, `Int32`, `Int64`, and unsigned `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt256`.

Further, and in the same order, they can be declared with postfix literals `i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, and `u64`.

The `UInt256` label will be supplied in a future version.

`Int32` is the compiler default so you don't need to explicitly declare this type.

!!! Warn
Negative unsigned integers are dealt with in the same way C++ deals with them. They return a positive wrapped result dependent on size.

Below is a selection of example integer assignations.

```c++
function main()

	// declaring the default signed positive 32 bit integer type
    var int32bit_default = 42;
    // declaring negative value
    var int32bit : Int32 = -42;
    printLn(toString(int32bit_default));
    printLn(toString(int32bit));

endfunction
```

```c++
function main()

    // assigning various signed integer types explicitly and with label
    var int8a = 0i8;
    printLn(toString(int8a));
    var int8b : Int8 = -1i8;
    printLn(toString(int8b));
    var int16a = 2i16;
    printLn(toString(int16a));
    var int16b : Int16 = -3i16;
    printLn(toString(int16b));

endfunction
```

```c++
function main()

    // Int32 is default but can be explicit also
    var int32a = 0i32;
    printLn(toString(int32a));
    var int32b : Int32 = -1i32;
    printLn(toString(int32b));
    var int64a = 2i64;
    printLn(toString(int64a));
    var int64b : Int64 = -3i64;
    printLn(toString(int64b));

endfunction
```

```c++
function main()

    // assigning various unsigned integer types
    var uint8a = 0u8;
    printLn(toString(uint8a));
    var uint8b : UInt8 = 1u8;
    printLn(toString(uint8b));
    var uint16a = 2u16;
    printLn(toString(uint16a));
    var uint16b : UInt16 = 3u16;
    printLn(toString(uint16b));

endfunction
```

```c++
function main()

    // assigning various unsigned integer types
    var uint32a = 0u32;
    printLn(toString(uint32a));
    var uint32b : UInt32 = 1u32;
    printLn(toString(uint32b));
    var uint64a = 2u64;
    printLn(toString(uint64a));
    var uint64b : UInt64 = 3u64;
    printLn(toString(uint64b));

endfunction
```

## 32 byte unsigned integer

Build a `UInt256` from a `UInt64` literal, like this:

```c++
function main()

    var uint256 = UInt256(100u64);
    printLn(toString(uint256));

endfunction
```

`UInt256` variables are printed in hexadecimal for brevity.

<!--
Due to the underlying C++ implementation, you can also build `UInt256` with a string:

``` c++
function main()

    var uint256 = UInt256("hello world");
    printLn(toString(uint256));

endfunction
```

However, be careful, as any string larger than 32 bytes will be truncated. This presents the possibility that two unique strings could be regarded as equal. This gotcha will be fixed in the next release.
-->

## Fixed point decimals

Low and high precision calculations can be performed by the use of Fixed point types. Fixed point variables are available as `Fixed32`, `Fixed64` and Fixed128 types. Fixed point types use the 

You must declare Fixed Point variables with the postfix literals `fp32`, `fp64` and `fp128`.

```c++
function main()

    var fixed32bit  : Fixed32  = 32.1fp32;
    var fixed64bit  : Fixed64  = 64.1fp64;
    var fixed128bit : Fixed128 = 64.1fp128;

    printLn(toString(fixed32bit));
    printLn(toString(fixed64bit));
    printLn(toString(fixed128bit));

endfunction
```

For brevity, you do not need the full declaration.

```c++
function main()

    var fixed32bit  = -32.0fp32;
    var fixed64bit  = -64.0fp64;
    var fixed128bit = -128.0fp128;

    printLn(toString(fixed32bit));
    printLn(toString(fixed64bit));
    printLn(toString(fixed128bit));

endfunction
```

Make sure you are aware of the precision limits for fixed point decimals in `etch`.

| Type     |               Minimum value               |             Maximum value                |
| -------- | ----------------------------------------- | ---------------------------------------- |
| Fixed32  |               -32766.9999                 |               32766.9999                 |
| Fixed64  |          -2147483646.999999999            |          2147483646.999999999            |
| Fixed128 | -9223372036854775806.10000000000000000000 | 9223372036854775806.10000000000000000000 |

For up to date information tolerance, maximum exponent, and number of decimal places for fixed point types, please check the <a href="https://github.com/fetchai/ledger/blob/master/libs/vectorise/include/vectorise/fixed_point/fixed_point.hpp#L69" target=_blank>comments</a>.

## Boolean

Declare and initialise `Bool` types as follows:

```c++
function main()

	var myFBool : Bool = false;
	var myTBool : Bool = true;

	printLn(toString(myFBool));
	printLn(toString(myTBool));

endfunction
```

## Strings

Declare and initialise strings as follows:

```c++
function main()

    var myString : String = "hello";
    var myInferredString = "hello again";
    var x: String = null;

    printLn(myString);
    printLn(myInferredString);
    printLn(myInferredString + " " + myString);
    printLn(x);

endfunction
```

Find out more about `etch` Strings <a href="./../strings" target=_blank>here</a>.

## Arrays

You must explicitly declare array element types and array size.

`Array<Type>(size)` declares an array with elements of type `Type` and size `size`.

```c++
function main()

    var myArray = Array<Int32>(5);
    myArray[0] = 40;
    myArray[1] = 41;
    myArray[2] = 42;
    myArray[3] = 43;
    myArray[4] = 44;

    printLn(toString(myArray[3]));

    for (i in 0:5)
        printLn(toString(myArray[i]));
    endfor

    printLn(myArray);

endfunction
```

Find out more about `etch` Arrays <a href="./../arrays" target=_blank>here</a>.

## Buffer

Create a `Buffer` byte array type like this, where the `Buffer` size is defined by a `UInt32` type.

```c++
function main()

    var myBuffer = Buffer(8);

endfunction
```

A `Buffer` is the medium for data transport/exchange between other types, such as `SHA256` and `UInt256`.

A parallel representation is the `Array<UInt8>` type.

## Maps

Declare the dictionary `Map` type with `Map<KeyType, ValueType>()`.

A duplicate key overrides the previous duplicate entry.

The function `count()` returns an `Int32` value representing the number of entries in the `Map`.

```c++
function main()

    var myMap = Map<String, Int32>();
    myMap["balance1"] = 1000;
    myMap["balance2"] = 2000;
    myMap["balance3"] = 3000;

    printLn(toString(myMap["balance1"]));
    printLn(toString(myMap["balance2"]));
    printLn(toString(myMap["balance3"]));

    printLn(toString(myMap.count()));

endfunction
```

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Coming soon: common `Map` operations.</p>
</div>

## StructuredData

`StructuredData` is another Map type containing key/value pairs.

Declare a `StructuredData` type with `var variable_name = StructuredData();`.

Add key/value pairs with the `variable_name.set(key, value);` function.

-   There is no appreciable size limit.

-   Keys must be strings.

-   No duplicate keys allowed.

-   A duplicate key overrides the previous duplicate entry.

-   Values can be any primitive, string, or array of primitives.

An important difference to the `Map` type is that a `StructuredData` type can generate `yaml`, `json`, or similar.

```c++
function main()

    var data = StructuredData();

    data.set("key1", 200i32);
    data.set("key2", 500u64);
    data.set("key3", "hello world");

    printLn(toString(data.getInt32("key1")));
    printLn(toString(data.getUInt64("key2")));
    printLn(data.getString("key3"));

endfunction

```

<!--
## Matrices

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Coming soon: `Matrix` type with common matrix operations.</p>
</div>

Declare the `Matrix` type with `Matrix<ElementType>(Rows, Cols)`.

``` c++
function main()

	// var myMatrix : Matrix<Int32>(5, 5); // error at '(', expected '=' or ';'
	// Failed to compile.

endfunction
```
-->

## State

A `State` is a data structure used by `etch` smart contracts for storing and querying data on the Fetch.ai Ledger shards.

Unique identifiers for the ledger data are created at `State` construction time. These are unique to the smart contract alone.

Declare and initialise a `State` type with `State<ValueType>("ledger_identifier")`.

```bash
function main()

    var myState = State<Int32>("account");

endfunction
```

Getters and setters are available for `State` types.

In the example, values set with the `set()` function map to the unique ledger identifier`account`.

```c++
function main()

    var myState = State<Int32>("account");
    myState.set(10);
    printLn("My state var value = " + toString(myState.get()));

endfunction
```

Find out more about `etch` States <a href="./../states" target=_blank>here</a>.

## ShardedState

Like `State`, a `ShardedState` is also used for reading and writing data to the Fetch.ai Ledger.

`ShardedState` manipulates `State` types behind the scenes but, for `etch` programmer purposes, a `ShardedState` operates like a Map with key/value pairs.

-   Keys must be either `String` or `Address` types.

-   Value types are declared at construction time.

-   No duplicate keys allowed.

-   A duplicate key overrides the previous duplicate entry.

Declare and initialise a `ShardedState`.

```c++
var my_sharded_state = ShardedState<ValueType>("ledger_identifier")
```

Call `set()` on it to create a key/value pair.

Print a value using `get()` with a key and a default value.

```c++
function main()

    var myShardedState = ShardedState<Int32>("account1");
    myShardedState.set("salary", 45000i32);
    printLn(toString(myShardedState.get("salary", 0i32)));

endfunction

```

Find out more about `etch` `ShardedState` types <a href="./../sharded-state" target=_blank>here</a>.

## Address

The cryptographic `Address` type is currently represented by a 64 byte binary canonical <a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm" target="_blank">ECDSA public key</a> which is then base 58 encoded.

Declare and initialise an `Address` like this:

```c++
function main()

  var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");

endfunction
```

Find out more about the `etch` `Address` type <a href="./../addresses" target=_blank>here</a>.

## Mathematical, ML, and AI

`etch` provides powerful mathematical, machine learning, and AI specific data types and functions.

For more details on the mathematical computation functions above, please check the section on maths functions <a href="./../maths-functions" target=_blank>here</a>.

For more details on the machine learning implementations, please check the section on machine learning functions <a href="./../graph" target=_blank>here</a>.

## Type casting

There is no implicit type casting in `etch`.

If you need a specific non-default numerical type, you can make an explicit cast of the default `Int32` and `Fixed64` types.

Use `to<Type>Name(variable_to_cast)`.

```c++
function main()

    // signed 32 bit integer type
    var int32bit = 42;
    // cast to Int8
    var int8Variable = toInt8(int32bit);
    // cast to Int16
    var int16Variable = toInt16(int32bit);
    // cast to Int64
    var int64Variable = toInt64(int32bit);
    // cast to UInt8
    var uint8Variable = toUInt8(int32bit);
    // cast to UInt16
    var uint16Variable = toUInt16(int32bit);
    // cast to UInt32
    var uint32Variable = toUInt32(int32bit);
    // cast to UInt64
    var uint64Variable = toUInt64(int32bit);
    // cast to UInt256
    // var uint256Variable = toUInt256(int32bit); // coming soon


    // fixed point casting
    var fixed32 : Fixed32 = 32.1fp32;
    var fixed64 : Fixed64 = 64.1fp64;
    // cast Fixed32 to Int32
    var int32var = toInt32(fixed32);
    // cast Fixed64 to Fixed32
    var fixed32Variable = toFixed32(fixed64);
    // cast Int32 to Fixed64
    var fixed64variable = toFixed64(int32bit);


    // cast to string
    var stringVariable = toString(int32bit);

endfunction
```

<!--

## Constants

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Coming soon: support for constants.</p>
  </div>
-->

## Data size

In the table below, we detail the memory size of each data type.

!!! Warning
Currently, the `const` value cannot be given precisely and varies depending on whether we are talking about _in-memory_ or _in-permanent_ size.

For more information on the integer size ranges, please see the <a href="https://github.com/msgpack/msgpack/blob/master/spec.md#int-format-family" target=_blank>MessagePack specification</a>.

| Type             | Memory size                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| `Int8`           | `1-2 byte`                                                                  |
| `Int16`          | `1-3 bytes`                                                                 |
| `Int32`          | `1-5 bytes`                                                                 |
| `Int64`          | `1-9 bytes`                                                                 |
| `UInt8`          | `1-2 byte`                                                                  |
| `UInt16`         | `1-3 bytes`                                                                 |
| `UInt32`         | `1-5 bytes`                                                                 |
| `UInt64`         | `1-9 bytes`                                                                 |
| `UInt256`        | `32 bytes`                                                                  |
| `Fixed32`        | `4 bytes`                                                                   |
| `Fixed64`        | `8 bytes`                                                                   |
| `Fixed128`       | `16 bytes`                                                                   |
| `Bool`           | `1 byte`                                                                    |
| `String`         | `len(string) + const`                                                       |
| `Array`          | `len(Array<Type>) * sizeof(Type) + const`                                   |
| `Map`            | `len(Map<K, V>) * (sizeof(KeyType) + sizeof(ValueType)) + const`            |
| `StructuredData` | `len(StructuredData<K, V>) * (sizeof(KeyType) + sizeof(ValueType)) + const` |
| `State`          | `sizeof(Type) + const`                                                      |
| `ShardedState`   | `len(ShardedState<K, V>) * (sizeof(KeyType) + sizeof(ValueType)) + const`   |
| `Address`        | `32 bytes`                                                                  |

## Scope

`etch` scripts have no traditional global variables. They do, however, have persistent global types that represent any `State` or `ShardedState` type residing on the Fetch.ai Ledger.

Find out more about persistent global types <a href="/etch-language/persistent-globals/" target=_blank>here.</a>

## Null

Reference types can be set to null.

```c++
function main()

    //  var myInt = null; // error: unable to infer type
    var str : String = null;
    var myArray : Array<Int32> = null;
    var myMap : Map<Int32, Int32> = null;
    var myState : State<Int32> = null;
    var myAddress : Address = null;

    var myString : String = null;
    printLn(myString); // (nullptr)

endfunction
```

## Default values

Certain types not explicitly initialised receive a default value.

| Type     | Default value |
| -------- | ------------- |
| Int8     | 0             |
| Int16    | 0             |
| Int32    | 0             |
| Int64    | 0             |
| UInt8    | 0             |
| UInt16   | 0             |
| UInt32   | 0             |
| UInt64   | 0             |
| UInt256  | tbc           |
| Fixed32  | 0.0           |
| Fixed64  | 0.0           |
| Fixed128 | 0.0           |
| Bool     | false         |
| String   | no default    |

<br/>
