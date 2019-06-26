<h1>Maths libraries and functions</h1>


In the current version, `release/v0.4.x`, the following maths functions are available:

## Logarithm

Natural log values are currently available for `UInt256` types only.

``` c++
function main()

     var int32 = 32;
     // var logI = int32.logValue(); // error: primitive type 'Int32' does not support member-access operator

     var uint256 = UInt256(256u64);
     var logY = uint256.logValue();
     printLn(logY); // prints -inf

endfunction

```

In a future release, log values will be available for all types as well as in base 2 and 10.



## Absolute value

`Abs()` returns the absolute value of an `Int32` or a `Float64`.

``` c++
function do_abs(value: Int32)

  printLn("Abs of " + toString(value) + ": ");
  printLn(toString(Abs(value)));

endfunction

function do_abs(value: Float64)

  printLn("Abs of " + toString(value) + ": ");
  printLn(toString(Abs(value)));

endfunction


function main()

  // positive int 32
  var x_int = 1;
  do_abs(x_int);

  // negative int 32
  x_int = -1;
  do_abs(x_int);

  // positive float 64
  var x_float = 0.1123;
  do_abs(x_float);

  // negative float 64
  x_float = -7.151;
  do_abs(x_float);

endfunction

```


## Random (non deterministic)

You can currently generate non-deterministic, random, signed and unsigned integers and floats.

The beginning value of the range *must* be less than the end value.

``` c++
function main()

    // var randUInt8 = Rand(0u8, 1000u8); // error: unable to find matching function for 'Rand'
    // printLn(toString(randUInt8));

    // unpermitted range
    // var rand_test = Rand(100u16, 0u16); // runtime error: Invalid argument: Rand(a, b) must satisfy a < b

    var randUInt16 = Rand(0u16, 1000u16);
    // printLn(toString(randUInt16));

    var randUInt32 = Rand(0u32, 1000u32);
    printLn(toString(randUInt32));

    var randUInt64 = Rand(0u64, 1000u64);
    printLn(toString(randUInt64));

    // var randInt8 = Rand(0u8, 1000u8);
    // printLn(toString(randInt8));

    var randInt16 = Rand(0i16, 1000i16);
    // printLn(toString(randInt16));

    var randInt32 = Rand(0i32, 1000i32);
    printLn(toString(randInt32));

    var randInt64 = Rand(0i64, 1000i64);
    printLn(toString(randInt64));

    var randFloat32 = Rand(0.0f, 1000.0f);
    printLn(toString(randFloat32));

    var randFloat64 = Rand(0.0, 1000.0);
    printLn(toString(randFloat64));

endfunction
```

## Exponent

* exp - next release.



## Square root

* sqrt - next release.


## Trig

* trig functions - next release.

<!--

`etch` supports trigonometric functions `Sin`, `Cos`, and `Tan`.

``` c++
function main()

  var x = 1.0;
  printLn("sin of 1");
  printLn(toString(sin(x)));

  x = 0.5;
  printLn("sin of 0.5");
  printLn(toString(sin(x)));

  x = 0.0;
  printLn("sin of 0");
  printLn(toString(sin(x)));

  x = 1.0;
  printLn("cos of 1");
  printLn(toString(cos(x)));

  x = 0.5;
  printLn("cos of 0.5");
  printLn(toString(cos(x)));

  x = 0.0;
  printLn("cos of 0");
  printLn(toString(cos(x)));

  x = 1.0;
  printLn("tan of 1");
  printLn(toString(tan(x)));

  x = 0.5;
  printLn("tan of 0.5");
  printLn(toString(tan(x)));

  x = 0.0;
  printLn("tan of 0");
  printLn(toString(tan(x)));

endfunction
```

Also `ArcSin`, `ArcCos`, and `ArcTan`.

``` c++
function main()

  var x = 1.0;
  printLn("asin of 1");
  printLn(toString(asin(x)));

  x = 0.5;
  printLn("asin of 0.5");
  printLn(toString(asin(x)));

  x = 0.0;
  printLn("asin of 0");
  printLn(toString(asin(x)));

  x = 1.0;
  printLn("acos of 1");
  printLn(toString(acos(x)));

  x = 0.5;
  printLn("acos of 0.5");
  printLn(toString(acos(x)));

  x = 0.0;
  printLn("acos of 0");
  printLn(toString(acos(x)));

  x = 1.0;
  printLn("atan of 1");
  printLn(toString(atan(x)));

  x = 0.5;
  printLn("atan of 0.5");
  printLn(toString(atan(x)));

  x = 0.0;
  printLn("atan of 0");
  printLn(toString(atan(x)));

endfunction
```

And hyperbolic functions `Sin`, `Cos`, and `Tan`.

``` c++
function main()

  var x = 1.0;
  printLn("sinh of 1");
  printLn(toString(sinh(x)));

  x = 0.5;
  printLn("sinh of 0.5");
  printLn(toString(sinh(x)));

  x = 0.0;
  printLn("sinh of 0");
  printLn(toString(sinh(x)));

  x = 1.0;
  printLn("cosh of 1");
  printLn(toString(cosh(x)));

  x = 0.5;
  printLn("cosh of 0.5");
  printLn(toString(cosh(x)));

  x = 0.0;
  printLn("cosh of 0");
  printLn(toString(cosh(x)));

  x = 1.0;
  printLn("tanh of 1");
  printLn(toString(tanh(x)));

  x = 0.5;
  printLn("tanh of 0.5");
  printLn(toString(tanh(x)));

  x = 0.0;
  printLn("tanh of 0");
  printLn(toString(tanh(x)));

endfunction
```

And hyperbolic `ArcSin`, `ArcCos`, and `ArcTan`.

``` c++
function main()

  var x = 1.0;
  printLn("asinh of 1");
  printLn(toString(asinh(x)));

  x = 0.5;
  printLn("asinh of 0.5");
  printLn(toString(asinh(x)));

  x = 0.0;
  printLn("asinh of 0");
  printLn(toString(asinh(x)));

  x = 1.0;
  printLn("acosh of 1");
  printLn(toString(acosh(x)));

  x = 0.5;
  printLn("acosh of 0.5");
  printLn(toString(acosh(x)));

  x = 0.0;
  printLn("acosh of 0");
  printLn(toString(acosh(x)));

  x = 1.0;
  printLn("atanh of 1");
  printLn(toString(atanh(x)));

  x = 0.5;
  printLn("atanh of 0.5");
  printLn(toString(atanh(x)));

  x = 0.0;
  printLn("atanh of 0");
  printLn(toString(atanh(x)));

endfunction
```

-->

<br/>

