<h1>Variables</h1>

`etch` is a statically-typed programming language. For good coding practice, you should explicitly declare all variable types.

Declare a variable with the keyword `var`. Declare numeric values with literals where possible. You can also use an explicit type cast operation. See below for explicit type declaration rules.

Any numerical variable not explicitly initialised receives a default value, such as `0` for integers and `0.0` for floats.

[comment]: <> (To clarify: how a default value is added to a variable, with a scenario and an example.)

!!! warning
	The `toString` function does not yet support all variable types.



## Integers

Integers can be signed or unsigned and are *currently* restricted to the width range 8-64 bits.

They are declared as signed `Int8`, `Int16`, `Int32`, `Int64`, and unsigned `UInt16`, `UInt32`, `UInt64`.

`Int32` is the compiler default so you don't need to explicitly declare this type.

Initialise an 8 bit unsigned integer with a `Byte` type. 

Below is a selection of example integer assignations including any errors on operations currently unsupported.

``` java
function main()

	// default signed 32 bit integer type
    var int32bit_default = 42;
    // declaring the variable type
    var int32bit : Int32 = -43;
    printLn(toString(int32bit_default));
    printLn(toString(int32bit));

endfunction
```

``` java
function main()

    // assigning various signed integer types explicitly and with label
    var int8a = 0i8; 
    // printLn(toString(int8a)); // error: unable to find matching function for 'toString'
    var int8b : Int8 = -0i8; 
    // printLn(toString(int8b)); // error: unable to find matching function for 'toString'
    var int16a = 0i16; 
    // printLn(toString(int16a)); // error: unable to find matching function for 'toString'
    var int16b : Int16 = -1i16; 
    // printLn(toString(int16b)); // error: unable to find matching function for 'toString'

endfunction
```

``` java
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

``` java
function main()

    // assigning various unsigned integer types
    var uint8a = 45u8; 
    // printLn(toString(uint8a));   // error: unable to find matching function for 'toString'
    // var uint8b : UInt8 = 1u16; // error: unknown type 'UInt8'
    var uint16a = 0u16; 
    // printLn(toString(uint16a)); // error: unable to find matching function for 'toString'
    var uint16b : UInt16 = 1u16; 
    // printLn(toString(uint16b)); // error: unable to find matching function for 'toString'

endfunction
``` 

``` java
function main()

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


## Floats

Signed and unsigned decimal numbers are available as floating point types in 32 and 64 bit representation.

!!! note
	Fixed point variables  `Fixed32` and `Fixed64` are coming soon.

Unspecified floats default to `Float64`. 

A `Float` declared with `f` is `Float32`.

Float types are declared as `Float32`, `Float64`.

``` java
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

	// fixed point types - wip
	// var fixed32bit : Fixed32 = 32.1; // error: unknown type 'Fixed32'
	// var fixed64bit : Fixed64 = 64.1; // error: unknown type 'Fixed64'

endfunction
```


## Byte - to be deprecated

Declare and initialise an 8 bit unsigned integer with the `Byte` type.

``` java
function main()

	// unsigned 8 bit integer type
	// var uint8bit : Byte = 42u8; // error: internal error at '42u8'
    // printLn(toString(uint8bit)); // error: unable to find matching function for 'toString'

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

``` java
function main()

	var myString : String = "hello";
	var myInferredString = "hello again";
	var x: String = null;

	printLn(myString);
	printLn(myInferredString);
	printLn(myInferredString + " " + myString);
	// printLn(toString(x)); // error: unable to find matching function for 'toString'

endfunction
```

Find out more about `etch` Strings [here](strings.md).


## Arrays

!!! note
	Coming soon: common `Array` operations.

[comment]: <> (<a href="https://github.com/uvue-git/fetch-ledger/issues/812" target=_blank>https://github.com/uvue-git/fetch-ledger/issues/812</a>)

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

	for (i in 0:4)
		printLn(toString(myArray[i]));
	endfor

endfunction
```

Find out more about `etch` Arrays [here](arrays.md).



## Maps

!!! note
	Coming soon: common `Map` operations.

Declare the dictionary `Map` type with `Map<KeyType, ValueType>`.

``` c++
function main()

	var myMap : Map<String, Int32>;
	// myMap["balance1"] = 1000; // runtime error: line 5: null reference
    // myMap["balance2"] = 2000; // runtime error: line 6: null reference
    // myMap["balance3"] = 3000; // runtime error: line 7: null reference

    // TODO:
    // var myMapState = State<Map<String, Int32>>(myMap, null); // error: unable to find matching constructor for type/function 'State<Map<String, Int32>>'

endfunction
```



## Matrices

!!! note
	Coming soon: `Matrix` type with common matrix operations.

Declare the `Matrix` type with `Matrix<ElementType>(Rows, Cols)`.

``` java
function main()

	// var myMatrix : Matrix<Int32>(5, 5); // error at '(', expected '=' or ';'
	// Failed to compile.

endfunction
```



## States 

A `State` is a data structure used by `etch` Smart Contracts for storing and querying data on the ledger. The data stored by a `State` is held on shards on the ledger. 

Declare and initialise a `State` type with `State<ValueType>` where values are mapped to a key:

`var myState = State<Int32>("var", 200);`

Getters and setters are available for `State` types.

``` c++
function main()

	var myState = State<Int32>("var", 200);
	myState.set(10);
	printLn("My state var value = " + toString(myState.get()));

endfunction
```

Currently, the `State` type supports primitive types only.

Find out more about `etch` States [here](states.md).




## PersistentMap

!!! note
	Coming soon: `PersistentMap` full implementation.

The `PersistentMap` type is similar to `State` but more flexible.

Declare a `PersistentMap` with `PersistentMap<K, V>` where `K` is the key and `V` is the value. 

Note that `K` must be a `String` or an `Address` type.

``` java
function main()

	// var myPm : PersistentMap<String, Int32>; 
	// error at '<', expected '=' or ';'
	// Failed to compile.

endfunction
```

Find out more about `etch` PersistentMaps [here](persistent-maps.md).




## Addresses

The cryptographic `Address` type is currently represented by a 64 byte binary canonical <a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm" target="_blank">ECDSA public key</a>. 

Declare and initialise an `Address` like this:

``` c++
function main()

    var myAddress = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+Pw==");

endfunction
```

Find out more about `etch` Addresses [here](addresses.md).



## Mathematical, ML, and AI

!!! note
	Coming soon: full implementation of mathematical, machine learning, and AI libraries.

`etch` has powerful mathematical, machine learning, and AI specific data types and processes. 

For example, `etch` provides a number of powerful data types such as `Graph`, `Tensor`, `TrainingPair`, and `CrossEntropy`.

We will look at these more complex data structures in a later section.



## Type casting

If you need a specific non-default numerical type, you can make an explicit cast of the default `Int32` and `Float64` types.

Use `to<Type>Name` to type cast. 

There is no implicit type casting in `etch`.

!!! warning
	`toString` is not currently universal.
 
``` c++
function main()

    // signed 32 bit integer type
    var int32bit = 42;
    // cast to byte
    var byteVariable = toByte(int32bit);
    // cast to Int8
    var int8Variable = toInt8(int32bit);
    // cast to Int16
    var int16Variable = toInt16(int32bit);
    // cast to Int64
    var int64Variable = toInt64(int32bit);
    // cast to UInt8
    // var uint8Variable = toUInt8(int32bit); // error: unknown symbol 'toUInt8'
    // cast to UInt16
    var uint16Variable = toUInt16(int32bit);
    // cast to UInt32
    var uint32Variable = toUInt32(int32bit);
    // cast to UInt64
    var uint64Variable = toUInt64(int32bit);

    //cast to Byte
    var mybyte = toByte(5);

    // float casting
    var float64bit = 42.0;
    // cast to byte
    var byteFVariable = toByte(float64bit);
    // cast to Int8
    var intFVariable = toInt32(float64bit);
    // cast to Float32
    var float32Variable = toFloat32(mybyte);
    // cast to Float64
    var float64variable = toFloat64(mybyte);

    // cast to string
    var stringVariable = toString(int32bit);

endfunction
```
 

## Constants

!!! note
	Coming soon: support for constants.



## Data measures

In the table below, we detail the exact memory size of each data type when added to the network.

!!! note 
	Coming soon: details on memory used on the ledger per variable type plus relative cost.


<table align="center" style="font-family: monospace;">
	<tr style="font-family: sans-serif;">
        <th align="center">Data type</th>
        <th align="center">Memory etched upon the ledger</th>
    </tr>
    <tr>
        <td align="center">Int8</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Int16</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Int32</td>
        <td align="center"></td>
    </tr>
     <tr>
        <td align="center">Int64</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Byte</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">UInt16</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">UInt32</td>
        <td align="center"></td>
    </tr>
     <tr>
        <td align="center">UInt64</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Float32</td>
        <td align="center"></td>
    </tr>
     <tr>
        <td align="center">Float64</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Bool</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">String</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Array</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Map</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Matrix</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">State</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">PersistentMap</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Address</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">Null</td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center">etc.</td>
        <td align="center"></td>
    </tr>
</table>



## Scope

`etch` has no global variables. 



## Null

Non-primitives can be set to null. 

!!! note
	You cannot print a null value.

``` java
function main()

	//  var myInt = null; // error: unable to infer type
	var str : String = null;
	var myArray : Array<Int32> = null;
	var myMap : Map<Int32, Int32> = null;
	var myState : State<Int32> = null;
	var myAddress : Address = null;

	var myString : String = null;
	// printLn(myString); // Segmentation fault: 11	

endfunction
```

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

Naming conventions are up to you. 







