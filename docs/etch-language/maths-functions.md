<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>`Fixed64` is the default variable data type used by the `etch` mathematics and machine learning libraries.</p>
</div>

In the current version, and further to the common mathematical operations provided by the `etch` language already discussed <a href="../operators/" target=_blank>here</a>, the following functions are available.

## Absolute value

`abs()` returns the absolute value of all signed integer types.

```c++
function main()

    // 8 bit signed integers
    var int_8_bit = 1i8;
    printLn(toString(abs(int_8_bit)));

    var neg_int_8_bit = -1i8;
    printLn(toString(abs(neg_int_8_bit)));

    // 16 bit signed integers
    var int_16_bit = 1i16;
    printLn(toString(abs(int_8_bit)));

    var neg_int_16_bit = -1i16;
    printLn(toString(abs(neg_int_16_bit)));

    // 32 bit signed integers
    var int_32_bit = 1;
    printLn(toString(abs(int_32_bit)));

    var neg_int_32_bit = -1;
    printLn(toString(abs(neg_int_32_bit)));

    // 64 bit signed integers
    var int_64_bit = 1i64;
    printLn(toString(abs(int_64_bit)));

    var neg_int_64_bit = -1i64;
    printLn(toString(abs(neg_int_64_bit)));

endfunction
```

And positive unsigned integer types.

```c++
function main()

    // 8 bit unsigned integers
    var int_8_bit = 1u8;
    printLn(toString(abs(int_8_bit)));

    // 16 bit unsigned integers
    var int_16_bit = 1u16;
    printLn(toString(abs(int_8_bit)));

    // 32 bit unsigned integers
    var int_32_bit = 1u32;
    printLn(toString(abs(int_32_bit)));

    // 64 bit unsigned integers
    var int_64_bit = 1u64;
    printLn(toString(abs(int_64_bit)));

endfunction
```

And fixed point types.

```c++
function main()

    // 32 bit fixed point
    var fixed_32 = 1.0fp32;
    printLn(toString(abs(fixed_32)));

    var neg_fixed_32 = -1.0fp32;
    printLn(toString(abs(neg_fixed_32)));

    // 64 bit fixed point
    var fixed_64 = 1.0fp64;
    printLn(toString(abs(fixed_64)));

    var neg_fixed_64 = -1.0fp64;
    printLn(toString(abs(neg_fixed_64)));

    // 128 bit fixed point
    var fixed_128 = 1.0fp128;
    printLn(toString(abs(fixed_128)));

    var neg_fixed_128 = -1.0fp128;
    printLn(toString(abs(neg_fixed_128)));
endfunction
```

## Exponential function

The exponential function returns the value of `e` to the number given, <code>exp(x) = e<sup>x</sup></code> where `e` is Euler's base of natural logarithms.

The exponential function is limited to fixed point variables.

```c++
function main()

    var a = 2.0fp32;
    var b = 3.0fp64;
    var c = 4.0fp128;
    printLn(toString(exp(a)));
    printLn(toString(exp(b)));
    printLn(toString(exp(c)));

endfunction
```

### Range restrictions

`Fixed32` accuracy is limited within the range `[-10.3974, 10.3974]`.

`Fixed64` accuracy is limited within the range `[-21.48756260, 21.48756260]`.

`Fixed128` accuracy is limited within the range `[-43.6682723752765511, 43.6682723752765511]`.

Running the exponential function on numbers outside of this range produces unexpected results.

!!! Warning
If the implementation of a function depends on `exp()` then accuracy is limited within a range dependent on the implementation.

!!! Warning
For Fixed point types, take extra care because, even though the type has a reduced range, it has an increased accuracy within that range.

### Special cases

| Scenario      | Result                     |
| ------------- | :------------------------- |
| `x` is `NaN`  | `e^x = NaN`                |
| `x < MIN_EXP` | `e^x = 0`                  |
| `x > MAX_EXP` | `overflow_error exception` |
| `x == 1`      | `e^x = e`                  |
| `x == 0`      | `e^x = 1`                  |
| `x == -inf`   | `e^(-inf) = 0`             |
| `x == +inf`   | `e^(+inf) = +inf`          |
| `x < 0`       | `e^x = 1/e^(-x)`           |

### Errors for x ∈ (-10, 5)

-   `Fixed32`: average: `0.000178116`, max: `0.00584819`
-   `Fixed64`: average: `4.97318e-09`, max: `1.66689e-07`

<!-- commenting out while broken https://github.com/fetchai/ledger/issues/1383
## Logarithms

also: https://github.com/fetchai/ledger/blob/master/libs/vectorise/include/vectorise/fixed_point/fixed_point.hpp#L1901

Natural log values are currently available for `UInt256` types only with the `logValue()` member function.

``` c++
function main()

    var uint256 = UInt256(256u64);
    var logY = uint256.logValue();
    printLn(logY);

endfunction
```

In a future release, log values will be available for all types as well as in base 2 and 10.
-->

## Power

The power function returns the value of the first parameter raised to the second.

The power function is limited to fixed point variables.

```c++
function main()

    var a = 2.0fp64;
    var b = 3.0fp64;
    printLn(toString(pow(a, b)));

    var c = 4.0fp32;
    var d = 5.0fp32;
    printLn(toString(pow(c, d)));

    var e = 2.0fp128;
    var f = 3.0fp128;
    printLn(toString(pow(e, f)));

endfunction
```

!!! Warn
The `pow()` implementation depends on `exp()` so the range is limited. The implementation is as follows:

    `x^y = exp(y * log(x));`

### Special cases

| Scenario             | Result                    |
| -------------------- | :------------------------ |
| `x` or `y` is `NaN`  | `pow(x, y) = NaN`         |
| `x == 0`, `y == 0`   | `pow(x, y) = NaN`         |
| `x == 0`, `y != 0`   | `pow(x, y) = 0`           |
| `x any`, `y == 0`    | `pow(x, y) = 1`           |
| `x < 0`, `y non int` | `pow(x, y) = NaN`         |
| `x +/-inf`           | `pow(x, y) =`             |
| `x < 0`, `y int`     | `pow(x, y) = \prod_1^y x` |

### Errors for x ∈ (0, 100), y ∈ (0, 10.5)

-   `Fixed32`: average: `1.49365e-06`, max: `3.04673e-05`
-   `Fixed64`: average: `8.45537e-12`, max: `8.70098e-10`

### Errors for x ∈ (-10, 10), y ∈ (-4, 4)

-   `Fixed32`: average: `3.9093e-06`, max: `9.15527e-06`
-   `Fixed64`: average: `7.71863e-11`, max: `2.25216e-10`

## Random (non deterministic)

You can currently generate non-deterministic, random, signed and unsigned integers (not 8 bit types), and floats.

The beginning value of the range _must_ be less than the end value.

```c++
function main()

    //var randUInt8 = rand(0u8, 1000u8); // error: unable to find matching function for 'Rand'
    //printLn(toString(randUInt8));

    // unpermitted range
    // var rand_test = rand(100u16, 0u16); // runtime error: Invalid argument: rand(a, b) must satisfy a < b

    var randUInt16 = rand(0u16, 1000u16);
    printLn(toString(randUInt16));

    var randUInt32 = rand(0u32, 1000u32);
    printLn(toString(randUInt32));

    var randUInt64 = rand(0u64, 1000u64);
    printLn(toString(randUInt64));

    // var randInt8 = rand(0u8, 1000u8);
    // printLn(toString(randInt8));

    var randInt16 = rand(0i16, 1000i16);
    printLn(toString(randInt16));

    var randInt32 = rand(0i32, 1000i32);
    printLn(toString(randInt32));

    var randInt64 = rand(0i64, 1000i64);
    printLn(toString(randInt64));

    var randFixed32 = rand(0.0fp32, 1000.0fp32);
    printLn(toString(randFixed32));

    var randFixed64 = rand(0.0fp64, 1000.0fp64);
    printLn(toString(randFixed64));

endfunction
```

## Square root

The square root of a number is found with the `sqrt()` function.

The square root function is limited to fixed point variables.

```c++
function main()

    var a = 4.0fp32;
    var b = 49.0fp64;
    var c = 49.0fp128;
    printLn(toString(sqrt(a)));
    printLn(toString(sqrt(b)));
    printLn(toString(sqrt(c)));

endfunction
```

### Special cases

| Scenario     | Result              |
| ------------ | :------------------ |
| `x` is `NaN` | `sqrt(NaN) = NaN`   |
| `x == 1`     | `sqrt(x) = 1`       |
| `x == 0`     | `sqrt(x) = 0`       |
| `x < 0`      | `sqrt(x) = NaN`     |
| `x == +inf`  | `sqrt(+inf) = +inf` |

### Errors for x ∈ (0, 5)

-   `Fixed32`: average: `0.000863796`, max: `0.00368993`
-   `Fixed64`: average: `3.71316e-10`, max: `1.56033e-09`

## Trigonometry

### `Sin`, `Cos`, and `Tan`

```c++
function main()

    var x = 1.0fp64;
    printLn("sin of 1");
    printLn(toString(sin(x)));

    x = 0.5fp64;
    printLn("sin of 0.5");
    printLn(toString(sin(x)));

    x = 0.0fp64;
    printLn("sin of 0");
    printLn(toString(sin(x)));

    x = 1.0fp64;
    printLn("cos of 1");
    printLn(toString(cos(x)));

    x = 0.5fp64;
    printLn("cos of 0.5");
    printLn(toString(cos(x)));

    x = 0.0fp64;
    printLn("cos of 0");
    printLn(toString(cos(x)));

    x = 1.0fp64;
    printLn("tan of 1");
    printLn(toString(tan(x)));

    x = 0.5fp64;
    printLn("tan of 0.5");
    printLn(toString(tan(x)));

    x = 0.0fp64;
    printLn("tan of 0");
    printLn(toString(tan(x)));

endfunction
```

#### `Sin` special cases

| Scenario        | Result              |
| --------------- | :------------------ |
| `x` is `NaN`    | `sin(x) = NaN`      |
| `x` is `+/-inf` | `sin(x) = NaN`      |
| `x == 0`        | `sin(x) = 0`        |
| `x < 0`         | `sin(x) = -sin(-x)` |

#### Errors for x ∈ (-100 _ `Pi`/2, 100 _ `Pi`/2)

-   `Fixed32`: average: `0.000552292`, max: `0.108399`
-   `Fixed64`: average: `4.52891e-09`, max: `1.38022e-06`

#### `Cos` special cases

| Scenario      | Result         |
| ------------- | :------------- |
| `x` is `NaN`  | `cos(x) = NaN` |
| `x == +/-inf` | `cos(x) = NaN` |
| `x == 0`      | `cos(x) = 1`   |

#### Errors for x ∈ (-100 _ `Pi`/2, 100 _ `Pi`/2)

-   `Fixed32`: average: `0.000552292`, max: `0.108399`
-   `Fixed64`: average: `4.52891e-09`, max: `1.38022e-06`

#### `Tan` special cases

| Scenario     | Result             |
| ------------ | :----------------- |
| `x` is `NaN` | `tan(NaN) = NaN`   |
| `x == 1`     | `tan(x) = 1`       |
| `x == 0`     | `tan(x) = 0`       |
| `x < 0`      | `tan(x) = NaN`     |
| `x == +inf`  | `tan(+inf) = +inf` |

#### Errors for x ∈ (-Pi/2 + 0.01, Pi/2 - 0.01)

-   `Fixed32`: average: `0.000552292`, max: `0.108399`
-   `Fixed32`: average: `4.52891e-09`, max: `1.38022e-06`

### `ArcSin`, `ArcCos`, and `ArcTan`

```c++
function main()

    var x = 1.0fp64;
    printLn("asin of 1");
    printLn(toString(asin(x)));

    x = 0.5fp64;
    printLn("asin of 0.5");
    printLn(toString(asin(x)));

    x = 0.0fp64;
    printLn("asin of 0");
    printLn(toString(asin(x)));

    x = 1.0fp64;
    printLn("acos of 1");
    printLn(toString(acos(x)));

    x = 0.5fp64;
    printLn("acos of 0.5");
    printLn(toString(acos(x)));

    x = 0.0fp64;
    printLn("acos of 0");
    printLn(toString(acos(x)));

    x = 1.0fp64;
    printLn("atan of 1");
    printLn(toString(atan(x)));

    x = 0.5fp64;
    printLn("atan of 0.5");
    printLn(toString(atan(x)));

    x = 0.0fp64;
    printLn("atan of 0");
    printLn(toString(atan(x)));

endfunction
```

#### `ASin` special cases

| Scenario        | Result                |
| --------------- | :-------------------- |
| `x` is `NaN`    | `asin(x) = NaN`       |
| `x` is `+/-inf` | `asin(x) = NaN`       |
| `|x| > 1`       | `asin(x) = NaN`       |
| `x < 0`         | `asin(x) = -asin(-x)` |

#### Errors for x ∈ (-1, 1)

-   `Fixed32`: average: `1.76928e-05`, max: `0.000294807`
-   `Fixed64`: average: `2.62396e-10`, max: `1.87484e-09`

#### `ACos` special cases

| Scenario        | Result          |
| --------------- | :-------------- |
| `x` is `NaN`    | `acos(x) = NaN` |
| `x` is `+/-inf` | `acos(x) = NaN` |
| `|x| > 1`       | `acos(x) = NaN` |

#### Errors for x ∈ (-1, 1)

-   `Fixed32`: average: `1.94115e-05`, max: `0.000305612`
-   `Fixed64`: average: `2.65666e-10`, max: `1.78974e-09`

#### `ATan` special cases

| Scenario        | Result                       |
| --------------- | :--------------------------- |
| `x` is `NaN`    | `atan(x) = NaN`              |
| `x` is `+/-inf` | `atan(x) = +/- Pi/2`         |
| `x < 0`         | `atan(x) = -atan(-x)`        |
| `x > 1`         | `atan(x) = Pi/2 - Atan(1/x)` |

#### Errors for x ∈ (-5, 5)

-   `Fixed32`: average: `9.41805e-06`, max: `3.11978e-05`
-   `Fixed64`: average: `9.69576e-10`, max: `2.84322e-08`

### Hyperbolic `Sin`, `Cos`, and `Tan`

```c++
function main()

    var x = 1.0fp64;
    printLn("sinh of 1");
    printLn(toString(sinh(x)));

    x = 0.5fp64;
    printLn("sinh of 0.5");
    printLn(toString(sinh(x)));

    x = 0.0fp64;
    printLn("sinh of 0");
    printLn(toString(sinh(x)));

    x = 1.0fp64;
    printLn("cosh of 1");
    printLn(toString(cosh(x)));

    x = 0.5fp64;
    printLn("cosh of 0.5");
    printLn(toString(cosh(x)));

    x = 0.0fp64;
    printLn("cosh of 0");
    printLn(toString(cosh(x)));

    x = 1.0fp64;
    printLn("tanh of 1");
    printLn(toString(tanh(x)));

    x = 0.5fp64;
    printLn("tanh of 0.5");
    printLn(toString(tanh(x)));

    x = 0.0fp64;
    printLn("tanh of 0");
    printLn(toString(tanh(x)));

endfunction
```

!!! Warn
The `sinh()` implementation depends on `exp()` so the range is limited. The implementation is as follows:

    `sinh(x) = (e^x - e^(-x)) / 2`

#### `SinH` special cases

| Scenario        | Result             |
| --------------- | :----------------- |
| `x` is `NaN`    | `sinh(x) = NaN`    |
| `x` is `+/-inf` | `sinh(x) = +/-inf` |

#### Errors for x ∈ (-5, 5)

-   `Fixed32`: average: `6.63577e-05`, max: `0.000479903`
-   `Fixed64`: average: `7.39076e-09`, max: `7.90546e-08`

#### `CosH` special cases

| Scenario        | Result           |
| --------------- | :--------------- |
| `x` is `NaN`    | `cosh(x) = NaN`  |
| `x` is `+/-inf` | `cosh(x) = +inf` |

!!! Warn
The `cosh()` implementation depends on `exp()` so the range is limited. The implementation is as follows:

    `cosh(x) = (e^x + e^(-x)) / 2`

#### Errors for x ∈ (-5, 5)

-   `Fixed32`: average: `6.92127e-05`, max: `0.000487532`
-   `Fixed64`: average: `7.30786e-09`, max: `7.89509e-08`

#### `TanH` special cases

| Scenario        | Result           |
| --------------- | :--------------- |
| `x` is `NaN`    | `tanh(x) = NaN`  |
| `x` is `+/-inf` | `tanh(x) = +/-1` |

!!! Warn
The `tanh()` implementation depends on `exp()` so the range is limited. The implementation is as follows:

    `tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))`

#### Errors for x ∈ (-3, 3)

-   `Fixed32`: average: `1.25046e-05`, max: `7.0897e-05`
-   `Fixed64`: average: `1.7648e-10`, max: `1.19186e-09`

### Hyperbolic `ArcSin`, `ArcCos`, and `ArcTan`

```c++
function main()

    var x = 1.0fp64;
    printLn("asinh of 1");
    printLn(toString(asinh(x)));

    x = 0.5fp64;
    printLn("asinh of 0.5");
    printLn(toString(asinh(x)));

    x = 0.0fp64;
    printLn("asinh of 0");
    printLn(toString(asinh(x)));

    x = 1.0fp64;
    printLn("acosh of 1");
    printLn(toString(acosh(x)));

    x = 0.5fp64;
    printLn("acosh of 0.5");
    printLn(toString(acosh(x)));

    x = 0.0fp64;
    printLn("acosh of 0");
    printLn(toString(acosh(x)));

    x = 1.0fp64;
    printLn("atanh of 1");
    printLn(toString(atanh(x)));

    x = 0.5fp64;
    printLn("atanh of 0.5");
    printLn(toString(atanh(x)));

    x = 0.0fp64;
    printLn("atanh of 0");
    printLn(toString(atanh(x)));

endfunction
```

#### `ArcSin` special cases

| Scenario        | Result              |
| --------------- | :------------------ |
| `x` is `NaN`    | `asinh(x) = NaN`    |
| `x` is `+/-inf` | `asinh(x) = +/-inf` |

#### Errors for x ∈ (-3, 3)

-   `Fixed32`: average: `5.59257e-05`, max: `0.00063489`
-   `Fixed64`: average: `3.49254e-09`, max: `2.62839e-08`

#### `ArcCos` special cases

| Scenario      | Result            |
| ------------- | :---------------- |
| `x` is `NaN`  | `acosh(x) = NaN`  |
| `x` is `+inf` | `acosh(x) = +inf` |
| `x < 1`       | `acosh(x) = NaN`  |

#### Errors for x ∈ (1, 3)

-   `Fixed32`: average: `8.53834e-06`, max: `6.62567e-05`

#### Errors for x ∈ (1, 5)

-   `Fixed64`: average: `2.37609e-09`, max: `2.28507e-08`

#### `ArcTan` special cases

| Scenario        | Result           |
| --------------- | :--------------- |
| `x` is `NaN`    | `atanh(x) = NaN` |
| `x` is `+/-inf` | `atanh(x) = NaN` |

#### Errors for x ∈ (-1, 1)

-   `Fixed32`: average: `2.08502e-05`, max: `0.000954267`
-   `Fixed64`: average: `1.47673e-09`, max: `1.98984e-07`

<br/>
