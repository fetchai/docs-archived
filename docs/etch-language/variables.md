<h1>Variables</h1>

`etch` is a statically-typed programming language. 

Declare a variable with the keyword `var`. Declare numeric values with literals where possible. You can also use an explicit type cast operation. See below for explicit type declaration rules.


[!comment]: <> (## Assignments TODO:)


## Naming

Variable naming follows the same rules as C++.

``` c++
function main()

    var ABC = 1;
    var abc = 2;
    var _abc = 3;
    // var *abc = 4; // error at '*', expected variable name
    // var 123 = 5; // error at '123', expected variable name
    var a123 = 6;
    var a_123 = 7;

endfunction
```





## Integers

Integers can be signed or unsigned and are *currently* restricted to the width range 8-256 bits (1 to 32 bytes).

They are declared as signed `Int8`, `Int16`, `Int32`, `Int64`, and unsigned `UInt8`, `UInt16`, `UInt32`, `UInt64`, `UInt256`.

Further, and in the same order, they can be declared with postfix literals `i8`, `i16`, `i32`, `i64`, `u8`, `u16`, `u32`, and `u64`. 

The `UInt256` label will be supplied in a future version.

`Int32` is the compiler default so you don't need to explicitly declare this type.

Below is a selection of example integer assignations.

``` c++
function main()

	// default signed 32 bit integer type
    var int32bit_default = 42;
    // declaring the variable type
    var int32bit : Int32 = -43;
    printLn(toString(int32bit_default));
    printLn(toString(int32bit));

endfunction
```

``` c++
function main()

    // assigning various signed integer types explicitly and with label
    var int8a = 0i8; 
    printLn(toString(int8a)); 
    var int8b : Int8 = -0i8; 
    printLn(toString(int8b)); 
    var int16a = 0i16; 
    printLn(toString(int16a)); 
    var int16b : Int16 = -1i16; 
    printLn(toString(int16b)); 

endfunction
```

``` c++
function main()

    // Int32 is default but can be explicit also
    var int32a = 0i32;
    printLn(toString(int32a));
    var int32b : Int32 = -1i32;
    printLn(toString(int32b));
    var int64a = 0i64;
    printLn(toString(int64a));
    var int64b : Int64 = -1i64; 
    printLn(toString(int64b));

endfunction
```

``` c++
function main()

    // assigning various unsigned integer types
    var uint8a = 45u8; 
    printLn(toString(uint8a)); 
    var uint8b : UInt8 = 1u8; 
    printLn(toString(uint8b)); 
    var uint16a = 0u16; 
    printLn(toString(uint16a)); 
    var uint16b : UInt16 = 1u16; 
    printLn(toString(uint16b)); 

endfunction
``` 

``` c++
function main()

    // assigning various unsigned integer types
    var uint32a = 0u32;
    printLn(toString(uint32a));
    var uint32b : UInt32 = 1u32; 
    printLn(toString(uint32b));
    var uint64a = 0u64;
    printLn(toString(uint64a));
    var uint64b : UInt64 = 1u64;
    printLn(toString(uint64b)); 

endfunction
```

## 32 byte unsigned integer

Build a `UInt256` from a `UInt64` literal, like this:

``` c++
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

## Floats

Signed and unsigned decimal numbers are available as floating point types in 32 and 64 bit representation (4 and 8 bytes).

Float types are declared as `Float32`, `Float64`.

Unspecified floats default to `Float64`. 

A `Float` declared with `f` is a `Float32`.


``` c++
function main()

	// default 64 bit float declaration
	var float64bit_default = 64.0;
	// 64 bit type declaration
	var float64bit : Float64 = 64.0;
	printLn(toString(float64bit_default));
	printLn(toString(float64bit));

	// var float32bit : Float32 = 32.0; // error: incompatible types
	// declare 32 bit float with `f`
	var float32bit = 32.0f;
	printLn(toString(float32bit));

endfunction
```


## Fixed Points

Fixed point variables are available as  `Fixed32` and `Fixed64` types.

You must declare `FixedPoint` variables with the postfix literals `fp32` and `fp64`.



``` c++
function main()

    var fixed32bit : Fixed32 = 32.1fp32; 
    var fixed64bit : Fixed64 = 64.1fp64; 

    printLn(toString(fixed32bit));
    printLn(toString(fixed64bit));

endfunction

```

For brevity, you do not need the full declaration.

``` c++
function main()

    var fixed32bit = 2.0fp32;
    var fixed64bit = 3.0fp64;

    printLn(toString(fixed32bit));
    printLn(toString(fixed64bit));

endfunction
```

## Boolean

Declare and initialise `Bool` types as follows:

``` c++
function main()

	var myFBool : Bool = false;
	var myTBool : Bool = true;
	
	printLn(toString(myFBool)); 
	printLn(toString(myTBool)); 	

endfunction
```


## Strings

Declare and initialise strings as follows:

``` c++
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


``` c++
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

``` c++
function main()

    var myBuffer = Buffer(8);

endfunction
```

Currently, a `Buffer` is the *medium* for transport/exchange of data between other types, such as `SHA256` and `UInt256`. 

A parallel representation is the `Array<UInt8>` type.




## Maps

Declare the dictionary `Map` type with `Map<KeyType, ValueType>()`.

The function `count()` returns an `Int32` value representing the number of entries in the `Map`.

``` c++
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

!!! note
    Coming soon: common `Map` operations.
    

## StructuredData

A `StructuredData` type is another map type containing key/value pairs. 

Declare a `StructuredData` type with `StructuredData()`.

The `StructuredData` type has no appreciable size limit. Keys must be strings. Duplicate keys are allowed and override the most recent entry.

Values can be any primitive, string, or array of primitives.

An important difference to the `Map` type is that a `StructuredData` type can generate `yaml`, `json`, or similar.

``` c++
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

!!! note
	Coming soon: `Matrix` type with common matrix operations.

Declare the `Matrix` type with `Matrix<ElementType>(Rows, Cols)`.

``` c++
function main()

	// var myMatrix : Matrix<Int32>(5, 5); // error at '(', expected '=' or ';'
	// Failed to compile.

endfunction
```
-->



## State

A `State` is a data structure used by `etch` smart contracts for storing and querying data on the Fetch.AI Ledger shards. 

Unique identifiers for the ledger data are created at `State` construction time. These are unique to the smart contract alone.

Declare and initialise a `State` type with `State<ValueType>("ledger_identifier")`.

``` bash
function main()

    var myState = State<Int32>("account");

endfunction
```

Getters and setters are available for `State` types.

In the example, values set with the `set()` function map to the unique ledger identifier`account`.

``` c++
function main()

    var myState = State<Int32>("account");
    myState.set(10);
    printLn("My state var value = " + toString(myState.get()));

endfunction
```

Find out more about `etch` States <a href="./../states" target=_blank>here</a>.




## ShardedState

Like `State`, a `ShardedState` is also used for reading and writing data to the Fetch.AI Ledger.

`ShardedState` manipulates `State` types behind the scenes but, for `etch` programmer purposes, a `ShardedState` operates like a Map with key/vlue pairs.

Keys must be either `String` or `Address` types.

Value types must be declared at construction time.

Declare and initialise a `ShardedState` with `ShardedState<ValueType>("ledger_identifier")`.

Call `set()` on it to create a key/value pair. 

Print a value using `get()` with a key and a default value.

``` c++
function main()

    var myShardedState = ShardedState<Int32>("account1");
    myShardedState.set("salary", 45000i32);
    printLn(toString(myShardedState.get("salary", 0i32)));

endfunction

```

Find out more about `etch` ShardedStates <a href="./../sharded-state" target=_blank>here</a>.



## Address

The cryptographic `Address` type is currently represented by a 64 byte binary canonical <a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm" target="_blank">ECDSA public key</a> which is then base 58 encoded. 

Declare and initialise an `Address` like this:

``` c++
function main()

  var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");

endfunction
```

Find out more about the `etch` `Address` type <a href="./../addresses" target=_blank>here</a>.



## Mathematical, ML, and AI

`etch` provides powerful mathematical, machine learning, and AI specific data types and functions. 

For more details on the mathematical computation functions above, please check the section on maths functions <a href="./../maths-functions" target=_blank>here</a>.

For more details on the machine learning implementations, please check the section on machine learning functions <a href="./../ml-functions" target=_blank>here</a>.



## Type casting

There is no implicit type casting in `etch`.

If you need a specific non-default numerical type, you can make an explicit cast of the default `Int32` and `Float64` types.

Use `to<Type>Name(variable_to_cast)`. 


 
``` c++
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


    // float casting
    var float64bit = 42.0;
    // cast Float64 to Int32
    var intFVariable = toInt32(float64bit);
    // cast Float64 to Float32
    var float32Variable = toFloat32(float64bit);
    // cast Int32 to Float64
    var float64variable = toFloat64(int32bit);


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

!!! note
	Coming soon: support for constants.
-->


## Data size

In the table below, we detail the memory size of each data type.

Type | Memory size 
------------ | ------------- 
Int8 | 1 byte 
Int16 | 2 bytes 
Int32 | 4 bytes  
Int64 | 8 bytes   
UInt8 | 1 byte 
UInt16 | 2 bytes 
UInt32 | 4 bytes   
UInt64 | 8 bytes 
UInt256 | 32 bytes 
Float32 | 4 bytes 
Float64 | 8 bytes 
Bool | 1 byte 
String | 8 bytes + length character size (changing with UTF-8) 
Array | 8 bytes + length x element size 
Map | 8 bytes +  n x (key + value) storage 
StructuredData | tbc
State | tbc
ShardedState | tbc
Address | 32 bytes 


Currently, there is a 2 unit charge per 1 byte of ledger storage.


## Scope

`etch` has no global variables.

However, values store on the Fetch.AI Ledger can be considered global. 



## Null

Non-primitives can be set to null. 

``` c++
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


Type | Default value 
------------ | ------------- 
Int8 | tbc 
Int16 | tbc  
Int32 | 0  
Int64 | 0  
UInt8 | tbc 
UInt16 | tbc 
UInt32 | 0  
UInt64 | 0 
UInt256 | tbc
Float32 | 0.000000
Float64 | 0.000000
Bool | false
String | no default


<br/>




