<h1>Operators</h1>

<center>


<table align="center">
    <tr>
        <td align="center">+</td>
        <td align="center">+=</td>
        <td align="center">==</td>
        <td align="center">!=</td>
        <td align="center">(   )</td>
        <td align="center">&&</td>
    </tr>
    <tr>
        <td align="center">-</td>
        <td align="center">-=</td>
        <td align="center">&#124;&#124;</td>
        <td align="center"><</td>
        <td align="center"><=</td>
        <td align="center">[   ]</td>
    </tr>
        <tr>
        <td align="center">*</td>
        <td align="center">*=</td>
        <td align="center">></td>
        <td align="center">>=</td>
        <td align="center"></td>
        <td align="center">/</td>
    </tr>
    <tr>
        <td align="center">/=</td>
        <td align="center">++</td>
        <td align="center">=</td>
        <td align="center"></td>
        <td align="center">:</td>
        <td align="center">,</td>
    </tr>
    <tr>
        <td align="center">%</td>
        <td align="center">%=</td>
        <td align="center">--</td>
        <td align="center">!</td>
        <td align="center"></td>
        <td align="center">.</td>
    </tr>
</table>


</center>


## Minus

``` c++
function main()

    var plus = 42;
    var minus = -42;
    printLn(toString(plus));
    printLn(toString(minus));

    var plusminused = -plus;
    printLn(toString(plusminused));

endfunction
```

## Increment

``` c++
function main()

	var int32bit : Int32 = 42;
	int32bit++;
	printLn(toString(int32bit));
	++int32bit;
	printLn(toString(int32bit));

endfunction
```

## Decrement

``` c++
function main()

    var int32bit : Int32 = 42;
	int32bit--;
	printLn(toString(int32bit));
	--int32bit;
	printLn(toString(int32bit));

endfunction
```


## Addition

``` c++
function main()

	var x = 42;
	var y = 66;
	var z = x + y;
	printLn(toString(z));
	z += 2;
	printLn(toString(z));

endfunction
```


## Subtraction

``` c++
function main()

    var x = 42;
    var y = 66;
    var z = y - x;
    printLn(toString(z));
    z -= 2;
    printLn(toString(z));

endfunction
```


## Multiplication

``` c++
function main()

	var x = 42;
	var y = 2;
	var z = y * x;
	printLn(toString(z));
	z *= 2;
	printLn(toString(z));

endfunction
```


## Division

Integer division returns a rounded down integer value.

``` c++
function main()

	var x = 41;
	var y = 7;
	var z = x / y;
	printLn(toString(z));
	z /= 2;
	printLn(toString(z));


	var a = 32.3f;
	var b = 31.2f;
	var c = a / b;
	printLn(toString(c));

endfunction
```



## Modulus

``` c++
function main()

	var x = 7;
	var y = 6;
	var z = x % y;
	printLn(toString(z));
	z %= 2;
	printLn(toString(z));

endfunction
```


## Ternary

Not currently supported.


## Precedence

``` c++
1. x++ x-- subscript[] .
2. ++x --x (+x) -x ! toType 
3. * / %
4. + -
5. < <= > >=
6. == !=
7. &&
8. ||
9. = += -= *= /= 
10. ,	
```

<br/>