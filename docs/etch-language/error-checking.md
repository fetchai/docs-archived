<H2>Forcing runtime errors</H2>

You can force runtime errors with `panic()`. 

Use `panic` for unrecoverable states. It terminates the progam immediately and provides optional feedback. 

For example:

``` c++
function main()

    var x = 1;
    var y = 2;
    var z = y + x;
    printLn(toString(z));
    z =- 2;
    if (z != -1)
    	panic("this is a terrible mistake!");
    endif
    printLn(toString(z));

endfunction
```

<br/>